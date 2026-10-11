from datetime import datetime, timedelta

class Transaksi:
    def __init__(self, id_transaksi, mahasiswa, daftar_alat=None):
        self.id_transaksi = str(id_transaksi)
        self.mahasiswa = mahasiswa
        # list: menyimpan kumpulan objek peralatan yang dipinjam dalam transaksi ini
        if daftar_alat is None:
            self.daftar_alat = []
        else:
            self.daftar_alat = daftar_alat
            
        self.tanggal_pinjam = datetime.now().date()
        self.batas_kembali = self.tanggal_pinjam + timedelta(days=7)
        self.status = "Aktif"

    def tambah_alat(self, alat):
        self.daftar_alat.append(alat)

    def catat_pengembalian(self, kode, kondisi):
        for alat in self.daftar_alat:
            if alat.kode_alat == kode:
                alat.terima_pengembalian(kondisi)
                return True
        return False

    def alat_belum_kembali(self):
        # list: menyimpan daftar peralatan yang statusnya masih dipinjam
        belum = []
        for alat in self.daftar_alat:
            if alat.status == "dipinjam":
                belum.append(alat)
        return belum

    def masih_aktif(self):
        return self.status.lower() == "aktif"

    def tampilkan_nota(self):
        print("\n" + "=" * 45)
        print("          STRUK PEMINJAMAN ALAT LAB          ")
        print("=" * 45)
        print(f" ID Transaksi   : {self.id_transaksi}")
        print(f" Peminjam       : {self.mahasiswa.nama} ({self.mahasiswa.nim})")
        print(f" No. HP         : {self.mahasiswa.no_hp}")
        print(f" Tgl Pinjam     : {self.tanggal_pinjam.strftime('%d-%m-%Y')}")
        print(f" Batas Kembali  : {self.batas_kembali.strftime('%d-%m-%Y')} (Maks. 7 Hari)")
        print(f" Status         : {self.status}")
        print("-" * 45)
        print(" Daftar Peralatan Dipinjam:")
        
        if not self.daftar_alat:
            print("   (Belum ada alat terdaftar)")
        else:
            for idx, alat in enumerate(self.daftar_alat, start=1):
                print(f"   {idx}. [{alat.kode_alat}] {alat.nama_alat} (Kondisi: {alat.kondisi})")
                
        print("=" * 45)
        print(" Catatan: Keterlambatan pengembalian akan")
        print(" dikenakan sanksi sesuai aturan Lab.")
        print("=" * 45 + "\n")