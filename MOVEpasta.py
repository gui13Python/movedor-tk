from ctypes.wintypes import DOUBLE
from plistlib import InvalidFileException
from tkinter  import *
import tkinter
from tkinter.ttk import Progressbar
from turtle import width
from numpy import size
import pyautogui
import os 
from shutil import ExecError, copyfile
from tkinter import filedialog
import time
from tkinter  import ttk


telacopy = Tk()




varbarra= DoubleVar()
varbarra.set(0)


lbpasta1 = PhotoImage(file=r'C:\\Users\\PC python\\Desktop\\copiador tk\\movedor pasta\\Search_Folder_25890.png')
lbpasta2 = PhotoImage(file=r'C:\\Users\\PC python\\Desktop\\copiador tk\\movedor pasta\\Search_Folder_25890.png')
btfoto = PhotoImage(file=r'C:\\Users\\PC python\\Desktop\\copiador tk\\movedor pasta\Download_icon-icons.com_75235.png')

#telacopy.attributes("-transparentcolor","black")

def OpenORIGEM():
    aqui = os.getcwd()
    global origem
    origem = tkinter.filedialog.askdirectory(initialdir= aqui,title="Dialog box")  #"'C:\\Users\\PC python\Desktop\\copiador tk\\testeprogama"
    #origem = pyautogui.prompt(text='orinem', title='pasta oriem' , default='')
     

def OpenDESTINO():
    aqui = os.getcwd()
    global destino
    #destino = pyautogui.prompt(text='destino', title='pasta destino' , default='')
    destino = tkinter.filedialog.askdirectory(initialdir= aqui,title="Dialog box")  #r"'C:\\Users\\PC python\\Desktop\\copiador tk\\testeprogama"
                                          




def copia(m):
    global origem
    global destino
    global size2
    
    os.chdir(str(origem))
    os.listdir(origem)
    
    os.listdir(destino)
    s = "\\"
    for origem in os.listdir():
        os.rename(origem, destino  + s + origem  )
        
        print("essa é origem"+origem)
        size2 = 0
    for i in os.scandir(destino): 
            size2 += os.path.getsize(i)
               
            
        
        
          
            #def barra(m):
            cont = 0
            etapas=m/100
            while cont < etapas:
                cont=cont+1
                i=0
                while i<1000000:
                    i=i+1
                varbarra.set(cont)
                telacopy.update()
            print("este é size2",size2) 
            print("este é o i ", i)
            print("este é destino" , destino)

    
    
            
    
      

            
            
            
            
            
            
            
            
            




origem ="origem"
def openPasta():
    global origem
    origem = tkinter.filedialog.askopenfilename(filetypes=[("all Files", "*.*")])
    #tkinter.filedialog.askopenfilename(filetypes=[("Mp3 Files", "*.mp3")])  #[("Mp3 Files", "*.mp3")])



    

orin = Label(telacopy,text='PASTA DE ORINGEM',fg='blue',bg='light gray',image=lbpasta1).place(x=200,y=10)
orinBT = Button(telacopy,text='Abrir Pasta',highlightbackground = "black", 
                         highlightthickness = 2, bd=0 , width=20, fg='blue',bg='light gray',command=openPasta).place(x=150,y=3)




orin = Label(telacopy,text='PASTA DE ORINGEM',fg='blue',bg='light gray',image=lbpasta1).place(x=330,y=10)
orinBT = Button(telacopy,text='Select pasta de origem',highlightbackground = "black", 
                         highlightthickness = 2, bd=0 , width=20, fg='green',bg='light gray',command=OpenORIGEM).place(x=275 ,y=3)

destin = Label(telacopy,text='PASTA DE DESTINO',fg='blue',bg='light gray',image=lbpasta2).place(x=460,y=10)


destinoBT = orinBT = Button(telacopy,text='Select pasta de destino',highlightbackground = "black", 
                         highlightthickness = 2, bd=0,  width=20, fg='red',bg='light gray',command=OpenDESTINO).place(x=410,y=3)


FRA = LabelFrame(telacopy, width=695,height=338,bg='white').place(x=5,y=60)



BTenvia = Button(telacopy,image=btfoto,width=120,height=50, text='COPIAR',fg='blue',command= lambda:copia(1000)).place(x=574,y=1)

pb=ttk.Progressbar(FRA,variable=varbarra,maximum=10,length=690)  
pb.place(x=7,y=372)


                                                                                                  #

telacopy.configure(background='light gray')
telacopy.iconbitmap('in.ico')
telacopy.title('copiador de arquivos')
telacopy.geometry('705x400')
telacopy.mainloop()