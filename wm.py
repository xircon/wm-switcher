#!/usr/bin/env python
from PyQt4 import QtGui, QtCore


import os
import time
import os.path


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout(self)
        self.setWindowTitle("WM selector")

        myFont = QtGui.QFont()
        myFont.setBold(True)

        fname="/usr/bin/metacity"
        if os.path.isfile(fname):
            self.lbl1 = QtGui.QLabel('Metacity Window Manager', self)
            self.lbl1.setFont(myFont)
            self.lbl1.setAlignment(QtCore.Qt.AlignHCenter)
            layout.addWidget(self.lbl1)

            self.button1 = QtGui.QPushButton('Metacity - no compositor', self)
            self.button1.clicked.connect(self.handleButton1)
            layout.addWidget(self.button1)

            self.button2 = QtGui.QPushButton('Metacity + native compositing', self)
            self.button2.clicked.connect(self.handleButton2)
            layout.addWidget(self.button2)

            self.button3 = QtGui.QPushButton('Metacity + Compton', self)
            self.button3.clicked.connect(self.handleButton3)
            layout.addWidget(self.button3)

        fname="/usr/bin/xfwm4"
        if os.path.isfile(fname):
            self.lbl2 = QtGui.QLabel('\nXFCE4 Window Manager', self)
            self.lbl2.setFont(myFont)
            self.lbl2.setAlignment(QtCore.Qt.AlignHCenter)
            layout.addWidget(self.lbl2)

            self.button4 = QtGui.QPushButton('xfwm4 - no compositor', self)
            self.button4.clicked.connect(self.handleButton4)
            layout.addWidget(self.button4)

            self.button5 = QtGui.QPushButton('xfwm4 + native compositing', self)
            self.button5.clicked.connect(self.handleButton5)
            layout.addWidget(self.button5)

            self.button6 = QtGui.QPushButton('xfwm4 + Compton', self)
            self.button6.clicked.connect(self.handleButton6)
            layout.addWidget(self.button6)

        fname="/usr/bin/compiz"
        if os.path.isfile(fname):
            self.lbl3 = QtGui.QLabel('\nCompiz compositing WM', self)
            self.lbl3.setFont(myFont)
            self.lbl3.setAlignment(QtCore.Qt.AlignHCenter)
            layout.addWidget(self.lbl3)

            self.button7 = QtGui.QPushButton('compiz', self)
            self.button7.clicked.connect(self.handleButton7)
            layout.addWidget(self.button7)

        fname="/usr/bin/openbox"
        if os.path.isfile(fname):
            self.lbl4 = QtGui.QLabel('\nOpenbox Window Manager', self)
            self.lbl4.setFont(myFont)
            self.lbl4.setAlignment(QtCore.Qt.AlignHCenter)
            layout.addWidget(self.lbl4)

            self.button8 = QtGui.QPushButton('openbox', self)
            self.button8.clicked.connect(self.handleButton8)
            layout.addWidget(self.button8)

            self.button9 = QtGui.QPushButton('openbox + Compton', self)
            self.button9.clicked.connect(self.handleButton9)
            #self.button9.setStyleSheet("background-color: green")
            layout.addWidget(self.button9)

    def handleButton1(self):
        #Metacity no compositor
        print("Button1")
        os.system("killall compton")
        os.system("metacity --no-composite --replace &")

    def handleButton2(self):
        #Metacity + native compositing
        print("Button2")
        os.system("killall compton")
        os.system("metacity -c --replace &")

    def handleButton3(self):
        #Metacity + compton
        print("Button3")
        os.system("killall compton")
        os.system("metacity --no-composite --replace &")
        time.sleep(3)
        os.system("compton -b &")

    def handleButton4(self):
        print("Button4")
        os.system("killall compton")
        os.system("xfwm4 --compositor=off --replace &")

    def handleButton5(self):
        print("Button5")
        os.system("killall compton")
        os.system("xfwm4 --compositor=on --replace &")

    def handleButton6(self):
        print("Button6")
        os.system("killall compton")
        os.system("xfwm4 --compositor=off --replace &")
        time.sleep(3)
        os.system("compton -b &")

    def handleButton7(self):
        print("Button7")
        os.system("killall compton")
        os.system("compiz --replace ccp &")

    def handleButton8(self):
        print("Button8")
        os.system("killall compton")
        os.system("openbox --replace &")

    def handleButton9(self):
        print("Button9")
        os.system("killall compiz")
        os.system("openbox --replace &")
        time.sleep(3)
        os.system("compton -b &")


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
