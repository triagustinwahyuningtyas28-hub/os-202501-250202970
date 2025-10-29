
# Laporan Praktikum Minggu [4]
Topik: Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas
- **NIM**   : 250202970  
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.
   

---

## Dasar Teori
1. User dan Identitas di Linux
Linux merupakan sistem operasi multi-user, artinya lebih dari satu pengguna dapat menggunakan sistem secara bersamaan. Untuk membedakan setiap pengguna, Linux menggunakan User ID (UID) dan Group ID (GID).

Seorang user adalah entitas yang memiliki akun dan dapat menjalankan perintah di sistem. Setiap user memiliki nama pengguna (username), UID, direktori home pribadi, serta shell yang digunakan untuk menjalankan perintah (misalnya bash).

Sementara itu, group digunakan untuk mengelompokkan beberapa user agar lebih mudah mengatur hak akses. Setiap user memiliki satu grup utama (primary group) dan bisa menjadi anggota dari beberapa grup tambahan (supplementary groups). Melalui sistem grup ini, administrator dapat memberikan atau membatasi izin terhadap file, perangkat, dan program tertentu.

Hak akses pada sistem Linux dibagi menjadi tiga kategori, yaitu owner (pemilik file), group (grup pengguna), dan others (pengguna lain). Setiap kategori bisa diberi izin untuk membaca (read), menulis (write), dan menjalankan (execute) suatu file.

2. Perintah Dasar untuk Manajemen User
Perintah whoami digunakan untuk menampilkan nama user yang sedang login di sistem. Ini berguna untuk memastikan identitas user yang sedang aktif, terutama ketika bekerja dengan banyak akun atau hak akses berbeda.

Perintah id digunakan untuk menampilkan informasi detail tentang user, seperti UID, GID, dan daftar grup yang diikuti. Dengan perintah ini, kita bisa mengetahui hak akses dan keanggotaan grup seorang user.

Perintah groups menampilkan nama-nama grup yang diikuti oleh user secara ringkas. Fungsinya sama seperti id, namun hanya menampilkan nama grup tanpa ID-nya.

3. Konsep Proses di Linux
Proses adalah program yang sedang berjalan di memori. Setiap proses memiliki PID (Process ID), yaitu nomor unik yang digunakan oleh sistem untuk mengenalinya. Linux dapat menjalankan banyak proses secara bersamaan karena mendukung konsep multitasking.

Proses di Linux dapat berjalan di dua mode, yaitu foreground dan background. Proses foreground berjalan langsung di terminal dan menahan input hingga selesai, sedangkan proses background berjalan di belakang layar, sehingga terminal tetap bisa digunakan untuk perintah lain. Simbol & di akhir perintah digunakan untuk menjalankan proses di background.

4. Pemantauan Proses
Untuk melihat proses yang sedang berjalan, digunakan perintah ps. Versi lengkapnya, ps aux, menampilkan semua proses dari seluruh user beserta informasi detailnya. Output dari perintah ini mencakup nama user yang menjalankan proses, PID, persentase penggunaan CPU dan memori, terminal tempat proses berjalan, status proses, serta nama perintah yang dijalankan.

Status proses ditunjukkan dalam kolom STAT, misalnya huruf S berarti “sleeping” atau proses sedang menunggu, sedangkan R berarti “running” atau sedang aktif menggunakan CPU.

Untuk memfilter proses tertentu, digunakan perintah grep, contohnya ps aux | grep sleep, yang akan menampilkan hanya proses yang mengandung kata “sleep”.

Jika ingin menghentikan proses, dapat digunakan perintah kill diikuti dengan nomor PID dari proses tersebut.

5. Manajemen Proses Latar Belakang
Proses yang dijalankan di background dapat dilihat menggunakan perintah jobs. Jika ingin mengembalikannya ke foreground, digunakan perintah fg. Mekanisme ini memungkinkan pengguna menjalankan banyak proses sekaligus tanpa harus menunggu satu per satu selesai.

---

## Langkah Praktikum
Setup Environment

Sistem: Linux (Ubuntu/WSL)
User login: non-root

Folder kerja:
praktikum/week4-proses-user/
Eksperimen 1 – Identitas User
Perintah dan penjelasan:

whoami

Output: tyas
Fungsi: Menampilkan nama user yang sedang aktif.
Berguna untuk memastikan identity user saat bekerja di sistem.

id
Output: uid=1000(tyas) gid=1000(tyas) groups=1000(tyas),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users)
Fungsi: Menunjukkan UID, GID, dan grup user, membantu mengetahui hak akses user.

groups


