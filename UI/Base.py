# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(659, 479)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 641, 411))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Home = QtGui.QWidget()
        self.Home.setObjectName(_fromUtf8("Home"))
        self.ToolIcon = QtGui.QLabel(self.Home)
        self.ToolIcon.setGeometry(QtCore.QRect(100, 70, 151, 151))
        self.ToolIcon.setText(_fromUtf8(""))
        self.ToolIcon.setPixmap(QtGui.QPixmap(_fromUtf8("code/Attify-zigbee-framework/UI/code/.designer/backup/icon.png")))
        self.ToolIcon.setScaledContents(True)
        self.ToolIcon.setObjectName(_fromUtf8("ToolIcon"))
        self.ToolName = QtGui.QLabel(self.Home)
        self.ToolName.setGeometry(QtCore.QRect(60, 230, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ToolName.setFont(font)
        self.ToolName.setTextFormat(QtCore.Qt.RichText)
        self.ToolName.setObjectName(_fromUtf8("ToolName"))
        self.ToolVersion = QtGui.QLabel(self.Home)
        self.ToolVersion.setGeometry(QtCore.QRect(120, 290, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ToolVersion.setFont(font)
        self.ToolVersion.setObjectName(_fromUtf8("ToolVersion"))
        self.line = QtGui.QFrame(self.Home)
        self.line.setGeometry(QtCore.QRect(330, 30, 16, 311))
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(self.Home)
        self.label.setGeometry(QtCore.QRect(360, 80, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.labelDeviceStatus = QtGui.QLabel(self.Home)
        self.labelDeviceStatus.setGeometry(QtCore.QRect(500, 90, 121, 31))
        self.labelDeviceStatus.setObjectName(_fromUtf8("labelDeviceStatus"))
        self.label_3 = QtGui.QLabel(self.Home)
        self.label_3.setGeometry(QtCore.QRect(360, 140, 121, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.labelDeviceDetails = QtGui.QLabel(self.Home)
        self.labelDeviceDetails.setGeometry(QtCore.QRect(360, 200, 251, 31))
        self.labelDeviceDetails.setText(_fromUtf8(""))
        self.labelDeviceDetails.setObjectName(_fromUtf8("labelDeviceDetails"))
        self.pushButton_Refresh = QtGui.QPushButton(self.Home)
        self.pushButton_Refresh.setGeometry(QtCore.QRect(360, 310, 261, 27))
        self.pushButton_Refresh.setObjectName(_fromUtf8("pushButton_Refresh"))
        self.tabWidget.addTab(self.Home, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(30, 50, 291, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("NanumMyeongjo"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.frame_3 = QtGui.QFrame(self.tab)
        self.frame_3.setGeometry(QtCore.QRect(30, 140, 551, 191))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_12 = QtGui.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 491, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(10, 36, 511, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(10, 56, 491, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.attifyWebLink = QtGui.QLabel(self.frame_3)
        self.attifyWebLink.setGeometry(QtCore.QRect(50, 120, 411, 21))
        self.attifyWebLink.setObjectName(_fromUtf8("attifyWebLink"))
        self.AttifyStoreLink = QtGui.QLabel(self.frame_3)
        self.AttifyStoreLink.setGeometry(QtCore.QRect(50, 150, 371, 21))
        self.AttifyStoreLink.setObjectName(_fromUtf8("AttifyStoreLink"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_zbstumbler = QtGui.QWidget()
        self.tab_zbstumbler.setObjectName(_fromUtf8("tab_zbstumbler"))
        self.zbstumblerConsole = QtGui.QTextEdit(self.tab_zbstumbler)
        self.zbstumblerConsole.setGeometry(QtCore.QRect(10, 60, 621, 311))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.zbstumblerConsole.setPalette(palette)
        self.zbstumblerConsole.setObjectName(_fromUtf8("zbstumblerConsole"))
        self.checkBox_zbstmblrVerbose = QtGui.QCheckBox(self.tab_zbstumbler)
        self.checkBox_zbstmblrVerbose.setGeometry(QtCore.QRect(390, 20, 99, 31))
        self.checkBox_zbstmblrVerbose.setObjectName(_fromUtf8("checkBox_zbstmblrVerbose"))
        self.pushButton_zbstumbler = QtGui.QPushButton(self.tab_zbstumbler)
        self.pushButton_zbstumbler.setGeometry(QtCore.QRect(498, 20, 121, 27))
        self.pushButton_zbstumbler.setObjectName(_fromUtf8("pushButton_zbstumbler"))
        self.label_2 = QtGui.QLabel(self.tab_zbstumbler)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.zbstumbler_Channel = QtGui.QComboBox(self.tab_zbstumbler)
        self.zbstumbler_Channel.setGeometry(QtCore.QRect(244, 20, 131, 27))
        self.zbstumbler_Channel.setObjectName(_fromUtf8("zbstumbler_Channel"))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.zbstumbler_Channel.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab_zbstumbler, _fromUtf8(""))
        self.tab_zbdump = QtGui.QWidget()
        self.tab_zbdump.setObjectName(_fromUtf8("tab_zbdump"))
        self.frame = QtGui.QFrame(self.tab_zbdump)
        self.frame.setGeometry(QtCore.QRect(110, 50, 411, 311))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(60, 76, 111, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(60, 140, 111, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(60, 200, 111, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.zbdumpFile = QtGui.QLineEdit(self.frame)
        self.zbdumpFile.setGeometry(QtCore.QRect(200, 140, 113, 21))
        self.zbdumpFile.setObjectName(_fromUtf8("zbdumpFile"))
        self.zbdumpCount = QtGui.QLineEdit(self.frame)
        self.zbdumpCount.setGeometry(QtCore.QRect(200, 196, 113, 21))
        self.zbdumpCount.setObjectName(_fromUtf8("zbdumpCount"))
        self.pushButton_Zbdump = QtGui.QPushButton(self.frame)
        self.pushButton_Zbdump.setGeometry(QtCore.QRect(120, 260, 161, 27))
        self.pushButton_Zbdump.setObjectName(_fromUtf8("pushButton_Zbdump"))
        self.zbdumpChannel = QtGui.QComboBox(self.frame)
        self.zbdumpChannel.setGeometry(QtCore.QRect(200, 70, 111, 31))
        self.zbdumpChannel.setObjectName(_fromUtf8("zbdumpChannel"))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.zbdumpChannel.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab_zbdump, _fromUtf8(""))
        self.tab_zbreplay = QtGui.QWidget()
        self.tab_zbreplay.setObjectName(_fromUtf8("tab_zbreplay"))
        self.frame_2 = QtGui.QFrame(self.tab_zbreplay)
        self.frame_2.setGeometry(QtCore.QRect(110, 50, 411, 311))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(60, 20, 111, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(60, 140, 111, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(60, 200, 111, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.zbreplayCount = QtGui.QLineEdit(self.frame_2)
        self.zbreplayCount.setGeometry(QtCore.QRect(200, 196, 113, 21))
        self.zbreplayCount.setObjectName(_fromUtf8("zbreplayCount"))
        self.pushButton_Zbreplay = QtGui.QPushButton(self.frame_2)
        self.pushButton_Zbreplay.setGeometry(QtCore.QRect(120, 260, 161, 27))
        self.pushButton_Zbreplay.setObjectName(_fromUtf8("pushButton_Zbreplay"))
        self.zbreplayChannel = QtGui.QComboBox(self.frame_2)
        self.zbreplayChannel.setGeometry(QtCore.QRect(200, 10, 111, 31))
        self.zbreplayChannel.setObjectName(_fromUtf8("zbreplayChannel"))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.zbreplayChannel.addItem(_fromUtf8(""))
        self.label_10 = QtGui.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(60, 80, 111, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.zbreplayDelay = QtGui.QLineEdit(self.frame_2)
        self.zbreplayDelay.setGeometry(QtCore.QRect(200, 80, 113, 21))
        self.zbreplayDelay.setObjectName(_fromUtf8("zbreplayDelay"))
        self.zbreplayFile = QtGui.QComboBox(self.frame_2)
        self.zbreplayFile.setGeometry(QtCore.QRect(200, 140, 111, 27))
        self.zbreplayFile.setObjectName(_fromUtf8("zbreplayFile"))
        self.tabWidget.addTab(self.tab_zbreplay, _fromUtf8(""))
        self.tab_zbwireshark = QtGui.QWidget()
        self.tab_zbwireshark.setObjectName(_fromUtf8("tab_zbwireshark"))
        self.frame_4 = QtGui.QFrame(self.tab_zbwireshark)
        self.frame_4.setGeometry(QtCore.QRect(110, 50, 411, 281))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label_15 = QtGui.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(70, 80, 68, 31))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(70, 150, 68, 17))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.wiresharkChannel = QtGui.QLineEdit(self.frame_4)
        self.wiresharkChannel.setGeometry(QtCore.QRect(170, 80, 113, 27))
        self.wiresharkChannel.setObjectName(_fromUtf8("wiresharkChannel"))
        self.wiresharkCount = QtGui.QLineEdit(self.frame_4)
        self.wiresharkCount.setGeometry(QtCore.QRect(170, 140, 113, 27))
        self.wiresharkCount.setObjectName(_fromUtf8("wiresharkCount"))
        self.wiresharkStart = QtGui.QPushButton(self.frame_4)
        self.wiresharkStart.setGeometry(QtCore.QRect(120, 220, 161, 27))
        self.wiresharkStart.setObjectName(_fromUtf8("wiresharkStart"))
        self.tabWidget.addTab(self.tab_zbwireshark, _fromUtf8(""))
        self.tab_zbdsniff = QtGui.QWidget()
        self.tab_zbdsniff.setObjectName(_fromUtf8("tab_zbdsniff"))
        self.tabWidget.addTab(self.tab_zbdsniff, _fromUtf8(""))
        self.tab_zbassocflood = QtGui.QWidget()
        self.tab_zbassocflood.setObjectName(_fromUtf8("tab_zbassocflood"))
        self.tabWidget.addTab(self.tab_zbassocflood, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Attify Zigbee Framework", None))
        self.ToolName.setText(_translate("MainWindow", "Attify Zigbee Framework", None))
        self.ToolVersion.setText(_translate("MainWindow", "Version 1.1", None))
        self.label.setText(_translate("MainWindow", "Device Status  :", None))
        self.labelDeviceStatus.setText(_translate("MainWindow", "Not Connected", None))
        self.label_3.setText(_translate("MainWindow", "Device Detials  :", None))
        self.pushButton_Refresh.setText(_translate("MainWindow", "Refresh Devices", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("MainWindow", "AZF", None))
        self.label_11.setText(_translate("MainWindow", "Attify Zigbee Framework", None))
        self.label_12.setText(_translate("MainWindow", "The Attify Zigbee Framework is developed and maintained by Attify Inc. ", None))
        self.label_13.setText(_translate("MainWindow", "in an effort to simplify pentesting Zigbee based IoT devices by providing ", None))
        self.label_14.setText(_translate("MainWindow", "developers and security researchers a user friendly platform to do so.", None))
        self.attifyWebLink.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://attify.com\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">Visit us at - attify.com </span></a></p></body></html>", None))
        self.AttifyStoreLink.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://attify-store.com\"><span style=\" font-weight:600; text-decoration: underline; color:#0000ff;\">Buy tools at - attify-store.com </span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "About", None))
        self.checkBox_zbstmblrVerbose.setText(_translate("MainWindow", "Verbose", None))
        self.pushButton_zbstumbler.setText(_translate("MainWindow", "Start", None))
        self.label_2.setText(_translate("MainWindow", "Zigbee Network Discovery", None))
        self.zbstumbler_Channel.setItemText(0, _translate("MainWindow", "All Channels", None))
        self.zbstumbler_Channel.setItemText(1, _translate("MainWindow", "11", None))
        self.zbstumbler_Channel.setItemText(2, _translate("MainWindow", "12", None))
        self.zbstumbler_Channel.setItemText(3, _translate("MainWindow", "13", None))
        self.zbstumbler_Channel.setItemText(4, _translate("MainWindow", "14", None))
        self.zbstumbler_Channel.setItemText(5, _translate("MainWindow", "15", None))
        self.zbstumbler_Channel.setItemText(6, _translate("MainWindow", "16", None))
        self.zbstumbler_Channel.setItemText(7, _translate("MainWindow", "17", None))
        self.zbstumbler_Channel.setItemText(8, _translate("MainWindow", "18", None))
        self.zbstumbler_Channel.setItemText(9, _translate("MainWindow", "19", None))
        self.zbstumbler_Channel.setItemText(10, _translate("MainWindow", "20", None))
        self.zbstumbler_Channel.setItemText(11, _translate("MainWindow", "21", None))
        self.zbstumbler_Channel.setItemText(12, _translate("MainWindow", "22", None))
        self.zbstumbler_Channel.setItemText(13, _translate("MainWindow", "23", None))
        self.zbstumbler_Channel.setItemText(14, _translate("MainWindow", "24", None))
        self.zbstumbler_Channel.setItemText(15, _translate("MainWindow", "25", None))
        self.zbstumbler_Channel.setItemText(16, _translate("MainWindow", "26", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_zbstumbler), _translate("MainWindow", "zbstumbler", None))
        self.label_4.setText(_translate("MainWindow", "Channel             :", None))
        self.label_5.setText(_translate("MainWindow", "Output File       :", None))
        self.label_6.setText(_translate("MainWindow", "Packet Count   :", None))
        self.pushButton_Zbdump.setText(_translate("MainWindow", "Start Capture", None))
        self.zbdumpChannel.setItemText(0, _translate("MainWindow", "        Select", None))
        self.zbdumpChannel.setItemText(1, _translate("MainWindow", "11", None))
        self.zbdumpChannel.setItemText(2, _translate("MainWindow", "12", None))
        self.zbdumpChannel.setItemText(3, _translate("MainWindow", "13", None))
        self.zbdumpChannel.setItemText(4, _translate("MainWindow", "14", None))
        self.zbdumpChannel.setItemText(5, _translate("MainWindow", "15", None))
        self.zbdumpChannel.setItemText(6, _translate("MainWindow", "16", None))
        self.zbdumpChannel.setItemText(7, _translate("MainWindow", "17", None))
        self.zbdumpChannel.setItemText(8, _translate("MainWindow", "18", None))
        self.zbdumpChannel.setItemText(9, _translate("MainWindow", "19", None))
        self.zbdumpChannel.setItemText(10, _translate("MainWindow", "20", None))
        self.zbdumpChannel.setItemText(11, _translate("MainWindow", "21", None))
        self.zbdumpChannel.setItemText(12, _translate("MainWindow", "22", None))
        self.zbdumpChannel.setItemText(13, _translate("MainWindow", "23", None))
        self.zbdumpChannel.setItemText(14, _translate("MainWindow", "24", None))
        self.zbdumpChannel.setItemText(15, _translate("MainWindow", "25", None))
        self.zbdumpChannel.setItemText(16, _translate("MainWindow", "26", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_zbdump), _translate("MainWindow", "zbdump", None))
        self.label_7.setText(_translate("MainWindow", "Channel             :", None))
        self.label_8.setText(_translate("MainWindow", "Pcap File            :", None))
        self.label_9.setText(_translate("MainWindow", "Packet Count   :", None))
        self.pushButton_Zbreplay.setText(_translate("MainWindow", "Start Replay", None))
        self.zbreplayChannel.setItemText(0, _translate("MainWindow", "        Select", None))
        self.zbreplayChannel.setItemText(1, _translate("MainWindow", "11", None))
        self.zbreplayChannel.setItemText(2, _translate("MainWindow", "12", None))
        self.zbreplayChannel.setItemText(3, _translate("MainWindow", "13", None))
        self.zbreplayChannel.setItemText(4, _translate("MainWindow", "14", None))
        self.zbreplayChannel.setItemText(5, _translate("MainWindow", "15", None))
        self.zbreplayChannel.setItemText(6, _translate("MainWindow", "16", None))
        self.zbreplayChannel.setItemText(7, _translate("MainWindow", "17", None))
        self.zbreplayChannel.setItemText(8, _translate("MainWindow", "18", None))
        self.zbreplayChannel.setItemText(9, _translate("MainWindow", "19", None))
        self.zbreplayChannel.setItemText(10, _translate("MainWindow", "20", None))
        self.zbreplayChannel.setItemText(11, _translate("MainWindow", "21", None))
        self.zbreplayChannel.setItemText(12, _translate("MainWindow", "22", None))
        self.zbreplayChannel.setItemText(13, _translate("MainWindow", "23", None))
        self.zbreplayChannel.setItemText(14, _translate("MainWindow", "24", None))
        self.zbreplayChannel.setItemText(15, _translate("MainWindow", "25", None))
        self.zbreplayChannel.setItemText(16, _translate("MainWindow", "26", None))
        self.label_10.setText(_translate("MainWindow", "Delay                  :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_zbreplay), _translate("MainWindow", "zbreplay", None))
        self.label_15.setText(_translate("MainWindow", "Channel", None))
        self.label_16.setText(_translate("MainWindow", "Count", None))
        self.wiresharkStart.setText(_translate("MainWindow", "Launch Wireshark", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_zbwireshark), _translate("MainWindow", "zbwireshark", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_zbdsniff), _translate("MainWindow", "zbdsniff", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_zbassocflood), _translate("MainWindow", "zbassocflood", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
