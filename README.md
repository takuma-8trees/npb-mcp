岡大海選手のプロフィール、通算成績、シーズン成績などを取得できるツールです。

# 概要
FastAPIを使用して、岡大海選手の成績情報を取得するRESTful APIを構築。

SPAIA NPB APIを使用してデータを取得し、APIエンドポイントを通じて簡単にアクセスできるようにしました。

ローカルで簡単に動作させ、データ取得を行うことができます。

# 使用技術
- FastAPI: 高速なAPIを簡単に構築するためのフレームワーク。

- SPAIA NPB API: プロ野球の選手データを提供するAPI。

- Python 3.13: 本プロジェクトで使用しているPythonのバージョン。

# セットアップ方法
1. クローン
まず、リポジトリをクローンします。

```bash
git clone https://github.com/takuma-8trees/npb-mcp.git
cd npb-mcp
```


2. 必要なパッケージをインストール
Poetryを使用して依存関係を管理しています。以下のコマンドで依存関係をインストールします。

```bash
poetry install
```

3. APIサーバの起動
次に、FastAPIサーバを起動します。

```bash
poetry run uvicorn src.api_server:app --reload --app-dir src
```
サーバが起動したら、ブラウザで以下のURLにアクセスできます。(動作確認未実施)
- http://localhost:8000/profile: 岡大海選手のプロフィール情報を取得

- http://localhost:8000/career: 通算成績

- http://localhost:8000/season?year=2023: 2023年シーズン成績


# ngrokを使用した外部公開方法
ngrokを使用することで、ローカルのFastAPIサーバを簡単に外部に公開することができます。

1. ngrokのインストール
もしまだngrokがインストールされていない場合は、以下のコマンドでインストールします。

```bash
brew install --cask ngrok
```
2. ngrokでローカルサーバを公開
FastAPIサーバが起動している状態で、以下のコマンドでngrokを使用して外部に公開します。

```bash
ngrok http 8000
```
成功すると、次のようなメッセージが表示されます。

```bash
Forwarding                    https://xxxxxxx.ngrok.io -> http://localhost:8000
```
これで、https://xxxxxxx.ngrok.ioが外部からアクセスできるURLとして提供されます。
このURLを使用して、他の人がインターネット経由でAPIにアクセスできるようになります。

3. ngrokのURLを使用
例えば、https://xxxxxxx.ngrok.io/profileにアクセスすると、岡大海選手のプロフィール情報を取得できます。


