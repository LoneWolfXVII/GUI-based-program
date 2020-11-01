from tkinter import *
from subprocess import Popen, PIPE

def callAPSP():
    Popen(['python','Floyd_Warshall_GUI.py'])

#def callAssemblyline():
    #Popen(['python','assemblyLineScheduling_GUI.py'])

def callmatrixchain():
    Popen(['python','matrixchain_GUI.py'])

def callLCS():
    Popen(['python','LCS_GUI.py'])

def callknapsack():
    Popen(['python','knapsack_GUI.py'])


mainWindow = Tk()
mainWindow.title("Dynamic Programming")
#this logo might not be in your pc so commenting out
#mainWindow.iconbitmap('D:/DOCUMENTS/SEM 4/Assignments/Logo.ico')

lbl_select = Label(text="Select Algorithm:\n",bd=5)
lbl_select.grid(row=0,column=0,columnspan=2)

btn_APSP = Button(
    master=mainWindow,
    text="All Pair Shortest Path",
    width = 25,
    pady=20,
    padx=30,
    command=callAPSP,
    bd=3
)
btn_APSP.grid(row=2,column=0)

#btn_Assemblyline = Button(
#    master=mainWindow,
#    text="Assembly Line Scheduling",
#    width = 25,
#    pady=20,
#    padx=30,
#    command=callAssemblyline,
#    bd=3
#)
#btn_Assemblyline.grid(row=2,column=1)


btn_matrixchain = Button(
    master=mainWindow,
    text="Matrix Chain Multiplication",
    width = 25,
    pady=20,
    padx=30,
    command=callmatrixchain,
    bd=3
)
btn_matrixchain.grid(row=2,column=1)

btn_LCS = Button(
    master=mainWindow,
    text="Longest Common Subsequence",
    width = 25,
    pady=20,
    padx=30,
    command=callLCS,
    bd=3
)
btn_LCS.grid(row=3,column=0)

btn_knapsack = Button(
    master=mainWindow,
    text="0/1 knapsack",
    width = 25,
    pady=20,
    padx=30,
    command=callknapsack,
    bd=3
)
btn_knapsack.grid(row=3,column=1)

btn_exit = Button(
    master=mainWindow,
    text="EXIT!",
    width = 25,
    pady=20,
    padx=30,
    command=exit,
    bd=3
)
btn_exit.grid(row=4,column=0,columnspan=2)

lbl_author = Label(
    mainWindow,
    text="\nWritten by Nischal Gupta (18103063)"
        +"\nPlatform used: Python3 with Tkinter library",
    bd=3
)
lbl_author.grid(row=8,column=0,columnspan=2)

mainWindow.mainloop()
