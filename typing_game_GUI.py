from tkinter import *
from tkinter import messagebox
import time
import threading
import random

#テキストファイルからお題を配列に格納する
with open("text_data.txt", "r", encoding="utf-8") as f:
    QUESTION = f.readline().split(",")

Landom_Question = [] #QUESTIONからランダムに問題を格納するための配列
random.seed(random.randint(1, 1000))
for i in range(20):
    Landom_Question.append(QUESTION[random.randint(0, len(QUESTION) - 1)])

class TypingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("タイピングゲーム")
        master.geometry("700x400")

        #メイン画面
        self.frame_main = Frame(self.master)
        self.frame_main.pack()

        self.main_label_title = Label(self.frame_main, text="タイピングゲーム", font=("Helvetica", 16))
        self.main_label_text = Label(self.frame_main, text="タイピングの速度を向上させよう!")
        self.main_start_button = Button(self.frame_main, text="Start Game", command=self.start_game)
        self.main_label_title.pack(pady=10)
        self.main_label_text.pack()
        self.main_start_button.pack(pady=10)

        #ゲーム画面
        self.frame_game = Frame(self.master)

        #結果画面
        self.frame_result = Frame(self.master)

    def start_game(self):
        self.index = 0       #お題を格納した配列に使う添え字
        self.corrent_cnt = 0 #正解数をカウントする変数
        #メイン画面を閉じる
        self.frame_main.pack_forget()

        #ゲーム画面を表示
        self.frame_game.pack()

        #お題を表示
        self.odai_label = Label(self.frame_game, text="お題：", font=("",20))
        self.odai_label.grid(row=0, column=0)
        self.question_label = Label(self.frame_game, text=Landom_Question[self.index], width=30, anchor="w", font=("",20))
        self.question_label.grid(row=0, column=1)

        #回答を表示
        self.ans_label = Label(self.frame_game, text="解答：", font=("",20))
        self.ans_label.grid(row=1, column=0)
        self.ans_label2 = Label(self.frame_game, text="", width=30, anchor="w", font=("",20))
        self.ans_label2.grid(row=1, column=1)
        self.ans_label2.focus_set()

        #正否を表示
        self.result_label = Label(self.frame_game, text="正否ラベル", font=("",20))
        self.result_label.grid(row=2, column=0, columnspan=2)

        #時間計測用のラベル
        self.time_label = Label(self.frame_game, text="", font=(" ", 20))
        self.time_label.grid(row=3, column=0, columnspan=2)

        #問題数を表示
        self.questionCount_label = Label(self.frame_game, text = "1問目", font=(" ", 20))
        self.questionCount_label.grid(row=4, column=0, columnspan=2)

        #Tkインスタンスに対してキーイベント処理を実装
        self.master.bind("<Key>", self.type_event)

        #測定開始
        t = threading.Thread(target=self.timer)
        t.start()



    # キー入力時のイベント処理
    def type_event(self, event):
        #入力値がEnterの場合は答え合わせ
        if event.keysym == "Return":
            if self.question_label["text"] == self.ans_label2["text"]:
                self.result_label.configure(text="正解!", fg = "red")
                self.corrent_cnt += 1
            else:
                self.result_label.configure(text="残念!", fg="blue")

            #回答欄をクリア
            self.ans_label2.configure(text="")

            #次の問題を出題
            self.index += 1

            if self.index == 20:
                self.flg = False
                self.result_label.configure(text="終了!")
                messagebox.showinfo("リザルド", f"あなたのスコアは{self.corrent_cnt}/{self.index}問正解です。")
                Landom_Question.clear()
                random.seed(random.randint(1, 1000))
                for i in range(20):
                    Landom_Question.append(QUESTION[random.randint(0, len(QUESTION) - 1)])
                self.frame_game.pack_forget()
                self.frame_main.pack()
            self.question_label.configure(text = Landom_Question[self.index])
            self.questionCount_label.configure(text = str(self.index + 1) + "問目")

        elif event.keysym == "BackSpace":
            text = self.ans_label2["text"]
            self.ans_label2["text"] = text[:-1]

        elif event.keysym == "Shift_L":
            self.ans_label2["text"] += event.char.upper()

        elif event.keysym == "Henkan_Mode":
            self.ans_label2["text"] += event.char
        else:
            #入力値がEnter以外の場合は文字列入力としてラベルを追記する
            self.ans_label2["text"] += event.char

    def timer(self):
        self.second = 0
        self.flg = True
        while self.flg:
            self.second += 1
            self.time_label.configure(text=f"経過時間:{self.second}秒")
            time.sleep(1)

if __name__ == "__main__":
    root = Tk()
    TypingGame(master=root)
    root.mainloop()