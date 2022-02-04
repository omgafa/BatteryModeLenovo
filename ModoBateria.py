from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 498)
        MainWindow.setMinimumSize(QtCore.QSize(539, 498))
        MainWindow.setMaximumSize(QtCore.QSize(539, 498))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 511, 81))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_Activado = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Activado.setGeometry(QtCore.QRect(90, 110, 371, 81))
        font = QtGui.QFont()
        font.setFamily("TeXGyreBonum")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Activado.setFont(font)
        self.btn_Activado.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_Activado.setObjectName("btn_Activado")
        self.btn_Desactivado = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Desactivado.setGeometry(QtCore.QRect(90, 220, 371, 81))
        font = QtGui.QFont()
        font.setFamily("TeXGyreBonum")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Desactivado.setFont(font)
        self.btn_Desactivado.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_Desactivado.setObjectName("btn_Desactivado")
        self.label_modo = QtWidgets.QLabel(self.centralwidget)
        self.label_modo.setGeometry(QtCore.QRect(-10, 430, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_modo.setFont(font)
        self.label_modo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_modo.setObjectName("label_modo")
        self.btn_Activado_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Activado_2.setGeometry(QtCore.QRect(90, 320, 371, 81))
        font = QtGui.QFont()
        font.setFamily("TeXGyreBonum")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Activado_2.setFont(font)
        self.btn_Activado_2.setStyleSheet("background-color: rgb(227, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_Activado_2.setObjectName("btn_Activado_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_Activado_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ahorro de Bateria"))
        self.label.setText(_translate("MainWindow", "Seleccione el modo de conservacion"))
        self.btn_Activado.setText(_translate("MainWindow", "Activado"))
        self.btn_Desactivado.setText(_translate("MainWindow", "Desactivado"))
        self.label_modo.setText(_translate("MainWindow", "Modo de Conservacion: "))
        self.btn_Activado_2.setText(_translate("MainWindow", "Salir"))


class MainWindowF(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        self.valortxt=''
        with open("/sys/bus/platform/devices/VPC2004:00/conservation_mode") as ar: 
            for x in ar: self.valortxt = int(x)
        if self.valortxt == 1:self.label_modo.setText('Modo de Conservacion: Activado'); self.label_modo.setStyleSheet("""background-color: rgb(85, 255, 127);""");
        if self.valortxt == 0:self.label_modo.setText('Modo de Conservacion: Desactivado'); self.label_modo.setStyleSheet("""background-color: rgb(255, 70, 70);""");
        self.btn_Activado.clicked.connect(lambda:self.Modo(1))
        self.btn_Desactivado.clicked.connect(lambda:self.Modo(0))
        self.valor=''
      

    def Modo(self,v):
        
        os.system(f'echo {v} > /sys/bus/platform/devices/VPC2004\:00/conservation_mode')
        if v == 1:
            self.label_modo.setText('Modo de Conservacion: Activado')
            self.label_modo.setStyleSheet("""background-color: rgb(85, 255, 127);""");
        if v == 0:
            self.label_modo.setText('Modo de Conservacion: Desactivado')
            self.label_modo.setStyleSheet("""background-color: rgb(255, 70, 70);""");
            
if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window=MainWindowF()
    window.show()
    app.exec_()

