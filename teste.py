import sys
import pyqtgraph as pg
import numpy as np
from PyQt4 import QtGui,QtCore

app = QtGui.QApplication(sys.argv)

x = [1,2,3,4,5]
y = [1,2,3,4,5]

xi = [8,9,10]


pen = QtGui.QPen()
pen.setColor(QtGui.QColor(125,175,25))
pen.setWidth(.7)




widget = pg.PlotWidget(title="Some Plotting")
widget.setWindowTitle("Random Plotting")

widget.plotItem.plot(x, pen=pen)
widget.plotItem.plot(xi, pen=pen)


widget.show()

sys.exit(app.exec_())