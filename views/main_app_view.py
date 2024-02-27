# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_app_view.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)
import resources.resource_file_rc

class Ui_main_app_view(object):
    def setupUi(self, main_app_view):
        if not main_app_view.objectName():
            main_app_view.setObjectName(u"main_app_view")
        main_app_view.resize(1283, 781)
        main_app_view.setMinimumSize(QSize(1283, 781))
        main_app_view.setMaximumSize(QSize(1283, 781))
        self.actionCytology_Report = QAction(main_app_view)
        self.actionCytology_Report.setObjectName(u"actionCytology_Report")
        self.actionNecropsy_Report = QAction(main_app_view)
        self.actionNecropsy_Report.setObjectName(u"actionNecropsy_Report")
        self.actionSave_on_This_PC = QAction(main_app_view)
        self.actionSave_on_This_PC.setObjectName(u"actionSave_on_This_PC")
        self.actionSave_on_Server = QAction(main_app_view)
        self.actionSave_on_Server.setObjectName(u"actionSave_on_Server")
        self.actionLoad_from_this_PC = QAction(main_app_view)
        self.actionLoad_from_this_PC.setObjectName(u"actionLoad_from_this_PC")
        self.actionLoad_from_Server = QAction(main_app_view)
        self.actionLoad_from_Server.setObjectName(u"actionLoad_from_Server")
        self.actionConfirm_Report = QAction(main_app_view)
        self.actionConfirm_Report.setObjectName(u"actionConfirm_Report")
        self.actionApprove_Report = QAction(main_app_view)
        self.actionApprove_Report.setObjectName(u"actionApprove_Report")
        self.centralwidget = QWidget(main_app_view)
        self.centralwidget.setObjectName(u"centralwidget")
        self.page_widget = QWidget(self.centralwidget)
        self.page_widget.setObjectName(u"page_widget")
        self.page_widget.setGeometry(QRect(10, 10, 161, 751))
        self.page_widget.setAutoFillBackground(False)
        self.page_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(131, 216, 255)\n"
