
# Laporan Praktikum Minggu [2]
Topik: System Call

---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas
- **NIM**   : 250202970 
- **Kelas** : 1IKRA

---

## Tujuan
1.Menjelaskan konsep dan fungsi system call dalam sistem operasi.

Konsep system call dalam sistem operasi
System call adalah mekanisme yang memungkinkan program pengguna (user program) berinteraksi dengan kernel (inti sistem operasi). Program di user mode tidak boleh langsung mengakses perangkat keras atau memori sistem, sehingga harus menggunakan system call sebagai perantara aman untuk meminta layanan dari OS.

Fungsi system call dalam sistem operasi
- Process Control: fork(), exec(), exit() – mengatur proses
- File Management: open(), read(), write(), close() – operasi file.
- Device Management: ioctl(), read(), write() – akses perangkat I/O.
- Information Maintenance: getpid(), alarm() – informasi sistem/proses.
- Communication: pipe(), socket(), send(), recv() – komunikasi antar proses.

2.Mengidentifikasi jenis-jenis system call dan fungsinya.
- Process Control (Pengendalian Proses):digunakan untuk membuat, mengatur, dan mengakhiri proses.
- File Management (Manajemen Berkas):digunakan untuk membuka, membaca, menulis, dan menutup file.
- Device Management (Manajemen Perangkat):digunakan untuk mengakses dan mengontrol perangkat input/output (I/O) seperti printer, disk, atau keyboard.
- Information Maintenance (Pemeliharaan Informasi):digunakan untuk mengambil atau mengatur informasi tentang sistem atau proses.
- Communication (Komunikasi Antarproses / Interprocess Communication – IPC):digunakan agar proses dapat bertukar data atau berkoordinasi satu sama lain.

3.Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
User Mode: Program aplikasi berjalan di user mode.
Pemanggilan System Call: Program memanggil system call (misal read(), write()).
Trap / Interrupt: CPU melakukan trap untuk berpindah ke kernel mode.
Kernel Mode: Kernel mengeksekusi permintaan system call.
Kembali ke User Mode: Setelah selesai, CPU kembali ke user mode, dan hasil system call dikembalikan ke program.

4.Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.
perintah linux untuk menampilkan system call adalah strace. strace ini juga berfungsi untuk menganalisis system call

---

## Dasar Teori
Berikut ringkasan teori yang mendasari percobaan pada gambar tersebut (menjalankan perintah strace ls di Linux):

System Call (Panggilan Sistem)
Merupakan antarmuka antara program pengguna (user mode) dan kernel (kernel mode).
Saat perintah seperti ls dijalankan, program tidak langsung mengakses hardware, tetapi meminta layanan kernel melalui system call seperti open(), read(), write(), dan close().

Perpindahan Mode User ke Kernel
Saat system call dipanggil, CPU berpindah dari user mode ke kernel mode untuk mengeksekusi fungsi kernel yang memiliki hak akses penuh terhadap perangkat keras.
Setelah selesai, kontrol dikembalikan lagi ke user mode.

Fungsi strace
strace digunakan untuk memantau semua system call yang dijalankan oleh suatu program.
Dengan strace ls, kita dapat melihat bagaimana ls memanggil system call untuk membuka file, membaca direktori, dan menampilkan hasilnya ke layar.

Manajemen Memori dan File System
Terlihat system call seperti mmap() (memetakan file ke memori), open(), read(), dan close() yang menunjukkan interaksi program dengan file sistem dan memori virtual.

Tujuan Analisis strace
Untuk memahami urutan kerja program di level sistem operasi.
Bermanfaat dalam debugging, optimasi, dan analisis keamanan sistem.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
hasil percobaan
<img width="959" height="539" alt="Screenshot 2025-10-15 211356" src="https://github.com/user-attachments/assets/d4a62ec5-bd22-461f-acc3-6aba149ad4ff" />


---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini =menjelaskan  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
