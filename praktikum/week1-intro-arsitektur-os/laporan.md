
# Laporan Praktikum Minggu [1]
Topik: Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : muhammad reza fahlevi  
- **NIM**   : 250202955
- **Kelas** : 1IKRA

---

## Tujuan
1. Fungsi Utama Sistem Operasi
Sistem operasi (Operating System/OS) adalah perangkat lunak sistem yang berfungsi sebagai penghubung antara pengguna dan perangkat keras komputer. Fungsi utamanya meliputi:
Manajemen Proses (Process Management)
Mengatur pembuatan, penjadwalan, dan penghentian proses (program yang sedang berjalan).

Contoh: OS mengatur agar beberapa aplikasi bisa berjalan bersamaan tanpa bentrok.
Manajemen Memori (Memory Management)
Mengalokasikan dan mengatur penggunaan memori utama (RAM) untuk setiap proses.

Contoh: OS memastikan setiap aplikasi hanya menggunakan bagian memori yang diberikan.
Manajemen File (File Management)
Mengatur penyimpanan, pembacaan, penulisan, dan penghapusan file dalam sistem.

Contoh: OS menyediakan sistem file seperti NTFS, FAT32, atau ext4.
Manajemen Perangkat I/O (Device Management)
Mengontrol dan mengoordinasikan perangkat input/output seperti printer, keyboard, dan hard disk.
Contoh: OS menggunakan driver untuk menghubungkan hardware dengan software.
Manajemen Keamanan dan Proteksi (Security & Protection)
Melindungi data dan sumber daya dari akses tidak sah.
Contoh: OS menyediakan autentikasi pengguna (password, izin akses).
User Interface (Antarmuka Pengguna)
Memberikan cara bagi pengguna untuk berinteraksi dengan komputer, baik melalui GUI (Graphical User Interface) atau CLI (Command Line Interface).

2. Peran Kernel
Kernel adalah inti dari sistem operasi yang berjalan di mode paling tinggi (privileged mode).
Fungsinya antara lain:
Mengelola sumber daya sistem seperti CPU, memori, dan perangkat keras.
Menjadi penghubung antara aplikasi dan hardware.
Menangani interupsi dan sistem waktu nyata (real-time).
Menjamin keamanan dan isolasi antar proses.

Contoh:
Ketika aplikasi ingin membaca file, kernel yang akan mengatur akses ke hard disk dan memberikan data ke aplikasi.

3. Peran System Call
System Call adalah jembatan antara program aplikasi dan kernel.
Program tidak bisa langsung mengakses hardware, jadi harus lewat system call.

Contoh jenis system call:
Process control: fork(), exec(), exit()
File management: open(), read(), write(), close()
Device management: ioctl(), read(), write()
Information maintenance: getpid(), alarm()

Analogi sederhana:
Aplikasi = pengguna restoran
Kernel = dapur
System call = pelayan yang menyampaikan pesanan dari pengguna ke dapur.

---

## Dasar Teori
Kernel sebagai inti sistem operasi
Kernel adalah komponen utama sistem operasi yang berfungsi mengatur komunikasi antara perangkat keras (hardware) dan perangkat lunak (software). Kernel mengelola sumber daya sistem seperti CPU, memori, dan perangkat I/O.

System Call sebagai penghubung user space dan kernel space
Program aplikasi tidak bisa langsung berinteraksi dengan hardware. Untuk itu, digunakan system call sebagai jembatan antara proses di user space dengan layanan kernel di kernel space.

Modul kernel (Kernel Modules)
Melalui perintah lsmod, dapat dilihat daftar modul kernel yang sedang dimuat. Modul ini bersifat dinamis—dapat dimuat atau dilepas tanpa perlu me-restart sistem, contohnya modul kvm_intel untuk virtualisasi.

Pesan kernel (dmesg)
Perintah dmesg menampilkan log atau pesan yang dihasilkan kernel saat proses booting dan operasi sistem. Informasi ini penting untuk mendiagnosa perangkat keras dan modul yang dimuat.

Identifikasi sistem (uname -a)
Perintah uname -a memberikan informasi lengkap tentang sistem operasi yang sedang berjalan, termasuk versi kernel, arsitektur CPU, dan tipe sistem (dalam hal ini WSL2 – Windows Subsystem for Linux versi 2)

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
hasil screenshot percobaan
<img width="1920" height="1078" alt="levi@LAPTOP-VEJOG5AI_ ~ 09_10_2025 21_18_19" src="https://github.com/user-attachments/assets/83db6c17-4d4a-4e56-93f2-7283cc7da899" />

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?

