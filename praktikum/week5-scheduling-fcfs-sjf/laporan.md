# Laporan Praktikum Minggu V
Topik: Scheduling FCFS dan FJS

---

## Identitas
- **Nama**  : Muhammad Reza Fahlevi  
- **NIM**   : 250202955
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.  

---

## Dasar Teori
1. FCFS (First Come First Served)

   - Konsep dasar: Proses yang datang lebih dulu akan dieksekusi lebih dulu, seperti antrian di loket — prinsipnya first in, first out (FIFO).

   - Sederhana & mudah diimplementasikan, karena proses dijadwalkan berdasarkan urutan waktu kedatangan (arrival time).

   - Tidak adil untuk proses pendek, karena proses dengan burst time kecil bisa menunggu lama di belakang proses besar (convoy effect).

   - Tidak preemptive, artinya proses yang sedang berjalan tidak bisa dihentikan sampai selesai.

   - Kinerja baik untuk beban kerja seragam, tapi kurang efisien untuk campuran proses panjang dan pendek.

2. SJF (Shortest Job First)

   - Konsep dasar: Proses dengan waktu eksekusi (burst time) paling pendek dieksekusi lebih dulu untuk meminimalkan waktu tunggu rata-rata.

   -  Tujuan utama: Menghasilkan rata-rata waiting time dan turnaround time paling kecil dibanding FCFS.

   - Dapat bersifat non-preemptive (sekali jalan sampai selesai) atau preemptive (dikenal sebagai Shortest Remaining Time First).

   - Butuh prediksi burst time, sehingga implementasinya sulit pada sistem nyata tanpa informasi tambahan.

   - Optimal secara teori, tetapi bisa menyebabkan starvation bagi proses panjang jika banyak proses pendek datang terus-menerus.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

| Proses | Burst Time | Arrival Time | Star Time | Finis Time |WT | TAT|
   |:--:|:--:|:--:|:--:|:--:|:--:|:--:|
   | P1 | 6 | 0 | 0 | 6 | 0 | 6 |
   | P2 | 8 | 1 | 6 | 14 | 5 | 13 |
   | P3 | 7 | 2 | 14 | 21 | 12 | 19 |
   | P4 | 3 | 3 | 21 | 24 | 18 | 21 |

   rata-rata Waiting Time (WT) = 8,75

   rata-rata Turnaround Time (TAT) = 14,75

   Gantt Chart:

    | P1 | P2 | P3 | P4 |
     0    6    14   21   24

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  

| Proses | Burst Time | Arrival Time | Star Time | Finis Time |WT | TAT|
   |:--:|:--:|:--:|:--:|:--:|:--:|:--:|
   | P4 | 3 | 3 | 3 | 6 | 0 | 3 |
   | P1 | 6 | 0 | 6  | 12  | 6  |  12 |
   | P3 | 7 | 2 | 12 | 19 | 10 | 17 |
   | P2 | 8 | 1 | 19  | 27 | 18  | 26 |
   
   rata-rata Waiting Time (WT) = 8,5
   rata-rata Turnaround Time (TAT) = 14,5

Gantt Chart:

    | P1 | P2 | P3 | P4 |
     0    6    12   19   27

   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | 8,5 | 14,5 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |



