import sys

import firebase_admin.firestore
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QComboBox
)
from PyQt5.QtGui import QFont


class SetGesturewindow(QWidget):
    def __init__(self,username):
        self.db=firebase_admin.firestore.client()
        self.uname=username
        super().__init__()
        self.setWindowTitle("Change!")
        self.resize(850, 400)
        # Create a QVBoxLayout instance
        #welcome label
        infolab = QLabel(self)
        infolab.setFont(QFont('Ariel', 20))
        infolab.move(400, 2)
        infolab.setText("Hello"+" "+self.uname)
        infolab.show()

        infolab=QLabel(self)
        infolab.setFont(QFont('Ariel',10))
        infolab.move(20,40)
        infolab.setText("Available Gestures")
        infolab.show()

        #Thumbsuplabel
        tuplab=QLabel(self)
        tuplab.move(20,80)
        tuplab.setText("Thumbs Up")
        tuplab.show()


        # ThumbsdownLabel
        tdlab = QLabel(self)
        tdlab.move(20,140)
        tdlab.setText("Thumbs Down")
        tdlab.show()


        # stopLabel
        stlab = QLabel(self)
        stlab.move(20, 200)
        stlab.setText("Stop")
        stlab.show()
        # rockLabel
        rlab = QLabel(self)
        rlab.move(20, 260)
        rlab.setText("Rock")
        rlab.show()

        #combox
        self.cb1=QComboBox(self)
        self.cb1.move(150,80)
        self.cb1.addItems(["Open Notepad","Open Chrome","Open Youtube","Play Trending film"])
        self.cb1.show()
        self.cb2 = QComboBox(self)
        self.cb2.move(150, 140)
        self.cb2.addItems(["Open Notepad", "Open Chrome","Open Youtube","Play Trending film"])
        self.cb2.show()
        self.cb3 = QComboBox(self)
        self.cb3.move(150, 200)
        self.cb3.addItems(["Open Notepad", "Open Chrome","Open Youtube","Play Trending film"])
        self.cb3.show()
        self.cb4 = QComboBox(self)
        self.cb4.move(150, 260)
        self.cb4.addItems(["Open Notepad", "Open Chrome","Open Youtube","Play Trending film"])
        self.cb4.show()


        #add button
        self.bu=QPushButton(self)
        self.bu.show()
        self.bu.move(130,300)
        self.bu.setText("Save")
        self.bu.clicked.connect(self.save)




    def save(self):
        self.tupt=self.cb1.currentText()
        self.tdt=self.cb2.currentText()
        self.st=self.cb3.currentText()
        self.rt=self.cb4.currentText()
        self.db.collection(u'Gests').document(self.uname).set(

            {
                'Thumbs up':self.tupt,
                'Thumbs Down':self.tdt,
                'Stop':self.st,
                'Rock':self.rt
            }
        )








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SetGesturewindow()
    window.show()
    sys.exit(app.exec_())