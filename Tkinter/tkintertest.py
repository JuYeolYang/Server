from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
'''
root = Tk()

lbl = Label(root, text = "이름")
lbl.grid(row = 0, column = 0)
# lbl.pack()

txt = Entry(root)
txt.grid(row = 0, column = 1)
# txt.pack()

btn = Button(root, text = "OK", width = 15)
btn.grid(row = 1, column = 1)
# btn.pack()

root.mainloop()
'''

'''
class MyFrame(Frame):
    def __init__(self, master):
        img = PhotoImage(file = 'test.gif')
        lbl = Label(image = img)
        lbl.image = img
        lbl.place(x = 0, y = 0)

def main():
    root = Tk()
    root.titile('이미지 보기')
    root.geometry('500x400+10+10')
    myframe = MyFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()

'''


'''
class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
 
        self.master = master
        self.master.title("고객 입력")
        self.pack(fill=BOTH, expand=True)
 
        # 성명
        frame1 = Frame(self)
        frame1.pack(fill=X)
 
        lblName = Label(frame1, text="성명", width=10)
        lblName.pack(side=LEFT, padx=10, pady=10)
 
        entryName = Entry(frame1)
        entryName.pack(fill=X, padx=10, expand=True)
 
        # 회사
        frame2 = Frame(self)
        frame2.pack(fill=X)
 
        lblComp = Label(frame2, text="회사명", width=10)
        lblComp.pack(side=LEFT, padx=10, pady=10)
 
        entryComp = Entry(frame2)
        entryComp.pack(fill=X, padx=10, expand=True)
 
        # 특징
        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)
 
        lblComment = Label(frame3, text="특징", width=10)
        lblComment.pack(side=LEFT, anchor=N, padx=10, pady=10)
 
        txtComment = Text(frame3)
        txtComment.pack(fill=X, pady=10, padx=10)
 
        # 저장
        frame4 = Frame(self)
        frame4.pack(fill=X)
        btnSave = Button(frame4, text="저장")
        btnSave.pack(side=LEFT, padx=10, pady=10)
 
 
def main():
    root = Tk()
    root.geometry("600x550+100+100")
    app = MyFrame(root)
    root.mainloop()
 
 
if __name__ == '__main__':
    main()

'''

root = Tk()

# 버튼 클릭 이벤트 핸들러
def okClick():
    name = txt.get()
    messagebox.showinfo("이름", name)

lbl = Label(root, text = "이름")
lbl.grid(row = 0, column = 0)
txt = Entry(root)
txt.grid(row = 0, column = 1)

# 버튼 클릭 이벤트와 핸들러 정의
btn = Button(root, text = "OK", command = okClick)

btn.grid(row = 1, column = 1)

root.mainloop()