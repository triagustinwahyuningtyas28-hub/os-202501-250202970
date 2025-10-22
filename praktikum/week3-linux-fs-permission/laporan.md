
# Laporan Praktikum Minggu [3]
Topik: Manajemen File dan Permission di Linux

---

## Identitas
- **Nama**  : Muhammad reza fahlevi
- **NIM**   : 250202955
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menggunakan perintah `ls`, `pwd`, `cd`, `cat` untuk navigasi file dan direktori.
2. Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.
---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari pengelolaan file dan direktori menggunakan perintah dasar Linux, serta konsep permission dan ownership.
Praktikum berfokus pada:

Navigasi sistem file dengan ls, pwd, cd, dan cat.
Pengaturan hak akses file menggunakan chmod.
Pengubahan kepemilikan file menggunakan chown.
Dokumentasi hasil eksekusi dan pengelolaan repositori praktikum.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
 ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
 ```bash
   cat /etc/passwd | head -n 5
   ```
```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
 ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```

---

## Hasil Eksekusi
screenshot hasil percobaan linux
<img width="1207" height="1032" alt="Screenshot 2025-10-22 140909" src="https://github.com/user-attachments/assets/54ee9d63-3edb-4cce-95f2-b4c88da5ae8e" />



---

## Analisis
- Jelaskan makna hasil percobaan.  
1. pwd
Artinya: Print Working Directory
Fungsi: Menampilkan lokasi direktori tempat kamu sedang berada.
Hasil di gambar:
/tmp
temp yaitu folder sementara (temporary directory) yang biasanya digunakan sistem atau program untuk menyimpan file sementara.

2.ls -l

Artinya: List (long format)
Fungsi: Menampilkan isi folder secara detail, termasuk hak akses, pemilik, grup, ukuran, dan waktu modifikasi.
Hasil di gambar:

drwx------ 2 root root 4096 Oct 21 15:18 snap-private-tmp
drwx------ 3 root root 4096 Oct 21 15:18 systemd-private-...-logind.service-FLd6gu
...


Penjelasan kolomnya:
drwx------ → tipe file dan hak akses:

d = directory
r = read
w = write
x = execute

root root → pemilik dan grup pemilik adalah root (administrator sistem).
4096 → ukuran direktori dalam byte.
Oct 21 15:18 → waktu terakhir dimodifikasi.
Nama folder di akhir adalah nama direktori dalam /tmp.

3. cd /tmp
Artinya: Change Directory ke /tmp.
Fungsi: Masuk atau berpindah ke direktori /tmp.
Hasil di gambar:
Tidak ada output — artinya perintah berhasil, dan kamu sekarang berada di dalam /tmp (yang sebenarnya sudah di situ sebelumnya, jadi ini tidak mengubah apa pun).

4. ls -a
Artinya: List all files
Fungsi: Menampilkan semua isi direktori, termasuk file atau folder tersembunyi (yang diawali dengan titik .).
Hasil di gambar:

.X11-unix  systemd-private-...  snap-private-tmp


Penjelasannya:
→ menunjuk ke direktori saat ini (/tmp itu sendiri).
→ menunjuk ke direktori induk (/, root).

.X11-unix → folder tersembunyi yang digunakan oleh sistem grafis X11.
systemd-private-* → folder sementara milik layanan systemd (misalnya logind, resolved, timesyncd, dll.).
snap-private-tmp → folder sementara untuk aplikasi yang dijalankan melalui Snap.

**Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).**

Format umum /etc/passwd
Setiap baris di file /etc/passwd punya 7 kolom yang dipisah dengan titik dua (:):
username:password:UID:GID:GECOS:home_directory:shell


Penjelasan kolom:
username — nama akun (login name).
password — biasanya berisi x yang berarti password disimpan terpisah di /etc/shadow. (Dulu hash disimpan di sini, tapi itu sudah tidak aman.)
UID — user ID (angka unik untuk user).
0 = root.
UID kecil (1–99/999) biasanya akun sistem.
UID ≥1000 biasanya user biasa.
GID — group ID utama user (angka), merujuk ke /etc/group.
GECOS — field informasi (biasanya nama lengkap, ruangan, telepon kerja, dll). Bisa kosong.
home_directory — path ke direktori home user.
shell — program shell/login yang dijalankan saat user login. Bisa berupa:
/bin/bash, /bin/sh → shell interaktif biasa
/usr/sbin/nologin atau /sbin/nologin → menolak login interaktif
program lain seperti /bin/sync → menjalankan program tersebut saat login (biasa untuk akun layanan khusus)
Contoh baris yang kamu tampilkan (dengan arti tiap field)
root:x:0:0:root:/root:/bin/bash

