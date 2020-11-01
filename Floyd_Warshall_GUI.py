from tkinter import *
import Floyd_Warshall

mainWindow = Tk()
mainWindow.title("Floyd Warshall Algorithm:")
#mainWindow.iconbitmap('D:/DOCUMENTS/SEM 4/Assignments/DAA/Logo.ico')

graph = []

def getVertices():
    V = ent_vertices.get()
    lbl_graph = Label(mainWindow, text="Graph initialized with " + str(V) + " vertices")
    lbl_graph.pack()
    btn_addEdge.pack(side="top")

def enter():
    global graph

    V = ent_vertices.get()

    #making a 2d(matrix) input field
    class SimpleTableInput(Frame):
        def __init__(self, parent, rows, columns):
            Frame.__init__(self, parent)

            self._entry = {}
            self.rows = rows
            self.columns = columns

            # register a command to use for validation
            vcmd = (self.register(self._validate), "%P")

            # create the table of widgets
            for row in range(self.rows):
                for column in range(self.columns):
                    index = (row, column)
                    e = Entry(self, validate="key", validatecommand=vcmd)
                    e.grid(row=row, column=column, stick="nsew")
                    self._entry[index] = e
            # adjust column weights so they all expand equally
            for column in range(self.columns):
                self.grid_columnconfigure(column, weight=1)
            # designate a final, empty row to fill up any extra space
            self.grid_rowconfigure(rows, weight=1)

        def get(self):
            '''Return a list of lists, containing the data in the table'''
            result = []
            for row in range(self.rows):
                current_row = []
                for column in range(self.columns):
                    index = (row, column)
                    current_row.append(self._entry[index].get())
                result.append(current_row)
            return result

        def _validate(self, P):
            '''Perform input validation.

            Allow only an empty value, or a value that can be converted to a float
            '''
            if P.strip() == "":
                return True

            try:
                f = float(P)
            except ValueError:
                self.bell()
                return False
            return True

    class Example(Frame):

        def __init__(self, parent):
            V = int(ent_vertices.get())
            Frame.__init__(self, parent)
            self.table = SimpleTableInput(self, V, V)
            self.submit = Button(self, text="Submit and Find All Pair Shortest Path", command=self.on_submit)
            self.table.pack(side="top", fill="both", expand=True)
            self.submit.pack(side="bottom")

        def on_submit(self):
            costGraph = self.table.get()
            lbl_graph = Label(mainWindow, text="\nGiven Cost Matrix:",width=25)
            lbl_graph.pack()
            lbl_graphOutput = Label(mainWindow,text=costGraph)
            lbl_graphOutput.pack()

            V = int(ent_vertices.get())
            global lbl_result
            lbl_result.pack_forget()
            costGraph = [[int(int(j))  for j in i] for i in costGraph]
            result = Floyd_Warshall.floyd_warshall(costGraph,V) #calling function floyd_warshall from Floyd_Warshall.py
            lbl_result = Label(mainWindow,text="Shortest distance matrix:\n"+ str(result))
            lbl_result.pack()
            lbl_complexity = Label(mainWindow, text="Time Complexity: O(V^3)\n"+
                "here V is the number of vertices in the graph")
            lbl_complexity.pack()

    Example(mainWindow).pack(expand=True)

def readme():
    top = Toplevel()
    top.title("Algorithm Overview:")
    top.iconbitmap('D:/DOCUMENTS/SEM 4/Assignments/DAA/Logo.ico')
    lbl_intro= Label(top,
        bd=5,
        text= "Input Format:"
       +'''\ngraph = [ [0, 5, 99999, 10],
                     [9999, 0, 3, 99999],
                     [9999, 99999, 0,   1],
                     [99999, 99999, 99999, 0] ]'''

       +"\nNote that the value of graph[i][j] is 0 if i is equal to j"
       +"\nAnd graph[i][j] is INF (infinite) = 99999 if there is no edge from vertex i to j."

       +'''\nOutput:
       Shortest distance matrix
          0        5      8      9
        99999      0      3      4
        99999   99999     0      1
        99999   99999    99999   0'''
            +"\n\n<<<INSTRUCTIONS>>>"
            +"\nEnter the no. of vertices"
            +"\nThen, use the 'Input Cost Matrix' button to input as in Input Format."
            +"\nMake sure to follow input format."
            +"\nFinally, press the 'Submit and Find All Pair Shortest Path' button."
            +"\nThe output will be displayed along with the Complexity of the Algorithm"
    )
    lbl_intro.pack()


btn_readme = Button(master=mainWindow,bd=3,text="Read Me!",command=readme)
btn_readme.pack()



frm_vertices = Frame(master=mainWindow, width=60,borderwidth=3)
lbl_vertices = Label(frm_vertices, bd=5, text="Enter number of vertices: ",width=25)
lbl_vertices.pack(side="left")
ent_vertices = Entry(master=frm_vertices, width=20)
ent_vertices.pack(side="left")
btn_vertices = Button(master=frm_vertices, text="Enter",command = getVertices)
btn_vertices.pack(side="left")
frm_vertices.pack()

frm_endButtons = Frame(mainWindow,borderwidth=3)
frm_endButtons.pack(side="bottom")

btn_addEdge = Button(mainWindow,text="Input Cost Matrix",command=enter)
lbl_result = Label()

mainWindow.mainloop()
