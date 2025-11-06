
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
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Siapkan Data Proses Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):

Proses	Burst Time	Arrival Time	Priority
P1	5	0	2
P2	3	1	1
P3	8	2	4
P4	6	3	3

2. Eksperimen 1 – Round Robin (RR)

Gunakan time quantum (q) = 3.
Hitung waiting time dan turnaround time untuk tiap proses.
Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).
| P1 | P2 | P3 | P4 | P1 | P3 | ...
0    3    6    9   12   15   18  ...
Catat sisa burst time tiap putaran.

3. Eksperimen 2 – Priority Scheduling (Non-Preemptive)

Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).
Lakukan perhitungan manual untuk:
WT[i] = waktu mulai eksekusi - Arrival[i]
TAT[i] = WT[i] + Burst[i]
Buat tabel perbandingan hasil RR dan Priority.

4. Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)

Ubah quantum menjadi 2 dan 5.
Amati perubahan nilai rata-rata waiting time dan turnaround time.
Buat tabel perbandingan efek quantum.

5. Eksperimen 4 – Dokumentasi

Simpan semua hasil tabel dan screenshot ke:

praktikum/week6-scheduling-rr-priority/screenshots/
Buat tabel perbandingan seperti berikut:

Algoritma	Avg Waiting Time	Avg Turnaround Time	Kelebihan	Kekurangan
RR	...	...	Adil terhadap semua proses	Tidak efisien jika quantum tidak tepat
Priority	...	...	Efisien untuk proses penting	Potensi starvation pada prioritas rendah

6. Commit & Push

git add .
git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
git push origin main

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

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
