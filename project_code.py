from tkinter import Y
from turtle import color
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
        self.mygraph=pg.PlotWidget(self.tab)
        self.mygraph.setGeometry(QtCore.QRect(15,411,831,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.mygraph.setYRange(0,100)
        self.mygraph.setTitle("Temperature and Humidity vs Time",color='r',size='15pt')
        self.mygraph.setLabel("left", "Temperature (°C) and Humidity (%)")
        self.mygraph.setLabel("bottom", "Time (s)")
        self.dataline= self.mygraph.plot()
        ##temp1
        self.mygraph1=pg.PlotWidget(self.tab_6)
        self.mygraph1.setGeometry(QtCore.QRect(10,80,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.mygraph1.setYRange(0,100)
        self.mygraph1.setTitle("Temp and RH in 1 hour",color=(170, 85, 0),size='15pt')
        self.mygraph1.setLabel("left", "Temperature (°C) and Humidity (%)")
        self.mygraph1.setLabel("bottom", "Time (s)")
        self.dataline= self.mygraph1.plot() 
        ##temp2
        self.mygraph2=pg.PlotWidget(self.tab_6)
        self.mygraph2.setGeometry(QtCore.QRect(590,80,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.mygraph2.setYRange(0,100)
        self.mygraph2.setTitle("Temp and RH in 1 week",color=(170, 85, 0),size='15pt')
        self.mygraph2.setLabel("left", "Temperature (°C) and Humidity (%)")
        self.mygraph2.setLabel("bottom", "Time (s)")
        self.dataline= self.mygraph2.plot()
        ##temp3
        self.mygraph3=pg.PlotWidget(self.tab_6)
        self.mygraph3.setGeometry(QtCore.QRect(10,390,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.mygraph3.setYRange(0,100)
        self.mygraph3.setTitle("Temp and RH in 1 month",color=(170, 85, 0),size='15pt')
        self.mygraph3.setLabel("left", "Temperature (°C) and Humidity (%)")
        self.mygraph3.setLabel("bottom", "Time (s)")
        self.dataline= self.mygraph3.plot()   
        ##temp4
        self.mygraph4=pg.PlotWidget(self.tab_6)
        self.mygraph4.setGeometry(QtCore.QRect(590,390,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.mygraph4.setYRange(0,100)
        self.mygraph4.setTitle("Temp and RH in 1 year",color=(170, 85, 0),size='15pt')
        self.mygraph4.setLabel("left", "Temperature (°C) and Humidity (%)")
        self.mygraph4.setLabel("bottom", "Time (s)")
        self.dataline= self.mygraph4.plot()
        ##temp5
        self.mygraph5=pg.PlotWidget(self.tab_5)
        self.mygraph5.setGeometry(QtCore.QRect(10,80,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.mygraph5.setYRange(0,100)
        self.mygraph5.setTitle("Temp and RH in 1 hour",color=(170, 85, 0),size='15pt')
        self.mygraph5.setLabel("left", "Temperature (°C) and Humidity (%)")
        self.mygraph5.setLabel("bottom", "Time (s)")
        self.dataline= self.mygraph5.plot() 
        ##temp6
        self.mygraph6=pg.PlotWidget(self.tab_5)
        self.mygraph6.setGeometry(QtCore.QRect(590,80,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.mygraph6.setYRange(0,100)
        self.mygraph6.setTitle("Temp and RH in 1 week",color=(170, 85, 0),size='15pt')
        self.mygraph6.setLabel("left", "Temperature (°C) and Humidity (%)")
        self.mygraph6.setLabel("bottom", "Time (s)")
        self.dataline= self.mygraph6.plot()
        ##temp7
        self.mygraph7=pg.PlotWidget(self.tab_5)
        self.mygraph7.setGeometry(QtCore.QRect(10,390,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.mygraph7.setYRange(0,100)
        self.mygraph7.setTitle("Temp and RH in 1 month",color=(170, 85, 0),size='15pt')
        self.mygraph7.setLabel("left", "Temperature (°C) and Humidity (%)")
        self.mygraph7.setLabel("bottom", "Time (s)")
        self.dataline= self.mygraph7.plot()   
        ##temp8
        self.mygraph8=pg.PlotWidget(self.tab_5)
        self.mygraph8.setGeometry(QtCore.QRect(590,390,561,291))
        self.x1 = np.arange(100)
        self.y1= np.arange(100)
        self.mygraph8.setYRange(0,100)
        self.mygraph8.setTitle("Temp and RH in 1 year",color=(170, 85, 0),size='15pt')
        self.mygraph8.setLabel("left", "Temperature (°C) and Humidity (%)")
        self.mygraph8.setLabel("bottom", "Time (s)")
        self.dataline= self.mygraph8.plot() 


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

