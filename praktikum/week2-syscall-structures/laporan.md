
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
Resolusi dan buka file
openat(AT_FDCWD, "/etc/passwd", O_RDONLY|O_CLOEXEC)
glibc modern biasanya memanggil openat (bukan open) dengan AT_FDCWD (artinya relatif ke current working directory, tetapi path absolut dipakai jadi sama efeknya).
Flags umum: O_RDONLY (baca saja) dan sering O_CLOEXEC (auto-tutup saat exec berikutnya).
Kernel: lakukan lookup path melalui VFS — dentry lookup untuk setiap komponen path, cek permission (mode dan ACL), dapatkan inode dan file structure.
Jika sukses, kernel mengembalikan file descriptor (contoh: 3) ke proses.
Membaca isi file
read(3, buf, 4096)
Proses memanggil read pada fd yang dikembalikan (3).
Kernel memproses read lewat VFS: cek file->f_op->read_iter (opsi implementasi file system).
Page cache: kernel dulu cek page cache. Jika halaman ada → data di-copy_to_user dari cache. Jika tidak ada → kernel meng-issue I/O blok ke disk (readpages), blok dibaca ke page cache lalu disalin ke buffer pengguna.
Return value = jumlah byte yang berhasil dikembalikan (>0). Untuk file kecil seperti /etc/passwd biasanya satu read mengembalikan seluruh isi (mis. 512 bytes).
Ketika sampai akhir file (EOF), read mengembalikan 0.
Menulis ke stdout
write(1, buf, n)
stdout. Jika stdout adalah terminal/pty, data dikirim ke driver pty/TTY, yang menaruh data ke buffer pty dan akhirnya tampil di layar. Jika stdout dialihkan ke file, data masuk ke page cache file yang dituju.
Kernel mengembalikan jumlah byte tertulis. Untuk perangkat karakter (tty) penulisan biasanya non-blok atau blok tergantung buffer/flow control.
Loop sampai EOF
Program (cat) biasanya membaca dalam loop: read → write → ulang sampai read mengembalikan 0.
Menutup file
close(3)
Kernel akan menutup FD: mengurangi counter referensi pada file struct. Jika ini referensi terakhir, file->f_op->release/inode/blob mungkin dipanggil; resources dilepas. close mengembalikan 0 bila sukses.  

---

## Kesimpulan
Kesimpulan Praktikum:

Interaksi user–kernel terjadi melalui system call.
Perintah cat /etc/passwd menggunakan system call open, read, write, dan close untuk meminta layanan kernel dalam membuka, membaca, menampilkan, lalu menutup file.

Kernel mengelola akses file secara aman dan efisien.
Kernel memeriksa izin akses saat membuka file, membaca data melalui mekanisme page cache, dan mengirimkan hasilnya ke stdout tanpa memberikan akses langsung ke perangkat keras.

System call menunjukkan alur dasar operasi file di Linux.
Urutan open → read → write → close mencerminkan proses standar yang dilakukan hampir semua program saat bekerja dengan file di sistem operasi berbasis UNIX.

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?
   Adalah sebagai penghubung antara program dan kernel agar program bisa memakai layanan sistem (seperti file, memori, dan proses) dengan aman dan terkontrol tanpa langsung mengakses perangkat keras.
2. Sebutkan 4 kategori system call yang umum digunakan.
   Manajemen proses, manajemen file, manajemen perangkat, pemeliharaan informasi,
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
   System call tidak bisa dipanggil langsung oleh user program karena alasan keamanan dan stabilitas sistem operasi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini = menjelskan fungsi system call (strace dll)
- Bagaimana cara Anda mengatasinya? = berdiskusi sesama teman yang sudah paham.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
