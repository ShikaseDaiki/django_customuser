cloneした際の環境構築コマンド
//イメージを作成する
> docker build
//コンテナを作成して、バックグラウンドで立ち上げる
>docker-compose up -d

コンテナに入る際のコマンド
//コンテナを立ち上げる
>docker-compose up -d
//コンテナのIDを調べる
>docker ps
//コンテナに入る
>docker exec -it (コンテナのID) bash
※bashでエラーが出る場合、shで再実行する
