# Form implementation generated from reading ui file 'c:\Users\julia\Documents\HS Worms\Fächer\GUI\hs_wo_gui_2023\frontend\GebrauchtwarenWindowAccessories.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header_frame = QtWidgets.QFrame(parent=self.main_frame)
        self.header_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.header_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.home_Button = QtWidgets.QPushButton(parent=self.frame)
        self.home_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/icons/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.home_Button.setIcon(icon)
        self.home_Button.setIconSize(QtCore.QSize(32, 32))
        self.home_Button.setObjectName("home_Button")
        self.horizontalLayout_3.addWidget(self.home_Button)
        self.web_label = QtWidgets.QLabel(parent=self.frame)
        self.web_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.web_label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.web_label.setObjectName("web_label")
        self.horizontalLayout_3.addWidget(self.web_label)
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_2 = QtWidgets.QFrame(parent=self.header_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.budget_label = QtWidgets.QLabel(parent=self.frame_2)
        self.budget_label.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.budget_label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.budget_label.setObjectName("budget_label")
        self.horizontalLayout_2.addWidget(self.budget_label)
        self.acc_Button = QtWidgets.QPushButton(parent=self.frame_2)
        self.acc_Button.setEnabled(True)
        self.acc_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/icons/self.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.acc_Button.setIcon(icon1)
        self.acc_Button.setIconSize(QtCore.QSize(32, 32))
        self.acc_Button.setObjectName("acc_Button")
        self.horizontalLayout_2.addWidget(self.acc_Button)
        self.shopping_Button = QtWidgets.QPushButton(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shopping_Button.sizePolicy().hasHeightForWidth())
        self.shopping_Button.setSizePolicy(sizePolicy)
        self.shopping_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.shopping_Button.setAutoFillBackground(False)
        self.shopping_Button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/icons/shopping-cart.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.shopping_Button.setIcon(icon2)
        self.shopping_Button.setIconSize(QtCore.QSize(32, 32))
        self.shopping_Button.setObjectName("shopping_Button")
        self.horizontalLayout_2.addWidget(self.shopping_Button)
        self.horizontalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_2.addWidget(self.header_frame)
        self.content_frame = QtWidgets.QFrame(parent=self.main_frame)
        self.content_frame.setAccessibleName("")
        self.content_frame.setAccessibleDescription("")
        self.content_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_frame.setObjectName("content_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.content_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_1 = QtWidgets.QFrame(parent=self.content_frame)
        self.frame_1.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_1.setObjectName("frame_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.name_label = QtWidgets.QLabel(parent=self.frame_1)
        self.name_label.setObjectName("name_label")
        self.verticalLayout_3.addWidget(self.name_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.picture = QtWidgets.QLabel(parent=self.frame_1)
        self.picture.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap(":/Traktoren/pictures/Traktoren/Claas_Axion_950.jpg"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.verticalLayout_3.addWidget(self.picture, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_4.addWidget(self.frame_1)
        self.frame_3 = QtWidgets.QFrame(parent=self.content_frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_8 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(parent=self.frame_4)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.anz_status = QtWidgets.QLabel(parent=self.frame_4)
        self.anz_status.setObjectName("anz_status")
        self.horizontalLayout_10.addWidget(self.anz_status)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.preis_label = QtWidgets.QLabel(parent=self.frame_6)
        self.preis_label.setObjectName("preis_label")
        self.horizontalLayout_6.addWidget(self.preis_label)
        self.alt_preis_status = QtWidgets.QLabel(parent=self.frame_6)
        self.alt_preis_status.setObjectName("alt_preis_status")
        self.horizontalLayout_6.addWidget(self.alt_preis_status)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_15.addWidget(self.label_4)
        self.zeit_status = QtWidgets.QLabel(parent=self.frame_7)
        self.zeit_status.setObjectName("zeit_status")
        self.horizontalLayout_15.addWidget(self.zeit_status)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.wert_label = QtWidgets.QLabel(parent=self.frame_9)
        self.wert_label.setObjectName("wert_label")
        self.horizontalLayout_7.addWidget(self.wert_label)
        self.wert_status = QtWidgets.QLabel(parent=self.frame_9)
        self.wert_status.setObjectName("wert_status")
        self.horizontalLayout_7.addWidget(self.wert_status)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_14.addWidget(self.label_2)
        self.neu_preis_status = QtWidgets.QLabel(parent=self.frame_5)
        self.neu_preis_status.setObjectName("neu_preis_status")
        self.horizontalLayout_14.addWidget(self.neu_preis_status)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.content_frame)
        self.frame_13 = QtWidgets.QFrame(parent=self.main_frame)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.comp_label = QtWidgets.QLabel(parent=self.frame_13)
        self.comp_label.setObjectName("comp_label")
        self.verticalLayout_5.addWidget(self.comp_label)
        self.verticalLayout_2.addWidget(self.frame_13)
        self.scroll_frame = QtWidgets.QFrame(parent=self.main_frame)
        self.scroll_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.scroll_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.scroll_frame.setObjectName("scroll_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.scroll_frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.dyn_scrollarea = QtWidgets.QScrollArea(parent=self.scroll_frame)
        self.dyn_scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.dyn_scrollarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.dyn_scrollarea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.dyn_scrollarea.setWidgetResizable(True)
        self.dyn_scrollarea.setObjectName("dyn_scrollarea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 936, 510))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.dyn_scrollarea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_8.addWidget(self.dyn_scrollarea)
        self.verticalLayout_2.addWidget(self.scroll_frame)
        self.verticalLayout.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gebrauchtwaren, Zubehör"))
        self.web_label.setText(_translate("MainWindow", "WEBSHOP.DE"))
        self.budget_label.setText(_translate("MainWindow", "Budget"))
        self.name_label.setText(_translate("MainWindow", "Gebrauchtware XY"))
        self.label.setText(_translate("MainWindow", "Zu Verkaufen:"))
        self.anz_status.setText(_translate("MainWindow", "%%%"))
        self.preis_label.setText(_translate("MainWindow", "Gesamtpreis"))
        self.alt_preis_status.setText(_translate("MainWindow", "%%%"))
        self.label_4.setText(_translate("MainWindow", "Wertminderung Zeit:"))
        self.zeit_status.setText(_translate("MainWindow", "%%%"))
        self.wert_label.setText(_translate("MainWindow", "Wertminderung:"))
        self.wert_status.setText(_translate("MainWindow", "0,00 €"))
        self.label_2.setText(_translate("MainWindow", "Gesamtpreis (nach Wertverlust)"))
        self.neu_preis_status.setText(_translate("MainWindow", "%%%"))
        self.label_3.setText(_translate("MainWindow", "Kompatible Hersteller:"))
        self.comp_label.setText(_translate("MainWindow", "%%%"))
