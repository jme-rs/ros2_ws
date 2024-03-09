# Minimal action node using r2r

[このリポジトリ](https://github.com/m-dahl/r2r_minimal_node)を参考に、r2rのアクションサーバーとクライアントをcolconでビルドできるようにしました。

## colconでビルドする
ビルド方法は以下の通りです

``` sh

mkdir ws_r2r/src
cd ws_r2r/src
git clone [this repo]
cd ..
colcon build
```

## 実行方法
実行方法は以下の通りです。

``` sh
. install/setup.sh
ros2 run r2r_minimal_action_server r2r_minimal_action_server
```

[新しい端末で]
``` sh
. install/setup.sh
ros2 run r2r_minimal_action_client r2r_minimal_action_client
```


## 参考資料
- https://github.com/sequenceplanner/r2r
    - r2rの本家
    - /examples下のソースを持ってきた
- https://github.com/m-dahl/r2r_minimal_node
    - サービスを使う場合の参考になる
    - メッセージ定義をした場合の使い方の参考になる