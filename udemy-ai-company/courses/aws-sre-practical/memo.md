## 指摘メモ

### 読み方
モグラたたき的にかいけつするのではなく
これを一気に解決するruleを検討するべきかも
script.jsonのnarrationを全部ひらがなでかいて、切れ目は句読点や空白入れるなど？？

※読み方はSkillとしてルール化済（各script.jsonへの反映はまだ）
  次のステップ候補（必要時に進めます）

  1. テーブル拡張: _EN_TO_KANA・_JP_READING_FIXES に SKILL.md 記載の候補を追加 → VOICEVOXで聴取確認
  2. script_generator.py の改修: 新規生成時に narration_system.md も併読させる
  3. 既存script.jsonへの一括レビュー: 違反検出のドライランレポートだけ先に出す

#### 読み方誤り例
今リリースできるか→こんりりーすできるか
上で→じょうで
引いた値で→ひいたねで
500ms→ごひゃくむす
5xx→ごくす
重大度→じゅうたいど
どの値→どのね
dmesg→どめすぐ
一気貫通→いっきとおりぬき
killall→きらる
正常値→せいじょうね
〇〇さんのミス→ぜろぜろさんのみす
Blameless（ブレームレス）→ぶれーむれすぶれーむれす（2回同じことを読んでしまう）
根本原因→ねもとげんいん
発報→はつむくい
キーと値→きーとね
右上→みぎじょう

### 単語の切れ目が微妙なことが多い
サービス名のスペースでかなり間が空いてしまう
Cost Anomaly Detection：こすと　　あのまりー　　でぃてくしょん
→これは一気に読んでよい

### s5-l5
/home/ubuntu/workspace/udemy/courses/aws-sre-practical/s5-l5/script.json

次のレクチャーでは複数アラームをまとめる複合アラームを学んでいきましょう。
とあるのに複合アラームのレクチャーがない。。


### s6-l1
/home/ubuntu/workspace/udemy/courses/aws-sre-practical/s6-l1/slides/slide_010.png
表がずれている。

### s6-l2
/home/ubuntu/workspace/udemy/courses/aws-sre-practical/s6-l2/slides/slide_007.png
表がずれている。

### s6-l4
/home/ubuntu/workspace/udemy/courses/aws-sre-practical/s6-l4/script.json
SLOドキュメント配布していると言っているが配布はしていない。。


/home/ubuntu/workspace/udemy/courses/aws-sre-practical/s6-l4/slides/slide_009.png
図がつぶれている

https://github.com/toma1110/aws-sre-cfn-templates
SLOダッシュボードを作成するCfnテンプレートを作った方が良い

### s7-l4
Amazon Linux 2023の前提になっていない（Extras設定不用）
※CLI_COMMANDS.mdの内容が正しいので、正確なコマンドはこちらを参照させる

###　s8-l2
これが実際に現場で使えるポストモーテムのMarkdownテンプレートです。この講義の資料からそのままコピーして使えます。
https://github.com/toma1110/aws-sre-cfn-templatesにはそのテンプレートが存在しない。。

Udemyのリソースで上記リンクを追加しましたのでMDファイルでテンプレート作成をおねがいします

###  s9-l3
/home/ubuntu/workspace/udemy/courses/aws-sre-practical/s9-l3/script.json
代表的なのがElastic IPで、インスタンスに割り当てていないEIPは月額で課金されます。
とありますが、ELASTIC IPは割り当てていても課金対象に変わった可能性がありますので、最新の状況をMCPサーバーに確認してください。

###  s9-l4
参考: Billing Alert（無料枠アラート）の設定　は必要ですか？Budgetのアラートで代替できそうな気がします
以下のテンプレートでもBudgetしか設定していないように見えます。

/home/ubuntu/workspace/publicRepo/aws-sre-cfn-templates/cloudformation/06-cost-alerts.yaml

### s10-l1
/home/ubuntu/workspace/udemy/courses/aws-sre-practical/s10-l1/script.json
このチェックリストは、コースの資料としてPDFでもダウンロードできるようにしています。
とありますが、PDF用意していないです。。
