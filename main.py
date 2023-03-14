import tkinter as tk
import requests
#dosya 1 i okuma fonksiyonu
def oku1():
    dosya = requests.get("http://bilgisayar.kocaeli.edu.tr/prolab2/url1.txt") #TODO: buralar generic bir fonksiyona dönüşmeli. Path'i parametre ile almalı ve sadece isminde geçen işi yapmalı. Gidip bir yere bir şey set etmemeli. 
    labirent["text"] = dosya.text

#dosya 2 yi okuma fonksiyonu
def oku2():
    dosya = requests.get("http://bilgisayar.kocaeli.edu.tr/prolab2/url2.txt")
    labirent["text"]=dosya.text

    
#TODO: tüm tkinter ayarlamaları bir fonksiyona atılmalı. Ortalık çok karışık. 
    
#gui açma yeri
pencere = tk.Tk()
pencere.title('proje')
pencere.geometry('750x750+550+150')

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

#text dosyasından çektiklerimizi yazma yeri
labirent=tk.Label(text="")
labirent.pack()

pencere.mainloop()


#TODO: if __main__ =  kullanılmlaı. 


