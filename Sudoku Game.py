#Name: Qianyi Ma
#Purpose: Sudoku Game

from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import random

# create a window (instructions)
window1 = Tk()
window1.title('Sudoku Game')
window1.geometry('400x400')
window1.config(background='#98a2af')

# create a menubar for user to quit the program
menubar = Menu(window1)
quitmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Quit', menu=quitmenu)
quitmenu.add_command(label='Quit', command=exit)
window1.config(menu = menubar)

# a label to show where to quit the program
quitlabel = Label(window1, text='👆Quit the program', font=('Consolas', 8), bg='#98a2af')
quitlabel.pack(anchor='nw')

# create three frame
topframe = Frame(window1, relief=GROOVE, borderwidth=5, bg='#98a2af')
middleframe = Frame(window1, relief=RAISED, borderwidth=5, bg='#98a2af')
bottomframe = Frame(window1, borderwidth=20, bg='#98a2af')
topframe.pack()
middleframe.pack()
bottomframe.pack()

# create the instruction label
instruction1 = Label(topframe, text='Welcome to Sudoku Game\n\n\
Choose which type of sudoku you would like to solve\n👇', font=('consolas', 10))
instruction1.pack()

# create a IntVar to store the user's choice
userchoice = IntVar()
userchoice.set(1)

# create two radio buttons for the user to select whether 4x4 or 9x9 Sudoku
radiobutton4x4 = Radiobutton(middleframe, text='4 x 4', variable=userchoice, value=1)
radiobutton9x9 = Radiobutton(middleframe, text='9 x 9', variable=userchoice, value=2)
radiobutton4x4.pack()
radiobutton9x9.pack()

# record how many sudoku the user solved
totalsolved = 0


# display random sudoku
def Show_Sudoku():
    global random4x4, random9x9, image4x4, image9x9, theuserchoice, show_sudoku_image
    # create a new window
    show_sudoku_image = Toplevel()
    
    # topmost
    show_sudoku_image.attributes('-topmost', 'true')
    
    # store the user-selected Sudoku type
    theuserchoice = userchoice.get()
    
    # According to the user's choice, display a random sudoku
    if theuserchoice == 1:
        random4x4 = str(random.randint(1, 12))
        image4x4 = ImageTk.PhotoImage(Image.open(rf'4x4\q{random4x4}.png'))
        image_label_4x4 = Label(show_sudoku_image, image=image4x4)
        image_label_4x4.pack()
        Enter_Answer_4x4()
        
    else:
        random9x9 = str(random.randint(1, 12))
        image9x9 = ImageTk.PhotoImage(Image.open(rf'9x9\q{random9x9}.png'))
        image_label_9x9 = Label(show_sudoku_image, image=image9x9)
        image_label_9x9.pack()
        Enter_answer_9x9()


# user input the answer (4x4)
def Enter_Answer_4x4():
    global entries_4x4, enterwindow4x4
    # create a new window
    enterwindow4x4 = Toplevel()
    enterwindow4x4.config(background='#98a2af')
    
    # topmost
    enterwindow4x4.attributes('-topmost', 'true')
    
    # instructions
    label_objective = Label(enterwindow4x4, text='''Objective: to fill a 4 x 4 grid with digits
so that each column, each row, and each of the nine 2 x 2 subgrids
that compose the grid contains all of the digits from 1 to 4.''', fg='#05423e', font=('Kristen ITC', 10), bg='#cee6f5')
    label_objective.pack()
    label_blank = Label(enterwindow4x4, text="Enter your answer", bg='#98a2af', font=('Consolas', 10))
    label_blank2 = Label(enterwindow4x4, text="Don't leave any entry box blank", fg='red', bg='#98a2af', font=('Consolas', 10))
    label_blank.pack()
    label_blank2.pack()
    
    # create 4 by 4 entry boxes
    entries_4x4 = []
    for i in range(4):
        tempframe = Frame(enterwindow4x4)
        tempframe.pack()
        temp = []
        for j in range(4):
            entry = Entry(tempframe, width=3, justify='center')
            entry.pack(side=LEFT)
            temp.append(entry)
        entries_4x4.append(temp)
    
    # create a submit button
    submitanswer = Button(enterwindow4x4, text='Submit Answer', command=Check_Answer_4x4, bg='#bad1db', font=('Consolas', 10))
    submitanswer.pack()


