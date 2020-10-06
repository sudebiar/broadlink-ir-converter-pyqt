


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import broadlink
import time,os
import binascii
import js2py
from pathlib import Path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditIp = QtWidgets.QLineEdit(self.tab)
        self.lineEditIp.setObjectName("lineEditIp")
        self.horizontalLayout.addWidget(self.lineEditIp)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditMac = QtWidgets.QLineEdit(self.tab)
        self.lineEditMac.setObjectName("lineEditMac")
        self.horizontalLayout_2.addWidget(self.lineEditMac)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEditName = QtWidgets.QLineEdit(self.tab)
        self.lineEditName.setObjectName("lineEditName")
        self.horizontalLayout_4.addWidget(self.lineEditName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditFile = QtWidgets.QLineEdit(self.tab)
        self.lineEditFile.setObjectName("lineEditFile")
        self.horizontalLayout_3.addWidget(self.lineEditFile)
        self.btnDir = QtWidgets.QPushButton(self.tab)
        self.btnDir.setObjectName("btnDir")
        self.horizontalLayout_3.addWidget(self.btnDir)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radioIr = QtWidgets.QRadioButton(self.tab)
        self.radioIr.setObjectName("radioIr")
        self.horizontalLayout_7.addWidget(self.radioIr)
        self.radioRf = QtWidgets.QRadioButton(self.tab)
        self.radioRf.setObjectName("radioRf")
        self.horizontalLayout_7.addWidget(self.radioRf)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.textEditCode = QtWidgets.QTextEdit(self.tab)
        self.textEditCode.setObjectName("textEditCode")
        self.verticalLayout_2.addWidget(self.textEditCode)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.textEditLog = QtWidgets.QTextEdit(self.tab)
        self.textEditLog.setObjectName("textEditLog")
        self.horizontalLayout_8.addWidget(self.textEditLog)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.btnGen = QtWidgets.QPushButton(self.tab)
        self.btnGen.setObjectName("btnGen")
        self.verticalLayout_3.addWidget(self.btnGen)
        self.btnSave = QtWidgets.QPushButton(self.tab)
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout_3.addWidget(self.btnSave)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEditBr = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditBr.setObjectName("lineEditBr")
        self.horizontalLayout_5.addWidget(self.lineEditBr)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.textEditCodeRaw = QtWidgets.QTextEdit(self.tab_2)
        self.textEditCodeRaw.setObjectName("textEditCodeRaw")
        self.verticalLayout_4.addWidget(self.textEditCodeRaw)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.textEditLogRaw = QtWidgets.QTextEdit(self.tab_2)
        self.textEditLogRaw.setObjectName("textEditLogRaw")
        self.horizontalLayout_6.addWidget(self.textEditLogRaw)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.btnGenRaw = QtWidgets.QPushButton(self.tab_2)
        self.btnGenRaw.setObjectName("btnGenRaw")
        self.verticalLayout_5.addWidget(self.btnGenRaw)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.radioRf.setChecked(True)

        self.btnDir.clicked.connect(self.dirSelect)
        self.btnSave.clicked.connect(self.save)
        self.btnGenRaw.clicked.connect(self.raw)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ip:    "))
        self.label_2.setText(_translate("MainWindow", "mac:"))
        self.label_4.setText(_translate("MainWindow", "name"))
        self.btnDir.setText(_translate("MainWindow", "Choose dir"))
        self.radioIr.setText(_translate("MainWindow", "IR"))
        self.radioRf.setText(_translate("MainWindow", "RF"))
        self.btnGen.setText(_translate("MainWindow", "Generate"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Broadlink"))
        self.label_3.setText(_translate("MainWindow", "Broadlink code :"))
        self.btnGenRaw.setText(_translate("MainWindow", "Generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Raw"))

    def dirSelect(self):
        selected_directory = QtWidgets.QFileDialog.getExistingDirectory()
        self.lineEditFile.setText(selected_directory)
    
    def save(self):
        host = self.lineEditIp.text()
        mac = self.lineEditMac.text()
        file = self.lineEditFile.text() + "/" + self.lineEditName.text()
        print(file)

        self.run(host,mac,file = file)


    def raw(self):
        context = js2py.EvalJs(enable_require=True)
        file = Path('jscommand.txt')
        br = self.lineEditBr.text()
        input = file.read_text().replace('jscom', br)
        context.execute(input)
        result = context.output
        self.textEditCodeRaw.insertPlainText(result.strip('[').strip(']'))
        print(result)

    def run(self,host,mac,file = None):

        host = (host, 80)
        mac = bytearray.fromhex(mac.replace(':', ' '))
        device = broadlink.rm4(host=host, mac=mac, devtype=0x51da)
        device.auth()
        if self.radioRf.isChecked :
            self.record_rf(device,file)
        elif self.radioIr.isChecked:
            self.record(device,file)

    def record(self,device, file):
        self.textEditLog.setText("Recording command to file " + file)
        QtWidgets.QApplication.processEvents()
        # receive packet
        device.enter_learning()
        ir_packet = None
        attempt = 0
        while ir_packet is None and attempt < 6:
            time.sleep(5)
            ir_packet = device.check_data()
            attempt = attempt + 1
        if ir_packet is not None:
            # write to file
            directory = os.path.dirname(file)
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(file, 'wb') as f:
                f.write(binascii.hexlify(ir_packet))
            self.textEditLog.setText("Done")
            QtWidgets.QApplication.processEvents()
        else:
            self.textEditLog.setText("No command received")
            QtWidgets.QApplication.processEvents()

    def record_rf(self,device, file):
        self.textEditLog.insertPlainText("Learning RF Frequency, press and hold the button to learn...\n")
        QtWidgets.QApplication.processEvents()
        device.sweep_frequency()
        timeout = 20

        while (not device.check_frequency()) and (timeout > 0):
            time.sleep(1)
            timeout -= 1

        if timeout <= 0:
            self.textEditLog.insertPlainText("RF Frequency not found\n")
            QtWidgets.QApplication.processEvents()
            device.cancel_sweep_frequency()
            return

        self.textEditLog.insertPlainText("Found RF Frequency - 1 of 2!\n")
        QtWidgets.QApplication.processEvents()
        time.sleep(5)
        self.textEditLog.insertPlainText("To complete learning, single press the button you want to learn\n")
        QtWidgets.QApplication.processEvents()

        # receive packet
        device.find_rf_packet()
        rf_packet = None
        attempt = 0
        while rf_packet is None and attempt < 6:
            time.sleep(5)
            rf_packet = device.check_data()
            attempt = attempt + 1
        if rf_packet is not None:
            # write to file
            directory = os.path.dirname(file)
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(file, 'wb') as f:
                f.write(binascii.hexlify(rf_packet))
            self.textEditLog.insertPlainText("Done\n")
            QtWidgets.QApplication.processEvents()
            self.textEditCode.insertPlainText(str(binascii.hexlify(rf_packet).decode("utf-8")))
            QtWidgets.QApplication.processEvents()


        else:
            self.textEditLog.insertPlainText("No command received\n")
            QtWidgets.QApplication.processEvents()
 
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())