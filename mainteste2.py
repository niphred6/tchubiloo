from PyQt4 import QtGui # Import the PyQt4 module
from scipy import stats
import decimal
import csv
import os, sys
import numpy as np

from decimal import Decimal

import matplotlib 
matplotlib.use('Qt4agg') # need to call use() before importing plt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar


import teste2

class ExampleApp(QtGui.QMainWindow, teste2.Ui_MainWindow):
    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)               
              
    #-------------------BUTTONS------------------------------#          
        
        #plot button
        self.pushButton.clicked.connect(self.plot1)
        self.pushButton_2.clicked.connect(self.plot2)
        
        #Canvas
        self.figure = plt.figure(figsize=(10,10))
        
        #ax1 = self.figure.add_subplot(211)
        #ax1.set_ylabel('volts')
        #ax1.set_title('a sine wave')
        #t = np.arange(0.0, 1.0, 0.01)
        #s = np.sin(2*np.pi*t)
        #line, = ax1.plot(t, s, color='blue', lw=2)
        # Fixing random state for reproducibility
        #np.random.seed(19680801)
        
        #ax2 = self.figure.add_axes([0.15, 0.1, 0.7, 0.3])
        #n, bins, patches = ax2.hist(np.random.randn(1000), 50,
        #    facecolor='yellow', edgecolor='yellow')
        #ax2.set_xlabel('time (s)')       

        
        self.canvas = FigureCanvas(self.figure)     
        self.gridLayout_4.addWidget(self.canvas, 2,0,1,2)
        

        
        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        self.gridLayout_4.addWidget(self.navi_toolbar, 1,0,1,2)
        
        
        
    def plot1(self): #media funcionando
        '''
        self.figure = plt.figure(figsize=(10,10))
        ax1 = self.figure.add_subplot(211)
        
        ax1.set_ylabel('volts')
        ax1.set_title('a sine wave')
        t = np.arange(0.0, 1.0, 0.01)
        s = np.sin(2*np.pi*t)
        line, = ax1.plot(t, s, color='blue', lw=2)
        np.random.seed(19680801)
        
        self.canvas = FigureCanvas(self.figure)     
        self.gridLayout_4.addWidget(self.canvas, 2,0,1,2)
        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        self.gridLayout_4.addWidget(self.navi_toolbar, 1,0,1,2)
        print "AAA"
        '''
        self.figure = plt.figure(figsize=(10,10))
        ax1 = self.figure.add_axes([0.1, 0.3, 0.85, 0.65])
        
        ax1.set_ylabel('volts')
        ax1.set_title('a sine wave')
        t = np.arange(0.0, 1.0, 0.01)
        s = np.sin(2*np.pi*t)
        line, = ax1.plot(t, s, color='blue', lw=2)
        np.random.seed(19680801)
        
        self.canvas = FigureCanvas(self.figure)     
        self.gridLayout_4.addWidget(self.canvas, 2,0,1,2)
        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        self.gridLayout_4.addWidget(self.navi_toolbar, 1,0,1,2)
        print "AAA"
        
    def plot2(self): #media funcionando
        
        ax2 = self.figure.add_axes([0.15, 0.05, 0.7, 0.2])
        n, bins, patches = ax2.hist(np.random.randn(1000), 50,
            facecolor='yellow', edgecolor='yellow')      
        print "bbb"

        
        self.canvas = FigureCanvas(self.figure)     
        self.gridLayout_4.addWidget(self.canvas, 2,0,1,2)
        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        self.gridLayout_4.addWidget(self.navi_toolbar, 1,0,1,2)

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function