"}")
        self.verticalLayout = QVBoxLayout(self.page_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 9, -1)
        self.label = QLabel(self.page_widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"TH Niramit AS"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.cutomer_reg_button = QPushButton(self.page_widget)
        self.cutomer_reg_button.setObjectName(u"cutomer_reg_button")
        font1 = QFont()
        font1.setFamilies([u"TH Niramit AS"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.cutomer_reg_button.setFont(font1)

        self.verticalLayout.addWidget(self.cutomer_reg_button)

        self.case_register_button = QPushButton(self.page_widget)
        self.case_register_button.setObjectName(u"case_register_button")
        self.case_register_button.setFont(font1)

        self.verticalLayout.addWidget(self.case_register_button)

        self.job_progress_button = QPushButton(self.page_widget)
        self.job_progress_button.setObjectName(u"job_progress_button")
        self.job_progress_button.setFont(font1)

        self.verticalLayout.addWidget(self.job_progress_button)

        self.employee_button = QPushButton(self.page_widget)
        self.employee_button.setObjectName(u"employee_button")
        self.employee_button.setFont(font1)

        self.verticalLayout.addWidget(self.employee_button)

        self.finished_report_button = QPushButton(self.page_widget)
        self.finished_report_button.setObjectName(u"finished_report_button")
        self.finished_report_button.setFont(font1)

        self.verticalLayout.addWidget(self.finished_report_button)

        self.bill_button = QPushButton(self.page_widget)
        self.bill_button.setObjectName(u"bill_button")
        self.bill_button.setFont(font1)

        self.verticalLayout.addWidget(self.bill_button)

        self.barcode_button = QPushButton(self.page_widget)
        self.barcode_button.setObjectName(u"barcode_button")
        self.barcode_button.setFont(font1)

        self.verticalLayout.addWidget(self.barcode_button)

        self.lab_order_button = QPushButton(self.page_widget)
        self.lab_order_button.setObjectName(u"lab_order_button")
        self.lab_order_button.setFont(font1)

        self.verticalLayout.addWidget(self.lab_order_button)

        self.verticalSpacer = QSpacerItem(5, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.personal_info_button = QPushButton(self.page_widget)
        self.personal_info_button.setObjectName(u"personal_info_button")
        font2 = QFont()
        font2.setFamilies([u"TH Niramit AS"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.personal_info_button.setFont(font2)

        self.verticalLayout.addWidget(self.personal_info_button)

        self.update_prog_button = QPushButton(self.page_widget)
        self.update_prog_button.setObjectName(u"update_prog_button")
        self.update_prog_button.setFont(font2)

        self.verticalLayout.addWidget(self.update_prog_button)

        self.sign_out_pushButton = QPushButton(self.page_widget)
        self.sign_out_pushButton.setObjectName(u"sign_out_pushButton")
        self.sign_out_pushButton.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/icons/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sign_out_pushButton.setIcon(icon)

        self.verticalLayout.addWidget(self.sign_out_pushButton)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(140, 10, 1131, 721))
        self.report_textEdit = QTextEdit(self.widget_3)
        self.report_textEdit.setObjectName(u"report_textEdit")
        self.report_textEdit.setEnabled(False)
        self.report_textEdit.setGeometry(QRect(40, 10, 1091, 741))
        main_app_view.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_app_view)
        self.statusbar.setObjectName(u"statusbar")
        main_app_view.setStatusBar(self.statusbar)

        self.retranslateUi(main_app_view)

        QMetaObject.connectSlotsByName(main_app_view)
    # setupUi

    def retranslateUi(self, main_app_view):
        main_app_view.setWindowTitle(QCoreApplication.translate("main_app_view", u"Registation", None))
        self.actionCytology_Report.setText(QCoreApplication.translate("main_app_view", u"Cytology Report", None))
        self.actionNecropsy_Report.setText(QCoreApplication.translate("main_app_view", u"Necropsy Report", None))
        self.actionSave_on_This_PC.setText(QCoreApplication.translate("main_app_view", u"Save on This PC", None))
        self.actionSave_on_Server.setText(QCoreApplication.translate("main_app_view", u"Save on Server", None))
        self.actionLoad_from_this_PC.setText(QCoreApplication.translate("main_app_view", u"Load from this PC", None))
        self.actionLoad_from_Server.setText(QCoreApplication.translate("main_app_view", u"Load from Server", None))
        self.actionConfirm_Report.setText(QCoreApplication.translate("main_app_view", u"Confirm Report", None))
        self.actionApprove_Report.setText(QCoreApplication.translate("main_app_view", u"Approve Report", None))
        self.label.setText(QCoreApplication.translate("main_app_view", u"\u0e23\u0e30\u0e1a\u0e1a\u0e25\u0e07\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19", None))
        self.cutomer_reg_button.setText(QCoreApplication.translate("main_app_view", u"\u0e25\u0e07\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e43\u0e2b\u0e21\u0e48", None))
        self.case_register_button.setText(QCoreApplication.translate("main_app_view", u"\u0e23\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e43\u0e2b\u0e21\u0e48", None))
        self.job_progress_button.setText(QCoreApplication.translate("main_app_view", u"\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e07\u0e32\u0e19", None))
        self.employee_button.setText(QCoreApplication.translate("main_app_view", u"\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1a\u0e38\u0e04\u0e25\u0e32\u0e01\u0e23", None))
        self.finished_report_button.setText(QCoreApplication.translate("main_app_view", u"\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e17\u0e35\u0e48\u0e2a\u0e48\u0e07\u0e41\u0e25\u0e49\u0e27", None))
        self.bill_button.setText(QCoreApplication.translate("main_app_view", u"\u0e2d\u0e2d\u0e01\u0e43\u0e1a\u0e40\u0e2a\u0e23\u0e47\u0e08", None))
        self.barcode_button.setText(QCoreApplication.translate("main_app_view", u"\u0e1b\u0e23\u0e34\u0e49\u0e19\u0e1a\u0e32\u0e23\u0e4c\u0e42\u0e04\u0e49\u0e14", None))
        self.lab_order_button.setText(QCoreApplication.translate("main_app_view", u"\u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e43\u0e1a\u0e2a\u0e48\u0e07\u0e41\u0e25\u0e1b", None))
        self.personal_info_button.setText(QCoreApplication.translate("main_app_view", u"\u0e41\u0e01\u0e49\u0e44\u0e02\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e31\u0e27", None))
        self.update_prog_button.setText(QCoreApplication.translate("main_app_view", u"UPDATE", None))
        self.sign_out_pushButton.setText(QCoreApplication.translate("main_app_view", u"Sign Out", None))
    # retranslateUi

