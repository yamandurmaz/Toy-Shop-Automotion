import time

print("""

oyuncakçı
1)araba/15$
2)bebek/20$
3)lego/30$
4)top/5$
5)kaykay/100$
Bakiye = 200$

@author Yaman Durmaz

""")
bakiye = 200
araba = 15
bebek = 20
lego = 30
top = 5
kaykay = 100


while True:
   oyuncak = input("hangi oyuncağı istersiniz")


   if bakiye <= 0:
      print("paranız bitmiştir")
   elif oyuncak == "1":
      print("satın alınıyor....")
      time.sleep(2)
      bakiye -= araba
      print("bakiye",bakiye )
   elif oyuncak == "2":
      print("satın alınıyor....")
      time.sleep(2)
      bakiye -= bebek
      print("bakiye", bakiye)
   elif oyuncak == "3":
      print("satın alınıyor....")
      time.sleep(2)
      bakiye -= lego
      print("bakiye", bakiye)
   elif oyuncak == "4":
      print("satın alınıyor....")
      time.sleep(2)
      bakiye -= top
      print("bakiye",bakiye)
   elif oyuncak == "5":
      print("satın alınıyor...")
      time.sleep(2)
      bakiye -= kaykay
      print("bakiye",bakiye)

   else:
      print("Hatalı Giriş Yeniden Deneyin")


   if bakiye == 0:
      print("""
      Merhaba, sizin için bir anket düzenledim, katılmak ister misiniz? Anket Sonunda Puan Kazanacaksınız.
      
      1) Evet, Katılmak İstiyorum.
      2) Hayır, Katılmak istemiyorum.
      3) Puanımı Göster
      4) çıkmak isterseniz q basın.
      
      """)

      islem = input("Lütfen Seçiniz: ")
      puan = 0


      if islem == "q":

         break


      elif islem == "3":
         print("Puanınız", puan)


      elif islem == "1":
         input("alışveriş keyiflimiydi ? :")
         puan += 10
         input("Bizi sevdiniz mi ? : ")
         puan += 10
         print("Puanınız", puan)


      elif islem == "2":
         print("Teşekkürler...")
         break







