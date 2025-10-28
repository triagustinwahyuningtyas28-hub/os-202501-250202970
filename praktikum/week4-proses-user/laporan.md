

# Laporan Praktikum Minggu IV
Topik: Manajemen Proses dan User di Linux
---

## Identitas
- **Nama**  : MUHAMMAD REZA FAHLEVI  
- **NIM**   : 250202955  
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem. 

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
 ```bash
   whoami
   id
   groups
   ```*-    
 ```bash
     sudo adduser praktikan
     sudo passwd praktikan
 ```
 ```bash
   ps aux | head -10
   top -n 1
   ```
```bash
     sleep 1000 &
     ps aux | grep sleep
```
 ```bash
     kill <PID>
 ```
 ```bash
   pstree -p | head -20
 ```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
<img width="1920" height="1020" alt="levi@LAPTOP-VEJOG5AI_ ~ 28_10_2025 16_56_55" src="https://github.com/user-attachments/assets/cf867f22-2f53-47a6-be32-d775ed21193e" />
<img width="1920" height="1020" alt="levi@LAPTOP-VEJOG5AI_ ~ 28_10_2025 16_56_25" src="https://github.com/user-attachments/assets/b80d30a3-3752-4fa4-9d1d-ccdfc8fa34f5" />



---
## Eksperimen 1
Perintah whoami digunakan untuk menampilkan nama user yang sedang aktif atau login saat ini. Saat muncul output levi, artinya user yang sedang menjalankan terminal adalah levi. Ini berguna untuk memastikan kamu sedang memakai akun mana di sistem Linux, terutama kalau ada banyak user atau saat berpindah ke root.

Perintah groups menampilkan daftar semua grup yang diikuti oleh user tersebut. Output-nya menunjukkan bahwa user levi tergabung dalam beberapa grup seperti adm, sudo, audio, video, dan lainnya.
Setiap grup memberikan hak akses tertentu, misalnya:

adm untuk membaca log sistem.

sudo untuk menjalankan perintah dengan hak superuser (root).

audio untuk mengakses perangkat suara.

video untuk mengakses GPU atau perangkat grafis.

plugdev untuk menggunakan perangkat eksternal seperti USB tanpa perlu root.

netdev untuk mengelola jaringan.

users, dialout, cdrom, dan floppy adalah grup umum yang menambah kemampuan akses perangkat tertentu.

Artinya, user levi punya cukup banyak izin dan bisa menjalankan banyak fungsi sistem tanpa harus menjadi root sepenuhnya.

Perintah id menampilkan informasi identitas lengkap user dalam bentuk angka dan nama.
Output uid=1000(levi) berarti user ID milik levi adalah 1000, sementara gid=1000(levi) menunjukkan group ID utama juga bernilai 1000 dengan nama grup levi.
Bagian groups=... menampilkan semua grup yang diikuti user, lengkap dengan ID-nya, misalnya 27(sudo) artinya grup sudo memiliki ID 27.

Fungsinya untuk memeriksa identitas user serta semua hak akses yang dimilikinya, termasuk apakah user tersebut bisa menjalankan perintah administratif seperti sudo.


## Eksperimen 2
Perintah ps aux dan top sama-sama digunakan untuk melihat proses yang sedang berjalan di sistem Linux.
Bedanya:

ps aux menampilkan snapshot (cuplikan sesaat) dari semua proses.

top menampilkan tampilan dinamis (real-time) yang terus diperbarui.

Keduanya punya kolom-kolom yang hampir sama dan penting untuk memahami aktivitas sistem.

2. Penjelasan kolom penting pada ps aux dan top
USER

Menunjukkan nama user (pemilik) proses tersebut.
Contoh:

root → proses milik sistem (hak akses tertinggi).

levi → proses yang dijalankan oleh user biasa (dalam hal ini kamu).

systemd+, message+, syslog → akun khusus sistem untuk layanan tertentu.

PID (Process ID)

Merupakan nomor unik untuk setiap proses yang sedang berjalan.
Contoh:

levi         557  0.0  0.0   3124  1664 pts/0    S    16:27   0:00 sleep 1000


Di sini, 557 adalah PID dari proses sleep 1000.
Kalau ingin menghentikan proses tersebut, digunakan perintah:

kill 557


Makanya ketika kamu mengetik kill sleep, muncul error — karena kill butuh PID, bukan nama program.

%CPU

Menunjukkan persentase penggunaan CPU oleh proses tersebut.

