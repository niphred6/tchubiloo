#teste estatistico
#para valores de 1 ate 10

'''
Para ui sera necessario abrir o programa com algumas linhas e colunas vazias
adicionar e remover linhas e colunas #OK
modificar nome das colunas #OK
realizar regressao linear com os valores plotados, e apos o teste de grubbs #OK
importar e salvar arquivos #OK

analise de residuos, grafico
heterocedasticidade min quad pond
coef de correlacao e determinaco
analise de variancia
'''

'''

importar dados na tabela, avisando quais valores devem ser retirados (colorir de veremelho)#OK
realizar calculos estatisticos: mean,var,stddev com os valores corretos #OK
realizar teste de Cochran #OK
realizar regressao linear #OK
realizar soma dos quadrados dos residuos #OK, !!!!!!!!!!!!!!!!!!!!<<<<<<<<<<<<<falta colocar uma label!!!!

'''


from PyQt4 import QtGui # Import the PyQt4 module
from scipy import stats
import decimal
import csv
import numpy as np
#import pyqtgraph as pg

import os, sys
import matplotlib 
matplotlib.use('Qt4agg') # need to call use() before importing plt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from decimal import Decimal


import tchubiloo # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer
              
class ExampleApp(QtGui.QMainWindow, tchubiloo.Ui_MainWindow):
    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)               
              
    #-------------------BUTTONS------------------------------#          

        #homocedastidade button
        self.homocedastidade_btn.clicked.connect(self.homocedastidade)
      
        #----------------END OF BUTTONS----------------------------#
        
        #-----------------Check Box-------------------------------#
        self.grubbs_checkBox.stateChanged.connect(self.grubbs_test)        
        #---------------------------------------------------------#
        
        #-------------------------outlier_tableWidget Table view------------#
        o_r = 0
        o_c = 0
        while o_r<=7:
          self.outlier_tableWidget.insertRow(o_r)
          o_r = o_r+1        
        while o_c<=5:
          self.outlier_tableWidget.insertColumn(o_c)
          o_c = o_c+1
        
        self.outlier_tableWidget.setHorizontalHeaderLabels(['Concentration']+['Rep 1']+['Rep 2']+ ['Rep 3']+['Mean']+['Standard Deviation'])
        self.outlier_tableWidget.resizeColumnsToContents()
        self.outlier_tableWidget.resizeRowsToContents()
        # Hide grid
        self.outlier_tableWidget.setShowGrid(False)
        # hide vertical header
        vh = self.outlier_tableWidget.verticalHeader()
        vh.setVisible(False)
        self.outlier_tableWidget.horizontalHeader().sectionDoubleClicked.connect(self.changeHorizontalHeader)
        
        #---------MENU--------#
        
        #Open menu
        self.actionOpen.triggered.connect(self.import_file)
        #Save menu
        self.actionSave.triggered.connect(self.save_file)
        # Edit tab
        self.actionAdd_Column.triggered.connect(self.addcolumn)
        self.actionRemove_column.triggered.connect(self.removecolumn)
        self.actionAdd_row.triggered.connect(self.addrow)
        self.actionRemove_row.triggered.connect(self.removerow)
        #-------- END OF MENU------------#
        
        #---------------------CA Canvas----------------------------#
        
        
        self.figure = plt.figure(figsize=(10,7))  
        self.canvas = FigureCanvas(self.figure)     
        self.gridLayout_graph.addWidget(self.canvas, 2,0,1,2)
        
        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        self.gridLayout_graph.addWidget(self.navi_toolbar, 1,0,1,2)
        
        
        #------------------------END OF CANVAS--------------------------------#
        
        #----------Insert row and column when opening DATA TABLE------------#
        r = 0
        c = 0
        while r<=7:
          self.tableWidget.insertRow(r)
          r = r+1        
        while c<=5:
          self.tableWidget.insertColumn(c)
          c = c+1
        
        self.tableWidget.setHorizontalHeaderLabels(['Concentration']+['Rep 1']+['Rep 2']+ ['Rep 3']+['Mean']+['Standard Deviation'])
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        self.tableWidget.horizontalHeader().sectionDoubleClicked.connect(self.changeHorizontalHeader)
        #----------------------------------------------------------------#
       
    #-------------analises estatisticas---------------#   

    #-----para dados_corretos----#

    def outlier_mean(self): #media funcionando
        o_row = 0
        o_column = 1
        o_columns = (self.outlier_tableWidget.columnCount())-2        
        o_rows = self.outlier_tableWidget.rowCount()           
        o_mean_column = (self.outlier_tableWidget.columnCount())-2
        
        
        sum = 0 #soma da linha
        n = 0 #numero de valores de cada linha
        while o_row < o_rows: #row e a linha atual, rows e o total de linhas      
            
            while o_column < o_columns:#column e a coluna atual, columns e o total de colunas                
                absorvance_item = self.outlier_tableWidget.item(o_row, o_column)
                if absorvance_item is not None:                  
                  absorvance_value = float(unicode(absorvance_item.text()).encode('utf8'))
                  sum = sum + absorvance_value
                  n = n+1                
                  o_column = o_column+1
                else:
                  o_column = o_column+1
            if n != 0:
              mean = sum/n
              mean_item = QtGui.QTableWidgetItem(str(mean).decode('utf8'))
              self.outlier_tableWidget.setItem(o_row, o_mean_column, mean_item)                        
              self.outlier_tableWidget.resizeColumnsToContents()
              self.outlier_tableWidget.resizeRowsToContents()              
            else:
              pass

            o_column = 1
            sum = 0
            n = 0            
            o_row = o_row+1
      


    def outlier_stddev(self): #OK
        o_row = 0
        o_column = 1
        o_columns = (self.outlier_tableWidget.columnCount())-2        
        o_rows = self.outlier_tableWidget.rowCount()           
        o_stddev_column = self.outlier_tableWidget.columnCount()-1
        #print o_stddev_column
        mean_column = (self.outlier_tableWidget.columnCount())-2
       
        o_sum_var = 0 #soma da linha
        n = 0 #numero de valores de cada linha
        while o_row < o_rows: #row e a linha atual, rows e o total de linhas      
            
            while o_column < o_columns:#column e a coluna atual, columns e o total de colunas                
                absorvance_item = self.outlier_tableWidget.item(o_row, o_column)
                mean_item = self.outlier_tableWidget.item(o_row, mean_column)
                if absorvance_item and mean_item is not None:                  
                  absorvance_value = float(unicode(absorvance_item.text()).encode('utf8'))
                  mean_value = float(unicode(mean_item.text()).encode('utf8'))
                  #print absorvance_value
                  #print mean_value                 
                  
                  o_sum_var = o_sum_var + (absorvance_value - mean_value)**2
                  #print o_sum_var                  
                  n = n+1                
                  o_column = o_column+1
                  #print n
                else:
                  o_column = o_column+1
            
            if n != 0:
              o_var = o_sum_var/(n-1) #o certo e n-1 ou n???????????????             
              o_std_dev = o_var**(1/2.0)
              #print o_std_dev
              stddev_item = QtGui.QTableWidgetItem(str(o_std_dev).decode('utf8'))
              self.outlier_tableWidget.setItem(o_row, o_stddev_column, stddev_item)                        
              self.outlier_tableWidget.resizeColumnsToContents()
              self.outlier_tableWidget.resizeRowsToContents()             
            else:
              pass
           
            o_column = 1
            o_sum_var = 0
            n = 0            
            o_row = o_row+1  


    def min_quad_ord_n_pond(self):
    
        #Sendo x concentracao e y absorvancia(media)
        casas_decimais = 4 #numero de casas decimais
        precision = '.'+str(casas_decimais)+'f'
        column = (self.outlier_tableWidget.columnCount())-2
        
        substance = self.substance_lineEdit.text()
        diluent = self.solution_lineEdit.text()
        if (substance and diluent) is not None:
          titulo = substance+' '+diluent
        else:
          titulo = ''

        y_list = []
        x_list = []
        e_list = []
        
        #---------------pegando os valores de media---------------#
        for row in range(self.outlier_tableWidget.rowCount()):
            item = self.outlier_tableWidget.item(row, column)                
            if item is not None:
              mean_absorvance_value = float(unicode(item.text()).encode('utf8')) 
              #value = format(value, precision)
              y_list = y_list+[mean_absorvance_value]
              
        y = y_list
        #----------------------------------------------------------#
        
        #--------------pegando valores de concentracao--------------------------#
        for row in range(self.outlier_tableWidget.rowCount()):
            item = self.outlier_tableWidget.item(row, 0) #coluna 0 indicando coluna de concentracao                
            if item is not None:#alterar para tirar os valores em vermelho!!!!!!!!!!!!!!!!!!!!!!
              concentration_value = float(unicode(item.text()).encode('utf8')) 
              #value = format(value, precision)
              x_list = x_list+[concentration_value]
              
        x = x_list
        #------------------------------------------------------------#
        
        #--------------------------pegando os valores do desvio padrao-------------------#
        for row in range(self.outlier_tableWidget.rowCount()):
            item = self.outlier_tableWidget.item(row, self.outlier_tableWidget.columnCount()-1) #coluna  indicando coluna de std dev                
            if item is not None:
              standard_dev_value = float(unicode(item.text()).encode('utf8')) 
              #value = format(value, precision)
              e_list = e_list+[standard_dev_value]              
        e = e_list 
        #------------------------------------------------------------------------------#
        
        #---- Sendo y = m*x + b; equacao da reta -----------------#        
        m,b = np.polyfit(x, y, 1)      
        eq_reta = "y = %sx + %s" %(m, b)   
        #---------------------------#
        
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        
        fit = np.polyfit(x,y,1)
        fit_fn = np.poly1d(fit)
       

        self.figure = plt.figure(figsize=(10,10))
        ax1 = self.figure.add_axes([0.1, 0.3, 0.85, 0.65])
        ax1.set_ylabel('Concentration')
        ax1.set_xlabel('Absorvance')
        ax1.plot(x,y, 'yo', x, fit_fn(x), 'b', label=eq_reta)
        plt.errorbar(x, y, e, linestyle='None', marker='.', color='r')
        plt.xlim()
        plt.ylim()
        ax1.scatter(x, y)
        plt.title(titulo)
        plt.grid(True, color='k')       
        
        self.canvas = FigureCanvas(self.figure)     
        self.gridLayout_graph.addWidget(self.canvas, 2,0,1,2)
        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        self.gridLayout_graph.addWidget(self.navi_toolbar, 1,0,1,2)
        

        self.equation_label.setText(eq_reta)
        self.R_label.setText("R: "+str(r_value))
        
        #Sendo x concentracao e y absorvancia medida e ycal absorvancia da reta
        #Sendo ycal = m*x + b; equacao da reta
        
        
        #----------------subtraindo absorvancias da media------------------#
        out_row = 0
        out_column = 1
        out_columns = (self.outlier_tableWidget.columnCount())-2        
        out_rows = self.outlier_tableWidget.rowCount()           
        out_mean_column = (self.outlier_tableWidget.columnCount())-2
        absorvance_list =[]
        abs_minus_med =[]
        av_res_x =[]
        
        n = 0 #numero de valores de cada linha
        while out_row < out_rows: #row e a linha atual, rows e o total de linhas 
            while out_column < out_columns:#column e a coluna atual, columns e o total de colunas                
                absorvance_item = self.outlier_tableWidget.item(out_row, out_column)
                if absorvance_item is not None:                  
                  absorvance_value = float(unicode(absorvance_item.text()).encode('utf8'))
                  abs_minus_med = abs_minus_med + [(absorvance_value - y_list[out_row])]
                  #print abs_minus_med
                  #print len(abs_minus_med)
                  absorvance_list = absorvance_list +[absorvance_value]
                  n = n+1                
                  out_column = out_column+1
                  av_res_x = av_res_x + [out_row]
                else:
                  out_column = out_column+1
            out_column = 1
            n = 0            
            out_row = out_row+1
        #print abs_minus_med
        #print av_res_x
        #-------------------------------#

        #-------------plotar pontos av res-----------------#
        ax2 = self.figure.add_axes([0.1, 0.01, 0.35, 0.2])
        ax2.plot(av_res_x,abs_minus_med, linestyle='None', marker='.', color='r')        
        #---------plotar linha 0--------------#
        numero = 0
        av_y = []
        while numero < len(av_res_x):
            av_y = av_y + [0]            
            numero = numero+1

        ax2.plot(av_res_x,av_y, 'b')
        self.canvas = FigureCanvas(self.figure)     
        self.gridLayout_graph.addWidget(self.canvas, 2,0,1,2)
        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        self.gridLayout_graph.addWidget(self.navi_toolbar, 1,0,1,2)
        


    def grubbs_test(self): #ok e passa os dados para tabela de outliers
        tabela = self.outlier_tableWidget
        casas_decimais = 4 #numero de casas decimais
        precision = '.'+str(casas_decimais)+'f'
        xi_column = 1
        xi_row = 0
        rows = self.tableWidget.rowCount()
        columns = (self.tableWidget.columnCount())-2
        mean_column = (self.tableWidget.columnCount())-2
        std_dev_column = (self.tableWidget.columnCount())-1
        
        n_amostras = self.tableWidget.columnCount()-3
        if n_amostras == 3:
          Gtab = 1.15
        elif n_amostras == 4:
          Gtab = 1.46
        elif n_amostras == 5:
          Gtab = 1.67
        elif n_amostras == 6:
          Gtab = 1.82
        elif n_amostras == 7:
          Gtab = 1.94
        elif n_amostras == 8:
          Gtab = 2.03
        elif n_amostras == 9:
          Gtab = 2.11
        elif n_amostras == 10:
          Gtab = 2.18
        elif n_amostras == 11:
          Gtab = 2.23
        elif n_amostras == 12:
          Gtab = 2.29

        #-----------------pegando valores de absorvancia (xi)-------------------#
        if self.grubbs_checkBox.isChecked():
          while xi_row < rows:
              while xi_column < columns:
                  absorvance_item = self.tableWidget.item(xi_row, xi_column)
                  concentration_item = self.tableWidget.item(xi_row, 0)
                  if absorvance_item and concentration_item is not None:
                    xi_absorvance_value = float(unicode(absorvance_item.text()).encode('utf8'))
                    
                    concentration_value = unicode(concentration_item.text()).encode('utf8')                    
                    outlier_concentration_item = QtGui.QTableWidgetItem(concentration_value.decode('utf8'))
                    
                    self.outlier_tableWidget.setItem(xi_row, 0, outlier_concentration_item)                        
                    self.outlier_tableWidget.resizeColumnsToContents()
                    self.outlier_tableWidget.resizeRowsToContents() 

                    xi_column = xi_column+1
                    #print xi_absorvance_value
                    mean_item = self.tableWidget.item(xi_row, mean_column)
                    std_dev_item = self.tableWidget.item(xi_row, std_dev_column)
                    if mean_item and std_dev_item is not None:
                      row_mean = float(unicode(mean_item.text()).encode('utf8')) #pegar media
                      row_std_dev = float(unicode(std_dev_item.text()).encode('utf8')) #pegar std_dev
                      Gcalc = abs((xi_absorvance_value - row_mean) / row_std_dev) #teste de grubbs
                      if Gcalc > Gtab:                      
                        absorvance_item.setTextColor(QtGui.QColor("red"))#trocar cores dos valores fora do teste
                      else:  #passa os valores para tabela outlier
                        
                        outlier_absorvance_value = str(xi_absorvance_value)                    
                        outlier_item = QtGui.QTableWidgetItem(outlier_absorvance_value.decode('utf8'))
                        self.outlier_tableWidget.setItem(xi_row, xi_column-1, outlier_item)                        
                        self.outlier_tableWidget.resizeColumnsToContents()
                        self.outlier_tableWidget.resizeRowsToContents()                       
                        
              xi_column = 1
              xi_row = xi_row+1
        else: # checkbox desmarcado, retornar todos os valores
          while xi_row < rows:
              while xi_column < columns:
                  absorvance_item = self.tableWidget.item(xi_row, xi_column)
                  if absorvance_item is not None:
                    xi_absorvance_value = float(unicode(absorvance_item.text()).encode('utf8')) 
                    xi_column = xi_column+1                    
                    absorvance_item.setTextColor(QtGui.QColor("black"))#trocar cores dos valores fora do teste       
  
              xi_column = 1
              xi_row = xi_row+1

        self.outlier_mean()
        self.outlier_stddev()
        
    
    def homocedastidade(self):#faltando pegar valores outliers
        
        xi_row = 0
        rows = self.outlier_tableWidget.rowCount()
        std_dev_column = (self.outlier_tableWidget.columnCount())-1
        list_std_dev = []
        soma_var = 0
        
        k = self.outlier_tableWidget.rowCount()
        n =  self.outlier_tableWidget.columnCount() - 3
        
        Ctab = 0.967 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        
        while xi_row < rows:
            std_dev_item = self.outlier_tableWidget.item(xi_row, std_dev_column)
            if std_dev_item is not None:  
              row_std_dev = unicode(std_dev_item.text()).encode('utf8') #pegar std_dev
              list_std_dev = list_std_dev + row_std_dev.split(" ")
              #print list_std_dev
              soma_var = soma_var + float(row_std_dev)
              #print soma_var
            xi_row = xi_row+1

        maior_var = max(list_std_dev)
        maior_var = (float(maior_var))**2
        
        Ccalc = maior_var / soma_var        
        if Ccalc > Ctab :
          self.homocedast_label.setText("Nao e homocedastico")
        else:
          self.homocedast_label.setText("Homocedastico")
          self.min_quad_ord_n_pond()
          self.analise_var()

    def analise_var(self):
        
        
        p = 2# numero de grupos!!!!!!!!!<<<<<<<<<<<<<???????????????
        
        
        x_list = []
        n = self.outlier_tableWidget.rowCount()
        gl = n-1
        casas_decimais = 4 #numero de casas decimais
        precision = '.'+str(casas_decimais)+'f'
        mean_list = []            
        concentration_list = []
        
        o_row = 0  
        o_rows = self.outlier_tableWidget.rowCount()           
        o_mean_column = (self.outlier_tableWidget.columnCount())-2
        o_concentration_column = 0
        
        while o_row < o_rows: #row e a linha atual, rows e o total de linhas      

            mean_item = self.outlier_tableWidget.item(o_row, o_mean_column)
            concentration_item = self.outlier_tableWidget.item(o_row, o_concentration_column)
            if mean_item is not None:                  
              mean_value = float(unicode(mean_item.text()).encode('utf8'))
              mean_list = mean_list+[mean_value]
            if concentration_item is not None:                  
              concentration_value = float(unicode(concentration_item.text()).encode('utf8'))
              concentration_list = concentration_list+[concentration_value]
            else:
              pass 
            o_row = o_row+1
            
        #print mean_list #lista de media das absrovancias
        #print concentration_list #lista de concentracoes
        eq_reta = (unicode(self.equation_label.text()).encode('utf8')).split()
        #print eq_reta
        b = eq_reta[4]
        m = eq_reta[2].replace("x","")
        #print b
        #print m

        o_row = 0
        o_column = 1
        o_columns = (self.outlier_tableWidget.columnCount())-2        
        o_rows = self.outlier_tableWidget.rowCount()           
        o_mean_column = (self.outlier_tableWidget.columnCount())-2
        absorvance_list =[]
        
        n = 0 #numero de valores de cada linha
        while o_row < o_rows: #row e a linha atual, rows e o total de linhas 
            while o_column < o_columns:#column e a coluna atual, columns e o total de colunas                
                absorvance_item = self.outlier_tableWidget.item(o_row, o_column)
                if absorvance_item is not None:                  
                  absorvance_value = float(unicode(absorvance_item.text()).encode('utf8'))
                  absorvance_list = absorvance_list +[absorvance_value]
                  n = n+1                
                  o_column = o_column+1
                else:
                  o_column = o_column+1
            o_column = 1
            n = 0            
            o_row = o_row+1
        #print absorvance_list
        #print concentration_list
        
        # sendo y a absorvancia
        y_barra = sum(absorvance_list)/len(absorvance_list) #media das absorvancias
        
        sq_reg = 0
        n = 0
        while n < len(concentration_list):
            y_chapeu = m*(int(concentration_list[n])) + b # calculando a absorvancia da reta com os valores de concentracao         
            q_reg = (float(y_chapeu) - float(y_barra))**2
            sq_reg = float(sq_reg + q_reg)
            n = n+1
            #print sq_reg
        #print sq_reg
        qm_reg = sq_reg/(p-1) #2 e o numero de parametros??? sq_reg/p-1
        print qm_reg# quadrado medio da regressao
        
        sq_res = 0
        #n_chapeu = len(concentration_list)
        #n_points = (self.outlier_tableWidget.columnCount())-2
        n = 0 #numero de valores de cada linha
        o_row = 0
        o_column = 1
        o_columns = (self.outlier_tableWidget.columnCount())-2        
        o_rows = self.outlier_tableWidget.rowCount()           
        o_mean_column = (self.outlier_tableWidget.columnCount())-2
        sq_res = 0
        
        while o_row < o_rows: #row e a linha atual, rows e o total de linhas 
            while o_column < o_columns:#column e a coluna atual, columns e o total de colunas                
                absorvance_item = self.outlier_tableWidget.item(o_row, o_column)
                concentration_item = self.outlier_tableWidget.item(o_row, 0)
                if absorvance_item and concentration_item is not None:                  
                  absorvance_value = float(unicode(absorvance_item.text()).encode('utf8'))
                  concentration_value = float(unicode(concentration_item.text()).encode('utf8'))
                  y_chapeu = m*int(concentration_value) +b
                  subtracao = (float(absorvance_value) - float(y_chapeu))**2
                  sq_res = sq_res + subtracao
                  o_column = o_column+1
                  n = n+1
                else:
                  o_column = o_column+1
            o_column = 1                
            o_row = o_row+1
        qm_res = sq_res/(len(absorvance_list)-p) #onde 2 e o valor de p???
        
        sq_tot = sq_res + sq_reg
        qm_tot = qm_reg + qm_res
        f = qm_reg/qm_res #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<faltando pegar o valor de f tabelado!!!!!!!!!
        #n e o numero de pontos!!!!!!
        #p e o numero de grupos!!!!!!!
        
        self.gl_reg_label.setText(str(p-1))
        self.gl_res_label.setText(str(n-p)) 
        self.gl_tot_label.setText(str(n-1)) 
        
        self.sq_reg_label.setText(str(sq_reg))
        self.sq_res_label.setText(str(sq_res))
        self.sq_tot_label.setText(str(sq_tot))
        
        self.qm_reg_label.setText(str(qm_reg))
        self.qm_res_label.setText(str(qm_res))
        self.qm_tot_label.setText(str(qm_tot))
        
        self.f_label.setText("F: "+str(f))
                
    #------------------------END OF ANALISES ESTATISTICAS--------------------#    
        
        
    #----------------OPERACOES GUI---------------------#
    
    
    def changeHorizontalHeader(self, index):#OK
        oldHeader = self.tableWidget.horizontalHeaderItem(index).text()
        newHeader, ok = QtGui.QInputDialog.getText(self,
                                                      'Change header label for column %d' % index,
                                                      'Header:',
                                                       QtGui.QLineEdit.Normal,
                                                       oldHeader)
        if ok:
            self.tableWidget.horizontalHeaderItem(index).setText(newHeader) 
                

    def import_file(self):#OK
                
        path = QtGui.QFileDialog.getOpenFileName(
                self, 'Open File', '', )
        if not path.isEmpty(): 
        
            #--------Numero de colunas de valores-----------#
            total = 0
            with open(unicode(path)) as f:
                for line in f:                    
                    finded = line.find('Values:')                    
                    if finded == 0:
                        total += 1               
            #--------------------#
            
            with open(unicode(path), 'rb') as stream:
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(total+1)
                column = 1                
                for row in csv.reader(open(unicode(path), 'rb')):
                  row = ','.join(row)
                  
                  #----inport Concentration------#
                  if row.startswith('Concentration:'):
                    rowdata = row.split(',')                    
                    rowdata = filter(None, rowdata)
                    rowdata = rowdata[1:]                    
                    for row in range(len(rowdata)):                        
                        self.tableWidget.insertRow(row)                     
                    for row, data in enumerate(rowdata):                        
                        item = QtGui.QTableWidgetItem(data.decode('utf8'))                        
                        self.tableWidget.setItem(row, 0, item)                        
                        self.tableWidget.resizeColumnsToContents()
                        self.tableWidget.resizeRowsToContents()
                  #-------------------------------#
                  
                  #----inport Values ------#                  
                  elif row.startswith('Values:'):
                    rowdata = row.split(',')                    
                    rowdata = filter(None, rowdata)
                    rowdata = rowdata[1:]
                    for row, data in enumerate(rowdata):                        
                        item = QtGui.QTableWidgetItem(data.decode('utf8'))                        
                        self.tableWidget.setItem(row, column, item)                        
                        self.tableWidget.resizeColumnsToContents()
                        self.tableWidget.resizeRowsToContents()
                    column = column+1
                  #------------------------#
                  
                  #----inport Mean ------#                  
                  elif row.startswith('Mean:'):
                    self.tableWidget.insertColumn(self.tableWidget.columnCount())#column mean
                    rowdata = row.split(',')                    
                    rowdata = filter(None, rowdata)
                    rowdata = rowdata[1:]                
                    for row, data in enumerate(rowdata):                        
                        item = QtGui.QTableWidgetItem(data.decode('utf8'))                        
                        self.tableWidget.setItem(row, (self.tableWidget.columnCount()-1), item)                        
                        self.tableWidget.resizeColumnsToContents()
                        self.tableWidget.resizeRowsToContents()
                  #------------------------#
                  
                  #----inport Standard Deviation ------#                  
                  elif row.startswith('Standard Deviation:'):
                    self.tableWidget.insertColumn(self.tableWidget.columnCount())#column std dev
                    rowdata = row.split(',')                    
                    rowdata = filter(None, rowdata)
                    rowdata = rowdata[1:]                
                    for row, data in enumerate(rowdata):                        
                        item = QtGui.QTableWidgetItem(data.decode('utf8'))                        
                        self.tableWidget.setItem(row, (self.tableWidget.columnCount()-1), item)                        
                        self.tableWidget.resizeColumnsToContents()
                        self.tableWidget.resizeRowsToContents()
                  #------------------------#
                  
                  #----Valores da caixa de texto------------#
                  elif row.startswith('Substance:')is True:                    
                    rowdata = row.split(',')
                    rowdata = filter(None, rowdata)
                    if len(rowdata) > 1:                        
                        self.substance_lineEdit.setText(rowdata[1])
                        #print rowdata[1]
                  elif row.startswith('Diluent:') is True:
                    rowdata = row.split(',')
                    rowdata = filter(None, rowdata)  
                    if len(rowdata) > 1:                        
                        self.solution_lineEdit.setText(rowdata[1])
                        #print rowdata[1]   
                  #-----------------------------------------#
        
        rep = self.tableWidget.columnCount() - 3 #arrumar o numero de replicatas
        self.tableWidget.setHorizontalHeaderLabels(['Concentration']+(rep*['A'])+['Mean']+['Standard Deviation'])
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        
    def save_file(self):#OK
        
        path = QtGui.QFileDialog.getSaveFileName(
                self, 'Save File', '', 'CSV(*.csv)')
        if not path.isEmpty():
            with open(unicode(path), 'wb') as stream:
                writer = csv.writer(stream)
                
                #substancia
                substance_data = []
                subst_text = self.substance_lineEdit.text()
                substance_data.append(subst_text)
                writer.writerow(['Substance:']+substance_data)                
                #diluente utilizado
                diluent_data = []
                diluent_text = self.solution_lineEdit.text()
                diluent_data.append(diluent_text)
                writer.writerow(['Diluent:']+diluent_data)
                
                #---Save Concentration Column----#   
                concentration_data =['Concentration:']
                for row in range(self.tableWidget.rowCount()):
                    concentration_item = self.tableWidget.item(row, 0)                         
                    if concentration_item is not None:                            
                        concentration_data.append(
                            unicode(concentration_item.text()).encode('utf8'))
                    else:
                        concentration_data.append('')
                writer.writerow(concentration_data)
                #------------------------#
                
                #-------- Save Rowdata-----------#
                for column in range(1, (self.tableWidget.columnCount()-2)):                
                    rowdata = ['Values:']                    
                    for row in range(self.tableWidget.rowCount()):
                        item = self.tableWidget.item(row, column)                         
                        if item is not None:                            
                            rowdata.append(
                                unicode(item.text()).encode('utf8'))
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)
                #----------------------------------#
                
                #---Save Mean Column----#    
                for column in range((self.tableWidget.columnCount()-2), (self.tableWidget.columnCount()-1)):
                    meandata =['Mean:']
                    for row in range(self.tableWidget.rowCount()):
                        meanitem = self.tableWidget.item(row, column)                         
                        if meanitem is not None:                            
                            meandata.append(
                                unicode(meanitem.text()).encode('utf8'))
                        else:
                            meandata.append('')
                    writer.writerow(meandata)
                #------------------------#
                
                #---Save Standard Deviation Column----#    
                for column in range((self.tableWidget.columnCount()-1), (self.tableWidget.columnCount())):
                    stddevdata =['Standard Deviation:']
                    for row in range(self.tableWidget.rowCount()):
                        stddevitem = self.tableWidget.item(row, column)                         
                        if stddevitem is not None:                            
                            stddevdata.append(
                                unicode(stddevitem.text()).encode('utf8'))
                        else:
                            stddevdata.append('')
                    writer.writerow(stddevdata)
                    
    def addrow(self):#OK
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()        
        
    def addcolumn(self):#OK
        self.tableWidget.insertColumn(1)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents() 
        
    def removerow(self):#OK precisa selecionar a linha
        self.tableWidget.removeColumn(self.tableWidget.currentRow())
        
    def removecolumn(self):#OK precisa selecionar a coluna
        self.tableWidget.removeColumn(self.tableWidget.currentColumn())   
        
    #----------------------END OF OPERACOES GUI---------------------#
    
    
#------------------------END OF FUNCTIONS--------------------------------------------#    
    
def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
