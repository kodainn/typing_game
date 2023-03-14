from tkinter import *
from tkinter import messagebox
import sys
import time
import threading

QUESTION = ["tkinter", "geometry", "widgets", "messagebox", "configure", 
            "label", "column", "rowspan", "grid", "init"]
class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry("500x200")
        master.title("typing game")

        self.index = 0

        self.corrent_cnt = 0

        self.create_widgets()

        t = threading.Thread(target=self.timer)
        t.start()

        # Tkインスタンスに対してキーイベント処理を実装
        self.master.bind("<KeyPress>", self.type_event)

    # ウィジェットの生成と配置
    def create_widgets(self):
        self.q_label = Label(self, text="お題：", font=("",20))
        self.q_label.grid(row=0, column=0)
        self.q_label2 = Label(self, text=QUESTION[self.index], width=10, anchor="w", font=("",20))
        self.q_label2.grid(row=0, column=1)
        self.ans_label = Label(self, text="解答：", font=("",20))
        self.ans_label.grid(row=1, column=0)
        self.ans_label2 = Label(self, text="", width=10, anchor="w", font=("",20))
        self.ans_label2.grid(row=1, column=1)
        self.result_label = Label(self, text="正否ラベル", font=("",20))
        self.result_label.grid(row=2, column=0, columnspan=2)

        #時間計測用のラベル
        self.time_label = Label(self, text="", font=(" ", 20))
        self.time_label.grid(row=3, column=0, columnspan=2)


    # キー入力時のイベント処理
    def type_event(self, event):
        #入力値がEnterの場合は答え合わせ
        if event.keysym == "Return":
            if self.q_label2["text"] == self.ans_label2["text"]:
                self.result_label.configure(text="正解!", fg = "red")
                self.corrent_cnt += 1
            else:
                self.result_label.configure(text="残念!", fg="blue")

            #回答欄をクリア
            self.ans_label2.configure(text="")

            #次の問題を出題
            self.index += 1

            if self.index == len(QUESTION):
                self.flg = False
                self.q_label2.configure(text="終了!")
                messagebox.showinfo("リザルド", f"あなたのスコアは{self.corrent_cnt}/{self.index}問正解です。")
                sys.exit(0)
            self.q_label2.configure(text = QUESTION[self.index])

        elif event.keysym == "BackSpace":
            text = self.ans_label2["text"]
            self.ans_label2["text"] = text[:-1]

        else:
            #入力値がEnter以外の場合は文字列入力としてラベルを追記する
            self.ans_label2["text"] += event.keysym

    def timer(self):
        self.second = 0
        self.flg = True
        while self.flg:
            self.second += 1
            self.time_label.configure(text=f"経過時間:{self.second}秒")
            time.sleep(1)

if __name__ == "__main__":
    root = Tk()
    Application(master=root)
    root.mainloop()