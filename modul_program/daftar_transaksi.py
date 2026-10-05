from transaksi import Transaksi


class DaftarTransaksi:
    def __init__(self):
        self.__data = {}
        self.__nomor_terakhir = 0

    def buat_transaksi(self, mahasiswa, daftar_alat):
        if not mahasiswa.bisa_meminjam():
            print("Gagal: Mahasiswa sudah mencapai batas maksimal transaksi aktif.")
            return None

        self.__nomor_terakhir += 1
        id_transaksi = f"TR{self.__nomor_terakhir:03d}"

        transaksi_baru = Transaksi(id_transaksi, mahasiswa, daftar_alat)

        self.__data[id_transaksi] = transaksi_baru
        mahasiswa.tambah_transaksi(transaksi_baru)

        print(f"Sukses: Transaksi {id_transaksi} berhasil dibuat.")

        return transaksi_baru

    def proses_pengembalian(self, id_transaksi, kode_alat, kondisi):
        transaksi = self.__data.get(id_transaksi)

        if transaksi is None:
            print("Gagal: Transaksi tidak ditemukan.")
            return False

        if not transaksi.masih_aktif():
            print("Gagal: Transaksi sudah selesai.")
            return False

        berhasil = transaksi.catat_pengembalian(kode_alat, kondisi)

        if not berhasil:
            print("Gagal: Alat tidak ditemukan dalam transaksi.")
            return False

        if not transaksi.alat_belum_kembali():
            transaksi.status = "Selesai"
            transaksi.mahasiswa.selesai_transaksi(transaksi)

        print("Sukses: Pengembalian alat berhasil diproses.")

        return True

    def cari_by_mahasiswa(self, nim):
        hasil = []

        for transaksi in self.__data.values():
            if transaksi.mahasiswa.get_nim() == nim:
                hasil.append(transaksi)

        return hasil

    def riwayat_mahasiswa(self, nim):
        hasil = self.cari_by_mahasiswa(nim)

        if not hasil:
            print("Riwayat transaksi mahasiswa tidak ditemukan.")
            return

        print(f"\nRiwayat Transaksi Mahasiswa: {nim}")

        for transaksi in hasil:
            transaksi.tampilkan_nota()

    def alat_ada_di_transaksi_aktif(self, alat):
        for transaksi in self.__data.values():
            if transaksi.masih_aktif():
                if alat in transaksi.daftar_alat:
                    return True

        return False

    def tampilkan_semua(self):
        if not self.__data:
            print("Data transaksi masih kosong.")
            return

        print("\nDaftar Semua Transaksi")

        for transaksi in self.__data.values():
            transaksi.tampilkan_nota()