from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget
from PyQt5.QtGui import QPainter, QBrush,QColor,QFont
from PyQt5.QtCore import Qt,QPoint
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.size=30
        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('canvas')
        self.show()
        self.i=True
        

    def paintEvent(self, e):
        self.width,self.height = (self.frameGeometry().width(),
                        self.frameGeometry().height())
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)

        rows=[row*self.size for row in range(self.height//self.size)]
        colums=[colum*self.size for colum in range(self.width//self.size)]
        for row in rows:
            self.makeRows(qp,row)
        for colum in colums:
            self.makeColums(qp,colum)
        i=0
        if self.i:
            self.txt= self.graftext("oi",(50,20),30)
            self.txt2= self.graftext("oi2",(50,600),60)
            self.i=False
        print(self.txt2.y)
        self.txt2.move(1)
        print(self.txt2.y)
        self.txt2.show(qp)
        qp.end()
        self.update()
        
    class graftext():
        def __init__(self,text,position,size):
            self.text=text
            self.x,self.y = position
            self.font=QFont()
            self.size=size
        def move(self,mov):
            self.y+=mov
        def show(self,qp):
            self.font.setPointSize(self.size)
            qp.setFont(self.font)
            qp.drawText (QPoint(self.x,self.y), self.text)

    def drawBrushes(self, qp):
      
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(0, 0, self.width, self.height)

    def makeColums(self,qp,place):
        qp.setPen(QColor(255, 255,255, 255))
        qp.drawLine(place,0,place,self.height)

    def makeRows(self,qp,place):
        qp.setPen(QColor(255, 255,255, 255))
        qp.drawLine(0,place,self.width,place)


       
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
