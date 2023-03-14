from tkinter import *

class Application(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()

        self.create_widgets()

        # Tkインスタンスに対してキーイベント処理を実装
        self.master.bind("<KeyPress>", self.type_event)

    # ウィジェットの生成と配置
    def create_widgets(self):
        self.q_label = Label(self, text="お題：", font=("",20))
        self.q_label.grid(row=0, column=0)
        self.q_label2 = Label(self, text="tkinter", width=5, anchor="w", font=("",20))
        self.q_label2.grid(row=0, column=1)
        self.ans_label = Label(self, text="解答：", font=("",20))
        self.ans_label.grid(row=1, column=0)
        self.ans_label2 = Label(self, text="", width=5, anchor="w", font=("",20))
        self.ans_label2.grid(row=1, column=1)
        self.result_label = Label(self, text="正否ラベル", font=("",20))
        self.result_label.grid(row=2, column=0, columnspan=2)

    # キー入力時のイベント処理
    def type_event(self, event):
        self.ans_label2["text"] += event.keysym

if __name__ == "__main__":
    root = Tk()
    root.geometry("300x200")
    root.title("タイピングゲーム")
    app = Application(root=root)
    root.mainloop()