
# Laporan Praktikum Minggu XI
Topik : Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas
- **NIM**   : 250202970
- **Kelas** : 1IKRA

---

## Tujuan
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```
---

## Kode / Perintah
```
import csv
import os
from collections import defaultdict

def read_dataset(filename):
    processes = []
    allocation = {}
    request = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            p = row['Process']
            processes.append(p)
            allocation[p] = row['Allocation']
            request[p] = row['Request']

    return processes, allocation, request

def build_wait_for_graph(processes, allocation, request):
    wfg = defaultdict(list)

    for p1 in processes:
        for p2 in processes:
            if p1 != p2:
                if request[p1] == allocation[p2]:
                    wfg[p1].append(p2)

    return wfg
    
def detect_cycle(wfg, processes):
    visited = set()
    stack = set()
    deadlock_processes = set()

    def dfs(p):
        if p in stack:
            deadlock_processes.update(stack)
            return True
        if p in visited:
            return False

        visited.add(p)
        stack.add(p)

        for neighbor in wfg[p]:
            if dfs(neighbor):
                return True

        stack.remove(p)
        return False

    for p in processes:
        if dfs(p):
            break

    return deadlock_processes

```

---

## Hasil Eksekusi
<img width="848" height="316" alt="Screenshot 2026-01-15 200842" src="https://github.com/user-attachments/assets/8e9e9c25-691c-4c5a-a475-09478bd4990c" />

---

## Analisis
   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).
 

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Tugas & Quiz
### Tugas
1. Buat program simulasi deteksi deadlock.  
2. Jalankan program dengan dataset uji.  
3. Sajikan hasil analisis dalam tabel dan narasi.  
4. Tulis laporan praktikum pada `laporan.md`.

## Quiz
1.Apa perbedaan antara deadlock prevention, avoidance, dan detection? 
   **Jawaban:**  Perbedaan Deadlock Prevention, Avoidance, dan Detection

1. Deadlock Prevention
Mencegah deadlock sebelum terjadi dengan menghilangkan salah satu kondisi deadlock.
➜ Deadlock tidak mungkin terjadi, tetapi kurang efisien.

2. Deadlock Avoidance
Menghindari deadlock dengan mengecek kondisi sistem saat alokasi resource (misalnya Banker’s Algorithm).
➜ Lebih efisien, tetapi butuh informasi lengkap resource.

3. Deadlock Detection
Membiarkan deadlock terjadi lalu mendeteksi dan memulihkannya.
➜ Resource efisien, tetapi proses bisa terganggu.

2.Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi? 
   **Jawaban:** 
   
   Deteksi deadlock tetap diperlukan karena deadlock tidak selalu bisa dicegah atau dihindari tanpa menurunkan kinerja sistem. Sistem operasi yang dinamis membutuhkan pemakaian resource secara efisien, dan jika deadlock terjadi, deteksi memungkinkan sistem menemukan dan memulihkannya agar tidak berhenti total.
   
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
   **Jawaban:**

Kelebihan deteksi deadlock
-Pemanfaatan resource lebih efisien.
-Tidak membatasi alokasi resource di awal.
-Cocok untuk sistem yang dinamis.

Kekurangan deteksi deadlock:
-Deadlock tetap bisa terjadi.
-Membutuhkan proses deteksi tambahan.
-Pemulihan dapat menghentikan proses atau menyebabkan kehilangan data.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
