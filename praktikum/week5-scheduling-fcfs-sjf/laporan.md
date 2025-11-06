
# Laporan Praktikum Minggu [5]
Topik:  Penjadwalan CPU – FCFS dan SJF 

---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas  
- **NIM**   : 250202970
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  

1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.


---

## Dasar Teori
FCFS (First-Come, First-Served):

-Prinsip dasar: Proses dieksekusi sesuai urutan kedatangan ke CPU; proses yang datang lebih dahulu akan dijalankan lebih dulu.

-Non-preemptive: Sekali CPU diberikan ke suatu proses, proses tersebut berjalan sampai selesai sebelum proses lain dijalankan.

-Sederhana: Implementasinya mudah, tetapi bisa menyebabkan konvoi effect jika proses panjang datang lebih dulu.

-Waktu tunggu: Waktu tunggu rata-rata bisa tinggi jika variasi durasi proses besar.

SJF (Shortest Job First):

-Prinsip dasar: Proses dengan burst time terpendek dijalankan lebih dulu untuk meminimalkan waktu tunggu.

-Non-preemptive atau preemptive (SRTF): Versi klasik non-preemptive, versi preemptive disebut Shortest Remaining Time First (SRTF).

-Efisiensi: Dapat menghasilkan waktu tunggu rata-rata minimum dibanding FCFS.

-Kelemahan: Sulit memprediksi burst time proses; bisa menyebabkan starvation bagi proses panjang.

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

**JAWABAN**
1. rata rata FCFS 
   - rata-rata Waiting Time (WT) = 8,75
   - rata-rata Turnaround Time (TAT) = 14,75

rata rata SJF
   - rata-rata Waiting Time (WT) = 8,5
   - rata-rata Turnaround Time (TAT) = 14,5

2. SJF (Shortest Job First) lebih unggul dari FCFS (First Come First Served) ketika waktu eksekusi tiap proses bervariasi dan dapat diprediksi, karena SJF memprioritaskan proses dengan waktu paling singkat, sehingga:

Rata-rata waktu tunggu dan waktu penyelesaian jadi lebih kecil.

Sistem menjadi lebih efisien untuk beban kerja batch atau non-interaktif.

Sebaliknya, FCFS lebih unggul dari SJF saat:

Semua proses memiliki waktu eksekusi yang mirip atau hampir sama,

Sistem bersifat interaktif atau real-time, karena FCFS lebih adil — setiap proses dilayani sesuai urutan datang tanpa menunggu proses lain selesai lebih dulu.



---

## Kesimpulan
FCFS dan SJF FCFS bekerja dengan mengeksekusi proses berdasarkan urutan kedatangan, sehingga mudah diterapkan namun dapat menimbulkan waktu tunggu yang lama bagi proses yang datang belakangan. Sebaliknya, algoritma SJF memberikan kinerja yang lebih efisien karena proses dengan waktu eksekusi paling singkat dijalankan terlebih dahulu, menghasilkan rata-rata waktu tunggu yang lebih rendah. Namun, penerapan SJF memiliki kelemahan pada sistem interaktif karena sulit memperkirakan lama eksekusi proses dan dapat menyebabkan proses berdurasi panjang tertunda atau mengalami starvation.

---

### D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.  
2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).  
3. Analisis kelebihan dan kelemahan tiap algoritma.  
4. Simpan seluruh hasil dan analisis ke `laporan.md`.  

**JAWABAN**

1. BB

<img width="1287" height="630" alt="Screenshot 2025-11-06 180158" src="https://github.com/user-attachments/assets/4fdd6f8f-5653-4fe5-8e5d-cfbec81afe5a" />

 
2.
| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
| SJF | 8,5 | 14,5 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

3. FCFS (First Come First Served)

Kelebihan: Sederhana, adil berdasarkan urutan datang, dan mudah diterapkan.

Kelemahan: Menyebabkan convoy effect, waktu tunggu lama, dan tidak cocok untuk sistem interaktif.

SJF (Shortest Job First)

Kelebihan: Waktu tunggu rata-rata kecil, efisien, dan throughput tinggi.

Kelemahan: Sulit tahu waktu proses, bisa terjadi starvation, dan tidak cocok untuk sistem real-time.


### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa perbedaan utama antara FCFS dan SJF?  
2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?  
3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?

**JAWABAN**

1.FCFS menjalankan proses berdasarkan urutan kedatangan — siapa datang dulu, dia yang diproses dulu.

SJF menjalankan proses berdasarkan waktu eksekusi paling pendek — proses dengan durasi terpendek dieksekusi lebih dulu, tanpa melihat kapan datangnya.

2.Proses yang cepat selesai dieksekusi lebih dulu, sehingga tidak membuat proses singkat menunggu lama di belakang proses yang panjang.

Dengan begitu, total waktu tunggu semua proses menjadi lebih kecil, karena proses-proses pendek tidak tertunda oleh proses panjang.

3.SJF tidak cocok untuk sistem interaktif karena algoritma ini lebih memprioritaskan proses dengan waktu eksekusi pendek, sehingga proses yang lebih panjang bisa tertunda terus-menerus (starvation). Selain itu, pada sistem interaktif sulit untuk mengetahui waktu eksekusi proses secara pasti di awal, sehingga penjadwalan tidak bisa dilakukan dengan akurat.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  Kurang memahami penggunaan excel dalam menghitung rata-rata.
- Bagaimana cara Anda mengatasinya? Mencari penjelasan di internet.  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
