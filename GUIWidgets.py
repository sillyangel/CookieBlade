## @file GUIWidgets.py
#
# @brief this file contains GUI Widget Classes
#
# @section libraries_main Libraries/Modules
# - sys standard library (https://docs.python.org/3/library/sys.html)
#   - access to sys.argv and sys.exit functions
# - PyQt5 external library (pip install PyQt5)
#   - access to PyQt5 GUI functions
# - PyQt5.QtWidgets external library
#   - access to PyQt5 UI Widgets
# - PyQt5.QtWebEngineWidgets external library (pip install PyQtWebEngine)
#   - access to PyQt5 web browser functions

#Imports
import sys
from PyQt5 import QtCore, QtGui, QtWidgets #pip3 install pyqt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import * #pip3 install PyQtWebEngine
from PyQt5.QtChart import * #pip3 install PyQtChart
from pyqtgraph import PlotWidget, plot, exporters #pip3 install pyqtgraph
import functools

## Documentation for GUIWidgets.py
# Contains all UI Widget classes
# We can reuse classes to make different widgets for diffferent purpose

#Class to initialize a new instance of QApplication module which is required to run PyQt5
class StartApp:
    """! StartApp class
    Defines the QApplication object which allows the creation of all QtWidgets
    """
    def __init__(self):
        self.QApp = QApplication(sys.argv)

#Class to create a new Window
class NewWindow:
    """! NewWindow class
    Defines the window object used to display widgets
    """
    def __init__(self, name, lenX, lenY):
        """! NewWindow class initializer
        @param name used to name the window title
        @param lenX used to set the horizontal length of the window
        @param lenY used to set the veritical height of the window
        """
        #Initialize new instance of Window UI
        self.QWin = QMainWindow()
        #Set Window Title
        self.QWin.setWindowTitle(name)
        #Set Window Size
        self.QWin.resize(lenX,lenY)

    #Method to set Window icon image
    def setWindowIcon(self,image):
        """! setWindowIcon method used to set image as Window Icon
        @param image image name to be used as Window Icon
        """
        self.QWin.setWindowIcon(QtGui.QIcon(image))
    
    def show(self):
        self.QWin.show()

#Class to create a new Label
class NewLabel:
    """! NewLabel class
    Defines the label object used to display text label to guide users
    """
    def __init__(self, window, posX, posY, lenX, lenY):
        """! NewLabel class initializer
        @param window used to determine which window for the widget to appear on
        @param posX used to set the X coordinate of where the label will appear
        @param posY used to set the Y coordinate of where the label will appear
        @param lenX used to set the horizontal length of the label
        @param lenY used to set the vertical height of the label
        """
        #Initialize new instance of Label UI
        self.label = QLabel(window)
        #Set Label x & y position and size
        self.label.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Set alignment of Label text to align center
        self.label.setAlignment(QtCore.Qt.AlignCenter)

    #Method to set Label Text
    def setText(self, text):
        """! setText method 
        @param text used to set the text to be displayed by the label
        """
        self.label.setText(text)
        #Automatically update the length of label to fit text
        self.label.update()

    def setFont(self, fontStyle, fontSize):
        self.label.setFont(QFont(fontStyle, fontSize))
    
    #Method to display image in Label
    def setImage(self, image):
        """! setImage method
        @param image used to determine what image to be displayed in label
        """
        #Set display image in parameter in Label
        self.label.setPixmap(QtGui.QPixmap(image))
        #Enable image scaling to fit Label size
        self.label.setScaledContents(True)
    
    def setFont(self, fontStyle, fontSize):
        self.label.setFont(QFont(fontStyle,int(fontSize)))

#Class to create new TextBox
class NewTextBox:
    """! NewTextBox class
    Defines the textbox object used to retrieve user input
    """
    def __init__(self, window, posX, posY, lenX, lenY):
        """! NewTextBox class initializer
        @param window used to determine which window for the widget to appear on
        @param posX used to set the X coordinate of where the label will appear
        @param posY used to set the Y coordinate of where the label will appear
        @param lenX used to set the horizontal length of the label
        @param lenY used to set the vertical height of the label
        """
        #Initialize new instance of TextBox UI
        self.textbox = QLineEdit(window)
        #Set TextBox x & y position and size
        self.textbox.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))

    #Method to set palceholder text
    def setText(self, text):
        """! setText method
        @param text used to set the text to be displayed by the label
        """
        self.textbox.setPlaceholderText(text)
    
    def setFont(self, fontStyle, fontSize):
        self.textbox.setFont(QFont(fontStyle,int(fontSize)))

