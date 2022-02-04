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
        
        self.mygraph=pg.PlotWidget(self.tab)
        self.mygraph.setGeometry(QtCore.QRect(310,390,471,261))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.dataline= self.mygraph.plot()  


    def gcn(self):
        self.tabWidget.tabBarClicked.connect(self.tab_1)    
    
    def tab_1(self):
        print("a")
        


        

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

