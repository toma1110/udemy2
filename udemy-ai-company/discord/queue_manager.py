from __future__ import annotations

import asyncio
import sys
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class RunRequest:
    issue_number: int
    requested_by: str
    response_channel_id: int | None


class RunQueue:
    def __init__(self, max_parallel_runs: int) -> None:
        self.max_parallel_runs = max_parallel_runs
        self.queue: asyncio.Queue[RunRequest] = asyncio.Queue()
        self.active_runs = 0
        self._workers: list[asyncio.Task[None]] = []

    def start(self, handler: Callable[[RunRequest], Awaitable[Any]]) -> None:
        if self._workers:
            return
        for _ in range(self.max_parallel_runs):
            self._workers.append(asyncio.create_task(self._worker(handler)))

    async def _worker(self, handler: Callable[[RunRequest], Awaitable[Any]]) -> None:
        while True:
            request = await self.queue.get()
            self.active_runs += 1
            try:
                await handler(request)
            except Exception as exc:  # noqa: BLE001 - one failed run must not stop the queue worker.
                print(f"run queue worker error for issue #{request.issue_number}: {exc}", file=sys.stderr)
            finally:
                self.active_runs -= 1
                self.queue.task_done()

    async def submit(self, request: RunRequest) -> int:
        await self.queue.put(request)
        return self.queue.qsize()