#Class to create new PushButton
class NewPushButton:
    """! NewPushButton class
    Defines the PushButton object to recieve button click input
    """
    def __init__(self, window, posX, posY, lenX, lenY, functionName):
        """! NewPushButton class initializer
        @param window used to determine which window for the widget to appear on
        @param posX used to set the X coordinate of where the label will appear
        @param posY used to set the Y coordinate of where the label will appear
        @param lenX used to set the horizontal length of the label
        @param lenY used to set the vertical height of the label
        @param functionname used to determine which function to call when button is clicked
        """
        #Initialize new instance of PushButton UI
        self.PushButton = QPushButton(window)
        #Set PushButton x & y position and size
        self.PushButton.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Calls function when PushButton is clicked
        self.PushButton.clicked.connect(functionName)

    #Set PushButton text
    def setText(self, text):
        """! setText method
        @param text used to set the text to be displayed by the label
        """
        self.PushButton.setText(text)
    
    def setFont(self, fontStyle, fontSize):
        self.PushButton.setFont(QFont(fontStyle,int(fontSize)))

class messageBox:
    def __init__(self, winTitle="", text="", winIcon="" ,show=True,icon="Critical"):
        self.msgBox = QMessageBox()
        msgBox = self.msgBox
        if winTitle:
            msgBox.setWindowTitle(winTitle)
        if winIcon:
            msgBox.setWindowIcon(QtGui.QIcon(winIcon))
        if text:
            msgBox.setText(text)
        if icon == "Critical":
            msgBox.setIcon(QMessageBox.Critical)
        if show:
            self.show()

    def show(self):
        msgBox = self.msgBox
        msgBox.exec_()

#Class to create new Graph
class NewGraph:
    """! NewGraph class
    Defines the Graph object to take in input and display graph
    """
    def __init__(self, window, posX, posY, lenX, lenY):
        """! NewGraph class initializer
        @param window used to determine which window for the graph to appear on
        @param posX used to set the X coordinate of where the graph will appear
        @param posY used to set the Y coordinate of where the graph will appear
        @param lenX used to set the horizontal length of the graph
        @param lenY used to set the vertical height of the graph
        """
        self.Graph = PlotWidget(window)
        self.Graph.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #Enables graph to show grid
        self.Graph.showGrid(x = True, y = True)

    def plotGraph(self, axisX, axisY, color, points):
        """! plotGraph method
        @param axisX takes in list to plot the X axis of graph
        @param axisY takes in list to plot the Y axis of graph
        @param color used to determine the line color of graph
        @param points used to determine symbol used to mark points
        """
        self.Graph.plot(axisX, axisY, pen = color, symbol = points)
        
    def setBackGroundColor(self, color):
        """! setBackGroundColor method
        @param color used to set the background color of graph
        """
        self.Graph.setBackground(color)
    
    def setGraphTitle(self, title, titleColor, titleSize):
        """! setGraphTitle method
        @param title used to set the graph title label
        @param titleColor used to set the graph title color
        @param titleSize used to set the font size of graph title
        """
        self.Graph.setTitle(title, color = titleColor, size = titleSize)

    def setAxisLabel(self, position, label, labelColor, labelSize):
        """! setAxisLabel method
        @param position used to determine the position of axis
        @param label used to determine what to display for axis
        @param labelcolor used to determine the color for axis
        @param labelSize used to determine the font size of axis
        """
        fontstyle = {"color":labelColor, "font-size":labelSize}
        self.Graph.setLabel(position, label, **fontstyle)
    
    def setAxisIntervalTo1(self, axisLabel, axis):
        """! setAxisIntervalTo1 method
        @param axisLabel used to determine which axis label to re-set interval
        @param axis used to determine the range of values to set for axis
        """
        storeAxis = self.Graph.getAxis(axisLabel)
        getValues = [(value, str(value)) for value in (range(int(min(axis)), int(max(axis)+1)))]
        storeAxis.setTicks([getValues, []])