# user input the answer (9x9)
def Enter_answer_9x9():
    global entries_9x9, enterwindow9x9
    # create a new window
    enterwindow9x9 = Toplevel()
    enterwindow9x9.config(background='#98a2af')
    
    # topmost
    enterwindow9x9.attributes('-topmost', 'true')
    
    # instructions
    label_objective = Label(enterwindow9x9, text='''Objective: to fill a 9 x 9 grid with digits
so that each column, each row, and each of the nine 3 x 3 subgrids
that compose the grid contains all of the digits from 1 to 9.''', fg='#05423e', font=('Kristen ITC', 10), bg='#cee6f5')
    label_objective.pack()
    label_blank = Label(enterwindow9x9, text="Enter your answer", bg='#98a2af', font=('Consolas', 10))
    label_blank2 = Label(enterwindow9x9, text="Don't leave any entry box blank", fg='red', bg='#98a2af', font=('Consolas', 10))
    label_blank.pack()
    label_blank2.pack()
    
    # create 9 by 9 entry boxes
    entries_9x9 = []
    for i in range(9):
        tempframe = Frame(enterwindow9x9)
        tempframe.pack()
        temp = []
        for j in range(9):
            entry = Entry(tempframe, width=3, justify='center')
            entry.pack(side=LEFT)
            temp.append(entry)
        entries_9x9.append(temp)
        
    # create a submit button
    submitanswer = Button(enterwindow9x9, text='Submit Answer', command=Check_Answer_9x9, bg='#bad1db', font=('Consolas', 10))
    submitanswer.pack()


# check the user's answer (4x4)
# if the user's answer is incorrect, call Wrong() function
# if the user's answer is correct, call Correct() function
def Check_Answer_4x4():
    # get the numbers from those entry boxes
    sudoku_grid_4x4 = []
    for i in entries_4x4:
        temp = []
        for j in i:
            temp.append(j.get().strip())
        sudoku_grid_4x4.append(temp)
    
    # input validation
    for i in range(4):
        for j in range(4):
            if sudoku_grid_4x4[i][j].isdigit() == False or int(sudoku_grid_4x4[i][j]) > 4 or int(sudoku_grid_4x4[i][j]) < 1:
                tkinter.messagebox.showerror('Invalid input', 'Please enter valid values')
                cancontinue = False
                return
    
    # Check if each row has no repeated number
    for x in range(4):
        temp = set()
        for y in range(4):
            temp.add(sudoku_grid_4x4[y][x])
        if len(temp) != 4:
            Wrong()
            return
    
    # Check if each column has no repeated number
    for x in range(4):
        temp = set(sudoku_grid_4x4[x])
        if len(temp) != 4:
            Wrong()
            return

    # Check if each smaller 2x2 square has no repeated number
    for x in range(0, 3, 2):
        for y in range(0, 3, 2):
            temp = set()
            temp.add(sudoku_grid_4x4[x][y])
            temp.add(sudoku_grid_4x4[x][y+1])

            temp.add(sudoku_grid_4x4[x+1][y])
            temp.add(sudoku_grid_4x4[x+1][y+1])
            
            if len(temp) != 4:
                Wrong()
                return
    
    # if the user answer correctly, call Correct() function
    Correct(1)
    return


# check the user's answer (9x9)
# if the user's answer is incorrect, call Wrong() function
# if the user's answer is correct, call Correct() function
def Check_Answer_9x9():
    # get the numbers from those entry boxes
    sudoku_grid_9x9 = []
    for i in entries_9x9:
        temp = []
        for j in i:
            temp.append(j.get().strip())
        sudoku_grid_9x9.append(temp)
    
    # input validation
    for i in range(9):
        for j in range(9):
            if sudoku_grid_9x9[i][j].isdigit() == False or int(sudoku_grid_9x9[i][j]) > 9 or int(sudoku_grid_9x9[i][j]) < 1:
                tkinter.messagebox.showerror('Invalid input', 'Please enter valid values')
                cancontinue = False
                return
    
    
    # Check if each row has no repeated number
    for x in range(9):
        temp = set()
        for y in range(9):
            temp.add(sudoku_grid_9x9[y][x])
        if len(temp) != 9:
            Wrong()
            return
    
    # Check if each column has no repeated numbe
    for x in range(9):
        temp = set(sudoku_grid_9x9[x])
        if len(temp) != 9:
            Wrong()
            return
    
    # Check if each smaller 3x3 square has no repeated number
    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            temp = set()
            temp.add(sudoku_grid_9x9[x][y])
            temp.add(sudoku_grid_9x9[x][y+1])
            temp.add(sudoku_grid_9x9[x][y+2])
            
            temp.add(sudoku_grid_9x9[x+1][y])
            temp.add(sudoku_grid_9x9[x+1][y+1])
            temp.add(sudoku_grid_9x9[x+1][y+2])
            
            temp.add(sudoku_grid_9x9[x+2][y])
            temp.add(sudoku_grid_9x9[x+2][y+1])
            temp.add(sudoku_grid_9x9[x+2][y+2])
            
            if len(temp) != 9:
                Wrong()
                return
    
    # if the user answer correctly, call Correct() function
    Correct(2)        
    return


