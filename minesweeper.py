from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCursor
import sys, threading, pygame

difficulty=0
pygame.init()
def pygameStuff():
    global window
    minesweeper=pygame.Surface()
    while True:
        mousePos=(QCursor.pos().x()-window.frameGeometry().topLeft().x(),QCursor.pos().y()-window.frameGeometry().topLeft().y()-23)
pygameThread=threading.Thread(target=pygameStuff)
def buttonPressed(action):
    global difficulty
    if action.text()=="Beginner":
        difficulty=0
    elif action.text()=="Intermediate":
        difficulty=1
    elif action.text()=="Expert":
        difficulty=2
    elif action.text()=="Custom...":
        difficulty=3

    print(action.text() +" pressed.")
app=QApplication(sys.argv)
window=QMainWindow()
m=QMenuBar(window)
game=m.addMenu("Game")
newGame=QAction("New")
newGame.setShortcut("F2")
game.addAction(newGame)
game.addSeparator()
beginner=QAction("Beginner")
beginner.setCheckable(True)
beginner.setChecked(True)
game.addAction(beginner)
intermediate=QAction("Intermediate")
intermediate.setCheckable(True)
game.addAction(intermediate)
expert=QAction("Expert")
expert.setCheckable(True)
game.addAction(expert)
custom=QAction("Custom...")
custom.setCheckable(True)
game.addAction(custom)
game.addSeparator()
marks=QAction("Marks(?)")
marks.setCheckable(True)
marks.setChecked(True)
game.addAction(marks)
game.triggered[QAction].connect(buttonPressed)
window.setGeometry(1280,720,200,50)
window.setWindowTitle("PyQt")
window.show()
pygameThread.setDaemon(True)
pygameThread.start()
app.exec_()
print('ok')
