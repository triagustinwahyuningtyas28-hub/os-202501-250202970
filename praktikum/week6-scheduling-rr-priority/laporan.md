
# Laporan Praktikum Minggu [6]
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Muhammad Reza Fahlevi  
- **NIM**   : 250202955  
- **Kelas** : 1 IKRA

---

## Tujuan

1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.  

---

## Dasar Teori

- **Round Robin (RR)**  
- **Priority Scheduling**

Kedua algoritma ini banyak digunakan pada sistem modern karena mempertimbangkan **keadilan waktu eksekusi (time quantum)** dan **tingkat prioritas proses**.  
Mahasiswa akan melakukan simulasi perhitungan manual untuk menghitung *waiting time* dan *turnaround time*, serta menganalisis efek perbedaan *time quantum* dan prioritas terhadap performa CPU scheduling.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
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
### Tugas
1. Hitung *waiting time* dan *turnaround time* untuk algoritma RR dan Priority.  
2. Sajikan hasil perhitungan dan Gantt Chart dalam `laporan.md`.  
3. Bandingkan performa dan jelaskan pengaruh *time quantum* serta prioritas.  
4. Simpan semua bukti (tabel, grafik, atau gambar) ke folder `screenshots/`

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?
   
Perbedaan utama antara Round Robin dan Priority Scheduling terletak pada cara menentukan urutan eksekusi proses. Round Robin menggunakan sistem pembagian waktu secara bergiliran dengan jatah waktu (time quantum) yang sama untuk setiap proses, sehingga lebih menekankan pada keadilan dan cocok untuk sistem time-sharing. Sementara itu, Priority Scheduling menentukan urutan eksekusi berdasarkan tingkat prioritas, di mana proses dengan prioritas lebih tinggi akan dijalankan terlebih dahulu, sehingga lebih menekankan pada kepentingan tugas daripada keadilan waktu. 
2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?

Besar atau kecilnya time quantum sangat memengaruhi performa sistem. Jika time quantum terlalu kecil, sistem akan sering melakukan pergantian proses (context switching), yang menyebabkan beban kerja prosesor meningkat dan efisiensi menurun. Sebaliknya, jika time quantum terlalu besar, maka sistem akan cenderung seperti algoritma FCFS, di mana proses yang lama bisa membuat proses lain menunggu terlalu lama. Jadi, time quantum harus dipilih seimbang agar sistem tetap responsif tanpa terlalu banyak overhead.
3. Mengapa algoritma Priority dapat menyebabkan *starvation*?
   
Algoritma Priority dapat menyebabkan starvation karena proses dengan prioritas rendah bisa terus tertunda eksekusinya jika selalu ada proses dengan prioritas lebih tinggi yang datang. Akibatnya, proses berprioritas rendah mungkin tidak pernah mendapat giliran untuk dijalankan. Hal ini terjadi karena CPU selalu memilih proses dengan prioritas tertinggi terlebih dahulu tanpa batas waktu bagi proses lainnya.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
