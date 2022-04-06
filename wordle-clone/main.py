import tkinter as tk
from tkinter import *

# Variable declarations
instructionsArray = []

# Function declarations
def RemoveInstructions():
	for a in instructionsArray:
		a.pack_forget()

def resizeEvent():
	widthSelf=win.winfo_width()
	return widthSelf
	# resizeEvent()


def windowChange():
	width=win.winfo_width()

# def findXCenter(self, canvas, item):
#       coords = canvas.bbox(item)
#       xOffset = (self.windowWidth / 2) - ((coords[2] - coords[0]) / 2)
#       return xOffset

# def makeAsBigAsScreen(self):
# 	return self.windowWidth
# # Code
win = Tk()
win.title('Wordle')
win.geometry('500x500')


width = resizeEvent()
widthTest=win.winfo_width()
widthTest2 = widthTest
# frame = Frame(win)

instructionsTitle = tk.Label(win, text="This is a test\n Test")
instructions = Text(win, height=8, bg="#fff")

print(width)

instructions_canva = Canvas(win, bg="SpringGreen2")
instructions_canva.create_text(width/2, 50, text="Welcome to my shitty version of Wordle", fill="black")
instructions_canva.place(relx=.5, rely=5, anchor="center")
btn = Button(win,text="Click to close instructions", command=RemoveInstructions)

instructionsArray.append(instructionsTitle)
instructionsArray.append(instructions)
instructionsArray.append(instructions_canva)
instructionsArray.append(btn)

for a in instructionsArray:
	a.pack()


win.update_idletasks() 

win.mainloop()