Output: tyas adm cdrom sudo dip plugdev users
Fungsi: Menampilkan grup yang diikuti user secara ringkas.

Menambahkan user baru:
sudo adduser praktikan
sudo passwd praktikan

Uji login ke user baru: memastikan user dapat login dengan password yang telah dibuat.

Eksperimen 2 – Monitoring Proses

Perintah:
ps aux | head -10
top -n 1


Kolom penting:
USER → user yang menjalankan proses
PID → ID unik proses, bisa digunakan untuk kill
%CPU → penggunaan CPU oleh proses
%MEM → penggunaan RAM oleh proses
COMMAND → perintah/proses yang berjalan
STAT → status proses (S=sleeping, R=running, dll.)

Contoh proses background:
sleep 1000 &
ps aux | grep sleep


Menghentikan proses:
kill <PID>

Eksperimen 3 – Analisis Hierarki Proses

Perintah:
pstree -p | head -20

Fungsi: Menampilkan pohon proses dan hierarki parent-child.
Catatan: Proses induk utama adalah init atau systemd (PID 1), yang mengatur seluruh proses lainnya.

Analisis
Hasil percobaan menunjukkan bahwa kernel Linux mengelola proses dan user melalui system call.
sleep 1000 & berjalan di background sehingga terminal tetap responsif.
User management menentukan hak akses: user biasa terbatas, root memiliki hak penuh.

Perbedaan dengan Windows: Linux memiliki sistem user dan permission yang lebih granular, sementara Windows menggunakan kombinasi user account dan ACL.

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
<img width="959" height="537" alt="2" src="https://github.com/user-attachments/assets/9a377c3f-aa51-4756-b68b-430980b7cc01" />
<img width="959" height="539" alt="3" src="https://github.com/user-attachments/assets/3a62e00e-299d-499e-b62d-926aa70344c2" />


---

## Eksperimen 1
1. Perintah: whoami
Output:
tyas


Penjelasan:
whoami menampilkan nama user saat ini yang sedang login di terminal.
Di sini, user yang sedang aktif adalah tyas.

Fungsi:
Berguna untuk memastikan identity user saat bekerja di sistem Linux, terutama ketika user memiliki hak akses berbeda.
Perintah: id

Output:
uid=1000(tyas) gid=1000(tyas) groups=1000(tyas),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users)


Penjelasan per bagian:
uid=1000(tyas) → UID (User ID) adalah 1000, mewakili user tyas. UID digunakan sistem untuk mengidentifikasi user secara unik.
gid=1000(tyas) → GID (Group ID) utama adalah 1000, juga bernama tyas. GID ini adalah grup utama user.
groups=1000(tyas),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users) → Daftar grup yang diikuti user ini:
tyas (1000) → grup utama user.
adm (4) → grup untuk user yang dapat melihat log sistem.
cdrom (24) → grup untuk akses ke perangkat CD-ROM.
sudo (27) → grup untuk user yang boleh menjalankan perintah dengan hak istimewa root menggunakan sudo.
dip (30) → grup untuk akses koneksi dial-up atau PPP (biasanya jaringan).
plugdev (46) → grup untuk akses perangkat USB atau perangkat plug-in lainnya.
users (100) → grup umum untuk user biasa di sistem.

Fungsi:
id membantu melihat UID, GID, dan grup user untuk mengetahui hak akses apa saja yang dimiliki user.

Perintah: groups

Output:
tyas adm cdrom sudo dip plugdev users


Penjelasan:
Menampilkan nama-nama grup yang diikuti user tyas.
Sama dengan daftar grup di output id, tapi lebih ringkas, hanya menampilkan nama grup tanpa ID.

Fungsi:
Memudahkan melihat hak akses grup yang dimiliki user untuk mengakses file, perangkat, dan menjalankan perintah tertentu.

---

## Eksperimen 2
Ketika kamu menjalankan ps aux, setiap baris mewakili satu proses yang berjalan di sistem. Misalnya:
tyas         474  0.0  0.0   3124  1664 pts/0    S    18:45   0:00 sleep 1000
USER (tyas) → Menunjukkan siapa yang menjalankan proses ini. Dalam kasus ini, user biasa tyas.
PID (474) → Nomor unik proses. Bisa digunakan untuk mengontrol proses, misalnya kill 474 untuk menghentikannya.
%CPU (0.0) → Persentase CPU yang digunakan proses. 0.0 artinya proses hampir tidak membebani CPU.
%MEM (0.0) → Persentase RAM yang digunakan. 0.0 berarti sangat sedikit memori yang dipakai.
COMMAND (sleep 1000) → Nama perintah atau proses yang dijalankan. Di sini sleep menunggu selama 1000 detik.
STAT (S) → Status proses. S berarti sleeping, yaitu proses menunggu dan tidak aktif di CPU.

