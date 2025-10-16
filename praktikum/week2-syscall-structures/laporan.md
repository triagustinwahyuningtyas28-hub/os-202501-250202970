
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
open() – Membuka file
Program cat meminta kernel untuk membuka file /etc/passwd.
Kernel memeriksa apakah file tersebut ada dan apakah user memiliki izin untuk membukanya.
Jika diizinkan, kernel membuat file descriptor, yaitu nomor unik yang mewakili file tersebut di dalam sistem.

read() – Membaca isi file
Program meminta kernel membaca isi file melalui file descriptor.
Kernel mengambil data dari disk (storage) dan menyalinnya ke memori (buffer) program.
Data tersebut kemudian siap ditampilkan atau diolah oleh program.

write() – Menulis ke output
Program cat menggunakan system call write() untuk menampilkan isi file ke layar (stdout).
Kernel mengirimkan data dari memori program ke perangkat output (biasanya terminal).

close() – Menutup file
Setelah selesai, program memanggil close() untuk memberitahu kernel bahwa file sudah tidak digunakan.
Kernel kemudian melepaskan file descriptor dan sumber daya lain yang terkait. 


dmesg (display message) menampilkan pesan-pesan dari kernel ring buffer, yaitu log yang dihasilkan oleh kernel Linux saat sistem melakukan booting atau saat perangkat keras dan driver dijalankan.

Log ini mencakup hal-hal seperti:
Proses inisialisasi perangkat keras (misal AC adapter, baterai, CPU, jaringan)
Pesan dari modul kernel (seperti kvm_intel, intel_rapl_msr)
Error atau peringatan sistem rendah (misal: “suspect GRO implementation”)
Jadi, dmesg menampilkan aktivitas sistem level kernel, bukan aktivitas aplikasi user biasa.

| Aspek            | Output `dmesg`                                            | Output Program Biasa                                   |
| ---------------- | --------------------------------------------------------- | ------------------------------------------------------ |
| **Sumber**       | Kernel (sistem operasi inti)                              | User-space program (misal `cat`, `ls`, `python`, dll.) |
| **Isi Pesan**    | Status hardware, driver, dan kernel internal              | Hasil dari instruksi atau log program                  |
| **Akses**        | Butuh hak akses ke kernel (bisa `sudo`)                   | Dijalankan langsung oleh user                          |
| **Tujuan**       | Debugging sistem & hardware                               | Memberikan hasil kerja program ke pengguna             |
| **Contoh Pesan** | `[7.981179] ACPI: battery: Slot [BAT1] (battery present)` | `Hello World`, hasil perhitungan, dsb.                 |

dmesg = log dari otak sistem operasi (kernel)
Program biasa = hasil kerja dari pengguna atau aplikasi di atas OS 

---

## Kesimpulan
Perintah dmesg digunakan untuk menampilkan log kernel, yaitu pesan-pesan yang dihasilkan oleh sistem operasi saat proses booting, inisialisasi perangkat keras, atau saat terjadi kesalahan di level sistem.
Output dmesg berbeda dari output program biasa, karena pesan tersebut berasal dari kernel mode (inti sistem), bukan dari user mode (aplikasi pengguna).
Analisis log dmesg membantu mendeteksi masalah hardware atau driver, seperti error jaringan, baterai, atau modul kernel yang bermasalah.

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?
Fungsi utama system call dalam sistem operasi adalah sebagai jembatan antara program (user mode) dan kernel (kernel mode).

Lebih jelasnya, fungsi utamanya yaitu:
Memberikan akses ke layanan kernel — seperti mengakses file, perangkat keras, atau memori.
Memungkinkan program berinteraksi dengan sistem operasi tanpa harus langsung mengakses perangkat keras.
Menjamin keamanan dan stabilitas sistem dengan membatasi akses langsung dari user ke kernel.
2. Sebutkan 4 kategori system call yang umum digunakan.
Process Control – untuk mengatur proses.
Contoh: fork(), exec(), exit().

File Management – untuk mengelola file.
Contoh: open(), read(), write(), close().

Device Management – untuk berinteraksi dengan perangkat keras.
Contoh: ioctl(), read(), write().

Information Maintenance – untuk mendapatkan atau mengatur informasi sistem.
Contoh: getpid(), alarm(), time().

3. Mengapa system call tidak bisa dipanggil langsung oleh user program?  
Keamanan: Agar user tidak bisa mengakses atau mengubah kernel dan perangkat keras secara langsung yang bisa merusak sistem.
Perlindungan sistem: Kernel berjalan di privileged mode, sedangkan program biasa di user mode. Hanya kernel yang boleh menjalankan instruksi tertentu.
Stabilitas: Dengan pembatasan ini, kesalahan dalam program user tidak akan membuat seluruh sistem crash. 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? = masih sesuai dengan week 1 yaitu mengejar deadline  
- Bagaimana cara Anda mengatasinya? = mengerjakan praktikum secepat mungkin

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
