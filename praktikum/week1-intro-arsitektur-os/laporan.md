
# Laporan Praktikum Minggu [1]
Topik: Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas
- **NIM**   : 250202970
- **Kelas** : 1IKRA

---

## Tujuan
Fungsi Utama Sistem Operasi
Sistem operasi (OS) adalah perangkat lunak sistem yang mengatur perangkat keras komputer dan menyediakan layanan umum untuk program aplikasi.
Fungsi utamanya meliputi:
Manajemen Proses
Menjalankan, menjadwalkan, dan menghentikan proses.
Contoh:
multitasking dan manajemen CPU time.
Manajemen Memori
Mengatur alokasi dan dealokasi memori untuk proses.Menyediakan memori virtual.
Manajemen Penyimpanan
Mengatur penyimpanan file dan direktori di disk.Sistem file seperti EXT4, NTFS, FAT32.
Manajemen Perangkat (Device Management)
Mengelola komunikasi antara perangkat keras dan sistem.Menggunakan driver perangkat.
Antarmuka Pengguna.CLI (Command Line Interface) seperti Bash, atau GUI (Graphical User Interface).

Peran Kernel
Kernel adalah inti dari sistem operasi. Ia bertanggung jawab atas komunikasi langsung antara perangkat keras dan perangkat lunak. Beberapa peran utamanya:
Mengelola CPU, memori,dan perangkat keras lainnya.
Menjalankan proses dan thread.
Menyediakan sistem file dan keamanan.
Menangani interupsi dan trap.
Mengatur konteks switching antar proses.
Di WSL2 (Windows Subsystem for Linux 2), kernel yang digunakan adalah kernel Linux nyata yang berjalan dalam virtual machine ringan di Windows.

System Call adalah antarmuka yang digunakan oleh program pengguna untuk berinteraksi dengan kernel.

Contoh umum system call:
read(), write() – untuk I/O file
fork() – untuk membuat proses baru
exec() – untuk menjalankan program
open(), close() – untuk membuka/menutup file
kill() – untuk mengirim sinyal ke proses
Di WSL2, system call dari program Linux diteruskan ke kernel Linux virtual.

---

## Dasar Teori
Sistem Operasi sebagai Pengelola Sumber Daya
Sistem operasi bertugas mengelola sumber daya perangkat keras seperti CPU, memori, dan perangkat I/O. Dalam percobaan ini, perintah seperti uname -a dan dmesg digunakan untuk melihat informasi kernel dan proses inisialisasi sistem operasi.

Kernel sebagai Inti Sistem Operasi
Kernel adalah bagian utama sistem operasi yang langsung berinteraksi dengan perangkat keras. Kernel Linux pada WSL2 bertanggung jawab atas manajemen proses, memori, dan perangkat. Modul kernel yang dimuat dapat dilihat melalui perintah lsmod.

Peran System Call
System call adalah antarmuka antara program aplikasi dan kernel. Saat pengguna menjalankan perintah di shell (misalnya whoami, lsmod, dmesg), program memanggil system call yang diteruskan ke kernel untuk dieksekusi.

Modularitas Kernel
Linux menggunakan kernel modular yang memungkinkan pemuatan dan pembongkaran modul perangkat keras secara dinamis. Ini terlihat pada daftar modul seperti kvm, intel_rapl_msr, dan lainnya yang dimuat saat sistem berjalan.

WSL2 sebagai Lingkungan Virtualisasi
Percobaan dilakukan di lingkungan WSL2, yang memungkinkan sistem operasi Linux berjalan di dalam Windows menggunakan virtualisasi ringan. Ini memungkinkan pengguna mengakses fitur kernel Linux tanpa harus melakukan dual-boot atau instalasi terpisah.

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
hasil percobaan wsl
<img width="1920" height="1128" alt="tyas@LAPTOP-N04BD9QM_ ~ 10_10_2025 17_36_44" src="https://github.com/user-attachments/assets/e0621fc8-25d8-446f-bf8a-705e93116af9" />

---

## Analisis
Makna Hasil Percobaan
Hasil percobaan menunjukkan bahwa:
Sistem operasi Linux yang berjalan di atas WSL2 (Windows Subsystem for Linux 2) tetap memiliki fungsi kernel yang lengkap dan aktif.

