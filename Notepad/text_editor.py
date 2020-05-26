import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class VincePad:

    __root = Tk()
    
    # window width and height
    __this_width = 300
    __this_height = 300
    __this_text_area = Text(__root)
    __this_menu_bar = Menu(__root)
    __this_file_menu = Menu(__this_menu_bar, tearoff=0)
    __this_edit_menu = Menu(__this_menu_bar, tearoff=0)
    __this_help_menu = Menu(__this_menu_bar, tearoff=0)
    
    __this_scroll_bar = Scrollbar(__this_text_area)
    __file = None
    
    def __init__(self, **kwargs):
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass
        
        try:
            self.__this_width = kwargs['width']
        except KeyError:
            pass
        
        self.__root.title("Untitled - VincePad") 
        screenWidth = self.__root.winfo_screenwidth() 
        screenHeight = self.__root.winfo_screenheight() 
        left = (screenWidth / 2) - (self.__this_width / 2)  
        top = (screenHeight / 2) - (self.__this_height /2) 
        
        self.__root.geometry('%dx%d+%d+%d' % (self.__this_width, self.__this_height, left, top))
        self.__root.grid_rowconfigure(0, weight=1) 
        self.__root.grid_columnconfigure(0, weight=1)
        self.__this_text_area.grid(sticky = N + E + S + W)
        self.__this_file_menu.add_command(label='New', command=self.__newFile)
        self.__this_file_menu.add_command(label='Open', command=self.__openFile)
        self.__this_file_menu.add_command(label='Save', command=self.__saveFile)
        self.__this_file_menu.add_separator()
        self.__this_file_menu.add_command(label='Exit', command=self.__quitApplication)
        self.__this_menu_bar.add_cascade(label='File', menu=self.__this_file_menu) 
        self.__this_edit_menu.add_command(label="Cut", command=self.__cut)              
        self.__this_edit_menu.add_command(label="Copy", command=self.__copy)
        self.__this_edit_menu.add_command(label="Paste", command=self.__paste) 
        self.__this_menu_bar.add_cascade(label="Edit", menu=self.__this_edit_menu)
        self.__this_help_menu.add_command(label="About VincePad", command=self.__showAbout)  
        self.__this_menu_bar.add_cascade(label="Help", menu=self.__this_help_menu) 
        self.__root.config(menu=self.__this_menu_bar) 
        self.__this_scroll_bar.pack(side=RIGHT,fill=Y)        
        self.__this_scroll_bar.config(command=self.__this_text_area.yview)      
        self.__this_text_area.config(yscrollcommand=self.__this_scroll_bar.set)
        
    def __quitApplication(self):
        self.__root.destroy()
        
    def __showAbout(self):
        showinfo("VincePad","Created by Vincent Fiorucci" \
            "\nVersion 1.0") 
        
    def __openFile(self):
        self.__file = askopenfilename(defaultextension=".txt", 
                                      filetypes=[("All Files","*.*"), 
                                        ("Text Documents","*.txt")]) 
  
        if self.__file == "": 
            self.__file = None
        else: 
            self.__root.title(os.path.basename(self.__file) + " - VincePad") 
            self.__this_text_area.delete(1.0,END) 
            file = open(self.__file,"r") 
            self.__this_text_area.insert(1.0,file.read()) 
            file.close() 
    
    def __newFile(self):
        self.__root.title('Untitled - VincePad')
        self.__file = None
        self.__this_text_area.delete(1.0,END)

    def __saveFile(self):
        if self.__file == None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                       ("Text Documents","*.txt")])
            if self.__file == '':
                self.__file = None
            else:
                file = open(self.__file,'w')
                file.write(self.__this_text_area.get(1.0,END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + ' - VincePad')
        else:
            file = open(self.__file, 'w')
            file.write(self.__this_text_area.get(1.0,END))
            file.close()
            
    def __cut(self): 
        self.__this_text_area.event_generate("<<Cut>>") 
  
    def __copy(self): 
        self.__this_text_area.event_generate("<<Copy>>") 
  
    def __paste(self): 
        self.__this_text_area.event_generate("<<Paste>>") 
  
    def run(self): 
        self.__root.mainloop() 
        
VincePad = VincePad(width=800,height=2000) 
VincePad.run() 