1. Makna Hasil Percobaan
Dari hasil perintah:
uname -a → menunjukkan informasi lengkap tentang sistem operasi, yaitu Linux kernel versi 6.6.87.2 yang berjalan pada WSL2 (Windows Subsystem for Linux). Ini berarti sistem Linux dijalankan secara virtual di atas sistem Windows.
lsmod → menampilkan daftar modul kernel yang sedang aktif. Modul seperti kvm_intel, battery, dan ac menunjukkan bahwa kernel memuat driver dan komponen yang mendukung fungsi virtualisasi dan perangkat keras tertentu.
dmesg → menampilkan log pesan kernel saat proses booting. Tercatat informasi seperti jenis CPU yang didukung (Intel, AMD), peta memori BIOS, serta konfigurasi awal sistem.
Makna dari hasil ini adalah bahwa kernel berfungsi dengan baik dalam mendeteksi perangkat keras virtual yang digunakan oleh WSL2 serta melakukan inisialisasi sumber daya sistem secara otomatis.

2. Hubungan dengan Teori
Fungsi Kernel: Kernel adalah inti sistem operasi yang mengatur interaksi antara perangkat keras dan perangkat lunak. Hasil dmesg menunjukkan aktivitas kernel saat mengelola CPU, memori, dan modul sistem.
System Call: Aplikasi pengguna tidak bisa langsung mengakses hardware, jadi mereka berkomunikasi dengan kernel melalui system call. Meskipun tidak terlihat langsung di output ini, system call adalah mekanisme yang memungkinkan perintah seperti lsmod dan dmesg mengakses data dari kernel.
Arsitektur OS: Berdasarkan hasil uname, sistem ini menggunakan arsitektur x86_64, yang menunjukkan bahwa OS berjalan pada arsitektur 64-bit. Selain itu, karena ini berjalan di WSL2, berarti kernel Linux dioperasikan dalam lingkungan virtual (microkernel-like) di atas Windows host.

3. Perbedaan Hasil di Lingkungan OS Berbeda (Linux vs Windows)
Aspek	Linux (Native)	Windows / WSL2
Kernel	Kernel asli Linux, berinteraksi langsung dengan hardware	Kernel Linux berjalan di atas hypervisor Windows (virtual layer)
System Call	Menggunakan system call table Linux secara langsung	System call diterjemahkan melalui WSL agar dapat berjalan di kernel virtual
Perintah dmesg dan lsmod	Menampilkan log kernel dan modul perangkat keras nyata	Menampilkan log dan modul virtual yang disimulasikan oleh WSL
Performa & Akses Hardware	Langsung ke hardware, performa lebih tinggi	Akses terbatas karena dijalankan melalui virtualisasi Windows

---

## Kesimpulan
Kernel berperan penting sebagai inti sistem operasi yang mengatur seluruh aktivitas antara perangkat keras dan perangkat lunak, termasuk pengelolaan sumber daya sistem.
Hasil percobaan menunjukkan bahwa Linux (dalam WSL2) menggunakan modul kernel yang dapat dimuat secara dinamis, serta mencatat proses booting dan konfigurasi perangkat melalui log kernel (dmesg).
Perintah seperti uname -a, lsmod, dan dmesg membantu pengguna memahami struktur, versi, dan aktivitas internal kernel, sehingga sangat berguna untuk analisis dan troubleshooting sistem operasi.

---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi. 
Manajemen Sumber Daya,Manajemen File dan Sistem,Antarmuka Pengguna
2. Jelaskan perbedaan antara keKernel Mode:
Akses penuh ke seluruh sistem.
Digunakan oleh sistem operasi.
Kesalahan bisa menyebabkan sistem crash.

User Mode:
Akses terbatas.
Digunakan oleh aplikasi pengguna.
Kesalahan hanya memengaruhi program, bukan seluruh sistem.rnel mode dan user mode.

3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.  
Monolithic Kernel:
Linux
MS-DOS
UNIX

Microkernel:
Minix
QNX
MacOS  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini = mencoba mengumpulkan tugas sebelum deadline
- Bagaimana cara Anda mengatasinya = mengerjakan dan tidak menunda nunda 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
