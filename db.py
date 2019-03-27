import sys
import mysql.connector
from PyQt5.QtWidgets import QWidget, QListWidget, QApplication, QRadioButton, QVBoxLayout

mydb = mysql.connector.connect(
    host="10.130.129.188",
    user="efe",
    passwd="efe",
    database="school"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT aciklama FROM bolum")
bolumler = mycursor.fetchall()



class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.yerlesim = QVBoxLayout(self)
        self.radyo = []
        for i in range(len(bolumler)):
            self.radyo.append(QRadioButton(self))
            self.radyo[i].setText(bolumler[i][0])
            self.yerlesim.addWidget(self.radyo[i])

        self.liste = QListWidget(self)
        self.yerlesim.addWidget(self.liste)

        self.radyo[0].clicked.connect(lambda: self.ogrenci_cek(1))
        self.radyo[1].clicked.connect(lambda: self.ogrenci_cek(2))
        self.radyo[2].clicked.connect(lambda: self.ogrenci_cek(3))
        self.radyo[3].clicked.connect(lambda: self.ogrenci_cek(4))

    def ogrenci_cek(self,bolum):
        mycursor.execute("SELECT * FROM ogrenci WHERE bid=" + str(bolum) )
        myresult = mycursor.fetchall()
        isimler = []
        for sıradaki in myresult:
            isimler.append(sıradaki[1] + " " + sıradaki[2])
        self.liste.clear()
        self.liste.addItems(isimler)

uygulama = QApplication(sys.argv)
yenipencere = Pencere()
yenipencere.show()
uygulama.exec_()
