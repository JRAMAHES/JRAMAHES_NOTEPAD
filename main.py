import webbrowser
import datetime
from tkinter import *
from tkinter.messagebox import askyesno
from tkinter import filedialog
from tkinter.colorchooser import askcolor

def No_Format():
    text.config(font=("Arial", 16))

def online_help():
    webbrowser.open("http://www.google.com/")

def Background():
    tripple, color = askcolor()
    if color:
        text.config(background=color)

def Bold():
    current_tag = text.tag_names("sel.first") 
    if "bt" in current_tag:
        text.tag_remove("bt", "sel.first", "sel.last")
        text.tag_config("bt", font=("Arial", 16, "bold"))
    else:
        text.tag_add("bt", "sel.first", "sel.last")
        text.tag_config("bt", font=("Arial", 16, "bold"))
        
def Underline():
    current_tag = text.tag_names("sel.first") 
    if "bt" in current_tag:
        text.tag_remove("bt", "sel.first", "sel.last")
        text.tag_config("bt", font=("Arial", 16, "underline"))
    else:
        text.tag_add("bt", "sel.first", "sel.last")
        text.tag_config("bt", font=("Arial", 16, "underline"))

def Italic():
    current_tag = text.tag_names("sel.first") 
    if "bt" in current_tag:
        text.tag_remove("bt", "sel.first", "sel.last")
        text.tag_config("bt", font=("Arial", 16, "italic"))
    else:
        text.tag_add("bt", "sel.first", "sel.last")
        text.tag_config("bt", font=("Arial", 16, "italic"))
     

def Text_color():
    triple, color = askcolor() 
    if color: 
        text.config(foreground=color)

def Date():
    date = datetime.date.today()
    text.insert(INSERT, date)

def New_File():
    if askyesno("JRAMAHES NOTEPAD", "Save the File."):
        filename = filedialog.asksaveasfilename()
        if filename:
            all_text = text.get(1.0, END)
            open(filename, 'w').write(all_text)
    
    if askyesno("JRAMAHES NOTEPAD", "Open Existing File ? "):
        text.delete(1.0, END)
        file = open(filedialog.askopenfilename(), "r")
        if file != "": 
            txt = file.read()
            text.insert(INSERT, txt)
        else:
            pass
    else:
        text.delete(1.0, END)

def Open_File():
    text.delete(1.0, END)
    file = open(filedialog.askopenfilename(), 'r')
    if file != "": 
        txt = file.read()
        text.insert(INSERT, txt)


def Save_As():
    filename = filedialog.asksaveasfilename()
    if filedialog:
        all_text = text.get(1.0, END)
        open(filename, 'w').write(all_text)
    
def Close():
    if askyesno("JRAMAHES NOTEPAD", "Save the File."):
        filename = filedialog.asksaveasfilename()
        if filename:
            all_text = text.get(1.0, END)
            open(filename, 'w').write(all_text)
        root.destroy()
    else:
        root.destroy()

def Cut():
    text.clipboard_clear()   
    text.clipboard_append(text.selection_get())
    sel = text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)

def Copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def Paste():
    try:
        text = text.selection_get(selection="CLIPBOARD")
        text.insert(INSERT, text)
    except:
        pass

def Erase():
    sel = text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)

def Clear_Screen():
    text.delete(1.0, END)

if __name__ == "__main__": 
    root = Tk()   
    root.title("JRAMAHE'S NOTEPAD")
    main_menu = Menu(root)
    commands = Menu(root)
    root.config(menu=main_menu)

    main_menu.add_cascade(label="File", menu=commands)
    commands.add_command(label="New File", command=New_File)
    commands.add_command(label="Open", command=Open_File)
    commands.add_command(label="Save As..", command=Save_As)
    commands.add_command(label="Close..", command=Close)

    Edit_menu = Menu(root)
    main_menu.add_cascade(label="Edit", menu=Edit_menu )
    Edit_menu.add_command(label="Cut", command=Cut)
    Edit_menu.add_command(label="Copy", command=Copy)
    Edit_menu.add_command(label="Paste", command=Paste)
    Edit_menu.add_separator()
    Edit_menu.add_command(label="Delete", command=Erase)
    Edit_menu.add_command(label="Clear Screen", command=Clear_Screen)

    Insert_in_Menu = Menu(root)
    main_menu.add_cascade(label="Insert", menu=Insert_in_Menu)
    Insert_in_Menu.add_command(label="Current Date", command=Date )

    change_format = Menu(root)
    main_menu.add_cascade(label="Format", menu=change_format)
    change_format.add_command(label="Font", command=Text_color)
    change_format.add_separator()
    change_format.add_command(label="No Format", command=No_Format)
    change_format.add_command(label="Bold", command=Bold)
    change_format.add_command(label="Italic", command=Italic)
    change_format.add_command(label="Underline", command=Underline)

    personalize = Menu(root)
    main_menu.add_cascade(label="Personalize", menu=personalize)
    personalize.add_command(label="Background", command=Background)

    user_help = Menu(root)
    main_menu.add_cascade(label="Help", menu=user_help)
    user_help.add_command(label="Online Help", command=online_help)

    text = Text(root, height=40, width=100, font=("Arial",16))
    scrollbar = Scrollbar(root, command=text.yview)
    scrollbar.config(command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    text.pack()

    root.resizable()
    root.mainloop()
