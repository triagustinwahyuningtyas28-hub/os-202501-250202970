
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
Perintah linux untuk menampilkan system call adalah strace.Strace ini juga berfungsi untuk menganalisis system call

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
Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.


1) Buka file

Contoh baris strace yang muncul:
openat(AT_FDCWD, "/etc/passwd", O_RDONLY) = 3
Proses (cat) meminta kernel membuka path /etc/passwd — modern strace biasanya menampilkan openat bukan open.
Flag O_RDONLY berarti hanya baca. Kernel mencari inode lewat VFS (virtual file system).
Kernel mengembalikan file descriptor (FD), mis. 3 — angka kecil di atas 0..2 (stdin/stdout/stderr).
Peran kernel: memeriksa hak akses, mengikat FD ke struktur file internal (struct file), dan menghubungkannya ke inode dan offset awal (0).

2) Membaca isi file (loop baca sampai EOF)

Contoh baris berulang:
read(3, "root:x:0:0:root:/root:/bin/bash\n...", 4096) = 204
read(3, ..., 4096) = 0

cat memanggil read(fd, buf, size) berulang — umumnya ukuran buffer adalah 4096 (atau nilai lain) tergantung implementasi libc.
Kernel mengisi buffer dengan data dari page cache (jika sudah ada) atau dari disk jika belum cached.
Setiap panggilan read mengembalikan jumlah byte yang berhasil dibaca. Ketika read mengembalikan 0 artinya EOF (tidak ada data lagi).
Peran kernel: mengelola offset file (menambah offset sesuai byte yang dibaca), memetakan data dari storage ke memori (page cache), dan memastikan akses aman sesuai permission.

3) Menulis ke stdout

write(1, "root:x:0:0:root:/root:/bin/bash\n...", 204) = 204
Setelah mendapat data, cat memanggil write(1, buf, n) untuk menyalurkan ke file descriptor 1 (stdout).
Kernel menyalin data dari buffer proses ke buffer kernel/driver yang mengelola tty atau pipe — akhirnya data muncul di terminal atau dialirkan ke program lain.
Peran kernel: menyalin data antar ruang proses dan perangkat/pipe, mengatur blocking/non-blocking tergantung mode.

4) Menutup file

close(3) = 0
Ketika cat selesai, ia memanggil close(fd). Kernel mengurangi referensi ke struktur file, jika tidak ada referensi lagi maka resource dilepas.
close memastikan flush metadata bila perlu (walau untuk read-only tidak ada tulis yang harus di-flush).
Peran kernel: membersihkan descriptor, mengurangi refcount internal, melepaskan struktur yang terkait.

Ringkasan — poin penting (2–3 kalimat)
open/openat meminta kernel mengikat path ke struktur file dan mengembalikan file descriptor (mis. 3).
read dipanggil dalam loop; kernel mengembalikan blok data (dari page cache atau disk) sampai read mengembalikan 0 → EOF.
write mengirim data ke stdout (FD 1); close melepaskan FD dan resource kernel.

Catatan tambahan berguna
Anda mungkin juga melihat read/write dengan ukuran berbeda (libc atau implementasi cat menentukan buffer).
Jika cat /etc/passwd dijalankan lewat pipe, kernel mengatur pipe buffer; jika output ke terminal, kernel mengirim ke driver TTY.
Untuk melihat juga pemanggilan stat atau open lain (mis. akses symlink, permisos), jalankan strace -e trace=file atau tanpa filter.

Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

1️ Output strace menampilkan aktivitas kernel (system call).
strace tidak menunjukkan hasil program (seperti isi /etc/passwd),
melainkan log interaksi antara program dan kernel.

Baris seperti:
openat(AT_FDCWD, "/etc/passwd", O_RDONLY) = 3
read(3, "root:x:0:0:root:/root:/bin/bash\n", 4096) = 204
write(1, "root:x:0:0:root:/root:/bin/bash\n", 204) = 204
close(3) = 0
adalah panggilan sistem yang terjadi di level kernel.

2️ Output program biasa (cat /etc/passwd) menampilkan hasil akhir ke user.
Tanpa strace, yang muncul di layar hanyalah isi file /etc/passwd, misalnya:
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...


3️ Jadi perbedaan utamanya:
Aspek	Output strace	Output program biasa (cat /etc/passwd)
Isi	Log aktivitas system call antara user space ↔ kernel	Data atau teks hasil eksekusi program
Level	Level kernel (debug, teknis)	Level user (hasil akhir yang ditampilkan)
Tujuan	Untuk analisis bagaimana program bekerja di dalam kernel	Untuk penggunaan normal, menampilkan isi file
Contoh	open(), read(), write(), close()	Isi file /etc/passwd

| Aspek                      | Log Kernel (`dmesg`, `/var/log/kern.log`)                                        | Output Program Biasa (mis. `printf`, `ls`, `cat`)   |
| -------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------- |
| **Sumber Output**          | Kernel (kernel space)                                                            | Aplikasi pengguna (user space)                      |
| **Isi Informasi**          | Aktivitas sistem: inisialisasi driver, error hardware, system call, boot message | Hasil proses logika program, data keluaran pengguna |
| **Akses dan Hak Istimewa** | Membutuhkan hak root atau akses khusus untuk melihat/modifikasi                  | Dapat dijalankan oleh user biasa                    |
| **Media Tampilan**         | Melalui `dmesg`, file log sistem (`/var/log/`)                                   | Langsung tampil di terminal atau GUI                |
| **Tujuan**                 | Debugging sistem, pemantauan kinerja kernel, keamanan                            | Memberi hasil/output program untuk pengguna         |
| **Contoh Output**          | `[1234.567890] usb 1-2: new USB device detected`                                 | `Hello World`, `File ditemukan: data.txt`           |



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
**Jawaban:** Fungsi utama system call adalah sebagai penghubung antara program dan kernel agar program bisa memakai layanan sistem (seperti file, memori, dan proses) dengan aman dan terkontrol tanpa langsung mengakses perangkat keras.
2. Sebutkan 4 kategori system call yang umum digunakan.
   **Jawaban:** Katagori system call yang umum digunakan adalah manajemen proses, manajemen file, manajemen perangkat, pemeliharaan informasi.
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
   **Jawaban:** System call tidak bisa dipanggil langsung oleh user program karena alasan keamanan dan stabilitas sistem operasi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini = menjelskan fungsi system call (strace dll)
- Bagaimana cara Anda mengatasinya? = berdiskusi sesama teman yang sudah paham.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
