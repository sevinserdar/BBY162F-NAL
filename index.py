from tkinter import *

class kitaplık:
    def __init__(self,anaSayfa):
        global ısbn, ısbnalanı
        global kitap, kitapadıalanı
        global yazaradı, yazaradıalanı
        global yıl, yayınyılı

        self.anaSayfa = anaSayfa
        anaSayfa.title("Kütüphane Kitap Arama Sayfası")

        anaSayfa.configure(background="brown")
        anaSayfa.geometry("500x600+650+90")

        ısbn = ["1234", "6262", "1221","1235",]
        kitapadıalanı = ["kırmızı karanfil","sevda sözleri","hasretinden prangalar eskittim","acıyı bal eyledik"]
        yazaradıalanı = ["gülten akın", "cemal süreya","ahmed arif","hasan hüseyin korkmazgil"]
        yayınyılı = ["1971", "1984", "1968", "1973"]

        giriş = Label(anaSayfa, text="Kitap Arama Sayfasına Hoşgeldiniz\n Lütfen Bir Kategori Seçiniz ve Arama Yapınız", bg="brown", fg="orange",font=("Times New Roman",14)).grid()


        kitapları_listele = Button(anaSayfa, text="Kitapları Listele", bg="orange", fg="brown",font="bold", command=self.kitaplari_listele)
        kitapları_listele.grid(row="1")

        self.kitap_ekle = Button(anaSayfa, text="Kitap Ekle", bg="orange", fg="brown", font="bold",
                                 command=self.kitap_ekle)
        self.kitap_ekle.grid()

        kitaparama = Label(anaSayfa, text="Lütfen ISBN Giriniz          :", bg="orange", fg="brown", font=("Times New Roman", 12)).grid(row=3,sticky=W )
        ısbnalanı = Entry(width=27)
        ısbnalanı.grid(row=3,sticky=E)
        aramabutonu = Button(anaSayfa,text="ARA", bg="orange", fg="brown", font=("calibri", 10), command=self.giris0).grid(row=3, column=2)


        kitaparama = Label(anaSayfa, text="Lütfen Kitap Adı Giriniz    :", bg="orange", fg="brown",font=("Times New Roman", 12)).grid(row=4, sticky=W)
        kitap = Entry(width=27)
        kitap.grid(row=4,sticky=E)
        aramabutonu = Button(anaSayfa, text="ARA", bg="orange", fg="brown", font=("calibri", 10), command=self.giris1).grid(row=4, column=2)


        kitaparama= Label(anaSayfa, text="Lütfen Yazar Adı Giriniz    :", bg="orange", fg="brown",font=("Times New Roman", 12)).grid(row=5, sticky=W)
        yazaradı = Entry(width=27)
        yazaradı.grid(row=5, sticky=E)
        aramabutonu = Button(anaSayfa, text="ARA", bg="orange", fg="brown", font=("calibri", 10),command=self.giris2).grid(row=5,column=2)

        kitaparama = Label(anaSayfa, text="Lütfen Yayın Yılını Giriniz  :", bg="orange", fg="brown",font=("Times New Roman", 12)).grid(row=6, sticky=W)
        yıl = Entry(width=27)
        yıl.grid(row=6, sticky=E)
        aramabutonu = Button(anaSayfa, text="ARA", bg="orange", fg="brown", font=("calibri", 10),command=self.giris3).grid(row=6, column=2)

        self.cikis = Button(anaSayfa, text="Kapat", command=exit, fg="orange", bg="brown",)
        self.cikis.grid(row=7, column=2)

