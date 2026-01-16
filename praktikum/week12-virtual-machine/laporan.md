
# Laporan Praktikum Minggu [XII]
Topik: Virtualisasi Menggunakan Virtual Machine
---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas
- **NIM**   : 250202970
- **Kelas** : 1IKRA

---

## Tujuan
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).  
2. Membuat dan menjalankan sistem operasi guest di dalam VM.  
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).  
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.  
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Instalasi Virtual Machine**
   - Instal VirtualBox atau VMware pada komputer host.  
   - Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

2. **Pembuatan OS Guest**
   - Buat VM baru dan pilih OS guest (misal: Ubuntu Linux).  
   - Atur resource awal:
     - CPU: 1–2 core  
     - RAM: 2–4 GB  
     - Storage: ≥ 20 GB

3. **Instalasi Sistem Operasi**
   - Jalankan proses instalasi OS guest sampai selesai.  
   - Pastikan OS guest dapat login dan berjalan normal.

4. **Konfigurasi Resource**
   - Ubah konfigurasi CPU dan RAM.  
   - Amati perbedaan performa sebelum dan sesudah perubahan resource.

5. **Analisis Proteksi OS**
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  
   - Kaitkan dengan konsep *sandboxing* dan *hardening* OS.

6. **Dokumentasi**
   - Ambil screenshot setiap tahap penting.  
   - Simpan di folder `screenshots/`.

7. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
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
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Tugas & Quiz
### Tugas
1. Instal dan jalankan OS guest menggunakan VM.  
2. Konfigurasikan resource VM sesuai instruksi.  
3. Dokumentasikan proses instalasi dan konfigurasi.  
4. Tulis laporan praktikum pada `laporan.md`.

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Apa perbedaan antara host OS dan guest OS?
 **Jawaban:**  Host OS adalah sistem operasi utama yang terpasang langsung di hardware dan mengelola seluruh sumber daya komputer.
Guest OS adalah sistem operasi yang berjalan di dalam mesin virtual, menggunakan sumber daya yang dialokasikan oleh Host OS.
Contoh:
- Windows di laptop = Host OS
- Ubuntu yang dijalankan lewat VirtualBox = Guest OS

2. Apa peran hypervisor dalam virtualisasi?
 **Jawaban:**  Hypervisor berperan sebagai pengelola virtualisasi yang memungkinkan beberapa Guest OS berjalan secara bersamaan di satu komputer fisik.
   
  Peran utama hypervisor:
- Mengalokasikan dan mengatur CPU, RAM, dan storage untuk tiap mesin virtual
- Menjadi perantara antara hardware dan Guest OS
-Menjaga isolasi agar satu mesin virtual tidak mengganggu yang lain

3. Mengapa virtualisasi meningkatkan keamanan sistem?
 **Jawaban:**     Virtualisasi meningkatkan keamanan sistem karena:
- Isolasi lingkungan → Setiap mesin virtual terpisah, sehingga serangan atau error di satu VM tidak langsung memengaruhi sistem lain.
- Pembatasan akses → Guest OS tidak memiliki akses langsung ke hardware, sehingga risiko penyalahgunaan lebih kecil.
- Pemulihan cepat → Jika sistem terinfeksi atau rusak, VM bisa dikembalikan dengan snapshot tanpa mengganggu Host OS.
- Pengujian aman → Aplikasi atau konfigurasi berisiko dapat diuji di VM tanpa membahayakan sistem utama.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
