
# Laporan Praktikum Minggu [3]
Topik: Manajemen File dan Permission di Linux

---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas
- **NIM**   : 250202970
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
Tujuan utama dari praktikum ini adalah agar mahasiswa mampu mengoperasikan perintah Linux dasar dengan benar, memahami sistem izin (permission), dan mendokumentasikan hasilnya dalam format laporan Git.

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
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
screenshot hasil linux
<img width="1920" height="1128" alt="tyas@LAPTOP-N04BD9QM_ ~ 10_10_2025 17_36_44" src="https://github.com/user-attachments/assets/c1c45346-d78b-4e11-b829-f6cf71d6581f" />


---

## Analisis
**Analisis perbedaan sebelum dan sesudah chmod.**
Sebelum chmod 600 percobaan.txt
Perintah:
ls -l percobaan.txt


Output:
-rw-r--r-- 1 tyas tyas 24 Oct 21 17:34 percobaan.txt
Analisis izin (permission):
-rw-r--r--
r = read (baca)
w = write (tulis)
x = execute (eksekusi)

Rinciannya:
Owner (tyas): rw- → bisa membaca dan menulis
Group (tyas): r-- → hanya membaca
Others (pengguna lain): r-- → hanya membaca
Artinya: File ini dapat dibaca oleh semua pengguna, tetapi hanya pemilik yang bisa mengubah isinya.

Sesudah chmod 600 percobaan.txt
Perintah:
chmod 600 percobaan.txt
ls -l percobaan.txt


Output:
-rw------- 1 tyas tyas 24 Oct 21 17:34 percobaan.txt
Analisis izin (permission):
-rw-------
Owner (tyas): rw- → bisa membaca dan menulis
Group: --- → tidak ada izin
Others: --- → tidak ada izin

Artinya: Hanya pemilik file (tyas) yang dapat membaca dan menulis file tersebut. Pengguna lain tidak dapat melihat atau mengakses isi file sama sekali.


:

1. pwd

Kepanjangan: print working directory
Fungsi: Menampilkan lokasi (path) direktori tempat kamu sedang bekerja sekarang.

Contoh hasil:
tyas@LAPTOP-N04BD9QM:~$ pwd
/home/tyas

Artinya kamu sedang berada di direktori /home/tyas.

2. ls -l
Kepanjangan: list (long format)
Fungsi: Menampilkan daftar isi direktori saat ini dengan informasi lengkap, seperti:
hak akses (permission)
jumlah link
pemilik (owner)
grup
ukuran file
waktu terakhir diubah
nama file/direktori
Contoh hasil:
-rw-r--r-- 1 tyas tyas  24 Oct 21 17:34 percobaan.txt
drwxr-xr-x 2 tyas tyas 4096 Oct 21 16:00 Documents

| Kolom           | Arti                  |
| --------------- | --------------------- |
| `-rw-r--r--`    | Izin akses file       |
| `1`             | Jumlah link ke file   |
| `tyas`          | Pemilik file          |
| `tyas`          | Grup pemilik          |
| `24`            | Ukuran file (byte)    |
| `Oct 21 17:34`  | Waktu terakhir diubah |
| `percobaan.txt` | Nama file             |


3. cd /tmp
Kepanjangan: change directory
Fungsi: Berpindah ke direktori lain, dalam hal ini ke /tmp.
Hasil:
tyas@LAPTOP-N04BD9QM:/tmp$
Artinya kamu sekarang berada di direktori /tmp, yaitu folder sementara (temporary folder) yang digunakan oleh sistem dan program untuk menyimpan file sementara.

4. ls -a
Kepanjangan: list all
Fungsi: Menampilkan semua file dan folder, termasuk file tersembunyi (hidden files).
File tersembunyi biasanya diawali dengan titik (.).

Contoh hasil:
percobaan.txt  .bashrc  .profile


Keterangan:
→ direktori saat ini (current directory)
→ direktori induk (parent directory)

bashrc, .profile → file konfigurasi tersembunyi


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa fungsi dari perintah `chmod`?
  **kata CHMOD adalah singkata dari change MODe, atau terjemahan bebasnya adalah merubah mode** 
2. Apa arti dari kode permission `rwxr-xr--`?
   **rwx r-xr-x) mewakili izin yang telah ditetapkan kepada pemilik berkas.** 
3. Jelaskan perbedaan antara `chown` dan `chmod`.
   **perintah chmod digunakan untuk mengatur hak akses, sedangkan perintah chown digunakan untuk mengatur kepemilikan.**

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  = memahami struktur sistem linux
- Bagaimana cara Anda mengatasinya?  = mencari tau struktur sistem linux dan bertanya kepada teman 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
