from Tkinter import *
root = Tk()

def callback(event):
    print "clicked at", event.x, event.y

if __name__ == "__main__":
    frame=Frame(root, width=100, height=100)
    frame.bind("<Button-1>", callback)
    frame.pack()
    frame.mainloop()