Nilai 0.0 berarti proses tidak sedang memakai CPU (mungkin sedang sleeping).

Nilai besar (misalnya 80.0) berarti proses itu menggunakan 80% kapasitas CPU saat ini.

Contoh:

root           1  0.3  0.3  21700 12128 ?        Ss   16:22   0:00 /sbin/init


Angka 0.3 di kolom %CPU menunjukkan proses init menggunakan 0.3% CPU.

%MEM

Persentase penggunaan RAM (memori utama) oleh proses.
Nilai ini menunjukkan seberapa besar bagian dari RAM total digunakan oleh proses tersebut.
Misal:

0.4 → 0.4% dari total RAM dipakai oleh proses ini.


Jadi kalau RAM total 4 GB, maka proses memakai sekitar 16 MB.

VSZ (Virtual Memory Size)

Menunjukkan total ukuran memori virtual yang digunakan proses, dalam kilobyte (KB).
Termasuk RAM + memori yang bisa dialokasikan dari swap.
Contoh:

21700 → berarti 21,700 KB (sekitar 21 MB)

RSS (Resident Set Size)

Menunjukkan memori fisik (RAM nyata) yang sedang digunakan proses (juga dalam KB).
Contoh:

12128 → berarti 12,128 KB (~12 MB RAM)

COMMAND

Menampilkan nama program atau perintah yang dijalankan.
Contoh:

/sbin/init → proses utama sistem.

sleep 1000 → perintah untuk menunda selama 1000 detik.

grep sleep → proses mencari teks “sleep” di daftar proses.

3. Contoh interpretasi baris
levi         557  0.0  0.0   3124  1664 pts/0    S    16:27   0:00 sleep 1000

-
## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---
Tugas & Quiz
### Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.  
2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.  
3. Jelaskan hubungan antara user management dan keamanan sistem Linux.  
4. Upload laporan ke repositori Git tepat waktu.

---
### jawab
1.| Perintah       | Fungsi Utama                  | Keterangan                       |
| -------------- | ----------------------------- | -------------------------------- |
| `whoami`       | Mengetahui user aktif         | Menunjukkan identitas pengguna   |
| `groups`       | Menampilkan grup user         | Menentukan hak akses             |
| `id`           | Detail UID, GID, grup         | Identitas lengkap user           |
| `sudo adduser` | Menambah user baru            | Butuh hak root                   |
| `ps aux`       | Menampilkan semua proses      | Daftar lengkap proses sistem     |
| `head -10`     | Batasi output                 | Hanya 10 baris pertama           |
| `top -n 1`     | Monitor sistem                | Statistik CPU, memori, proses    |
| `sleep 1000 &` | Jalankan proses di background | Proses diam selama 1000 detik    |
| `grep sleep`   | Filter hasil ps               | Menyaring teks tertentu          |
| `kill PID`     | Hentikan proses               | Mengakhiri program dengan sinyal |
| `kill sleep`   | Salah format                  | Harus pakai PID                  |
| `slep`         | Salah ketik                   | Tidak dikenal oleh sistem        |



2.p<img width="1918" height="920" alt="diagram pohon" src="https://github.com/user-attachments/assets/5ffce68e-903e-43d4-8a87-f579aeda8844" />

3.User management memiliki peran penting dalam keamanan sistem Linux karena sistem ini berbasis pada konsep multi-user. Dengan pengelolaan user yang baik, administrator dapat mengatur siapa saja yang memiliki akses ke sistem, menentukan hak dan izin (permission) untuk setiap user maupun grup, serta membatasi tindakan yang dapat dilakukan oleh masing-masing pengguna. Hal ini membantu mencegah akses tidak sah, penyalahgunaan sumber daya, dan menjaga kerahasiaan, integritas, serta ketersediaan data dalam sistem Linux.

---

### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?
2. Apa perbedaan antara `kill` dan `killall`?  
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?

---


## jawab
1. Fungsi utama proses init / systemd

Berikut fungsi-fungsi pentingnya dalam sistem Linux:

a. Menginisialisasi sistem setelah boot
Setelah kernel selesai dimuat, init atau systemd langsung dijalankan oleh kernel (PID = 1).
Ia bertugas:
Menjalankan semua layanan (service) penting.
Mengatur urutan proses startup (misalnya jaringan, login, filesystem, dsb).
Menyiapkan lingkungan agar sistem siap digunakan.