Perintah seperti uname -a, lsmod, dan dmesg mengungkapkan informasi kernel, modul kernel yang dimuat, dan log booting.
Ini menunjukkan bahwa meskipun Linux berjalan dalam lingkungan virtual (di dalam Windows), ia tetap berfungsi seolah-olah berada di perangkat keras asli, termasuk pengelolaan CPU, memori, dan perangkat lainnya.

Hubungan Hasil dengan Teori
Fungsi Kernel
Kernel bertugas menangani manajemen perangkat keras, memori, dan proses.
Dalam hasil percobaan, kita melihat kernel mengenali CPU (Intel GenuineIntel, AMD AuthenticAMD) dan menyusun peta memori (RAM map) yang dibaca dari BIOS (dmesg output).
Modul-modul seperti kvm, intel_rapl_msr menunjukkan kernel bersifat modular dan dapat menyesuaikan dengan kebutuhan sistem.

System Call
Perintah yang dijalankan (whoami, uname, dll.) memanfaatkan system call untuk berinteraksi dengan kernel.
Contohnya, whoami menggunakan system call untuk mengakses informasi pengguna dari sistem.

Arsitektur Sistem Operasi
Linux menganut arsitektur monolitik di mana seluruh fungsi kernel dijalankan dalam satu ruang alamat (termasuk manajemen perangkat).
Dalam WSL2, arsitektur ini dijalankan di atas Windows melalui virtualisasi, yang tetap mempertahankan arsitektur Linux seutuhnya.

Perbedaan Hasil di Lingkungan OS yang Berbeda (Linux vs Windows)
Aspek	Linux (Asli / WSL2)	Windows
Kernel	Terlihat secara langsung, bisa dimodifikasi	Tertutup (closed-source), tidak dapat diakses langsung
System Call	Dapat diamati dan dimanfaatkan melalui tools CLI	Tidak terlihat langsung, API berbasis Win32
Modul Kernel	Bisa dimuat/diturunkan (via lsmod, modprobe)	Tidak tersedia secara terbuka untuk user
CLI Tools	Native di Linux (dmesg, lsmod, dll.)	Harus pakai PowerShell/CMD dan terbatas
Virtualisasi / Subsystem	WSL2 memungkinkan menjalankan kernel Linux di Windows	Tidak ada fitur serupa native di Linux  

---

## Kesimpulan
Sistem operasi Linux melalui WSL2 dapat diakses dan dianalisis untuk memahami fungsi dasar kernel, seperti manajemen modul, inisialisasi sistem, dan interaksi perangkat keras, tanpa perlu instalasi Linux secara langsung.

Kernel Linux berperan penting dalam mengelola sumber daya sistem dan menjalankan instruksi dasar, yang dapat diamati melalui log sistem (dmesg) dan modul yang dimuat (lsmod), menunjukkan bagaimana sistem mendeteksi dan mengatur perangkat keras secara dinamis.

Perintah-perintah shell seperti uname, whoami, lsmod, dan dmesg memberikan wawasan langsung tentang cara kerja internal sistem operasi, sehingga mendukung pemahaman konsep-konsep penting seperti system call, kernel, dan manajemen perangkat.

---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi.
   Manajemen Proses,Manajemen Memori,Manajemen Perangkat
2. Jelaskan perbedaan antara kernel mode dan user mode. 
   Dalam mode kernel, perangkat lunak dan aplikasi memiliki lebih banyak hak istimewa untuk mengakses sumber daya sistem        seperti RAM atau perangkat keras. Dalam mode pengguna, perangkat lunak dan aplikasi memiliki hak istimewa yang relatif       lebih sedikit untuk mengakses sumber daya sistem seperti RAM atau perangkat keras
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.
   Arsitektur Monolithic:
   Linux (Ubuntu, Debian, Fedora, dll.)
   MS-DOS
   Unix klasik (BSD awal)

   Arsitektur Microkernel
   MINIX
   QNX
   GNU Hurd
   L4 Microkernel

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini = terkendala saat login akun git.
- Bagaimana cara Anda mengatasinya = Saya cek ulang username dan password, lalu cari solusi di internet,dan bertanya kepada   teman yang sudah bisa

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