#Class to create new bowser
class newWebBrowser():
    """! newWebBrowser class
    Defines the web browser object to display webpage
    """
    def __init__(self, lenX, lenY):
        """! newWebBrowser class initializer
        @param lenX used to set the horizontal length of the browser
        @param lenY used to set the vertical height of the browser
        """
        self.webEngine = QWebEngineView()
        self.webEngine.resize(lenX, lenY)
    
    def openURL(self, link):
        """! openURL method
        @param link used to determine which webpage to display/set as window name
        """
        self.webEngine.setWindowTitle(link)
        self.webEngine.load(QtCore.QUrl(link))
    
    def showWeb(self):
        """! showWeb method
        Used to show browser
        """
        self.webEngine.show()
    
class newPieChart():
    def __init__(self):
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.AllAnimations)
        
        #self.chart.legend().setAlignment(QtCore.Qt.AlignLeft)
        #self.chart.mapToPosition(QtCore.QPointF(500,500))
        self.chart.setBackgroundVisible(False)
        self.series = QPieSeries()
        
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(QtCore.Qt.AlignBottom)
        self.chartview = QChartView(self.chart)

    def setPos(self, posX, posY):
        #self.Graph = PlotWidget(window)
        #self.Graph.setGeometry(QtCore.QRect(posX, posY, lenX, lenY))
        #self.chart.setGeometry(posX,posY,100,100)
        #self.chart.setPos(posX,posY)
        #QChartView(self.chart).frameGeometry, #frameGeometry returns QRect
        #self.chartview.setGeometry(posX, posY,100,100)
        #functions i have tested that did not work ^

        #function im currently testing but made it disappear instead:
        test = QtCore.QRectF()
        test.setHeight(500)
        test.setWidth(500)
        test.moveTo(250,250)#This move the pi chart without the label.
        self.chart.setPlotArea(test)
        pass

    def setSize(self, width, height):
        self.chartview.setFixedSize(width,height)

    def setTitle(self, title):
        self.chart.setTitle(title)

    def setSeries(self, series):
        self.chart.addSeries(series)

    #data is a dictionary
    def addData(self, data):
        minSize = 0.1
        maxSize = 0.9
        donut = QPieSeries()
        sliceCount = len(data)
        j=0
        for x,y in data.items():
            slice_ = QPieSlice(x,y)
            slice_.setLabelVisible(True)
            slice_.setLabelColor(Qt.white)
            slice_.setLabelPosition(QPieSlice.LabelInsideTangential)
            slice_.hovered[bool].connect(functools.partial(self.explodeSlice, slice_=slice_))
            slice_.doubleClicked.connect(functools.partial(self.doubleClickSlice, slice_=slice_))
            donut.append(slice_)
            donut.setHoleSize(minSize)
            donut.setPieSize(minSize + (1) * (maxSize - minSize) )
            j+=1

        self.setSeries(donut)
    
    def viewChart(self, window):
        self.chartview.setRenderHint(QPainter.Antialiasing)
        window.setCentralWidget(self.chartview)

    def explodeSlice(self, exploded, slice_):
        if exploded:
            self.chart.setToolTip(str(int(slice_.value())))
        else:
            self.chart.setToolTip("")
        slice_.setExploded(exploded)

    def doubleClickSlice(self, slice_):
        print("test")


class newBarChart():
    def __init__(self):
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        
        #self.chart.legend().setAlignment(QtCore.Qt.AlignLeft)
        #self.chart.mapToPosition(QtCore.QPointF(500,500))
        self.chart.setBackgroundVisible(False)
        self.series = QPercentBarSeries()
        
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(QtCore.Qt.AlignBottom)


    def setTitle(self, title):
        self.chart.setTitle(title)

    def setSeries(self, series):
        self.chart.addSeries(series)

    #data is a list of list
    def addData(self, data, categories):
        for a in data:
            tempset = QBarSet(a[0])
            for idx, x in enumerate(a):
                if idx == 0:
                    continue
                tempset << x
            self.series.append(tempset) 

        axis = QBarCategoryAxis()
        axis.append(categories)
        self.chart.createDefaultAxes()
        self.chart.setAxisX(axis, self.series)
    
    def viewChart(self, window):
        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        window.setCentralWidget(self.chartview)
        test = QtCore.QRectF()
        test.setHeight(500)
        test.setWidth(500)
        test.moveTo(250,250)#This move the pi chart without the label.
        self.chart.setPlotArea(test)