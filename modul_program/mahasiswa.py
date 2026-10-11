class Mahasiswa:
    MAKS_TRANSAKSI_AKTIF = 2

    def __init__(self, nim, nama, no_hp):
        self.nim = nim
        self.nama = nama
        self.no_hp = no_hp
        # list: menyimpan objek transaksi yang sedang aktif dipinjam oleh mahasiswa
        self.transaksi_aktif = []

    def get_nama(self):
        return self.nama

    def get_nim(self):
        return self.nim

    def bisa_meminjam(self):
        return len(self.transaksi_aktif) < self.MAKS_TRANSAKSI_AKTIF

    def tambah_transaksi(self, transaksi):
        if self.bisa_meminjam():
            self.transaksi_aktif.append(transaksi)
        else:
            print("Gagal: Mahasiswa ini sudah mencapai batas maksimal peminjaman.")

    def selesai_transaksi(self, transaksi):
        if transaksi in self.transaksi_aktif:
            self.transaksi_aktif.remove(transaksi)
        else:
            print("Transaksi tidak ditemukan dalam daftar transaksi aktif.")

    def punya_transaksi_aktif(self):
        return len(self.transaksi_aktif) > 0

    def ubah_data(self, nama_baru, no_hp_baru):
        self.nama = nama_baru
        self.no_hp = no_hp_baru

    def tampilkan_info(self):
        print(f"NIM: {self.nim}")
        print(f"Nama: {self.nama}")
        print(f"No HP: {self.no_hp}")
        print(f"Transaksi Aktif: {len(self.transaksi_aktif)}")

    def tampilkan_data(self):
        self.tampilkan_info()
