import tkinter as tk
from tkinter import messagebox

def convert_case():
    input_str = entry_input.get()
    converted = []
    for c in input_str:
        if c.isupper():
            converted.append(c.lower())
        elif c.islower():
            converted.append(c.upper())
        else:
            converted.append(c)
    result = ''.join(converted)
    
    # 显示结果前临时启用输入框
    entry_result.config(state='normal')
    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)
    entry_result.config(state='readonly')

def about():
    messagebox.showinfo("关于", "大小写转换器\n作者：yueyue\n版本：1.5")

# 创建主窗口
root = tk.Tk()
root.title("大小写转换器 by yueyue")
root.geometry("500x250")

# 创建菜单栏
menubar = tk.Menu(root)
root.config(menu=menubar)
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="帮助", menu=helpmenu)
helpmenu.add_command(label="关于", command=about)

# 界面组件
frame = tk.Frame(root)
frame.pack(pady=20)

# 输入部分
tk.Label(frame, text="输入文本：").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_input = tk.Entry(frame, width=40)
entry_input.grid(row=0, column=1, padx=5, pady=5)

# 转换按钮
btn_convert = tk.Button(frame, text="转换大小写", command=convert_case)
btn_convert.grid(row=1, column=0, columnspan=2, pady=10)

# 输出部分
tk.Label(frame, text="转换结果：").grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_result = tk.Entry(frame, width=40, state='readonly')
entry_result.grid(row=2, column=1, padx=5, pady=5)

# 设置焦点到输入框
entry_input.focus_set()

root.mainloop()