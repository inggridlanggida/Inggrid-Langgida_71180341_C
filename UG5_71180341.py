class Mobil : 
    _merk = ""
    _tipe = ""
    _kapasitasBBM = None
    _jenisBahanBakar = None

    def __init__(self, merk, tipe):
        self._merk = merk
        self._tipe = tipe
    
    def setMerk(self, merk):
        self._merk = merk
    
    def getMerk(self):
        return self._merk
    
    def setTipe(self, tipe):
        self._tipe = tipe
    
    def getTipe(self):
        return self._tipe
    
    def setKapasitasBBM(self, kapasitasbbm):
        self._kapasitasBBM = kapasitasbbm
    
    def getKapasitasBBM(self):
        return self._kapasitasBBM
    
    def setJenisBahanBakar(self, jenisbahanbakar):
        self._jenisBahanBakar = jenisbahanbakar
    
    def getJenisBahanBakar(self):
        return self._jenisBahanBakar
    
    def printInfo(self):
        print("============ INFO ============")
        print("Merk            : "+self.getMerk())
        print("Tipe            : "+self.getTipe())
        print("Bahan Bakar     : "+str(self.getJenisBahanBakar()))
        print("Kapasitas BBM   : "+str(self.getKapasitasBBM()))
    
    def isiBBM(self, harga):
        if(str(self.getKapasitasBBM) != "None"):
            print("Mengisi "+str(self.getKapasitasBBM())+ " Liter")
            print("Total Harga : Rp"+str(self.getKapasitasBBM()*harga))
        else:
            print("ERROR! Kapasitas BBM atau Jenis Bahan Bakar belum di inputkan")

if __name__ == "__main__":
    mobil1 = Mobil("Toyota", "Avanza")
    mobil1.printInfo()
    mobil2 = Mobil("Nissan", "Grand Livina")
    mobil2.setJenisBahanBakar("Bensin")
    mobil2.setKapasitasBBM(20)
    mobil2.printInfo()
    # mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)