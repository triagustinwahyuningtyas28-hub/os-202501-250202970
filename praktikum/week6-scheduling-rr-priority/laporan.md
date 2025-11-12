

# Laporan Praktikum Minggu [VI]
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas  
- **NIM**   : 250202970
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
- Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
- Menyusun tabel hasil perhitungan dengan benar dan sistematis.
- Membandingkan performa algoritma RR dan Priority.
- Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
- Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori

Round Robin adalah algoritma penjadwalan CPU yang menggunakan sistem antrian melingkar, di mana setiap proses mendapat jatah waktu eksekusi tetap (time quantum). Setelah jatah waktu habis, proses akan dihentikan sementara dan dikembalikan ke akhir antrian, lalu CPU diberikan ke proses berikutnya.


RR termasuk algoritma preemptive scheduling karena proses dapat dihentikan sebelum selesai ketika time quantum-nya habis. Mekanisme ini memastikan bahwa tidak ada satu proses pun yang mendominasi CPU terlalu lama.


Algoritma ini dianggap paling adil dibandingkan algoritma lainnya karena semua proses mendapatkan kesempatan yang sama untuk dieksekusi. Tidak ada proses yang diabaikan atau didahulukan berdasarkan ukuran atau prioritas tertentu.


Kinerja RR sangat bergantung pada besar kecilnya time quantum. Jika terlalu kecil, sistem akan sering melakukan context switching sehingga efisiensi menurun. Sebaliknya, jika terlalu besar, respons terhadap proses interaktif menjadi lambat.


Round Robin paling cocok digunakan pada sistem time-sharing dan lingkungan interaktif, karena mampu memberikan respon cepat terhadap banyak proses secara bergantian, menjaga keseimbangan antara efisiensi CPU dan kenyamanan pengguna.

---

## Langkah Praktikum
1. langkah-langkah yang digunakan.
2. perintah yang dijalankan.
3. file dan kode yang dibuat.
4. commit message yang digunakan.

---

## kode / perintah
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

   | Proses |   CT   | Arivaal| TAT(ct-at) |	WT(TAT-bt) |
   | :----: | :----: | :----: | :--------: | :--------: |
   |   P1   |	 14   |    0   |	14-0=14   |	14-5=9     |
   |   P2   |   6 	|    1	|  6-1=5	    | 5-3=2      |
   |   P3	|   22   |	  2   |	22-2=20   |	20-8=12    |
   |   P4	|   20   |    3	|  20-3=17   |	17-6=11    |
