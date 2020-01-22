from PyQt5.Qt import *
import sys, PIL

class MinesweeperWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.m = QMenuBar(self)
        self.game = self.m.addMenu("Game")
        self.newGame = QAction("New",self)
        self.newGame.setShortcut("F2")
        self.game.addAction(self.newGame)
        self.game.addSeparator()
        self.beginner = QAction("Beginner",self)
        self.beginner.setCheckable(True)
        self.beginner.setChecked(True)
        self.game.addAction(self.beginner)
        self.intermediate = QAction("Intermediate",self)
        self.intermediate.setCheckable(True)
        self.game.addAction(self.intermediate)
        self.expert = QAction("Expert",self)
        self.expert.setCheckable(True)
        self.game.addAction(self.expert)
        self.custom = QAction("Custom...",self)
        self.custom.setCheckable(True)
        self.game.addAction(self.custom)
        self.game.addSeparator()
        marks = QAction("Marks(?)",self)
        marks.setCheckable(True)
        marks.setChecked(True)
        self.game.addAction(marks)
        color = QAction("Color",self)
        color.setCheckable(True)
        color.setChecked(True)
        self.game.addAction(color)
        sound = QAction("Sound",self)
        sound.setCheckable(True)
        sound.setChecked(False)
        self.game.addAction(sound)
        self.game.addSeparator()
        self.game.addAction("Best Times...")
        self.game.addSeparator()
        exit_ = QAction("Exit_",self)
        self.game.addAction(exit_)
        help = self.m.addMenu("Help")
        contents=QAction("Contents",self)
        contents.setShortcut("F1")
        help.addAction(contents)
        self.game.triggered[QAction].connect(self.buttonPressed)
        exit_.triggered.connect(sys.exit)
        self.setGeometry(1280, 720, 200, 50)
        timer = QTimer(self)
        timer.timeout.connect(self.pygameLoop)
        timer.start(1)
        self.setWindowTitle("Minesweeper")
        self.show()
    def pygameLoop(self):
        global window
        mousePos = (QCursor.pos().x() - window.frameGeometry().topLeft().x(),
                    QCursor.pos().y() - window.frameGeometry().topLeft().y() - 23)
        # print(mousePos)
    def buttonPressed(self,action):
        if action.text() == "Beginner":
            self.intermediate.setChecked(False)
            self.expert.setChecked(False)
            self.custom.setChecked(False)
        elif action.text() == "Intermediate":
            self.beginner.setChecked(False)
            self.expert.setChecked(False)
            self.custom.setChecked(False)
        elif action.text() == "Expert":
            self.beginner.setChecked(False)
            self.intermediate.setChecked(False)
            self.custom.setChecked(False)
        elif action.text() == "Custom...":
            self.beginner.setChecked(False)
            self.intermediate.setChecked(False)
            self.expert.setChecked(False)
        print(action.text() + " pressed.")
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button()==Qt.LeftButton:
            print("left button")
        elif QMouseEvent.button()==Qt.RightButton:
            print("right button")
app=QApplication(sys.argv)
window=MinesweeperWindow()
if __name__=="__main__":
    sys.exit(app.exec_())
