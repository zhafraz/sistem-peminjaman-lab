from daftar_mahasiswa import DaftarMahasiswa
from daftar_peralatan import DaftarPeralatan
from daftar_transaksi import DaftarTransaksi


class SistemLab:
    def __init__(self):
        self.daftar_mahasiswa = DaftarMahasiswa()
        self.daftar_peralatan = DaftarPeralatan()
        self.daftar_transaksi = DaftarTransaksi()
        self.log_aktivitas = []

    # =========================
    # METHOD 
    # =========================

    def jalankan(self):
        """Menjalankan program utama."""
        while True:
            self.tampilkan_menu()
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.menu_mahasiswa()

            elif pilihan == "2":
                self.menu_peralatan()

            elif pilihan == "3":
                self.menu_peminjaman()

            elif pilihan == "4":
                self.menu_pengembalian()

            elif pilihan == "5":
                self.daftar_transaksi.tampilkan_semua()

            elif pilihan == "6":
                self.tampilkan_log()

            elif pilihan == "0":
                print("\nProgram selesai. Terima kasih!")
                break

            else:
                print("Pilihan tidak valid.")

    def tampilkan_menu(self):
        print("\n" + "=" * 50)
        print("          SISTEM PEMINJAMAN LAB")
        print("=" * 50)
        print("1. Kelola Mahasiswa")
        print("2. Kelola Peralatan")
        print("3. Peminjaman Peralatan")
        print("4. Pengembalian Peralatan")
        print("5. Daftar Transaksi")
        print("6. Log Aktivitas")
        print("0. Keluar")
        print("=" * 50)

    def catat_log(self, pesan: str):
        self.log_aktivitas.append(pesan)

    def tampilkan_log(self):
        print("\n=== LOG AKTIVITAS ===")

        if not self.log_aktivitas:
            print("Belum ada aktivitas.")
            return

        for i, log in enumerate(self.log_aktivitas, start=1):
            print(f"{i}. {log}")

    # =========================
    # UI MAHASISWA
    # =========================

    def menu_mahasiswa(self):
        while True:
            print("\n=== MENU MAHASISWA ===")
            print("1. Tambah Mahasiswa")
            print("2. Edit Mahasiswa")
            print("3. Hapus Mahasiswa")
            print("4. Cari Mahasiswa")
            print("5. Tampilkan Semua")
            print("0. Kembali")

            pilihan = input("Pilih: ")

            if pilihan == "1":
                nim = input("NIM    : ")
                nama = input("Nama   : ")
                no_hp = input("No. HP : ")

                if self.daftar_mahasiswa.tambah(nim, nama, no_hp):
                    self.catat_log(f"Menambah mahasiswa {nim}")
                    print("Mahasiswa berhasil ditambahkan.")
                else:
                    print("Gagal menambahkan mahasiswa.")

            elif pilihan == "2":
                nim = input("NIM       : ")
                nama = input("Nama baru : ")
                no_hp = input("No. HP    : ")

                if self.daftar_mahasiswa.edit(nim, nama, no_hp):
                    self.catat_log(f"Mengubah data mahasiswa {nim}")
                    print("Data mahasiswa berhasil diubah.")
                else:
                    print("Mahasiswa tidak ditemukan.")

            elif pilihan == "3":
                nim = input("NIM yang akan dihapus: ")

                if self.daftar_mahasiswa.hapus(nim):
                    self.catat_log(f"Menghapus mahasiswa {nim}")
                    print("Mahasiswa berhasil dihapus.")
                else:
                    print("Gagal menghapus mahasiswa.")

            elif pilihan == "4":
                nim = input("NIM: ")
                mahasiswa = self.daftar_mahasiswa.cari(nim)

                if mahasiswa:
                    mahasiswa.tampilkan_info()
                else:
                    print("Mahasiswa tidak ditemukan.")

            elif pilihan == "5":
                self.daftar_mahasiswa.tampilkan_semua()

            elif pilihan == "0":
                break

            else:
                print("Pilihan tidak valid.")

    # =========================
    # UI PERALATAN
    # =========================

    def menu_peralatan(self):
        while True:
            print("\n=== MENU PERALATAN ===")
            print("1. Tambah Peralatan")
            print("2. Edit Peralatan")
            print("3. Hapus Peralatan")
            print("4. Cari Berdasarkan Kode")
            print("5. Cari Berdasarkan Nama")
            print("6. Cari Berdasarkan Kategori")
            print("7. Lihat Alat Tersedia")
            print("8. Lihat Alat Dipinjam")
            print("9. Lihat Alat Rusak")
            print("10. Tampilkan Semua")
            print("0. Kembali")

            pilihan = input("Pilih: ")

            if pilihan == "1":
                print("\nKategori: komputasi / jaringan / multimedia")

                kategori = input("Kategori : ")
                kode = input("Kode     : ")
                nama = input("Nama     : ")

                if self.daftar_peralatan.tambah(kategori, kode, nama):
                    self.catat_log(f"Menambah peralatan {kode}")
                    print("Peralatan berhasil ditambahkan.")
                else:
                    print("Gagal menambahkan peralatan.")

            elif pilihan == "2":
                kode = input("Kode alat : ")
                nama = input("Nama baru : ")

                if self.daftar_peralatan.edit(kode, nama):
                    self.catat_log(f"Mengubah peralatan {kode}")
                    print("Peralatan berhasil diubah.")
                else:
                    print("Peralatan tidak ditemukan.")

            elif pilihan == "3":
                kode = input("Kode alat yang akan dihapus: ")

                if self.daftar_peralatan.hapus(kode):
                    self.catat_log(f"Menghapus peralatan {kode}")
                    print("Peralatan berhasil dihapus.")
                else:
                    print("Gagal menghapus peralatan.")

            elif pilihan == "4":
                kode = input("Kode alat: ")
                alat = self.daftar_peralatan.cari_kode(kode)

                if alat:
                    alat.tampilkan_info()
                else:
                    print("Peralatan tidak ditemukan.")

            elif pilihan == "5":
                nama = input("Nama/kata kunci: ")
                hasil = self.daftar_peralatan.cari_nama(nama)

                if hasil:
                    for alat in hasil:
                        alat.tampilkan_info()
                else:
                    print("Peralatan tidak ditemukan.")

            elif pilihan == "6":
                kategori = input("Kategori: ")
                hasil = self.daftar_peralatan.cari_kategori(kategori)

                if hasil:
                    for alat in hasil:
                        alat.tampilkan_info()
                else:
                    print("Peralatan tidak ditemukan.")

            elif pilihan == "7":
                hasil = self.daftar_peralatan.alat_tersedia()

                if hasil:
                    for alat in hasil:
                        alat.tampilkan_info()
                else:
                    print("Tidak ada alat yang tersedia.")

            elif pilihan == "8":
                hasil = self.daftar_peralatan.alat_dipinjam()

                if hasil:
                    for alat in hasil:
                        alat.tampilkan_info()
                else:
                    print("Tidak ada alat yang sedang dipinjam.")

            elif pilihan == "9":
                hasil = self.daftar_peralatan.alat_rusak()

                if hasil:
                    for alat in hasil:
                        alat.tampilkan_info()
                else:
                    print("Tidak ada alat rusak.")

            elif pilihan == "10":
                self.daftar_peralatan.tampilkan_semua()

            elif pilihan == "0":
                break

            else:
                print("Pilihan tidak valid.")

    # =========================
    # UI PEMINJAMAN
    # =========================

    def menu_peminjaman(self):
        print("\n=== PEMINJAMAN PERALATAN ===")

        nim = input("NIM mahasiswa: ")
        mahasiswa = self.daftar_mahasiswa.cari(nim)

        if mahasiswa is None:
            print("Mahasiswa tidak ditemukan.")
            return

        if not mahasiswa.bisa_meminjam():
            print("Mahasiswa sudah mencapai batas peminjaman.")
            return

        self.daftar_peralatan.tampilkan_semua()

        kode_input = input(
            "Masukkan kode alat (pisahkan dengan koma): "
        )

        kode_list = [
            kode.strip()
            for kode in kode_input.split(",")
            if kode.strip()
        ]

        daftar_alat = []

        for kode in kode_list:
            alat = self.daftar_peralatan.cari_kode(kode)

            if alat is None:
                print(f"Alat dengan kode {kode} tidak ditemukan.")
                return

            if not alat.bisa_dipinjam():
                print(f"Alat {kode} tidak dapat dipinjam.")
                return

            daftar_alat.append(alat)

        transaksi = self.daftar_transaksi.buat_transaksi(
            mahasiswa,
            daftar_alat
        )

        if transaksi:
            self.catat_log(
                f"Peminjaman dibuat: {transaksi.id_transaksi}"
            )
            print("Peminjaman berhasil.")
            transaksi.tampilkan_nota()
        else:
            print("Peminjaman gagal.")

    # =========================
    # UI PENGEMBALIAN
    # =========================

    def menu_pengembalian(self):
        print("\n=== PENGEMBALIAN PERALATAN ===")

        id_transaksi = input("ID transaksi: ")

        transaksi = self.daftar_transaksi.data.get(id_transaksi)

        if transaksi is None:
            print("Transaksi tidak ditemukan.")
            return

        print("\nAlat yang belum dikembalikan:")

        for alat in transaksi.alat_belum_kembali():
            print(f"- {alat.kode_alat} | {alat.nama_alat}")

        kode = input("\nKode alat: ")
        kondisi = input(
            "Kondisi alat (baik/rusak/hilang): "
        ).lower()

        if kondisi not in ["baik", "rusak", "hilang"]:
            print("Kondisi tidak valid.")
            return

        berhasil = self.daftar_transaksi.proses_pengembalian(
            id_transaksi,
            kode,
            kondisi
        )

        if berhasil:
            self.catat_log(
                f"Pengembalian alat {kode}, transaksi {id_transaksi}"
            )
            print("Pengembalian berhasil.")
        else:
            print("Pengembalian gagal.")


# =========================
# PROGRAM UTAMA / UI
# =========================

if __name__ == "__main__":
    sistem = SistemLab()
    sistem.jalankan()