Rata rata TAT:14
Rata rata WT :8,5

   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
     0    3    6    9   12   14   17   20   22
     ```
   - Catat sisa *burst time* tiap putaran.
   
   | waktu | Brust | sisa waktu|
   |:-----:|:-----:|:---------:|
   | 0-3   | 5-3=0 | P1 sisa 2 |
   | 3-6   | 3-3=0 | 2 selesai |
   | 6-9   | 8-3=5 | P3 sisa 5 |
   | 9-12  | 6-3=3 | P4 sisa 3 |
   | 12-14 | 2 < 3 | P1 selesai|
   | 14-17 | 5-3=0 | P3 sisa 2 |
   | 17-20 | 3-3=0 | P4 selesai|
   | 20-22 | 2 < 3 | P3 selesai|
   

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]o
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

|Proses|	BT | AT |PRIO|	ST |	WT(ST-AT)	|TAT(WT+BT)|
|:----:|:--:|:--:|:--:|:--:|:------------:|:--------:|
|  P1  |	 5 | 0  |  2 |	0  |	   0        | 	  5     |
|  P2  |	 3 | 1  |  1 |	5  | 	   4        |	  7     |
|  P4  |	 6 | 3  |  3 |	8  |	   5        |	  11    |
|  P3  |	 8 | 2  |  4 |	14 |     12       |    20    |

Rata rata WT  :5,25
Rata rata TAT :10,75

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  

Quantum 2
|Proses|	CT | AT |BT | TAT | WT |
|:----:|:--:|:--:|:-:|:---:|:--:|
|  P1  |	18 |  0 | 5 |	18 |  13|
|  P2  |	13 |	1 | 3 |	12 |	9 |
|  P3  |	24 |	2 | 8 |	22 |	14|
|  P4  |	22 |  3 | 6 |	19 |	13|
|Rata-rata  |    |   ||17.75|12.25|

Quantum 5
|Proses|	CT | AT |BT | TAT | WT |
|:----:|:--:|:--:|:-:|:---:|:--:|
|  P1  |	5  |  0 | 5 |	5  |  0 |
|  P2  |	8  |	1 | 3 |	7  |	4 |
|  P3  |	21 |	2 | 8 |	19 |	11|
|  P4  |	22 |  3 | 6 |	19 |	13|
|Rata-rata  |    |  || 12.5|  7 |




   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | 8,5 | 14 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | 5,25 | 10,75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

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
Algoritma Round Robin (RR) memberikan waktu tunggu (waiting time) dan waktu penyelesaian (turnaround time) yang relatif lebih tinggi dibandingkan Priority Scheduling. Hal ini karena RR membagi CPU secara merata kepada semua proses, sehingga proses panjang dan pendek mendapat perlakuan yang sama.

Nilai time quantum sangat memengaruhi performa RR.
Saat quantum kecil (misal 2), sistem menjadi lebih responsif, tetapi context switching meningkat dan efisiensi menurun.

Saat quantum besar (misal 5), efisiensi meningkat namun respons terhadap proses interaktif menurun.
Algoritma Priority Scheduling lebih efisien dalam total waktu eksekusi, karena proses dengan prioritas tinggi dijalankan terlebih dahulu. Namun, kekurangannya adalah potensi starvation bagi proses dengan prioritas rendah.

Secara umum, RR unggul dalam keadilan dan respon cepat, sedangkan Priority unggul dalam efisiensi dan pengaturan kepentingan proses.

---

## Kesimpulan
- Algoritma Round Robin (RR) cocok digunakan pada sistem interaktif karena memberikan pembagian waktu CPU yang adil bagi semua proses.

- Priority Scheduling lebih efisien untuk proses-proses penting, tetapi berpotensi menyebabkan starvation jika prioritas tidak diatur dengan baik.

- Besar kecilnya time quantum berpengaruh besar terhadap performa sistem: quantum yang terlalu kecil menurunkan efisiensi, sedangkan yang terlalu besar menurunkan responsivitas.
---

## Tugas & Quiz

**Tugas**
1. Hitung waiting time dan turnaround time untuk algoritma RR dan Priority.
2. Sajikan hasil perhitungan dan Gantt Chart dalam laporan.md.
3. Bandingkan performa dan jelaskan pengaruh time quantum serta prioritas.
4. Simpan semua bukti (tabel, grafik, atau gambar) ke folder screenshots/.


WT dan TAT RR dan Prioriry
WT dan TAT RR dan Priority

Round Robin
   | Proses |   CT   | Arivaal| TAT(ct-at) |	WT(TAT-bt) |
   | :----: | :----: | :----: | :--------: | :--------: |
   |   P1   |	 14   |    0   |	14-0=14   |	14-5=9     |
   |   P2   |   6 	|    1	|  6-1=5	    | 5-3=2      |
   |   P3	|   22   |	  2   |	22-2=20   |	20-8=12    |
   |   P4	|   20   |    3	|  20-3=17   |	17-6=11    |
Rata rata TAT:14
Rata rata WT :8,5

Priority
|Proses|	BT | AT |PRIO|	ST |	WT(ST-AT)	|TAT(WT+BT)|
|:----:|:--:|:--:|:--:|:--:|:------------:|:--------:|
|  P1  |	 5 | 0  |  2 |	0  |	   0        | 	  5     |
|  P2  |	 3 | 1  |  1 |	5  | 	   4        |	  7     |
|  P4  |	 6 | 3  |  3 |	8  |	   5        |	  11    |
|  P3  |	 8 | 2  |  4 |	14 |     12       |    20    |

Rata rata WT  :5,25
Rata rata TAT :10,75


perbandingan quantumm dan priority

Perbandingan performa:
Round Robin (RR): Performa tergantung pada besar time quantum (semakin tepat nilainya, semakin adil dan responsif).
Priority Scheduling: Performa tergantung pada pembagian prioritas (proses dengan prioritas tinggi mendapat layanan lebih dulu).

Pengaruh time quantum (pada Round Robin):

Terlalu kecil: Terjadi terlalu banyak pergantian konteks → overhead tinggi, efisiensi turun.
Terlalu besar: Respons terhadap proses interaktif menurun → sistem terasa lambat.

Pengaruh prioritas (pada Priority Scheduling):

Jika prioritas tidak diatur seimbang, proses prioritas rendah bisa starvation (tidak pernah mendapat giliran).
Sistem dapat cepat untuk proses penting, tapi kurang adil untuk proses lainnya.


Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?  **jawab** Round Robin (RR): Setiap proses mendapat jatah waktu (time quantum) yang sama secara bergiliran, tanpa melihat prioritas.
Priority Scheduling: Proses dijalankan berdasarkan tingkat prioritas, bukan urutan kedatangan atau waktu giliran.
2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?  **jawab** Time quantum terlalu kecil: sistem sering melakukan context switching, sehingga overhead meningkat dan efisiensi menurun.
Time quantum terlalu besar: proses pendek harus menunggu lama, sehingga waktu respons menjadi buruk.
3. Mengapa algoritma Priority dapat menyebabkan *starvation*? **jawab** Algoritma Priority dapat menyebabkan starvation karena proses dengan prioritas rendah bisa terus tertunda jika selalu ada proses berprioritas lebih tinggi yang masuk ke antrian. 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
