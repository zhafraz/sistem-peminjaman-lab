# Sistem Peminjaman Peralatan Laboratorium

Proyek aplikasi berbasis Python dengan menerapkan konsep **Object-Oriented Programming (OOP)** untuk mengelola pencatatan, peminjaman, pengembalian, dan inventaris peralatan laboratorium komputer.

---

## 👥 Anggota Kelompok

| Nama | NIM | Status |
| :--- | :---: | :---: |
| **Thiraza Naufal Zhafran Windra** | K3525086 | **Ketua** |
| **Udzma Fithratun Nufusu** | K3525076 | Anggota |
| **Nadia Indah Santika** | K3525084 | Anggota |
| **Aghni Ilman Karismart** | K3525080 | Anggota |
| **Fazril Arghana Putra Septyawan** | K3525083 | Anggota |

---

## 📁 Struktur Direktori

Berikut adalah struktur folder dan penjelasan masing-masing berkas dalam proyek:

```text
sistem-peminjaman-lab/
│
├── main.py                     # Entry point & pengendali antarmuka CLI (Class SistemLab)
├── README.md                   # Dokumentasi proyek, struktur berkas, dan anggota kelompok
│
├── modul_program/              # Package modul inti logika bisnis dan OOP
│   ├── __init__.py             # Inisialisasi package Python
│   ├── mahasiswa.py            # Model entitas Mahasiswa (data peminjam & kuota transaksi aktif)
│   ├── peralatan.py            # Abstract Base Class Peralatan & subclass spesifik kategori
│   ├── transaksi.py            # Model entitas Transaksi peminjaman & nota peminjaman
│   ├── daftar_mahasiswa.py     # Koleksi & manajemen data mahasiswa (CRUD)
│   ├── daftar_peralatan.py     # Koleksi & inventarisasi peralatan laboratorium
│   └── daftar_transaksi.py     # Manajemen pembuatan transaksi, pengembalian & riwayat
│
└── dokumentasi/                # Berkas pendukung dan diagram perancangan sistem
    ├── diagram-class.png       # Rancangan awal Class Diagram
    └── UML_Class_Diagram_Revisi.png # Revisi Diagram Kelas UML final
```

---

## 📖 Penjelasan Modul Program

1. **`main.py` (`SistemLab`)**
   * Berperan sebagai antarmuka utama berbasis teks (CLI) yang mengintegrasikan seluruh modul.
   * Menyediakan menu pengelolaan mahasiswa, pengelolaan peralatan, alur peminjaman, alur pengembalian, daftar seluruh transaksi, serta pencatatan log aktivitas sistem.

2. **`modul_program/peralatan.py`**
   * **`Peralatan` (Abstract Base Class)**: Kerangka dasar peralatan laboratorium dengan method abstrak `kategori()`.
   * **Subclass Polimorfisme**:
     * `PerangkatKomputasi`: Kategori perangkat komputasi (laptop, PC, dsb).
     * `PerangkatJaringan`: Kategori perangkat jaringan (router, switch, kabel LAN, dsb).
     * `PerangkatMultimedia`: Kategori perangkat multimedia (proyektor, kamera, mic, dsb).

3. **`modul_program/mahasiswa.py` (`Mahasiswa`)**
   * Menyimpan identitas mahasiswa (NIM, Nama, No. HP).
   * Mengatur batas kuota maksimal peminjaman aktif (`MAKS_TRANSAKSI_AKTIF = 2`).

4. **`modul_program/transaksi.py` (`Transaksi`)**
   * Menyimpan identitas transaksi unik, data peminjam, tanggal pinjam, batas kembali (7 hari), status transaksi, dan daftar detail peralatan (`dict[str, dict]`).
   * Mengelola pencatatan kondisi alat saat pengembalian dan pencetakan struk/nota peminjaman resmi.

5. **`modul_program/daftar_mahasiswa.py` (`DaftarMahasiswa`)**
   * Menyimpan dan mengelola kamus (*dictionary*) mahasiswa dengan kunci NIM.
   * Menangani operasi penambahan, pengubahan data, pencarian, dan penghapusan (dengan proteksi jika mahasiswa masih memiliki pinjaman aktif).

6. **`modul_program/daftar_peralatan.py` (`DaftarPeralatan`)**
   * Menyimpan kamus peralatan dengan pemetaan kategori dinamis (`daftar_kategori: dict[str, type]`).
   * Menangani filtering peralatan: tersedia, sedang dipinjam, atau rusak.

7. **`modul_program/daftar_transaksi.py` (`DaftarTransaksi`)**
   * Menangani siklus hidup peminjaman (`buat_transaksi`) dengan validasi minimal 1 alat (`1..*`) dan kuota peminjam.
   * Menangani alur pengembalian per alat, pelunasan status transaksi, dan penelusuran riwayat transaksi per mahasiswa.

---

## 🚀 Cara Menjalankan Program

### Prasyarat
* Python versi 3.8 atau lebih baru terpasang di komputer Anda.

### Langkah Menjalankan
1. Buka terminal / command prompt pada folder utama proyek:
   ```bash
   cd "sistem-peminjaman-lab"
   ```
2. Jalankan perintah berikut:
   ```bash
   python main.py
   ```
3. Gunakan nomor menu pada antarmuka terminal untuk mengoperasikan sistem:
   * **Menu 1**: Mendaftarkan atau mengelola data Mahasiswa.
   * **Menu 2**: Menambahkan atau melihat stok Peralatan Lab.
   * **Menu 3**: Melakukan transaksi Peminjaman Alat.
   * **Menu 4**: Memproses Pengembalian Alat & mencatat kondisinya.
   * **Menu 5**: Melihat semua transaksi peminjaman.
   * **Menu 6**: Memeriksa log riwayat aktivitas sistem.
   * **Menu 0**: Keluar dari aplikasi.
