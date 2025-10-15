
# Laporan Praktikum Minggu [2]
Topik: system call

---

## Identitas
- **Nama**  : muhammad reza fahlevi
- **NIM**   : 250202955 
- **Kelas** : 1IKRA

---

## Tujuan
1. Konsep dan Fungsi System Call
Konsep:
System call adalah mekanisme yang digunakan oleh program di mode user untuk meminta layanan dari kernel (mode kernel). Karena program biasa tidak memiliki hak akses langsung ke perangkat keras atau sumber daya sistem, system call menjadi jembatan penghubung antara user space dan kernel space.

Fungsi utama system call:
Mengizinkan program berinteraksi dengan sistem operasi.
Menyediakan antarmuka aman antara aplikasi dan perangkat keras.
Mengatur penggunaan sumber daya sistem (CPU, memori, file, perangkat I/O).
Melindungi sistem dari kesalahan atau akses ilegal oleh user program.

2.Mengidentifikasi jenis-jenis system call dan fungsinya
Contoh sederhana:
Ketika kamu mengetik perintah cat file.txt, sistem akan melakukan system call seperti:
open() → membuka file
read() → membaca isi file
write() → menampilkan isi ke layar
close() → menutup file

Manajemen Proses
Mengatur pembuatan, eksekusi, dan penghentian proses.
Contoh: fork(), exec(), wait(), exit()

Manajemen File
Mengelola file dan direktori.
Contoh: open(), read(), write(), close(), unlink()

Manajemen Memori
Mengatur alokasi dan pelepasan memori proses.
Contoh: brk(), mmap(), munmap()

Manajemen I/O (Input/Output)
Berinteraksi dan mengontrol perangkat input/output.
Contoh: read(), write(), ioctl()

Informasi Sistem
Mengambil atau mengubah informasi sistem dan proses.
Contoh: getpid(), getuid(), uname()

Komunikasi Antar Proses (IPC)
Memungkinkan proses bertukar data dan berkoordinasi.
Contoh: pipe(), shmget(), msgsnd(), socket()

3.Mengamati alur perpindahan mode user ke kernel saat system call terjadi.

Alur Perpindahan Mode User ke Kernel
Saat program di mode user memanggil system call, terjadi perpindahan kendali dari user mode → kernel mode → user mode.
Hal ini karena hanya kernel mode yang punya hak akses penuh ke perangkat keras dan sumber daya sistem.

Langkah-langkah Alur Eksekusi:
Program user menjalankan perintah (misalnya read() atau write()).
Library system call (seperti glibc) menerjemahkan perintah tersebut menjadi trap atau interrupt (contohnya int 0x80 pada Linux).
CPU berpindah dari user mode ke kernel mode dan menjalankan kode kernel yang sesuai.
Kernel mengeksekusi layanan yang diminta (misalnya membaca data dari disk, menulis ke layar, dsb).
Setelah selesai, kernel mengembalikan hasil ke program user.
CPU berpindah kembali ke user mode untuk melanjutkan eksekusi program.

4.Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.
Menggunakan Perintah Linux untuk Menampilkan dan Menganalisis System Call

strace ls
Menampilkan system call yang dilakukan oleh perintah ls.

strace -o hasil.txt ls
Menyimpan hasil system call ke file hasil.txt.

strace -e open,read,write cat /etc/passwd
Menampilkan hanya system call open, read, dan write.

dmesg
Menampilkan pesan dari kernel untuk analisis lebih lanjut.

---

## Dasar Teori
System call adalah mekanisme yang digunakan program di user mode untuk meminta layanan dari kernel mode, seperti membaca file atau membuat proses.
Setiap interaksi antara program dan perangkat keras harus melalui system call agar sistem tetap aman dan terkontrol.
Kernel memiliki hak akses penuh ke sumber daya sistem, sedangkan user mode dibatasi untuk mencegah kerusakan sistem.
Proses system call melibatkan perpindahan dari user mode ke kernel mode menggunakan instruksi trap, lalu kembali ke user mode setelah layanan selesai.
Perintah seperti strace digunakan di Linux untuk mengamati dan menganalisis system call yang dilakukan oleh program

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
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10
```

---

## Hasil Eksekusi
hasil percobaan system call
<img width="1918" height="1017" alt="Screenshot 2025-10-15 182828" src="https://github.com/user-attachments/assets/fb989cbc-5ede-422b-9486-68644c5402be" />

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
1. Apa fungsi utama system call dalam sistem operasi? 
    
2. Sebutkan 4 kategori system call yang umum digunakan.
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