4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan. 

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
   ```

---

## Hasil Eksekusi

---

## Analisis
   1. Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   2. Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   3. Tambahkan kesimpulan singkat di akhir laporan. 

**JAWBAN**
 
1. RATA RATA  FCFS 
- rata-rata Waiting Time (WT) = 8,75
- rata-rata Turnaround Time (TAT) = 14,75

RATA RATA FJS
- rata-rata Waiting Time (WT) = 8,5
- rata-rata Turnaround Time (TAT) = 14,5
2. - SJF lebih unggul dari FCFS ketika:

- Waktu eksekusi (burst time) setiap proses sudah diketahui atau dapat diperkirakan dengan baik.
Karena SJF memilih proses dengan waktu terpendek, algoritma ini dapat meminimalkan waktu tunggu rata-rata dan meningkatkan efisiensi CPU.

- Proses-proses yang datang memiliki variasi burst time yang besar.
Dalam kondisi ini, SJF mampu menyelesaikan proses-proses kecil dengan cepat, sehingga total waktu tunggu keseluruhan menjadi jauh lebih kecil dibanding FCFS.

- Lingkungan sistem bersifat batch (non-interaktif).
Pada sistem batch, semua proses sudah diketahui di awal, sehingga mudah menentukan urutan yang paling efisien dengan SJF.

   - FCFS lebih unggul dari SJF ketika:

- Waktu kedatangan proses tidak dapat diprediksi dan burst time sulit diketahui.
FCFS tidak memerlukan perkiraan waktu eksekusi, jadi lebih sederhana dan mudah diterapkan dalam kondisi nyata.

- Lingkungan sistem bersifat interaktif atau multitasking.
Dalam sistem seperti ini, FCFS lebih adil karena setiap proses dilayani berdasarkan urutan datangnya, tanpa menunda proses panjang terlalu lama.

- Tujuan utama adalah keadilan, bukan efisiensi.
FCFS memastikan semua proses mendapat giliran secara berurutan, sehingga tidak terjadi starvation seperti pada SJF.

---

## Kesimpulan

Algoritma FCFS (First Come First Served) bekerja berdasarkan urutan kedatangan proses, sehingga mudah diterapkan dan adil, tetapi dapat menyebabkan waktu tunggu lama jika ada proses berdurasi panjang di awal. Sedangkan SJF (Shortest Job First) memilih proses dengan waktu eksekusi paling singkat terlebih dahulu, sehingga lebih efisien dan menghasilkan waktu tunggu rata-rata lebih kecil, namun sulit diterapkan karena membutuhkan perkiraan waktu proses dan dapat menyebabkan proses panjang tertunda (starvation).

---

## D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.  
2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).  
3. Analisis kelebihan dan kelemahan tiap algoritma.  
4. Simpan seluruh hasil dan analisis ke `laporan.md`.  

**JAWABAN**

1. 

2. di eksperimen 2.

3. 1. FCFS (First Come First Served)

Kelebihan:

Sederhana dan mudah diimplementasikan.

Adil karena setiap proses dilayani sesuai urutan kedatangan.

Kelemahan:

Dapat menyebabkan convoy effect, yaitu proses pendek harus menunggu proses panjang selesai.

Waktu tunggu rata-rata bisa menjadi tinggi jika proses pertama berdurasi lama.

2. SJF (Shortest Job First)

Kelebihan:

Memberikan waktu tunggu rata-rata paling rendah dibanding algoritma lain.

Efisien dalam pemanfaatan CPU karena proses singkat segera selesai.

Kelemahan:

Sulit diterapkan karena waktu eksekusi proses sering tidak diketahui sebelumnya.

Bisa menyebabkan starvation, di mana proses panjang tidak mendapat giliran karena selalu didahului proses pendek.

### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa perbedaan utama antara FCFS dan SJF?  
2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?  
3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?  


**JAWABAN**
1. Perbedaan utama antara FCFS dan SJF adalah cara menentukan urutan proses. FCFS menjalankan proses berdasarkan urutan kedatangan, sedangkan SJF menjalankan proses dengan waktu eksekusi paling singkat terlebih dahulu. FCFS lebih sederhana tapi bisa menyebabkan proses lama menunggu, sementara SJF lebih efisien namun sulit diterapkan jika waktu eksekusi tidak diketahui.

2. SJF dapat menghasilkan rata-rata waktu tunggu minimum karena proses dengan waktu eksekusi paling singkat dijalankan lebih dulu. Dengan begitu, proses-proses kecil cepat selesai dan tidak menunggu proses panjang, sehingga total waktu tunggu semua proses menjadi lebih rendah dibanding algoritma lain.

3. Kelemahan SJF pada sistem interaktif adalah sulitnya memperkirakan waktu eksekusi setiap proses, karena proses di sistem interaktif sering berubah-ubah dan tidak dapat diprediksi. Selain itu, SJF bisa membuat proses yang membutuhkan waktu lama terus tertunda (starvation), karena selalu didahului oleh proses yang lebih pendek.



---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?   sulit Mencari nilai star time dan finis time pada FCFS dan SJF pada awal praktikum 
- Bagaimana cara Anda mengatasinya? dengan cara  mencari materi di berbagai website dan Ai,kemudian saya mempelajari dan memahami materi yang saya cari di web site dan Ai .
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
