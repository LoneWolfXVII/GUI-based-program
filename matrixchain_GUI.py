from tkinter import *
import matrixchain

mainWindow = Tk()
mainWindow.title('Matrix Chain Multiplication:')
#mainWindow.iconbitmap('D:/DOCUMENTS/SEM 4/Assignments/DAA/Logo.ico')

arr = []
frames = []
labels = []

def createElement():
    global arr
    global frames

    frame = Frame(mainWindow, borderwidth=1)
    frames.append(frame)

    frame.pack(side="top")

    lbl_arr = Label(frame, text="Element " + str(len(frames)) + ":")
    labels.append(lbl_arr)
    lbl_arr.pack(side="left")

    ent_arr = Entry(master=frame, width = 5, borderwidth = 2)
    arr.append(ent_arr)
    ent_arr.pack(side="left")

inputArr = []

def calculate():
    global arr
    global array
    for i in range(len(arr)):
        array = arr[i].get()
        inputArr.append(int(array))
    print(inputArr)
    size = len(arr)
    lbl_arraySize = Label(mainWindow,text="Size of array: " + str(size))
    lbl_arraySize.pack()
    global lbl_MCM
    lbl_MCM.pack_forget()

    minMul = matrixchain.MatrixChainOrder(inputArr,size)
    lbl_minMul = Label(mainWindow,text="Minimum number of multiplications is: "+ str(minMul))
    lbl_minMul.pack()
    lbl_complexity = Label(mainWindow, text='''
        Time Complexity: O(n^3)
        where n is size of the array''')
    lbl_complexity.pack()


lbl_intro = Label(mainWindow,
    bd=5,
    text= '''Given an array p[] which represents the chain of matrices
     such that the ith matrix Ai is of dimension p[i-1] x p[i].
     The algorithm returns the minimum number of multiplications
     needed to multiply the chain.'''
     "\n\n<<<INSTRUCTIONS>>>"
     +"\nUse the 'Add Element' button to add as many elements in the array"
     +"\nThen, use the 'Run' button to save the input and get the result."
     +"\nThe output will be displayed along with the Complexity of the Algorithm")
lbl_intro.pack()


frm_elements = Frame(master=mainWindow, width=60, borderwidth=3)
#lbl_elements = Label(master=frm_elements, text="Enter array elements: ", width=25)
#lbl_elements.pack(side="left")
btn_addElement = Button(frm_elements, text="Add Element",command = createElement)
btn_addElement.pack(side="left")

frm_elements.pack()


frm_endButtons = Frame(mainWindow)
frm_endButtons.pack(side="bottom")
btn_selectItems = Button(frm_endButtons, text="RUN!", command=calculate)
btn_selectItems.pack()
lbl_MCM = Label()

mainWindow.mainloop()
