from PyQt5.QtWidgets import *
import os
from PyQt5.QtGui import *
from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt

def choose():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, ext):
    result = list()
    for i in files:
        for b in ext:
            if i.endswith(b) == True:
                result.append(i)
    return result

def showlist():
    choose()
    ext = ["png", "jpg"]
    files = os.listdir(workdir)
    files = filter(files, ext)
    chtoto.clear()
    chtoto.addItems(files)
class Method():
    def imageopener(self, filename):
        self.filename = filename
        self.pytb = os.path.join(workdir, filename)
        self.image = Image.open(self.pytb)
        self.copyfile = self.image.copy()
    def showimage(self, pas):
        imagener = QPixmap(pas)
        x, y = png.width(), png.height()
        imagener = imagener.scaled(x, y, Qt.KeepAspectRatio)
        png.setPixmap(imagener)
        png.setVisible(True)
    def saveimage(self):
        self.nur = "kez"
        pytnik = os.path.join(workdir, self.nur)
        if not(os.path.exists(pytnik) or os.path.isdir(pytnik)):
            os.mkdir(pytnik)
        self.saveimag = os.path.join(pytnik, self.filename)
        self.image.save(self.saveimag)
    def dw(self):
        self.image = self.image.convert("L")
        self.saveimage()
        self.showimage(self.saveimag)
    def leftimage(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveimage()
        self.showimage(self.saveimag)
    def rightimage(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveimage()
        self.showimage(self.saveimag)
    def zerkalno(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveimage()
        self.showimage(self.saveimag)
    def rezko(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveimage()
        self.showimage(self.saveimag)
    def sbros(self):
        self.image = self.copyfile.copy()
        self.showimage(self.pytb)
    def savenew(self):
        path = os.path.join(workdir,  "flugernew" + self.filename)
        self.image.save(path)
def click():
    if chtoto.currentRow() >= 0:
        filename = chtoto.currentItem().text()
        pinger.imageopener(filename)
        pinger.showimage(pinger.pytb)
    
pinger = Method()
app = QApplication([])
main = QWidget()
left = QPushButton("Лево")
prav = QPushButton("Право")
zerkalo = QPushButton("Зеркало")
rezkost = QPushButton("Резкость")
chb = QPushButton("Ч/Б")
save = QPushButton("Сохранить")
reset = QPushButton("Сбросить фильтры")
filename = QPushButton("Папка")
chtoto = QListWidget()
png = QLabel("Картинка")
qv1 = QVBoxLayout()
qv2 = QVBoxLayout()
qh1 = QHBoxLayout()
qh2 = QHBoxLayout()
qv1.addWidget(filename)
qv1.addWidget(chtoto)
qv2.addWidget(png)
qh1.addWidget(left)
qh1.addWidget(prav)
qh1.addWidget(zerkalo)
qh1.addWidget(rezkost)
qh1.addWidget(chb)
qh1.addWidget(save)
qh1.addWidget(reset)
qv2.addLayout(qh1)
qh2.addLayout(qv1, 30)
qh2.addLayout(qv2, 70)






main.setLayout(qh2)
chb.clicked.connect(pinger.dw)
reset.clicked.connect(pinger.sbros)
rezkost.clicked.connect(pinger.rezko)
left.clicked.connect(pinger.leftimage)
prav.clicked.connect(pinger.rightimage)
filename.clicked.connect(showlist)
save.clicked.connect(pinger.savenew)
chtoto.currentRowChanged.connect(click)
zerkalo.clicked.connect(pinger.zerkalno)
main.show()
app.exec()