Saat kamu menjalankan sleep 1000 &, proses berjalan di background, sehingga terminal tetap bisa digunakan untuk perintah lain. Lalu ps aux | grep sleep menampilkan proses itu dengan informasinya, termasuk PID dan statusnya.

---

## Analisis
- Jelaskan makna hasil percobaan.  
 Praktikum ini membahas manajemen user dan proses di Linux. User mengeksplorasi perintah seperti whoami, id, dan groups untuk mengenali identitas serta hak aksesnya, lalu membuat user baru dan menguji login. Pada monitoring proses, digunakan ps aux dan top untuk melihat daftar serta penggunaan sumber daya sistem.

---

## Kesimpulan
Sistem Linux mengatur user dan proses secara terpisah namun saling berkaitan. User management digunakan untuk mengontrol siapa yang dapat mengakses sistem dan sumber daya, sedangkan process management berfungsi mengatur program apa saja yang sedang dijalankan dan bagaimana sistem mengalokasikan sumber dayanya.

Pemahaman tentang perintah seperti whoami, id, groups, dan ps aux sangat penting karena menjadi dasar dalam mengenali identitas pengguna serta memantau aktivitas proses di sistem Linux.

---

### Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.

2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.
   ![WhatsApp Image 2025-10-28 at 18 37 38](https://github.com/user-attachments/assets/1c5ae767-f24d-4cc2-b9e6-0898b722d3c1)


3. Jelaskan hubungan antara user management dan keamanan sistem Linux.
   
Kontrol Akses
Melalui user management, administrator dapat menentukan siapa yang boleh mengakses sistem dan sejauh mana hak aksesnya.
Setiap user memiliki akun dan password sendiri, sehingga hanya pengguna yang sah yang bisa masuk.

Pemisahan Hak Akses (Privilege Separation)
Sistem Linux membedakan antara user biasa dan user dengan hak istimewa (root).
Dengan membatasi hak istimewa, risiko kerusakan sistem atau penyalahgunaan dapat diminimalkan.

Manajemen File dan Permission
User management bekerja bersama sistem izin file (read, write, execute) untuk memastikan hanya user yang berhak dapat mengakses atau mengubah data tertentu.

Audit dan Monitoring Aktivitas
Setiap user memiliki riwayat aktivitas yang bisa dilacak. Hal ini penting untuk mendeteksi aktivitas mencurigakan atau pelanggaran keamanan.
 
5. Upload laporan ke repositori Git tepat waktu.

## Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?

jawab:Fungsi dari proses init atau systemd dalam sistem Linux adalah sebagai proses pertama (PID 1) yang dijalankan setelah kernel selesai melakukan booting.
-Menginisialisasi sistem: memulai semua proses penting setelah booting.
-Menjalankan layanan (services): seperti network, login, cron, dan lainnya.
-Mengatur urutan startup: menentukan layanan mana yang dijalankan lebih dulu.
-Mengelola proses dan shutdown: memastikan proses dihentikan dengan benar saat sistem dimatikan atau di-restart.

2. Apa perbedaan antara `kill` dan `killall`?

jawab:
Perbedaan utama antara kill dan killall adalah:
kill → Menghentikan proses berdasarkan PID (Process ID).
Contoh: kill 1234 akan menghentikan proses dengan PID 1234.
killall → Menghentikan semua proses dengan nama tertentu.
Contoh: killall firefox akan menghentikan semua proses bernama firefox.

3. Mengapa user `root` memiliki hak istimewa di sistem Linux?

jawab:
Administrator sistem (superuser) root adalah akun yang memiliki kendali penuh atas seluruh sistem — dapat mengakses, mengubah, atau menghapus semua file   dan konfigurasi, termasuk milik user lain.
Tidak ada batasan izin (permission)
Akun root tidak terikat oleh aturan izin file (rwx). Ia bisa membaca, menulis, dan mengeksekusi file apa pun di sistem.
Diperlukan untuk tugas sistem penting
Hanya root yang bisa melakukan operasi seperti:
Menginstal atau menghapus paket sistem
Mengelola user dan grup
Mengubah konfigurasi kernel dan jaringan
Mem-boot atau mematikan sistem
Didesain untuk keamanan dan kontrol
Dengan memusatkan hak tertinggi hanya pada satu akun (root), Linux dapat membatasi potensi kerusakan akibat kesalahan user biasa atau serangan dari luar.

---


## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
