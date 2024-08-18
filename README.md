# Streamlit キャッチアップの会

このプロジェクトは、Streamlitというインタラクティブなウェブアプリケーションを作成するための人気のあるPythonのライブラリを使用します。

## はじめに

### 前提条件

以下のソフトウェアがマシンにインストールされていることを確認してください：

- Git
- Python 3.7以上
- Streamlit

### インストール手順

1. リポジトリをクローンする:

    ```bash
    git clone https://github.com/YuseiSato0302/catchup_streamlit.git
    ```
    

2. 仮想環境を作成する:

    ```cmd
    python -m venv .venv
    ```
    

3. 仮想環境をアクティベートする:

    ```cmd
    # Windows command prompt
    .venv\Scripts\activate.bat
    
    # Windows PowerShell(windowsユーザーはPowerShellの使用を推奨)
    .venv\Scripts\Activate.ps1
    
    # macOS and Linux
    source .venv/bin/activate
    ```
    

4. 必要な依存関係をインストールする:

    ```bash
    pip install -r requirements.txt
    ```
    
    
5. `.env.sample`ファイルを`.env`ファイルに変更後、ファイル内の"YOUR_API_KEY_HERE"を取得したGemini APIキーで上書きする:

   ```bash
   GOOGLE_API_KEY="YOUR_API_KEY_HERE"
   ```
   

6. Streamlitアプリケーションを実行する:

    ```bash
    streamlit run example.py
    ```
