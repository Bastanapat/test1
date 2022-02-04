from PyQt5 import QtCore, QtGui, QtWidgets
from project import Ui_MainWindow
from datetime import datetime
import sys
import pyqtgraph as pg
import numpy as np
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
class myproject(Ui_MainWindow):
    def __init__(self) -> None:
        super().setupUi(MainWindow)
        self.date()
        self.tm()
        self.gcn()
        self.graphtemp1()
        

    def graphtemp1(self):
        ##Main
        self.mygraph=pg.PlotWidget(MainWindow)
        self.mygraph.setGeometry(QtCore.QRect(15,411,821,281))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.dataline= self.mygraph.plot()
        ##temp1
        self.mygraph=pg.PlotWidget(self.tab_6)
        self.mygraph.setGeometry(QtCore.QRect(10,80,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.dataline= self.mygraph.plot() 
        ##temp2
        self.mygraph=pg.PlotWidget(self.tab_6)
        self.mygraph.setGeometry(QtCore.QRect(590,80,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.dataline= self.mygraph.plot()
        ##temp3
        self.mygraph=pg.PlotWidget(self.tab_6)
        self.mygraph.setGeometry(QtCore.QRect(10,390,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.dataline= self.mygraph.plot()   
        ##temp4
        self.mygraph=pg.PlotWidget(self.tab_6)
        self.mygraph.setGeometry(QtCore.QRect(590,390,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.dataline= self.mygraph.plot()
        ##temp5
        self.mygraph=pg.PlotWidget(self.tab_5)
        self.mygraph.setGeometry(QtCore.QRect(10,80,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.dataline= self.mygraph.plot() 
        ##temp6
        self.mygraph=pg.PlotWidget(self.tab_5)
        self.mygraph.setGeometry(QtCore.QRect(590,80,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.dataline= self.mygraph.plot()
        ##temp7
        self.mygraph=pg.PlotWidget(self.tab_5)
        self.mygraph.setGeometry(QtCore.QRect(10,390,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.dataline= self.mygraph.plot()   
        ##temp8
        self.mygraph=pg.PlotWidget(self.tab_5)
        self.mygraph.setGeometry(QtCore.QRect(590,390,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.dataline= self.mygraph.plot() 


    
        

    def gcn(self):
        print('Ok')
        pass  
        


        

    def tm(self):
        self.mytm1=QtCore.QTimer() 
        self.mytm1.timeout.connect(self.date)
        self.mytm1.setInterval(1000)
        self.mytm1.start()


    def date(self):
        self.now_1 = datetime.now()
        self.day_1 = self.now_1.day
        self.x = self.now_1.strftime("%a")
        self.month_1 = self.now_1.strftime("%B")
        self.year_1 = self.now_1.year
        self.date_time1 = self.now_1.strftime("%X")
        self.label.setText(f"{self.x} {self.day_1} {self.month_1} {self.year_1} {self.date_time1}")
        self.label_20.setText(f"{self.x} {self.day_1} {self.month_1} {self.year_1} {self.date_time1}")
        self.label_22.setText(f"{self.x} {self.day_1} {self.month_1} {self.year_1} {self.date_time1}")
        


if __name__ == "__main__":
    myp_j = myproject()
    MainWindow.show()
    sys.exit(app.exec_())

