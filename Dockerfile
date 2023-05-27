# ubuntu:20.04をベースのコンテナイメージとして設定する
FROM ubuntu:20.04

# ubuntuを最新の状態に更新後python3.9とpipをインストールする
RUN apt update && apt install -y python3.9 && apt install -y python3-pip

# pipをアップグレード
RUN pip3 install --upgrade pip

# ローカルに存在するrequirements.txtをコピーする
# COPY requirements.txt .
# RUN python3.9 -m pip install -r requirements.txt

# Djangoのインストール
RUN pip3 install django

# ワーキングディレクトリを設定
WORKDIR /app
# ホストのファイルをコンテナの/appディレクトリにコピー
COPY . /app

# Djangoサーバーの起動
CMD python3 manage.py runserver 0.0.0.0:8000