# from mahasiswa import Mahasiswa

# class DaftarMahasiswa:
#     def __init__(self):
#         self.__data = {}

#     def tambah(self, nim: str, nama: str, no_hp: str):
#         if nim in self.__data:
#             print("Gagal: NIM sudah terdaftar!")
#         else:
#             mahasiswa_baru = Mahasiswa(nim, nama, no_hp)
#             self.__data[nim] = mahasiswa_baru
#             print(f"Sukses: Mahasiswa {nama} berhasil ditambahkan.")

#     def edit(self, nim: str, nama_baru: str, no_hp_baru: str):
#         mahasiswa = self.cari(nim)
#         if mahasiswa:
#             mahasiswa.ubah_data(nama_baru, no_hp_baru)
#             print("Sukses: Data mahasiswa berhasil diperbarui.")
#         else:
#             print("Gagal: Mahasiswa tidak ditemukan.")

#     def hapus(self, nim: str):
#         mahasiswa = self.cari(nim)
#         if mahasiswa:
#             if mahasiswa.punya_transaksi_aktif():
#                 print(f"Tidak bisa menghapus {mahasiswa.get_nama()} karena masih punya pinjaman aktif!")
#             else:
#                 del self.__data[nim]
#                 print("Sukses: Data mahasiswa berhasil dihapus.")
#         else:
#             print("Gagal: Mahasiswa tidak ditemukan.")

#     def cari(self, nim: str):
#         return self.__data.get(nim)

#     def tampilkan_semua(self):
#         if not self.__data:
#             print("Data mahasiswa masih kosong.")
#             return
        
#         print("\nDaftar Semua Mahasiswa")
#         for mhs in self.__data.values():
#             mhs.tampilkan_info()
#             print("-" * 30)