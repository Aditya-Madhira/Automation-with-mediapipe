import sys
from PyQt5.QtWidgets import  QApplication, QLabel, QFileDialog, QAction,QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import face_recognition
from firebase_admin import credentials,initialize_app,firestore
import firebase_admin
import cv2
import numpy as np

username=""

class UploadWindow(QMainWindow):
    if not firebase_admin._apps:
        cred = credentials.Certificate(r'C:\Users\Aditya\Desktop\Myproject\code\serviceaccountcred.json')
        initialize_app(cred)


    db = firestore.client()






    myimagepath=""


    def __init__(self, username,parent = None):
        super(UploadWindow, self).__init__(parent)
        self.setuname=username


        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        editMenu = menubar.addMenu('Edit')
        upload=menubar.addMenu('Upload ')
        self.resize(500, 500)

        openAction = QAction('Open Image', self)
        openAction.triggered.connect(self.openImage)
        fileMenu.addAction(openAction)

        uploadaction=QAction('upload to firebase',self)
        uploadaction.triggered.connect(self.upload)
        upload.addAction(uploadaction)

        closeAction = QAction('Exit', self)
        closeAction.triggered.connect(self.close)
        fileMenu.addAction(closeAction)
        self.label = QLabel()
        self.setCentralWidget(self.label)

    def openImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(pixmap)
        self.resize(pixmap.size())
        self.adjustSize()
        self.myimagepath=imagePath


    def upload(self):
        self.tempimg=face_recognition.load_image_file(self.myimagepath)
        self.enc=face_recognition.face_encodings(self.tempimg)[0]
        self.arrep=np.array_str(self.enc)
        self.db.collection(u'enc').document(self.setuname).set({
            'value':self.arrep,
        })
















class TakeNamewin(QDialog):


    # constructor
    def __init__(self):
        super(TakeNamewin, self).__init__()

        # setting window title
        self.setWindowTitle("Python")

        # setting geometry to the window
        self.setGeometry(100, 100, 300, 400)

        # creating a group box
        self.formGroupBox = QGroupBox("name Form")

        # creating spin box to select age

        # creating a line edit
        self.nameLineEdit = QLineEdit()

        # calling the method that create the form
        self.createForm()

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.getInfo)

        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)

        # creating a vertical layout
        mainLayout = QVBoxLayout()

        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)

        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)

        # setting lay out
        self.setLayout(mainLayout)

    # get info method called when form is accepted
    def getInfo(self):
        # closing the window
        self.close()

    # creat form method
    def createForm(self):
        # creating a form layout
        layout = QFormLayout()

        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("Name"), self.nameLineEdit)

        # setting layout
        self.formGroupBox.setLayout(layout)

    def return_val(self):
        return self.nameLineEdit.text()








