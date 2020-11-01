from tkinter import *
import LCS

mainWindow = Tk()
mainWindow.title('Longest Common Subsequence:')
#mainWindow.iconbitmap('D:/DOCUMENTS/SEM 4/Assignments/DAA/Logo.ico')

maximum = 1000

def findLCS():
    global lbl_LCS
    global str1
    global str2

    str1 = ent_getstr1.get()
    lenStr1 = len(str1)
    print(lenStr1)

    str2 = ent_getstr2.get()
    lenStr2 = len(str2)
    print(lenStr2)

    lbl_LCS.pack_forget()

    dp = [[-1 for i in range(maximum)] for i in range(lenStr1)]

    lwstCmnSub = LCS.lcs(str1,str2,lenStr1,lenStr2,dp)

    lbl_LCS = Label(mainWindow,text="Length of LCS: " + str(lwstCmnSub))
    lbl_LCS.pack()
    lbl_complexity = Label(mainWindow, text='''
        Time Complexity: O(n*m)
        where n and m are the lengths of the strings''')
    lbl_complexity.pack()



lbl_intro = Label(mainWindow,
    bd=5,
    text= '''LCS Problem Statement: Given two sequences,
    find the length of longest subsequence present in
    both of them. A subsequence is a sequence that appears
    in the same relative order, but not necessarily contiguous.
    For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc
    are subsequences of “abcdefg”.'''
    +"\n\n<<<INSTRUCTIONS>>>"
    +"\nEnter two strings in the input area"
    +"\nUse the 'Find LCS!' button to find length of longest subsequence"
    +"\nThe output will be displayed along with the Complexity of the Algorithm")
lbl_intro.pack()


frm_getStr1 = Frame(mainWindow)
frm_getStr1.pack()
lbl_getstr1 = Label(frm_getStr1, text = 'Str1: ', bd=5)
lbl_getstr1.pack(side="left")
ent_getstr1 = Entry(frm_getStr1)
ent_getstr1.pack(side="left")
#btn_getStr1 = Button(frm_getStr1, text="Enter", command=getStr1)
#btn_getStr1.pack(side="left")

frm_getStr2 = Frame(mainWindow)
frm_getStr2.pack()
lbl_getstr2 = Label(frm_getStr2, text = 'Str2: ', bd=5)
lbl_getstr2.pack(side="left")
ent_getstr2 = Entry(frm_getStr2)
ent_getstr2.pack(side="left")
#btn_getStr2 = Button(frm_getStr2, text="Enter", command=getStr2)
#btn_getStr2.pack(side="left")

frm_endButtons = Frame(mainWindow)
frm_endButtons.pack(side="bottom")
btn_selectItems = Button(frm_endButtons, text="Find LCS!", command=findLCS)
btn_selectItems.pack()
lbl_LCS = Label()

mainWindow.mainloop()