b. Mengelola service (daemon)
systemd bertugas memulai, menghentikan, me-restart, dan memonitor layanan sistem, seperti:
networking.service (jaringan)
cron.service (penjadwalan tugas)
ssh.service (akses remote)
dbus.service (komunikasi antarproses)

2.kill

Perintah kill digunakan untuk mengirim sinyal ke proses berdasarkan PID (Process ID).
Biasanya dipakai untuk menghentikan satu proses tertentu yang kamu tahu ID-nya.

Contoh:
ps aux | grep sleep
levi     557  0.0  0.0   3124  1664 pts/0    S    16:27   0:00 sleep 1000
Untuk menghentikan proses di atas:
kill 557
Di sini angka 557 adalah PID proses sleep.

Fungsi dasar:
kill <PID> → Mengirim sinyal default SIGTERM (menghentikan proses dengan sopan).
kill -9 <PID> → Mengirim sinyal SIGKILL (mematikan paksa proses).

Ciri khas:
Butuh nomor PID, bukan nama program.
Hanya memengaruhi proses tertentu.

2. killall
Perintah killall digunakan untuk mengirim sinyal ke semua proses dengan nama yang sama.
Jadi, kamu tidak perlu tahu PID-nya — cukup tahu nama prosesnya.

Contoh:
killall sleep


Ini akan menghentikan semua proses yang bernama sleep di sistem.
Kalau ada 3 proses sleep yang sedang jalan, semuanya akan dihentikan sekaligus.

Fungsi dasar:
killall <nama_proses> → Mengirim SIGTERM ke semua proses bernama itu.
killall -9 <nama_proses> → Mengirim SIGKILL (paksa mati semua proses dengan nama itu).

Ciri khas:
Berdasarkan nama program (bukan PID).
Dapat menghentikan banyak proses sekaligus.
Lebih cepat untuk membunuh semua instance program.

3.User root memang punya posisi istimewa di sistem Linux — bisa dibilang raja dari semua user.
Yuk kita bahas secara lengkap biar jelas kenapa dia punya kekuasaan sebesar itu 👇

Siapa itu user root
User root adalah superuser atau administrator utama dalam sistem Linux.
Akun ini dibuat secara default ketika sistem diinstal dan memiliki hak penuh (full privilege) atas seluruh sistem operasi.

root memiliki:
UID (User ID) = 0
Nilai ini jadi tanda khusus bagi kernel bahwa user tersebut tidak dibatasi oleh aturan permission biasa.

2. Mengapa root punya hak istimewa
Karena Linux dirancang dengan model keamanan berbasis izin (permission-based security), setiap file dan proses punya aturan siapa yang boleh:
membaca (read),
menulis (write),
menjalankan (execute).

Nah, user biasa (levi, misalnya) hanya bisa mengakses file atau proses yang diizinkan oleh sistem.
Sedangkan root tidak dibatasi oleh aturan ini.

Alasannya:
Sistem butuh satu user yang bisa mengatur segalanya (misal: memperbaiki error, instal software, ubah konfigurasi sistem).
Kernel mengenali UID 0 sebagai otoritas tertinggi yang bisa melewati semua pembatasan permission.

3. Hak istimewa yang dimiliki root
User root bisa melakukan hal-hal yang user biasa tidak bisa lakukan, seperti:
Mengubah file sistem (misalnya /etc/passwd, /etc/shadow).
Menambah, menghapus, atau mengubah akun user lain.
Menginstal dan menghapus aplikasi sistem.
Mengatur dan memulai/berhenti service (systemctl, service, dll).
Mengubah permission dan kepemilikan file apa pun.
Mengakses semua direktori, bahkan yang dilindungi (/root, /boot, /etc).
Mengontrol semua proses, termasuk milik user lain.
Melakukan operasi jaringan tingkat rendah dan mengubah kernel setting.

4. Risiko dan alasan keamanan
Karena kekuasaan root tidak terbatas, dia juga sangat berbahaya jika disalahgunakan.

Contohnya:
Salah mengetik perintah rm -rf / bisa menghapus seluruh sistem.
Program berbahaya (malware) yang dijalankan sebagai root bisa mengambil alih sistem sepenuhnya.
Oleh karena itu, sistem Linux menganjurkan:
Tidak login langsung sebagai root, tapi gunakan sudo saat perlu.
sudo memberikan hak sementara, bukan permanen, sehingga lebih aman.

Contoh:
sudo apt update
Perintah di atas dijalankan dengan hak root hanya untuk saat itu saja.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
