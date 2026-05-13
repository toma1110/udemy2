from __future__ import annotations

import discord


def truncate(text: str, limit: int = 1850) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 20] + "\n... truncated ..."


class DiscordNotificationService:
    def __init__(self, client: discord.Client, channel_id: int | None) -> None:
        self.client = client
        self.channel_id = channel_id

    async def send(self, message: str) -> None:
        if not self.channel_id:
            return
        channel = self.client.get_channel(self.channel_id)
        if channel is None:
            channel = await self.client.fetch_channel(self.channel_id)
        if isinstance(channel, discord.abc.Messageable):
            await channel.send(truncate(message))
