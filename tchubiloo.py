# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tchubiloo.ui'
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
        MainWindow.resize(1036, 618)
        MainWindow.setMinimumSize(QtCore.QSize(598, 606))
        self.main_window = QtGui.QWidget(MainWindow)
        self.main_window.setObjectName(_fromUtf8("main_window"))
        self.gridLayout_3 = QtGui.QGridLayout(self.main_window)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.main_window)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.curva_analitica = QtGui.QWidget()
        self.curva_analitica.setObjectName(_fromUtf8("curva_analitica"))
        self.gridLayout_2 = QtGui.QGridLayout(self.curva_analitica)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_CAtab = QtGui.QGridLayout()
        self.gridLayout_CAtab.setObjectName(_fromUtf8("gridLayout_CAtab"))
        self.verticalLayout_table = QtGui.QVBoxLayout()
        self.verticalLayout_table.setObjectName(_fromUtf8("verticalLayout_table"))
        self.tableWidget = QtGui.QTableWidget(self.curva_analitica)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_table.addWidget(self.tableWidget)
        self.gridLayout_btns = QtGui.QGridLayout()
        self.gridLayout_btns.setObjectName(_fromUtf8("gridLayout_btns"))
        self.homocedastidade_btn = QtGui.QPushButton(self.curva_analitica)
        self.homocedastidade_btn.setObjectName(_fromUtf8("homocedastidade_btn"))
        self.gridLayout_btns.addWidget(self.homocedastidade_btn, 2, 1, 1, 1)
        self.remove_row_btn = QtGui.QPushButton(self.curva_analitica)
        self.remove_row_btn.setObjectName(_fromUtf8("remove_row_btn"))
        self.gridLayout_btns.addWidget(self.remove_row_btn, 1, 2, 1, 1)
        self.grubbs_checkBox = QtGui.QCheckBox(self.curva_analitica)
        self.grubbs_checkBox.setObjectName(_fromUtf8("grubbs_checkBox"))
        self.gridLayout_btns.addWidget(self.grubbs_checkBox, 3, 1, 1, 1)
        self.linear_reg_btn = QtGui.QPushButton(self.curva_analitica)
        self.linear_reg_btn.setObjectName(_fromUtf8("linear_reg_btn"))
        self.gridLayout_btns.addWidget(self.linear_reg_btn, 1, 0, 1, 1)
        self.add_column_btn = QtGui.QPushButton(self.curva_analitica)
        self.add_column_btn.setObjectName(_fromUtf8("add_column_btn"))
        self.gridLayout_btns.addWidget(self.add_column_btn, 0, 1, 1, 1)
        self.se_btn = QtGui.QPushButton(self.curva_analitica)
        self.se_btn.setObjectName(_fromUtf8("se_btn"))
        self.gridLayout_btns.addWidget(self.se_btn, 3, 0, 1, 1)
        self.grubbs_btn = QtGui.QPushButton(self.curva_analitica)
        self.grubbs_btn.setObjectName(_fromUtf8("grubbs_btn"))
        self.gridLayout_btns.addWidget(self.grubbs_btn, 2, 0, 1, 1)
        self.import_table_btn = QtGui.QPushButton(self.curva_analitica)
        self.import_table_btn.setObjectName(_fromUtf8("import_table_btn"))
        self.gridLayout_btns.addWidget(self.import_table_btn, 0, 0, 1, 1)
        self.sse_btn = QtGui.QPushButton(self.curva_analitica)
        self.sse_btn.setObjectName(_fromUtf8("sse_btn"))
        self.gridLayout_btns.addWidget(self.sse_btn, 2, 2, 1, 1)
        self.remove_column_btn = QtGui.QPushButton(self.curva_analitica)
        self.remove_column_btn.setObjectName(_fromUtf8("remove_column_btn"))
        self.gridLayout_btns.addWidget(self.remove_column_btn, 0, 2, 1, 1)
        self.add_row_btn = QtGui.QPushButton(self.curva_analitica)
        self.add_row_btn.setObjectName(_fromUtf8("add_row_btn"))
        self.gridLayout_btns.addWidget(self.add_row_btn, 1, 1, 1, 1)
        self.verticalLayout_table.addLayout(self.gridLayout_btns)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.outlier_tableWidget = QtGui.QTableWidget(self.curva_analitica)
        self.outlier_tableWidget.setObjectName(_fromUtf8("outlier_tableWidget"))
        self.outlier_tableWidget.setColumnCount(0)
        self.outlier_tableWidget.setRowCount(0)
        self.gridLayout_5.addWidget(self.outlier_tableWidget, 0, 0, 1, 1)
        self.verticalLayout_table.addLayout(self.gridLayout_5)
        self.gridLayout_CAtab.addLayout(self.verticalLayout_table, 1, 1, 1, 1)
        self.verticalLayout_plot = QtGui.QVBoxLayout()
        self.verticalLayout_plot.setObjectName(_fromUtf8("verticalLayout_plot"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_plot.addItem(spacerItem)
        self.gridLayout_graph = QtGui.QGridLayout()
        self.gridLayout_graph.setObjectName(_fromUtf8("gridLayout_graph"))
        self.verticalLayout_plot.addLayout(self.gridLayout_graph)
        self.gridLayout_info = QtGui.QGridLayout()
        self.gridLayout_info.setObjectName(_fromUtf8("gridLayout_info"))
        self.equation_label = QtGui.QLabel(self.curva_analitica)
        self.equation_label.setText(_fromUtf8(""))
        self.equation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.equation_label.setObjectName(_fromUtf8("equation_label"))
        self.gridLayout_info.addWidget(self.equation_label, 0, 3, 1, 1)
        self.solution_lineEdit = QtGui.QLineEdit(self.curva_analitica)
        self.solution_lineEdit.setObjectName(_fromUtf8("solution_lineEdit"))
        self.gridLayout_info.addWidget(self.solution_lineEdit, 2, 1, 1, 1)
        self.R_label = QtGui.QLabel(self.curva_analitica)
        self.R_label.setText(_fromUtf8(""))
        self.R_label.setAlignment(QtCore.Qt.AlignCenter)
        self.R_label.setObjectName(_fromUtf8("R_label"))
        self.gridLayout_info.addWidget(self.R_label, 2, 3, 1, 1)
        self.substance_label = QtGui.QLabel(self.curva_analitica)
        self.substance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.substance_label.setObjectName(_fromUtf8("substance_label"))
        self.gridLayout_info.addWidget(self.substance_label, 0, 0, 1, 1)
        self.substance_lineEdit = QtGui.QLineEdit(self.curva_analitica)
        self.substance_lineEdit.setObjectName(_fromUtf8("substance_lineEdit"))
        self.gridLayout_info.addWidget(self.substance_lineEdit, 0, 1, 1, 1)
        self.solution_label = QtGui.QLabel(self.curva_analitica)
        self.solution_label.setScaledContents(True)
        self.solution_label.setAlignment(QtCore.Qt.AlignCenter)
        self.solution_label.setObjectName(_fromUtf8("solution_label"))
        self.gridLayout_info.addWidget(self.solution_label, 2, 0, 1, 1)
        self.verticalLayout_plot.addLayout(self.gridLayout_info)
        self.gridLayout_CAtab.addLayout(self.verticalLayout_plot, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_CAtab, 1, 1, 1, 1)
        self.tabWidget.addTab(self.curva_analitica, _fromUtf8(""))
        self.dissolucao = QtGui.QWidget()
        self.dissolucao.setObjectName(_fromUtf8("dissolucao"))
        self.gridLayout_6 = QtGui.QGridLayout(self.dissolucao)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.grid_layou_diss = QtGui.QGridLayout()
        self.grid_layou_diss.setObjectName(_fromUtf8("grid_layou_diss"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.grid_layou_diss.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.grid_layou_diss, 0, 0, 2, 1)
        self.tableWidget_2 = QtGui.QTableWidget(self.dissolucao)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_6.addWidget(self.tableWidget_2, 0, 1, 1, 3)
        self.iplotbtn_2 = QtGui.QPushButton(self.dissolucao)
        self.iplotbtn_2.setObjectName(_fromUtf8("iplotbtn_2"))
        self.gridLayout_6.addWidget(self.iplotbtn_2, 1, 1, 1, 1)
        self.itablebtn_2 = QtGui.QPushButton(self.dissolucao)
        self.itablebtn_2.setObjectName(_fromUtf8("itablebtn_2"))
        self.gridLayout_6.addWidget(self.itablebtn_2, 1, 2, 1, 1)
        self.mediabtn_2 = QtGui.QPushButton(self.dissolucao)
        self.mediabtn_2.setObjectName(_fromUtf8("mediabtn_2"))
        self.gridLayout_6.addWidget(self.mediabtn_2, 1, 3, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.dissolucao)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_6.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.ptablebtn_2 = QtGui.QPushButton(self.dissolucao)
        self.ptablebtn_2.setObjectName(_fromUtf8("ptablebtn_2"))
        self.gridLayout_6.addWidget(self.ptablebtn_2, 2, 2, 1, 1)
        self.pmediabtn_2 = QtGui.QPushButton(self.dissolucao)
        self.pmediabtn_2.setObjectName(_fromUtf8("pmediabtn_2"))
        self.gridLayout_6.addWidget(self.pmediabtn_2, 2, 3, 1, 1)
        self.tabWidget.addTab(self.dissolucao, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.main_window)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1036, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFIle = QtGui.QMenu(self.menubar)
        self.menuFIle.setObjectName(_fromUtf8("menuFIle"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionImport_CSV = QtGui.QAction(MainWindow)
        self.actionImport_CSV.setObjectName(_fromUtf8("actionImport_CSV"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout_it = QtGui.QAction(MainWindow)
        self.actionAbout_it.setObjectName(_fromUtf8("actionAbout_it"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionEditor = QtGui.QAction(MainWindow)
        self.actionEditor.setObjectName(_fromUtf8("actionEditor"))
        self.menuFIle.addAction(self.actionNew)
        self.menuFIle.addAction(self.actionOpen)
        self.menuFIle.addAction(self.actionSave)
        self.menuFIle.addAction(self.actionImport_CSV)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_it)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.homocedastidade_btn.setText(_translate("MainWindow", "Homocedastidade", None))
        self.remove_row_btn.setText(_translate("MainWindow", "Remove Row", None))
        self.grubbs_checkBox.setText(_translate("MainWindow", "Teste de Grubbs", None))
        self.linear_reg_btn.setText(_translate("MainWindow", "Linear regression", None))
        self.add_column_btn.setText(_translate("MainWindow", "Add Column", None))
        self.se_btn.setText(_translate("MainWindow", "Erro padrao da estimativa", None))
        self.grubbs_btn.setText(_translate("MainWindow", "Teste Grubbs", None))
        self.import_table_btn.setText(_translate("MainWindow", "import to table", None))
        self.sse_btn.setText(_translate("MainWindow", "Soma dos quadrados dos residuos", None))
        self.remove_column_btn.setText(_translate("MainWindow", "Remove Column", None))
        self.add_row_btn.setText(_translate("MainWindow", "Add Row", None))
        self.substance_label.setText(_translate("MainWindow", "Susbtance:", None))
        self.solution_label.setText(_translate("MainWindow", "Solution:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.curva_analitica), _translate("MainWindow", "Curva Analitica", None))
        self.iplotbtn_2.setText(_translate("MainWindow", "import Plot", None))
        self.itablebtn_2.setText(_translate("MainWindow", "import to table", None))
        self.mediabtn_2.setText(_translate("MainWindow", "media", None))
        self.pushButton_2.setText(_translate("MainWindow", "standard deviation", None))
        self.ptablebtn_2.setText(_translate("MainWindow", "plot from table", None))
        self.pmediabtn_2.setText(_translate("MainWindow", "plot media", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dissolucao), _translate("MainWindow", "Dissolucao", None))
        self.menuFIle.setTitle(_translate("MainWindow", "&File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionImport_CSV.setText(_translate("MainWindow", "Import CSV", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout_it.setText(_translate("MainWindow", "About it", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionEditor.setText(_translate("MainWindow", "Editor", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
