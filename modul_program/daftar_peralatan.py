from peralatan import (
PeralatanKomputasi,
PeralatanJaringan,
PeralatanMultimedia
)

class DaftarPeralatan:
    def __init__(self):
        self.data = {}

def tambah(self, kategori, kode, nama):
    if kode in self.data:
        print("Gagal: Kode alat sudah terdaftar.")
        return False

    kategori = kategori.lower()

    if kategori == "komputasi":
        alat = PeralatanKomputasi(kode, nama)

    elif kategori == "jaringan":
        alat = PeralatanJaringan(kode, nama)

    elif kategori == "multimedia":
        alat = PeralatanMultimedia(kode, nama)

    else:
        print("Kategori tidak tersedia.")
        return False

    self.data[kode] = alat
    return True

def edit(self, kode, nama_baru):
    alat = self.cari_kode(kode)

    if alat is None:
        return False

    if nama_baru == "":
        return False

    alat.nama_alat = nama_baru
    return True

def hapus(self, kode):
    alat = self.cari_kode(kode)

    if alat is None:
        return False

    if alat.status == "dipinjam":
        print("Alat masih dipinjam dan tidak dapat dihapus.")
        return False

    del self.data[kode]
    return True

def cari_kode(self, kode):
    return self.data.get(kode)

def cari_nama(self, nama):
    hasil = []
    nama = nama.lower()

    for alat in self.data.values():
        if nama in alat.nama_alat.lower():
            hasil.append(alat)

    return hasil

def cari_kategori(self, kategori):
    hasil = []
    kategori = kategori.lower()

    for alat in self.data.values():
        if alat.kategori().lower() == kategori:
            hasil.append(alat)

    return hasil

def alat_tersedia(self):
    hasil = []

    for alat in self.data.values():
        if alat.bisa_dipinjam():
            hasil.append(alat)

    return hasil

def alat_dipinjam(self):
    hasil = []

    for alat in self.data.values():
        if alat.status == "dipinjam":
            hasil.append(alat)

    return hasil

def alat_rusak(self):
    hasil = []

    for alat in self.data.values():
        if alat.kondisi == "rusak ringan" or alat.kondisi == "rusak berat":
            hasil.append(alat)

    return hasil

def tampilkan_semua(self):
    if len(self.data) == 0:
        print("Data peralatan masih kosong.")
        return

    print("\n=== DAFTAR PERALATAN ===")

    for alat in self.data.values():
        alat.tampilkan_info()
        print("-" * 30)