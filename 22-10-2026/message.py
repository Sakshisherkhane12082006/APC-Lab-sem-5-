from tkinter import *

main = Tk()

ourMessage = 'This is our Message'

messageVar = Message(main, text=ourMessage)

messageVar.config(bg='black')

messageVar.pack()

main.mainloop()