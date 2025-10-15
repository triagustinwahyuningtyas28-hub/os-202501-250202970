
# Laporan Praktikum Minggu [2]
Topik: System Call

---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas
- **NIM**   : 250202970 
- **Kelas** : 1IKRA

---

## Tujuan
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
Konsep system call dalam sistem operasi
System call adalah mekanisme yang memungkinkan program pengguna (user program) berinteraksi dengan kernel (inti sistem operasi). Program di user mode tidak boleh langsung mengakses perangkat keras atau memori sistem, sehingga harus menggunakan system call sebagai perantara aman untuk meminta layanan dari OS.

Fungsi system call dalam sistem operasi
Process Control: fork(), exec(), exit() – mengatur proses.
File Management: open(), read(), write(), close() – operasi file.
Device Management: ioctl(), read(), write() – akses perangkat I/O.
Information Maintenance: getpid(), alarm() – informasi sistem/proses.
Communication: pipe(), socket(), send(), recv() – komunikasi antar proses.

2.Mengidentifikasi jenis-jenis system call dan fungsinya.
Process Control (Pengendalian Proses):digunakan untuk membuat, mengatur, dan mengakhiri proses.
File Management (Manajemen Berkas):digunakan untuk membuka, membaca, menulis, dan menutup file.
Device Management (Manajemen Perangkat):digunakan untuk mengakses dan mengontrol perangkat input/output (I/O) seperti printer, disk, atau keyboard.
Information Maintenance (Pemeliharaan Informasi):digunakan untuk mengambil atau mengatur informasi tentang sistem atau proses.
Communication (Komunikasi Antarproses / Interprocess Communication – IPC):digunakan agar proses dapat bertukar data atau berkoordinasi satu sama lain.

3.Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
User Mode: Program aplikasi berjalan di user mode.
Pemanggilan System Call: Program memanggil system call (misal read(), write()).
Trap / Interrupt: CPU melakukan trap untuk berpindah ke kernel mode.
Kernel Mode: Kernel mengeksekusi permintaan system call.
Kembali ke User Mode: Setelah selesai, CPU kembali ke user mode, dan hasil system call dikembalikan ke program.

4.Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

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
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

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
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
