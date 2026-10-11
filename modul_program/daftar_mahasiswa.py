from .mahasiswa import Mahasiswa

class DaftarMahasiswa:
    def __init__(self):
        # dictionary: menyimpan data mahasiswa dengan key = nim dan value = objek Mahasiswa
        self.__data = {}

    def tambah(self, nim, nama, no_hp):
        if nim in self.__data:
            print("Gagal: NIM sudah terdaftar!")
            return False
        else:
            mahasiswa_baru = Mahasiswa(nim, nama, no_hp)
            self.__data[nim] = mahasiswa_baru
            print(f"Sukses: Mahasiswa {nama} berhasil ditambahkan.")
            return True

    def edit(self, nim, nama_baru, no_hp_baru):
        mahasiswa = self.cari(nim)
        if mahasiswa:
            mahasiswa.ubah_data(nama_baru, no_hp_baru)
            print("Sukses: Data mahasiswa berhasil diperbarui.")
            return True
        else:
            print("Gagal: Mahasiswa tidak ditemukan.")
            return False

    def hapus(self, nim):
        mahasiswa = self.cari(nim)
        if mahasiswa:
            if mahasiswa.punya_transaksi_aktif():
                print(f"Tidak bisa menghapus {mahasiswa.get_nama()} karena masih punya pinjaman aktif!")
                return False
            else:
                del self.__data[nim]
                print("Sukses: Data mahasiswa berhasil dihapus.")
                return True
        else:
            print("Gagal: Mahasiswa tidak ditemukan.")
            return False

    def cari(self, nim):
        return self.__data.get(nim)

    def tampilkan_semua(self):
        if not self.__data:
            print("Data mahasiswa masih kosong.")
            return
        
        print("\nDaftar Semua Mahasiswa")
        for mhs in self.__data.values():
            mhs.tampilkan_info()
            print("-" * 30)

