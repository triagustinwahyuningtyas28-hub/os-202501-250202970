
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
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

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
<img width="1919" height="1036" alt="Screenshot 2025-10-21 152652" src="https://github.com/user-attachments/assets/8e5e5caf-8d5b-4440-ab89-a1c340fcc92a" />


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
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Tugas


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
- Apa bagian yang paling menantang minggu ini? =Memahami struktur sistem Linux
- Bagaimana cara Anda mengatasinya?  = dengan cara belajar otodidak bersama teman teman

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
