# Streamlit キャッチアップの会

このプロジェクトは、Streamlitというインタラクティブなウェブアプリケーションを作成するための人気のあるツールを使用します。

## はじめに

### 前提条件

以下のソフトウェアがマシンにインストールされていることを確認してください：

- Git
- Python 3.7以上
- Streamlit

また今回GemeniAPIを利用します。まだAPIキーを取得していない方は以下のURLからキーを発行してください。
https://ai.google.dev/gemini-api?gad_source=1&gclid=CjwKCAjw34qzBhBmEiwAOUQcF23MZ0YXeaoqD7xJIOib1zt6kgwx1-MIPspDGndnqkh3mR0oYrJa1RoCPtEQAvD_BwE&hl=ja

### インストール手順

1. **リポジトリをクローンする:**

    ```bash
    git clone https://github.com/YuseiSato0302/catchup_streamlit.git
    ```

2. 仮想環境を作成する:

    ```cmd
    python -m venv venv
    ```

3. 仮想環境をアクティベートする:

    ```cmd
    # Windows command prompt
    .venv\Scripts\activate.bat
    
    # Windows PowerShell
    .venv\Scripts\Activate.ps1
    
    # macOS and Linux
    source .venv/bin/activate
    ```

4. 必要な依存関係をインストールする:

    ```bash
    pip install -r requirements.txt
    ```

5. Streamlitアプリケーションを実行する:

    ```bash
    streamlit run app.py
    ```

    `app.py`は、メインのStreamlitアプリケーションファイルの名前に置き換えてください。
