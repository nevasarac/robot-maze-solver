import tkinter as tk
import turtle
import requests

#gui açma yeri
pencere = tk.Tk()
pencere.title('PROJE')
pencere.geometry('850x850+500+100')

#Kalem Oluştur
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#dosya 1 i okuma fonksiyonu
def oku1():
    dosya = requests.get("http://bilgisayar.kocaeli.edu.tr/prolab2/url1.txt")
    liste = str(dosya.text).splitlines()
    liste1 = list()
    for i in range(len(liste)):
        tmp = list()
        for j in range(len(liste[i])):
            tmp.append(int(liste[i][j]))
        liste1.append(tmp.copy())

    setup_maze(liste1)


#dosya 2 yi okuma fonksiyonu
def oku2():
    dosya = requests.get("http://bilgisayar.kocaeli.edu.tr/prolab2/url2.txt")
    liste=str(dosya.text).splitlines()
    liste1=list()
    for i in range(len(liste)):
        tmp=list()
        for j in range(len(liste[i])):
            tmp.append(int(liste[i][j]))
        liste1.append(tmp.copy())

    setup_maze(liste1)

def setup_maze(liste1):
    arayuz = turtle.Screen()
    arayuz.bgcolor("black")
    arayuz.title("GEZGİN ROBOT PROJESİ")
    arayuz.setup(750, 750)

    for y in range(len(liste1)):
        for x in range(len(liste1[y])):
            character = liste1[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # X olup olmadığını kontrol et (duvarı temsil ediyor)
            if character == 1 or 2 or 3:
                pen.goto(screen_x, screen_y)
                pen.stamp()

            if character == 0:
                player.goto(screen_x, screen_y)
                player.stamp()


#Sınıf örnekleri oluştur
pen = Pen()
player=Player()

#buton 1 tanımlama yeri
buton=tk.Button(pencere,text='url1.txt',fg='white',background='black',command=oku1) #URL'i öyle direk set yapılabilir ama free text bir alanda lazım anlatacağım.
buton.place(
    x=50,
    y=30,
    height=30,
    width=60
)

#buton 2 tanımlama yeri
buton=tk.Button(pencere,text='url2.txt',fg='white',background='black',command=oku2)
buton.place(
    x=50,
    y=70,
    height=30,
    width=60
)

#pencere oluşturma yeri
pencere.mainloop()


#TODO: if __main__ =  kullanılmlaı.
