from tkinter import *

root = Tk()
memory = []
counter = 0
buttonNums = []
personalCounter = []

answer = ''
answerText = Label(root, text='No answer!')
def clear():
    global answer
    answerText.configure(text='No answer!')
    answer = ''


def evaluate():
    global answer
    try:
        answerText.configure(text=eval(answer))
        answer = eval(answer)
    except:
        answerText.configure(text='Error!')
        answer = ''

def updateAnswer(number):
    global answer
    global answerText
    answer = '%s%s' % (answer, str(number))
    answerText.configure(text=answer)

answerText.grid(row=0,  column=2)

button0 = Button(root, text=0, command = lambda : updateAnswer(0), height=1, width=7)
button0.grid(row=2, column=1)
button1 = Button(root, text=1, command = lambda : updateAnswer(1), height=1, width=7)
button1.grid(row=2, column=2)
button2 = Button(root, text=2, command = lambda : updateAnswer(2), height=1, width=7)
button2.grid(row=2, column=3)
button3 = Button(root, text=3, command = lambda : updateAnswer(3), height=1, width=7)
button3.grid(row=2, column=4)
button4 = Button(root, text=4, command = lambda : updateAnswer(4), height=1, width=7)
button4.grid(row=3, column=1)
button5 = Button(root, text=5, command = lambda : updateAnswer(5), height=1, width=7)
button5.grid(row=3, column=2)
button6 = Button(root, text=6, command = lambda : updateAnswer(6), height=1, width=7)
button6.grid(row=3, column=3)
button7 = Button(root, text=7, command = lambda : updateAnswer(7), height=1, width=7)
button7.grid(row=3, column=4)
button8 = Button(root, text=8, command = lambda : updateAnswer(8), height=1, width=7)
button8.grid(row=4, column=1)
button9 = Button(root, text=9, command = lambda : updateAnswer(9), height=1, width=7)
button9.grid(row=4, column=2)
buttonPlus = Button(root, text='+', command = lambda : updateAnswer('+'), height=1, width=7)
buttonPlus.grid(row=4, column=3)
buttonMinus = Button(root, text='-', command = lambda : updateAnswer('-'), height=1, width=7)
buttonMinus.grid(row=4, column=4)
buttonTimes = Button(root, text='*', command = lambda : updateAnswer('*'), height=1, width=7)
buttonTimes.grid(row=5, column=1)
buttonDivide = Button(root, text='/', command = lambda : updateAnswer('/'), height=1, width=7)
buttonDivide.grid(row=5, column=2)
buttonClear = Button(root, text='Clear', command = clear, height=1, width=7)
buttonClear.grid(row=5, column=3)
buttonEqual = Button(root, text='=', command = evaluate, height=1, width=7)
buttonEqual.grid(row=5, column=4)


root.mainloop()

