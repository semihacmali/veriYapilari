######## bunun tamamliyacaksiniz 
######## randevuya kac gun kaldigini hesaplayan metodu ekleyin
######## ornek tarih :  22/03/2024
######## guncel tarih : 26/04/2022
######## Çıktı        : 1 yil 11 ay .... gun        

######## ... gun ... ay .... yil kaldi

class HastaTakip:
    hastaTc = 0
    hastaAd = ""
    hastaSoyad = ""
    hastaAdres = ""
    hastaRandevuTarih = ""
    hastaRandevuBolum = ""
    
    def __init__(self):
        self.hastaTc = 0
        self.hastaAd = ""
        self.hastaSoyad = ""
        self.hastaAdres = ""
        self.hastaRandevuTarih = ""
        self.hastaRandevuBolum = ""
     
    def __init__(self, hastaTc, hastaAd, hastaSoyad, hastaRandevuTarih, hastaRandevuBolum):
      self.hastaTc, self.hastaAd, self.hastaSoyad = hastaTc, hastaAd, hastaSoyad
      self.hastaRandevuBolum, self.hastaRandevuTarih = hastaRandevuBolum, hastaRandevuTarih

  
    def __init__(self, hastaTc, hastaAd, hastaSoyad, hastaAdres, hastaRandevuTarih, hastaRandevuBolum):
        self.hastaTc, self.hastaAd, self.hastaSoyad = hastaTc, hastaAd, hastaSoyad
        self.hastaAdres, self.hastaRandevuTarih, self.hastaRandevuBolum = hastaAdres, hastaRandevuTarih, hastaRandevuBolum
    
    def sethastaTc(self, hastaTc):
        self.hastaTc = hastaTc
    
    def sethastaAd(self, hastaAd):
        self.hastaAd = hastaAd
    
    def sethastaSoyad(self, hastaSoyad):
        self.hastaSoyad = hastaSoyad

    def gethastaTc(self):
        return self.hastaTc
    
    def gethastaAd(self):
        return self.hastaAd
    
    def gethastaSoyad(self):
        return self.hastaSoyad
    
#### setDegiskenadi(self, degiskenadi)

hasta1 = HastaTakip(121334, "Sueda", "ÖTÜNÇ","Bağlum","30/04/2022", "Kardiyoloji")


hasta1.hastaAd

hasta1.hastaAd = "Kaan" # tavsiye edilen deger güncelleme yontemi değil
hasta1.hastaAd

hasta1.sethastaAd("Oğuz")
hasta1.hastaAd

hasta1.gethastaSoyad()
