# TwikeChanneler

## 概要

ツイッター(現 X)上でいいねしたポストを slack で通知するプログラム  
単一のチャンネルに通知するのではなく、ポストの内容によって通知するチャンネルを切り替えたい  
汎用化は一旦考えなくてよいものとして。自分の slack チャンネルで動けば OK

## 構成

想定する構成は以下の通り
IFTTT -> 本プログラム -> slack

## 主なマイルストン

1. cursor をインストール、設定する
   インストール,日本語化,cursor pro にアップグレード done
   todo:チュートリアルを探す
   [候補](https://zenn.dev/yasuna/articles/9dadbcdc3be48d)
   設定の[参考](https://www.creationline.com/tech-blog/chatgpt-ai/ai/68729)
2. lambda への CICD を構築する
3. ハローワールドの出力
4. IFTTT -> lambda の実行とリクエストボディの出力
5. skalck への通知
6. 任意の AI を使って対象のチャンネルを決定する機能の追加
