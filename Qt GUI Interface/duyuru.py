from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from gensim.summarization import summarize
from googletrans import Translator
from pprint import pprint
import requests
import urllib3
import string

k,l,m=0,0,0

class Ui_Form(object):
    def setupUi(self, Form):
        global eq,k,l,m
        Form.setObjectName("Form")
        Form.resize(1364, 738)
        self.brown = QtWidgets.QLabel(Form)
        self.brown.setGeometry(QtCore.QRect(0, 0, 1364, 738))
        self.brown.setText("")
        self.brown.setPixmap(QtGui.QPixmap("kahverengi.jpg"))
        self.brown.setScaledContents(True)
        self.brown.setObjectName("brown")
        self.green = QtWidgets.QLabel(Form)
        self.green.setGeometry(QtCore.QRect(0, 0, 1364, 738))
        self.green.setText("")
        self.green.setPixmap(QtGui.QPixmap("yesil.jpg"))
        self.green.setScaledContents(True)
        self.green.setObjectName("green")
        self.blue = QtWidgets.QLabel(Form)
        self.blue.setGeometry(QtCore.QRect(0, 0, 1364, 738))
        self.blue.setText("")
        self.blue.setPixmap(QtGui.QPixmap("mavi.jpg"))
        self.blue.setScaledContents(True)
        self.blue.setObjectName("blue")
        self.red = QtWidgets.QLabel(Form)
        self.red.setGeometry(QtCore.QRect(0, 0, 1364, 738))
        self.red.setText("")
        self.red.setPixmap(QtGui.QPixmap("kırmızı.jpg"))
        self.red.setScaledContents(True)
        self.red.setObjectName("red")
        self.purple = QtWidgets.QLabel(Form)
        self.purple.setGeometry(QtCore.QRect(0, 0, 1364, 738))
        self.purple.setText("")
        self.purple.setPixmap(QtGui.QPixmap("mor.jpg"))
        self.purple.setScaledContents(True)
        self.purple.setObjectName("purple")
        self.headline = QtWidgets.QLabel(Form)
        self.headline.setGeometry(QtCore.QRect(10, 20, 1322, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 146, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.headline.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.headline.setFont(font)
        self.headline.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.headline.setWordWrap(False)
        self.headline.setObjectName("headline")
        self.time = QtWidgets.QLabel(Form)
        self.time.setGeometry(QtCore.QRect(1030, 100, 250, 120))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 146, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.time.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.time.setFont(font)
        self.time.setScaledContents(False)
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.date = QtWidgets.QLabel(Form)
        self.date.setGeometry(QtCore.QRect(970, 250, 380, 120))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 146, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.date.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.date.setFont(font)
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setObjectName("date")
        self.temp = QtWidgets.QLabel(Form)
        self.temp.setGeometry(QtCore.QRect(960, 500, 400, 200))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 146, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.temp.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.temp.setFont(font)
        self.temp.setObjectName("temp")
        self.cloudy = QtWidgets.QLabel(Form)
        self.cloudy.setGeometry(QtCore.QRect(1095, 390, 80, 80))
        self.cloudy.setText("")
        self.cloudy.setPixmap(QtGui.QPixmap("Cloudy.png"))
        self.cloudy.setScaledContents(False)
        self.cloudy.setObjectName("cloudy")
        self.snowy = QtWidgets.QLabel(Form)
        self.snowy.setGeometry(QtCore.QRect(1100, 390, 80, 80))
        self.snowy.setText("")
        self.snowy.setPixmap(QtGui.QPixmap("Snowy_2.png"))
        self.snowy.setScaledContents(False)
        self.snowy.setObjectName("snowy")
        self.foggy = QtWidgets.QLabel(Form)
        self.foggy.setGeometry(QtCore.QRect(1100, 390, 90, 90))
        self.foggy.setText("")
        self.foggy.setPixmap(QtGui.QPixmap("foggy.png"))
        self.foggy.setScaledContents(True)
        self.foggy.setObjectName("foggy")
        self.sunny = QtWidgets.QLabel(Form)
        self.sunny.setGeometry(QtCore.QRect(1100, 390, 80, 80))
        self.sunny.setText("")
        self.sunny.setPixmap(QtGui.QPixmap("Sunny.png"))
        self.sunny.setScaledContents(False)
        self.sunny.setObjectName("sunny")
        self.rainy = QtWidgets.QLabel(Form)
        self.rainy.setGeometry(QtCore.QRect(1100, 390, 80, 80))
        self.rainy.setText("")
        self.rainy.setPixmap(QtGui.QPixmap("Rainy_2.png"))
        self.rainy.setScaledContents(False)
        self.rainy.setObjectName("rainy")
        self.windy = QtWidgets.QLabel(Form)
        self.windy.setGeometry(QtCore.QRect(1090, 380, 120, 88))
        self.windy.setText("")
        self.windy.setPixmap(QtGui.QPixmap("Windy.png"))
        self.windy.setScaledContents(False)
        self.windy.setObjectName("windy")
        self.announcement = QtWidgets.QTextBrowser(Form)
        self.announcement.setGeometry(QtCore.QRect(26, 110, 900, 602))
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.announcement.setFont(font)
        self.announcement.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.announcement.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.announcement.setLineWrapColumnOrWidth(0)
        self.announcement.setObjectName("announcement")
        self.announcement_2 = QtWidgets.QTextBrowser(Form)
        self.announcement_2.setGeometry(QtCore.QRect(26, 110, 900, 602))
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.announcement_2.setFont(font)
        self.announcement_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.announcement_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.announcement_2.setLineWrapColumnOrWidth(0)
        self.announcement_2.setObjectName("announcement_2")
        self.announcement_3 = QtWidgets.QTextBrowser(Form)
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75) 
        self.red.raise_()
        self.purple.raise_()
        self.green.raise_()
        self.brown.raise_()
        self.blue.raise_()
        self.headline.raise_()
        self.time.raise_()
        self.date.raise_()
        self.temp.raise_()
        self.cloudy.raise_()
        self.snowy.raise_()
        self.foggy.raise_()
        self.sunny.raise_()
        self.rainy.raise_()
        self.windy.raise_()
        self.announcement_2.raise_()
        self.announcement.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.snowy.hide()
        self.cloudy.hide()
        self.sunny.hide()
        self.rainy.hide()
        self.foggy.hide()
        self.windy.hide()
        
        
        timer = QtCore.QTimer(self.time)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime()
        
        dater = QtCore.QTimer(self.date)
        dater.timeout.connect(self.showDate)
        dater.start(3600000)
        self.showDate()
        
        self.showTemp()
        timer_2 = QtCore.QTimer(self.temp)
        timer_2.timeout.connect(self.showTemp)
        timer_2.start(900000)
        
        k,l,m=0,0,0
        
        eq=[]
        dk,eq = self.ann_web_scrap()
        timer_3 = QtCore.QTimer(self.announcement)
        timer_3.timeout.connect(self.ann_web_scrap)
        timer_3.start(dk*60000)
        
        self.ann_control()
        timer_4 = QtCore.QTimer()
        timer_4.timeout.connect(self.ann_control)
        timer_4.start(20000)
        
    def showTime(self):
        c_time = QtCore.QTime.currentTime()
        text = c_time.toString('hh:mm')
      
        self.time.setText(text)
        
    def showDate(self):
        c_date=QtCore.QDate.currentDate()
        text=c_date.toString("dd MMM yyyy")
            
        self.date.setText(text)
        
    def showTemp(self):
        city=('Eskişehir')
        print()
        query='q='+city;
        w_data=self.weather_data(query);
        self.print_weather(w_data,city)
        
    def weather_data(self,query):
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
        return res.json();
    
    def print_weather(self,result,city):
        trans=Translator()
        w_main=trans.translate(result['weather'][0]['main'], src='en', dest='tr')
        self.temp.setText("%s\nSıcaklık: %s °C \nRüzgar Hızı: %s m/s \nHava Durumu Bilgisi: %s"%(city,result['main']['temp'],result['wind']['speed'], w_main.text))
        
        if result['weather'][0]['main'].lower() =='snow':
            self.snowy.show()
        elif result['weather'][0]['main'].lower() =='clouds':
            self.cloudy.show()
        elif result['weather'][0]['main'].lower() =='clear':
            self.sunny.show()
        elif result['weather'][0]['main'].lower() =='rain':
            self.rainy.show()
        elif result['weather'][0]['main'].lower() =='smoke':
            self.foggy.show()
        elif result['weather'][0]['main'].lower() =='wind':
            self.windy.show()  
       
    def ann_control(self):
        global timer,eq 
        url = 'http://192.168.0.104/esogu/'
        page = requests.get(url).text

        soup = BeautifulSoup(page ,'lxml')
        soup.findAll("h3",class_="entry-content")

        headline = soup.find('h3').get_text()
        if str(headline.lower())=="acil":
            self.ann_web_scrap()
    
    def ann_web_scrap(self):
        global timer,eq
        url = 'http://192.168.0.104/esogu/'
        page = requests.get(url).text

        soup = BeautifulSoup(page ,'lxml')
        soup.findAll("h3",class_="entry-content")
        
        headline = soup.find('h3').get_text()
        self.h=''.join(str(elem) for elem in headline)
        self.headline_effect()

        soup.findAll("div",class_="entry-content")

        p_tags = soup.find_all('p')
        p_tags_text = [tag.get_text().strip() for tag in p_tags]
        x = p_tags_text[1].split()
            
        if str(x[0]).isdigit():
            duration = int(x[0])
            if(str(x[1].lower())=="kırmızı" or str(x[1].lower())=="yeşil" or str(x[1].lower())=="mor" or str(x[1].lower())=="kahverengi" or str(x[1].lower())=="mavi"):
                col = str(x[1].lower())
                self.duyur = x[2:]
            else:
                col="mavi"
                self.duyur=x[1:]
                
        else:
            duration=1
            if(str(x[0].lower())=="kırmızı" or str(x[0].lower())=="yeşil" or str(x[0].lower())=="mor" or str(x[0].lower())=="kahverengi" or str(x[0].lower())=="mavi"):
                col=str(x[0].lower())
                self.duyur = x[1:]
            else:
                col="mavi"
                self.duyur=x
        
        if self.h.lower()=="acil":
            col="kırmızı"
        self.colorSel(col)
        self.ann_effect()
       
        return duration, p_tags_text[1]    
    
    def ann_effect(self):
        self.announcement_2.hide()
        self.showAnn_young()
        self.ann_timer = QtCore.QTimer()
        self.ann_timer.timeout.connect(self.showAnn_young)
        self.ann_timer.start(8000)

        #self.announcement.hide()
        #self.showAnn_old()
        #self.ann_timer_2 = QtCore.QTimer()
        #self.ann_timer_2.timeout.connect(self.showAnn_old)
        #self.ann_timer_2.start(10000)
        
    def showAnn_young(self):
        global m
        k=20
        ann = ' '.join(str(elem) for elem in self.duyur[m:m+k])
        while len(ann)>160:
            k-=1
            ann=' '.join(str(elem) for elem in self.duyur[m:m+k])
        m+=k
        self.announcement.setText(ann)
        if m>=len(self.duyur):
            m=0

    def showAnn_old(self):
        global m
        k=15
        ann=' '.join(str(elem) for elem in self.duyur[m:m+k])
        while len(ann)>120:
            k-=1
            ann=' '.join(str(elem) for elem in self.duyur[m:m+k])
        m+=k
        self.announcement_2.setText(ann)
        if m>=len(self.duyur):
            m=0
    
    def headline_effect(self):
        self.timer_1=QtCore.QTimer()
        self.timer_1.timeout.connect(self.blink)
        self.timer_2 = QtCore.QTimer()
        self.timer_2.timeout.connect(self.sliding)
        if len(self.h)<=50:
            self.timer_2.stop()
            self.headline.setText(self.h.replace('i','İ').upper())
            self.blink()
            
        if len(self.h)>50:
            self.timer_1.stop()
            self.sliding()
            self.timer_2.start(300)
        
    def sliding(self):
        global k,l
        self.headline.setText(self.h[k:].replace('i','İ').upper()+"...     "+self.h[l:].replace('i','İ').upper())
        k+=1
        if k==len(self.h):
            k=0
        if l==len(self.h):
            l=0
    
    def colorSel(self,color):
        self.blue.hide()
        self.red.hide()
        self.brown.hide()
        self.purple.hide()
        self.green.hide()
        
        if(color=='mavi'):
            self.blue.show()
            
        if(color=='kırmızı'):
            self.red.show()
            
        if(color=='mor'):
            self.purple.show()
            
        if(color=='kahverengi'):
            self.brown.show()
            
        if(color=='yeşil'):
            self.green.show()
        
    def blink(self):
        if(self.headline.isHidden()):
            self.headline.show()
            self.timer_1.start(1500)
        else:
            self.headline.hide()
            self.timer_1.start(1000)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ESKİŞEHİR OSMANGAZİ ÜNİVERSİTESİ DUYURU EKRANI"))
        self.headline.setText(_translate("Form", "DUYURU BAŞLIĞI"))
        self.time.setText(_translate("Form", "SAAT"))
        self.date.setText(_translate("Form", "TARİH"))
        self.temp.setText(_translate("Form", "  SICAKLIK"))
        self.announcement.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'FreeSerif\'; font-size:48pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:45pt;\">DUYURU</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

