import tkinter

drawing = False
lineIndex = 0
lineNum = {}

def drawLine(event):
    global curLine
    global initXCoords
    global initYCoords

    global drawing
    global lineIndex
    global lineNum

    if drawing:
        drawing = False
        lineIndex += 1
        lineNum["line{0}".format(lineIndex)] = curLine

    else:
        drawing = True
        initXCoords = event.x
        initYCoords = event.y
        curLine = rootCanvas.create_line(initXCoords, initYCoords, event.x, event.y)


def lineMove(event):
    if drawing:
        rootCanvas.coords(curLine, initXCoords, initYCoords, event.x, event.y)

root = tkinter.Tk()
root.geometry("1920x1080")
rootCanvas = tkinter.Canvas(root)
rootCanvas.pack(fill="both", expand=True)

root.bind("<Button-1>", drawLine)
root.bind("<Motion>", lineMove)


root.mainloop()