import rclpy  # 1.ROS2化：ヘッダ
from rclpy.node import Node  # 1.ROS2化：ヘッダ
from std_msgs.msg import String

import speech_recognition as sr  # speech_recognitionモジュールにsrという名前を付ける．


def main():
    r = sr.Recognizer()  # Recognizerクラスのインスタンスを生成
    m = sr.Microphone()  # Microphoneクラスのインスタンスを生成

    rclpy.init()  # 2. ROS2化：ノード
    node = Node("speech_recog")  # 2. ROS2化：ノード

    try:
        print("A moment of silence, please...")
        # with文．マイクの終了処理を自動でやってくれる．
        with m as source:
            r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))

        # 3. ROS2化：パブリッシャ
        result_pub = node.create_publisher(String, "/speech_recog_result", 10)

        while True:
            while rclpy.ok():  # 5. ROS2化：その他
                print("Say something!")
                pub_msg = String()

                with m as source:
                    audio = r.listen(source)
                    print("Got it! Now to recognize it...")
                try:  # 例外処理
                    # recognize speech using Google Speech Recognition
                    value = r.recognize_google(audio, language="ja-JP")

                    # we need some special handling here to correctly print unicode characters to standard output

                    target_word = str(value).split(" ")
                    # if target_word[0] == "しんくま":
                    #     msg = target_word[1]
                    #     pub_msg.data = msg

                    #     result_pub.publish(pub_msg)  # 3. ROS2化：パブリッシャ関連

                    # else:
                    #     msg = "My name is Shinkuma"

                    if str(value).find("くまさん") == -1:
                        msg = "My name is Shinkuma"
                    else:
                        index_of_shinkuma = target_word.index("くまさん")
                        msg = target_word[index_of_shinkuma + 1]

                        pub_msg.data = msg
                        result_pub.publish(pub_msg)  # 3. ROS2化：パブリッシャ関連

                    if (
                        str is bytes
                    ):  # this version of Python uses bytes for strings (Python 2)
                        print("You said {}".format(msg).encode("utf-8"))
                    else:  # this version of Python uses unicode for strings (Python 3+)
                        print("You said {}".format(msg))

                except sr.UnknownValueError:
                    print("Oops! Didn't catch that")
                except sr.RequestError as e:
                    print(
                        "Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(
                            e
                        )
                    )
    except KeyboardInterrupt:  # Ctrl+Cが入力された場合
        pass  # 何も処理をしない．Pythonのインデントのため必要．

    rclpy.shutdown()  # ROS2化。終了処理。


if (
    __name__ == "__main()__"
):  # このコードをモジュールとしてimport可能にする。ROS2推奨の書き方。
    main()  # setup.pyのエントリーポイント
