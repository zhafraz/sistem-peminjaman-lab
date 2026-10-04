from datetime import datetime, timedelta

class Transaksi:
    def __init__(self, id_transaksi, mahasiswa, daftar_alat=None, tanggal_pinjam=None):
        self.id_transaksi = str(id_transaksi)
        self.mahasiswa = mahasiswa
        self.daftar_alat = daftar_alat if daftar_alat is not None else []
        
        if isinstance(tanggal_pinjam, str):
            self.tanggal_pinjam = datetime.strptime(tanggal_pinjam, "%Y-%m-%d").date()
        elif isinstance(tanggal_pinjam, datetime):
            self.tanggal_pinjam = tanggal_pinjam.date()
        elif tanggal_pinjam is None:
            self.tanggal_pinjam = datetime.now().date()
        else:
            self.tanggal_pinjam = tanggal_pinjam
            
        self.batas_kembali = self.tanggal_pinjam + timedelta(days=7)
        self.status = "Aktif"

    def tambah_alat(self, alat):
        self.daftar_alat.append(alat)

    def catat_pengembalian(self, kode, kondisi, tgl_date=None):
        for alat in self.daftar_alat:
            if getattr(alat, 'kode_alat', None) == kode:
                alat.kondisi = kondisi
                if hasattr(alat, 'terima_pengembalian'):
                    alat.terima_pengembalian(kondisi)
                return True
        return False

    def alat_belum_kembali(self):
        return [
            alat for alat in self.daftar_alat 
            if getattr(alat, 'status', '').lower() in ['dipinjam', 'dipinjamkan', 'aktif']
        ]

    def masih_aktif(self):
        return self.status.lower() == "aktif"

    def tampilkan_nota(self):
        print("\n" + "=" * 45)
        print("          STRUK PEMINJAMAN ALAT LAB          ")
        print("=" * 45)
        print(f" ID Transaksi   : {self.id_transaksi}")
        print(f" Peminjam       : {getattr(self.mahasiswa, 'nama', 'N/A')} ({getattr(self.mahasiswa, 'nim', '-')})")
        print(f" No. HP         : {getattr(self.mahasiswa, 'no_hp', '-')}")
        print(f" Tgl Pinjam     : {self.tanggal_pinjam.strftime('%d-%m-%Y')}")
        print(f" Batas Kembali  : {self.batas_kembali.strftime('%d-%m-%Y')} (Maks. 7 Hari)")
        print(f" Status         : {self.status}")
        print("-" * 45)
        print(" Daftar Peralatan Dipinjam:")
        
        if not self.daftar_alat:
            print("   (Belum ada alat terdaftar)")
        else:
            for idx, alat in enumerate(self.daftar_alat, start=1):
                nama = getattr(alat, 'nama_alat', str(alat))
                kode = getattr(alat, 'kode_alat', '-')
                kondisi = getattr(alat, 'kondisi', '-')
                print(f"   {idx}. [{kode}] {nama} (Kondisi: {kondisi})")
                
        print("=" * 45)
        print(" Catatan: Keterlambatan pengembalian akan")
        print(" dikenakan sanksi sesuai aturan Lab.")
        print("=" * 45 + "\n")