username: root
password: x (hash di /etc/shadow)
UID: 0 (superuser)
GID: 0 (group root)
GECOS: root
home: /root
shell: /bin/bash (root dapat login interaktif dengan bash)
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin

username: daemon
UID: 1 (akun sistem untuk daemon)
GID: 1
home: /usr/sbin (tidak untuk login user biasa)
shell: /usr/sbin/nologin (tidak mengizinkan login interaktif)
Digunakan oleh proses layanan yang tidak butuh shell login.
bin:x:2:2:bin:/bin:/usr/sbin/nologin

username: bin
UID: 2 (akun sistem tua, historis)
home: /bin
shell: /usr/sbin/nologin (tidak untuk login)
Biasanya akun ini hanya historis/untuk kepentingan sistem.
sys:x:3:3:sys:/dev:/usr/sbin/nologin

username: sys
UID: 3 (akun sistem)
home: /dev
shell: /usr/sbin/nologin
Juga akun sistem untuk tugas OS internal.
sync:x:4:65534:sync:/bin:/bin/sync

username: sync
UID: 4
GID: 65534 (seringkali nobody/non-privileged group)
home: /bin
shell: /bin/sync — kalau ada yang mencoba login ke akun sync, program /bin/sync akan dijalankan (menyinkronkan buffer ke disk) lalu keluar. Ini adalah akun utilitas khusus, bukan akun login normal.

---

## Kesimpulan
Dari hasil praktikum minggu ke-3 ini, dapat disimpulkan bahwa:
Navigasi sistem file di Linux dilakukan menggunakan perintah dasar seperti
pwd, ls, cd, dan cat yang berfungsi untuk mengetahui lokasi kerja, menampilkan isi direktori, berpindah folder, serta membaca isi file.
Dengan memahami ini, pengguna dapat bergerak dengan efisien di dalam struktur sistem Linux.

File /etc/passwd berisi informasi penting tentang akun pengguna dalam sistem, seperti username, UID, GID, direktori home, dan shell login.
Setiap baris mewakili satu akun user dengan 7 kolom yang dipisahkan tanda titik dua (:).
Manajemen permission (hak akses) menggunakan perintah chmod memungkinkan kita mengatur siapa yang boleh membaca (r), menulis (w), atau mengeksekusi (x) file/direktori.
Misalnya, chmod 600 memberi hak akses hanya kepada pemilik file (read & write saja).

Ownership (kepemilikan file) dapat diubah dengan perintah chown, misalnya sudo chown root file.txt menjadikan root sebagai pemilik file tersebut.
Hal ini penting untuk keamanan sistem agar file sensitif tidak dapat dimodifikasi oleh user biasa.
Secara keseluruhan, pemahaman terhadap file system dan permission di Linux adalah dasar penting dalam administrasi sistem karena berhubungan langsung dengan keamanan, privasi, dan stabilitas sistem operasi.

---

## Tugas


1. Dokumentasikan hasil seluruh perintah pada tabel observasi di laporan.md.
2. Jelaskan fungsi tiap perintah dan arti kolom permission (rwxr-xr--).
3. Analisis peran chmod dan chown dalam keamanan sistem Linux.
4. Upload hasil dan laporan ke repositori Git sebelum deadline.

**jawab**


1.