##############################################################################

    def giris3(self):
        yılı = yıl.get()

        if yılı == yayınyılı[0]:
            ilk = Label(root,text="KİTAP ADI: KIRMIZI KARANFİL \n YAZAR ADI: GÜLTEN AKIN \n TÜRÜ: ŞİİR \n YAYIN YILI: 1971 \n ISBN: 1234 \n RAF NUMARASI:S94", bg="orange",fg="brown" , font=("Times New Roman",12)).grid()
        elif yılı == yayınyılı[1]:
            ikinci = Label(root,text="KİTAP ADI: SEVDA SÖZLERİ \n YAZAR ADI: CEMAL SÜREYA \n TÜRÜ: ŞİİR \n YAYIN YILI: 1984 \n ISBN: 6262 \n RAF NUMARASI:S62",bg="orange", fg="brown", font=("Times New Roman", 12)).grid()

        elif yılı == yayınyılı[2]:
            üçüncü = Label(root,text="KİTAP ADI: HASRETİNDEN PRANGALAR ESKİTTİM \n YAZAR ADI: ADMED ARİF \n TÜRÜ:ŞİİR \n YAYIN YILI: 1968 \n ISBN: 1221 \n RAF NUMARASI:S21",bg="orange", fg="brown", font=("Times New Roman", 12)).grid()

        elif yılı == yayınyılı[3]:
            dördüncü = Label(root,text="KİTAP ADI: ACIYI BAL EYLEDİK \n YAZAR ADI: HASAN HÜSEYİN KORKMAZGİL \n TÜRÜ: ŞİİR \n YAYIN YILI: 1973 \n ISBN: 1235 \n RAF NUMARASI:S12",bg="orange", fg="brown", font=("Times New Roman", 12)).grid()

        else:
            son = Label(root,text="Aradığınız kitap kütüphanemizde mevcut değildir." , bg="orange",fg="brown", font=("Times New Roman", 12)).grid()






    def giris2(self):
        yaz = yazaradı.get()

        if yaz == yazaradıalanı[0]:
            ilk = Label(root,text="KİTAP ADI: KIRMIZI KARANFİL \n YAZAR ADI: GÜLTEN AKIN \n TÜRÜ: ŞİİR \n YAYIN YILI: 1971 \n ISBN: 1234 \n RAF NUMARASI:S94", bg="orange",fg="brown" , font=("Times New Roman",12)).grid()

        elif yaz ==yazaradıalanı[1]:
            ikinci = Label(root,text="KİTAP ADI: SEVDA SÖZLERİ \n YAZAR ADI: CEMAL SÜREYA \n TÜRÜ: ŞİİR \n YAYIN YILI: 1984 \n ISBN: 6262 \n RAF NUMARASI:S62", bg="orange",fg="brown", font=("Times New Roman", 12)).grid()

        elif yaz == yazaradıalanı[2]:
            üçüncü = Label(root,text="KİTAP ADI: HASRETİNDEN PRANGALAR ESKİTTİM \n YAZAR ADI: ADMED ARİF \n TÜRÜ:ŞİİR \n YAYIN YILI: 1968 \n ISBN: 1221 \n RAF NUMARASI:S21", bg="orange",fg="brown", font=("Times New Roman", 12)).grid()

        elif yaz == yazaradıalanı[3]:
            dördüncü = Label(root,text="KİTAP ADI: ACIYI BAL EYLEDİK \n YAZAR ADI: HASAN HÜSEYİN KORKMAZGİL \n TÜRÜ: ŞİİR \n YAYIN YILI: 1973 \n ISBN: 1235 \n RAF NUMARASI:S12", bg="orange",fg="brown", font=("Times New Roman", 12)).grid()

        else :
            son = Label(root,text="Aradığınız kitap kütüphanemizde mevcut değildir." , bg="orange",fg="brown", font=("Times New Roman", 12)).grid()




    def giris1(self):
        adı = kitap.get()

        if adı == kitapadıalanı[0]:

            ilk = Label(root,text="KİTAP ADI: KIRMIZI KARANFİL \n YAZAR ADI: GÜLTEN AKIN \n TÜRÜ: ŞİİR \n YAYIN YILI: 1971 \n ISBN: 1234 \n RAF NUMARASI:S94", bg="orange",fg="brown", font=("Times New Roman",12)).grid()

        elif adı == kitapadıalanı[1]:
            ikinci = Label(root,text="KİTAP ADI: SEVDA SÖZLERİ \n YAZAR ADI: CEMAL SÜREYA \n TÜRÜ: ŞİİR \n YAYIN YILI: 1984 \n ISBN: 6262 \n RAF NUMARASI:S62", bg="orange",fg="brown", font=("Times New Roman", 12)).grid()

        elif adı == kitapadıalanı[2]:
            üçüncü = Label(root, text="KİTAP ADI: HASRETİNDEN PRANGALAR ESKİTTİM \n YAZAR ADI: ADMED ARİF \n TÜRÜ:ŞİİR \n YAYIN YILI: 1968 \n ISBN: 1221 \n RAF NUMARASI:S21", bg="orange",fg="brown", font=("Times New Roman", 12)).grid()

        elif adı == kitapadıalanı[3]:
            dördüncü = Label(root,text="KİTAP ADI: ACIYI BAL EYLEDİK \n YAZAR ADI: HASAN HÜSEYİN KORKMAZGİL \n TÜRÜ: ŞİİR \n YAYIN YILI: 1973 \n ISBN: 1235 \n RAF NUMARASI:S12", bg="orange",fg="brown", font=("Times New Roman", 12)).grid()

        else:
            son = Label(root, text="Aradığınız kitap kütüphanemizde mevcut değildir." , bg="orange",fg="brown", font=("Times New Roman", 12)).grid()



    def giris0(self):
        ısbnn = ısbnalanı.get()

        if ısbnn == ısbn[0]:

            ilk = Label(root,text="KİTAP ADI: KIRMIZI KARANFİL \n YAZAR ADI: GÜLTEN AKIN \n TÜRÜ: ŞİİR \n YAYIN YILI: 1971 \n ISBN: 1234 \n RAF NUMARASI:S94",  bg="orange",fg="brown", font=("Times New Roman",12)).grid()

        elif ısbnn == ısbn[1]:
            ikinci = Label(root,text="KİTAP ADI: SEVDA SÖZLERİ \n YAZAR ADI: CEMAL SÜREYA \n TÜRÜ: ŞİİR \n YAYIN YILI: 1984 \n ISBN: 6262 \n RAF NUMARASI:S62", bg="orange",fg="brown", font=("Times New Roman", 12)).grid()

        elif ısbnn == ısbn[2]:
            üçüncü = Label(root,text="KİTAP ADI: HASRETİNDEN PRANGALAR ESKİTTİM \n YAZAR ADI: ADMED ARİF \n TÜRÜ: ŞİİR \n YAYIN YILI: 1968 \n ISBN: 1221 \n RAF NUMARASI:S21", bg="orange",fg="brown", font=("Times New Roman", 12)).grid()

        elif ısbnn == ısbn[3]:
            dördüncü = Label(root,text="KİTAP ADI: ACIYI BAL EYLEDİK \n YAZAR ADI: HASAN HÜSEYİN KORKMAZGİL \n TÜRÜ: ŞİİR \n YAYIN YILI: 1973 \n ISBN: 1235 \n RAF NUMARASI:S12", bg="orange",fg="brown", font=("Times New Roman", 12)).grid()

        else:
            son = Label(root,text="Aradığınız kitap kütüphanemizde mevcut değildir." , bg="orange",fg="brown", font=("Times New Roman", 12)).grid()


    def kitap_ekle(self):
        global kitap_adi, yazar_adi, tur, isbn, raf_numarası, yy, pencere1
        pencere1 = Tk()

        baslik1 = pencere1.title("Kitap Kayıt Penceresi")
        pencere1.configure(background="brown")

        kitap_adi = Entry(pencere1)
        kitap_adi.grid(row=3)
        yazar_adi = Entry(pencere1)
        yazar_adi.grid(row=4)
        isbn = Entry(pencere1)
        isbn.grid(row=6)
        raf_numarası = Entry(pencere1)
        raf_numarası.grid(row=7)
        yy = Entry(pencere1)
        yy.grid(row=8)
        self.kaydet = Button(pencere1, text="Kaydet", command=self.kitap_kaydet, fg="orange", bg="brown")
        self.kaydet.grid(row=9)

        self.cıkıs = Button(pencere1, text="Kapat", command=pencere1.destroy, fg="orange", bg="brown")
        self.cıkıs.grid(column=3, row=9)

        Label(pencere1, bg="orange", fg="brown", text="Kitap Adı:").grid(column=2, row=3)
        Label(pencere1, bg="orange", fg="brown", text="Yazar Adı:").grid(column=2, row=4)
        Label(pencere1, bg="orange", fg="brown", text="ISBN:").grid(column=2, row=6)
        Label(pencere1, bg="orange", fg="brown", text="Raf Numarası:").grid(column=2, row=7)
        Label(pencere1, bg="orange", fg="brown", text="Yayın Yılı:").grid(column=2, row=8)

    def kitap_kaydet(self):
        kayit_sis = str((
                                    kitap_adi.get() + "\n" + yazar_adi.get() + "\n" + isbn.get() + "\n" + raf_numarası.get() + "\n" + yy.get()) + "\n")
        dosya = open("katalog.txt", "a")
        for i in kayit_sis:
            dosya.write(i)
        dosya.close()
        ('Mesaj', 'Kitap Başarıyla Eklendi')
        command = pencere1.destroy()

    def kitaplari_listele(self):
            pencerex= Tk()
            baslik2 = pencerex.title("Kayıtlı Kitaplar")
            pencerex.configure(background="brown")
            file = open("katalog.txt")
            data = file.read()
            file.close()

            kitap_liste = Label(pencerex, text=data,fg="orange", bg="brown")
            kitap_liste.pack()

root = Tk()
yeniPencere = kitaplık(root)
root.mainloop()

