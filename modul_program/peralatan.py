from abc import ABC, abstractmethod

class Peralatan(ABC):
   def __init__(self, kode_alat, nama_alat):
        self.kode_alat = kode_alat
        self.nama_alat = nama_alat
        self.kondisi = "baik"
        self.status = "tersedia"

@abstractmethod
def kategori(self):
    pass

def bisa_dipinjam(self):
    return self.status == "tersedia" and self.kondisi == "baik"

def dipinjam(self):
    self.status = "dipinjam"

def terima_pengembalian(self, kondisi):
    if kondisi == "baik":
        self.kondisi = "baik"
        self.status = "tersedia"

    elif kondisi == "rusak ringan":
        self.kondisi = "rusak ringan"
        self.status = "rusak"

    elif kondisi == "rusak berat":
        self.kondisi = "rusak berat"
        self.status = "rusak"

def tampilkan_info(self):
    print(f"Kode     : {self.kode_alat}")
    print(f"Nama     : {self.nama_alat}")
    print(f"Kategori : {self.kategori()}")
    print(f"Kondisi  : {self.kondisi}")
    print(f"Status   : {self.status}")


class PeralatanKomputasi(Peralatan):
    def kategori(self):
        return "komputasi"

class PeralatanJaringan(Peralatan):
    def kategori(self):
        return "jaringan"

class PeralatanMultimedia(Peralatan):
    def kategori(self):
        return "multimedia"
