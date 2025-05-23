#добавление библиотек
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QFileDialog)
import os
from PIL import Image, ImageOps, ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

#классы
class Imageprocessor():
    def __init__(self):
        self.filename = None
        self.Image = None
        self.dir = None
        self.save_dir = 'Modified/'

    def loadImage(self, filename):
        self.filename = filename
        self.dir = workdir
        image_path = os.path.join(self.dir , self.filename)
        self.image = Image.open(image_path) 
    
    def showimage(self, path):
        pixmapimage = QPixmap(path) 
        label_width, label_height = fotografi.width(), fotografi.height()
        scaled_pixmap = pixmapimage.scaled(label_width,
                                           label_height,
                                           Qt.KeepAspectRatio) 
        fotografi.setPixmap(scaled_pixmap) 
        fotografi.setVisible(True)
    
    def saveImage(self):#сохранение
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_bw(self):#черно белая
        self.image = ImageOps.grayscale(self.image)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showimage(image_path)

    def do_left(self):#лево
        self.image = self.image.rotate(90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showimage(image_path)

    def do_right(self):#право
        self.image = self.image.rotate(-90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showimage(image_path)

    def do_mirror(self):#зеркало
        self.image = ImageOps.mirror(self.image)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showimage(image_path)

    def do_sharpen(self):#резкость
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showimage(image_path)


workoimage = Imageprocessor()

#выбор папки
workdir = ''

#функции
def chooseWorkdir(): #работа с папкой любой
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):#список всех файлов и  подходящих расширений
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
                break
    return result

def showfilenameslist(): #список всех картинок
    chooseWorkdir()
    extensions = ['.png','.jpg','.jpeg','.gif','.bmp',]
    files = os.listdir(workdir)
    files = filter(files, extensions)
    spisok_okno.clear()
    spisok_okno.addItems(files)

def showChosenImage():
    if spisok_okno.currentRow() >= 0:
        filename = spisok_okno.currentItem().text()
        workoimage.loadImage(filename)
        image_path = os.path.join(workdir, filename)
        workoimage.showimage(image_path)



#создание окна приложения
app = QApplication([])
window = QWidget()
window.resize(700,500)
window.setWindowTitle('Фотообработка')

#создание кнопок
rbtn_folder = QPushButton('Папка')
rbtn_left = QPushButton('Лево')
rbtn_right = QPushButton('Право')
rbtn_mirror = QPushButton('Зеркало')
rbtn_sharpen = QPushButton('Резкость')
rbtn_bw = QPushButton('Ч/Б')

#создание окон
spisok_okno = QListWidget()

#картинка/фотография
fotografi = QLabel('здесь могла бы быть ваша реклама')

#создание линии окна
h_line = QHBoxLayout() #глав
h_line1 = QHBoxLayout() # второстепенные
v_line2 = QVBoxLayout()
v_line3 = QVBoxLayout()

#прикрепеление линий 
v_line2.addWidget(rbtn_folder)
v_line2.addWidget(spisok_okno)
h_line1.addWidget(rbtn_left)
h_line1.addWidget(rbtn_right)
h_line1.addWidget(rbtn_mirror)
h_line1.addWidget(rbtn_sharpen)
h_line1.addWidget(rbtn_bw)
v_line3.addWidget(fotografi)
v_line3.addLayout(h_line1)
h_line.addLayout(v_line2)
h_line.addLayout(v_line3)

#конец
rbtn_folder.clicked.connect(showfilenameslist)
rbtn_bw.clicked.connect(workoimage.do_bw)
rbtn_left.clicked.connect(workoimage.do_left)
rbtn_right.clicked.connect(workoimage.do_right)
rbtn_mirror.clicked.connect(workoimage.do_mirror)
rbtn_sharpen.clicked.connect(workoimage.do_sharpen)
spisok_okno.currentRowChanged.connect(showChosenImage)
window.setLayout(h_line)
window.show()
app.exec_()