| **No** | **Perintah** | **Penjelasan Perintah** | **Hasil/Output** | **Kesimpulan / Analisis** |
| :----: | :------------ | :---------------------- | :---------------- | :------------------------- |
| 1 | `pwd` | Menampilkan direktori kerja saat ini (current directory). | `/home/levi` | Lokasi kerja aktif pengguna berada di direktori home milik user **levi**. |
| 2 | `ls -l` | Menampilkan daftar file secara detail (long listing format). | `-rw------- 1 root levi 24 Oct 21 16:37 percobaan.txt` | File `percobaan.txt` ada di direktori home dengan hak akses hanya untuk root. |
| 3 | `cd /tmp` | Berpindah ke direktori `/tmp`. | *(tidak ada output)* | Direktori aktif sekarang adalah `/tmp`. |
| 4 | `ls -a` | Menampilkan semua file, termasuk file tersembunyi. | `. .. .X11-unix snap-private-tmp systemd-private-...` | Berisi direktori sementara sistem dan beberapa folder service. |
| 5 | `cat /etc/passwd \| head -n 5` | Menampilkan 5 baris pertama dari file `/etc/passwd`. | Menampilkan informasi 5 akun sistem pertama: root, daemon, bin, sys, sync. | Menunjukkan struktur file `/etc/passwd` yang berisi informasi user sistem. |
| 6 | `echo "Hello <levi><250202955>" > percobaan.txt` | Menulis teks ke dalam file baru bernama `percobaan.txt`. | *(tidak ada output)* | File `percobaan.txt` berhasil dibuat di direktori `/tmp` dengan isi teks tersebut. |
| 7 | `ls -l percobaan.txt` | Menampilkan detail file `percobaan.txt`. | `-rw-r--r-- 1 levi levi 24 Oct 22 14:05 percobaan.txt` | File dimiliki oleh user dan grup **levi** dengan izin baca untuk semua orang. |
| 8 | `chmod 600 percobaan.txt` | Mengubah permission agar hanya owner yang bisa membaca dan menulis. | *(tidak ada output)* | Izin akses file kini hanya untuk user pemilik (read & write). |
| 9 | `ls -l percobaan.txt` | Mengecek ulang hak akses setelah `chmod`. | `-rw------- 1 levi levi 24 Oct 22 14:05 percobaan.txt` | Hak akses sudah berubah menjadi hanya untuk **levi**. |
| 10 | `sudo chown root percobaan.txt` | Mengubah kepemilikan file menjadi milik user **root**. | *(diminta password, lalu tidak ada output)* | Kepemilikan file berhasil diubah ke root. |
| 11 | `ls -l percobaan.txt` | Menampilkan kembali detail file setelah diubah owner-nya. | `-rw------- 1 root levi 24 Oct 22 14:05 percobaan.txt` | File sekarang dimiliki oleh **root** dengan grup **levi**, hak akses tetap hanya untuk owner. |

2. Fungsi Tiap Perintah

pwd → Menampilkan direktori kerja saat ini (print working directory).

ls -l → Menampilkan daftar file secara detail (izin akses, pemilik, ukuran, waktu, dsb).

cd /tmp → Berpindah ke direktori /tmp, tempat file sementara sistem disimpan.

ls -a → Menampilkan semua file termasuk file tersembunyi (yang diawali titik).

cat /etc/passwd → Menampilkan isi file /etc/passwd yang berisi data akun pengguna sistem.

head -n 5 → Menampilkan lima baris pertama dari hasil keluaran perintah sebelumnya.

echo "teks" > file.txt → Menulis teks ke dalam file, membuat file baru jika belum ada.

chmod 600 file.txt → Mengubah izin akses file agar hanya pemilik dapat membaca dan menulis.

chown root file.txt → Mengubah pemilik file menjadi user root (administrator sistem).

sudo → Menjalankan perintah dengan hak akses superuser (administrator).

ls -l file.txt → Menampilkan detail file untuk memeriksa hasil perubahan izin dan kepemilikan.

3. Peran chmod dalam Keamanan Sistem

Perintah chmod (change mode) berfungsi untuk mengatur izin akses (permission) terhadap file atau direktori.
Tujuannya adalah untuk membatasi siapa saja yang dapat membaca, menulis, atau mengeksekusi file di dalam sistem.

---

## Quiz
1. Apa fungsi dari perintah `chmod`? 
   **Kata CHMOD adalah singkatan dari CHange MODe, atau terjemahan bebasnya adalah merubah mode**  
2. Apa arti dari kode permission `rwxr-xr--`?  
   **rwx r-xr-x) mewakili izin yang telah ditetapkan kepada pemilik berkas.**  
3. Jelaskan perbedaan antara `chown` dan `chmod`.  
   **perintah chmod digunakan untuk mengatur hak akses, sedangkan perintah chown digunakan untuk mengatur kepemilikan.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? = Memahami struktur sistem Linux
- Bagaimana cara Anda mengatasinya?  = dengan cara belajar otodidak bersama teman teman

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
