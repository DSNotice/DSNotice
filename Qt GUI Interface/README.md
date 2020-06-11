# Qt GUI Interface
## Installations
* Download and Install [Anaconda](https://www.anaconda.com/products/individual#windows)
* Open Anaconda Prompt enter following commands and install PyQt5
```bash
(base) C:\Users\Ceren> cd C:\Users\Ceren\path_where_the_file_is_located
(base) C:\Users\Ceren> pyqt5 -x ui_file_name.ui -o python_file_name.py
```
### XML Çıktısını Python Komut Dosyasına Dönüştürme
The designed screen should be saved in a folder. The location where the interface designed from the command prompt should be opened. Then, XML files obtained from Qt Designer with PyQt5 should be converted to Python code.
```bash
C:\Users\Ceren> cd C:\Users\Ceren\path_where_the_file_is_located
C:\Users\Ceren> pyqt5 -x ui_file_name.ui -o python_file_name.py
```
## Instructions
* Install Anaconda and PyQt5 with Qt Designer
* Clone this repo.
* Open python duyuru.py
* Change website URL where you send announcements to screen
* Run python duyuru.py

## Description
Qt, a graphical user interface development toolkit supporting multiple platforms, was used with the Qt Designer program for the created interface. With the widget development tools of the Qt Widgets module, a graphical interface design, including time, date, weather, announcement and their headlines has been realized. 

<p align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/59059790/84431684-5c988e00-ac34-11ea-9ee7-b4d6260bd623.png">
  <br><br>
</p>

Time and date information is displayed instantly via the PyQt5 module. Weather, announcements and their headlines are obtained by Python data scraping method. In the web scraping process, requests are made to the websites with the Request module, and the Hyper Text Markup Language (HTML) code of the sites is divided with the Beautiful Soup module and the code part containing the desired data is used.

In order to increase the attention of the screen, different effects such as sliding and blinking have been added to the announcements and their headlines. Announcements are divided into categories for the announcement board that is planned to be used in school and different background colors are applied according to the categories. The background color and the duration of the announcements on the screen can be managed by the people authorized to send the announcement through the website. If the announcements with an emergency title are sent before the duration of the announcements whose stay duration on the screen has not expired, the timer is stopped and the emergency announcement is displayed on the screen. A notification sound has been identified that alerts the viewer when the new announcement arrives.

