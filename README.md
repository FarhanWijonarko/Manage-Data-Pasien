---

# Sistem Manajemen Data Pasien Sederhana

Aplikasi konsol Python ini dirancang sebagai **sistem manajemen data pasien yang komprehensif namun mudah digunakan**, beroperasi sepenuhnya melalui antarmuka baris perintah (CLI). Sistem ini memungkinkan pengguna untuk **mengelola informasi pasien secara efisien** mulai dari proses pendaftaran awal hingga pemantauan statistik kesehatan. Dengan fokus pada fungsionalitas inti, aplikasi ini menyediakan serangkaian fitur lengkap yang esensial untuk pencatatan data medis dasar, menjadikannya alat yang ideal untuk kebutuhan administrasi data pasien di lingkungan kecil atau sebagai fondasi untuk pengembangan lebih lanjut.

---

## Fitur Utama

Aplikasi ini dilengkapi dengan fitur-fitur yang memungkinkan pengelolaan data pasien secara menyeluruh:

* **Menambah Data Pasien**: Anda dapat dengan mudah **memasukkan data pasien baru** ke dalam sistem, termasuk informasi detail seperti nama depan, nama belakang, Nomor Induk Kependudukan (NIK), usia, jenis kelamin, status kesehatan (misalnya, 'Dirawat' atau 'Sembuh'), dan alamat tempat tinggal. Setiap entri data pasien akan menghasilkan ID unik secara otomatis untuk identifikasi yang mudah.

* **Melihat Data Pasien**: Sistem menawarkan beberapa opsi untuk melihat data:
    * **Tampilkan Semua Data Pasien**: Menampilkan seluruh daftar pasien dalam format tabel yang terorganisir, memudahkan tinjauan umum.
    * **Tampilkan Data Pasien Berdasarkan ID**: Anda dapat mencari dan menampilkan detail spesifik dari satu pasien dengan memasukkan ID unik mereka, sangat berguna untuk akses cepat ke informasi individu.
    * **Tampilkan Data Pasien Berdasarkan Status Kesehatan**: Fitur ini memungkinkan Anda untuk **memfilter dan menampilkan pasien berdasarkan status kesehatan** mereka (misalnya, semua pasien yang sedang 'Dirawat' atau yang sudah 'Sembuh'), memberikan gambaran kondisi pasien secara kelompok.

* **Memperbarui Data Pasien**: Fleksibilitas untuk **memperbarui informasi pasien** kapan saja. Anda dapat mengubah detail pribadi seperti nama, umur, jenis kelamin, dan alamat, serta **memperbarui status kesehatan** pasien sesuai dengan perkembangan kondisi mereka.

* **Menghapus Data Pasien**: Jika diperlukan, Anda dapat **menghapus data pasien** dari sistem. Proses ini dilengkapi dengan konfirmasi untuk mencegah penghapusan yang tidak disengaja.

* **Statistik Data Pasien**: Fitur ini menyediakan **ringkasan analitis** dari data pasien yang ada, membantu dalam pemahaman demografi dan kondisi umum pasien:
    * **Jumlah Total Pasien**: Menampilkan total pasien yang terdaftar dalam sistem.
    * **Distribusi Pasien Berdasarkan Gender**: Menunjukkan jumlah pasien pria dan wanita.
    * **Rata-rata Umur Pasien, Umur Termuda, dan Umur Tertua**: Memberikan gambaran tentang rentang usia pasien.
    * **Distribusi Umur Pasien**: Mengkategorikan pasien ke dalam kelompok usia tertentu (<18 tahun, 18-30 tahun, 30-60 tahun, dan >=60 tahun) untuk analisis demografis yang lebih mendalam.
    * **Persentase Pasien Dirawat dan Sembuh**: Memberikan wawasan tentang proporsi pasien berdasarkan status kesehatan mereka.

---

## Cara Menjalankan Aplikasi

1.  **Pastikan Anda memiliki Python terinstal** di sistem Anda (versi 3.x direkomendasikan untuk kompatibilitas terbaik).
2.  **Unduh file kode** `main.py` (atau nama file Python Anda yang berisi kode program) ke komputer Anda.
3.  **Buka terminal atau *command prompt*** di sistem operasi Anda.
4.  **Navigasikan ke direktori** tempat Anda menyimpan file Python tersebut menggunakan perintah `cd`.
5.  **Jalankan aplikasi** dengan perintah berikut:

    ```bash
    python nama_file_anda.py
    ```

    *(Ganti `nama_file_anda.py` dengan nama aktual dari file Python Anda, misalnya `pasien_app.py`)*

6.  Setelah aplikasi berjalan, Anda akan melihat **menu interaktif di konsol**. Ikuti petunjuk yang ditampilkan untuk memilih operasi yang ingin Anda lakukan (menambah, melihat, memperbarui, menghapus, atau melihat statistik data pasien).

---

## Struktur Kode

Kode program ini terorganisir dengan baik ke dalam beberapa fungsi modular, yang masing-masing bertanggung jawab atas fungsionalitas tertentu, sehingga memudahkan pemahaman dan pemeliharaan:

* `dataStatistik()`: Bertanggung jawab untuk menghitung berbagai metrik statistik dari data pasien yang ada dan menampilkannya dalam format yang mudah dibaca.
* `data()`: Fungsi ini digunakan untuk menambahkan data pasien baru yang telah divalidasi ke dalam struktur data utama program.
* `tabelPasien()`: Digunakan untuk menampilkan seluruh kumpulan data pasien dalam format tabel yang rapi di konsol.
* `tabelPasienSatuan()`: Mirip dengan `tabelPasien()`, namun khusus digunakan untuk menampilkan data satu pasien saja atau hasil filter dari pencarian.
* `updateDataPasien()`: Mengelola alur untuk memodifikasi informasi detail pasien yang sudah ada.
* `deleteDataPasien()`: Berisi logika untuk menghapus data pasien dari sistem setelah konfirmasi.

Program utama berjalan dalam sebuah *loop* `while True` yang secara terus-menerus menampilkan menu pilihan kepada pengguna dan memanggil fungsi yang relevan berdasarkan input pilihan pengguna, menciptakan pengalaman interaktif yang intuitif.

---