# if the user's answer is correct, create a pop-up window
def Correct(choice):
    global totalsolved
    
    # update the numbers of solved sudokus
    totalsolved += 1
    totalsolvedlabel.config(text=f'Total solved: {totalsolved}')
    
    # if the user's answer is correct, create a pop-up window
    tkinter.messagebox.showinfo('Congratulations', "That's Correct!")
    
    # destroy other Toplevels
    show_sudoku_image.destroy()
    if choice == 1:
        enterwindow4x4.destroy()
    else:
        enterwindow9x9.destroy()


# check if the user answer the math question correctly
def Check_Math():
    global answer
    # if the answer is correct, show the correct answer of the sudoku
    if float(questionentry.get()) == mathquestions[randomquestion]:
        if theuserchoice == 1:
            answer = ImageTk.PhotoImage(Image.open(rf'4x4\a{random4x4}.png'))
            image_label_4x4 = Label(wronganswer, image=answer)
            image_label_4x4.pack()
        else:
            answer = ImageTk.PhotoImage(Image.open(rf'9x9\a{random4x4}.png'))
            image_label_9x9 = Label(wronganswer, image=answer)
            image_label_9x9.pack()
            
    # otherwise, let the user try again
    else:
        wrongmath = Label(wronganswer, text='Try Again...', fg='red')
        wrongmath.pack()


# a function for destroying Toplevels
def windowdestroy():
    wronganswer.destroy()
    if theuserchoice == 1:
        enterwindow4x4.destroy()
    else:
        enterwindow9x9.destroy()
    show_sudoku_image.destroy()


# if the user's answer is inccorect
# give the user a math question
# if they answer correctly
# show the correct answer of the sudoku
def Wrong():
    global questionentry, mathquestions, wronganswer, randomquestion
    # create a list of math questions
    mathquestions = [100 * 100, 200 / 10, 15 * 15, 123 + 456, 987 - 321]
    mathquestionsstr = ['100 * 100', '200 / 10', '15 * 15', '123 + 456', '987 - 321']
    
    # create a new window
    wronganswer = Toplevel()
    wronganswer.attributes('-topmost', 'true')
    wronganswer.config(background='#98a2af')
    
    # create a button for user to go back to the main window
    # (destroy every Toplevels)
    returntomainwindow = Button(wronganswer, text='Return to main window', font=('Consolas', 8), fg='red', bg='#bad1db', command=windowdestroy)
    returntomainwindow.pack(anchor=NE)
    
    # choose a random math question
    randomquestion = random.randint(0, 4)
    
    # instruction
    wronglabel = Label(wronganswer, text="That's incorrect...😅😅😅\nHere is a math question.\n\
If you answer it correctly, I will tell you the answer of that sudoku.", fg='#154a27',bg='#98a2af', font=('Consolas', 10))
    wronglabel2 = Label(wronganswer, text=str(mathquestionsstr[randomquestion]), font=('Consolas', 10), bg='#08243d', fg='white')
    wronglabel.pack()
    wronglabel2.pack()
    
    # create an entry box for user to input the answer
    questionentry = Entry(wronganswer, justify='center')
    questionentry.pack()
    
    # create a button for user to submit the answer
    questionsubmit = Button(wronganswer, text='Submit', command=Check_Math, bg='#bad1db', font=('Consolas', 10))
    questionsubmit.pack()
    


# create a button for user to submit the selection
submitselection = Button(bottomframe, text='Submit Selection', command=Show_Sudoku, font=('Consolas', 10), bg='#bad1db')
submitselection.pack()

# show the number of sudoku that have been solved
totalsolvedlabel = Label(bottomframe, text=f'Total solved: {totalsolved}', font=('Consolas', 10), bg='#98a2af', fg='red')
totalsolvedlabel.pack()

# an image
sudoku = ImageTk.PhotoImage(Image.open('sudoku.jpg').resize((333, 250), Image.NEAREST))
sudokulabel = Label(window1, image=sudoku)
sudokulabel.pack(side=BOTTOM)

# run the window
window1.mainloop()


# images from: 
# 1. Google Images
# 2. https://www.shutterstock.com/en/search/sudoku