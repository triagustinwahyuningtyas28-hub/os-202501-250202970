
# Laporan Praktikum Minggu [XIII]
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas
- **NIM**   : 250202970 
- **Kelas** : 1IKRA

---

## Tujuan
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.


---

## Dasar Teori

Containerization pada Docker
Docker menjalankan aplikasi di dalam container yang terisolasi dari sistem host, tetapi tetap berbagi kernel yang sama. Isolasi ini memungkinkan pengelolaan sumber daya yang lebih efisien dibandingkan virtual machine.
Cgroups (Control Groups)
Docker memanfaatkan fitur Linux cgroups untuk membatasi dan mengontrol penggunaan sumber daya seperti CPU dan memori pada setiap container, sehingga satu container tidak menghabiskan seluruh resource host.
Pembatasan CPU
Resource CPU dapat dibatasi menggunakan parameter seperti --cpus atau --cpu-shares. Mekanisme ini mengatur seberapa besar jatah waktu CPU yang dapat digunakan oleh sebuah container.
Pembatasan Memori
Docker menyediakan opsi --memory untuk membatasi penggunaan RAM container. Jika container melebihi batas memori yang ditentukan, maka proses di dalamnya dapat dihentikan (OOM – Out of Memory).
Stabilitas dan Keamanan Sistem
Pembatasan resource pada container membantu menjaga stabilitas sistem host, mencegah resource starvation, serta meningkatkan keamanan dan keandalan aplikasi yang berjalan secara bersamaan.

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```


---

## Kode / Perintah
```
import time

print("=== CPU STRESS TEST DIMULAI ===")
start_time = time.time()

count = 0
while time.time() - start_time < 20:
    count += 1

print("CPU Stress Test selesai")
print(f"Total loop: {count}")

print("\n=== MEMORY STRESS TEST DIMULAI ===")

memory = []
try:
    for i in range(50):  # 50 x 10MB = 500MB
        memory.append(bytearray(10 * 1024 * 1024))
        print(f"Memory terpakai: {(i+1)*10} MB")
        time.sleep(1)
except MemoryError:
    print("Memory limit tercapai!")

print("Memory Stress Test selesai")

print("\nContainer aktif untuk monitoring (Ctrl+C untuk keluar)")
while True:
    time.sleep(1)
```

## Hasil Eksekusi

![hasil](<screenshots/Screenshot (6).png>) 
![hasil](<screenshots/Screenshot (7).png>)

---

## Analisis
| Kondisi Container | CPU      | Memori   | Perilaku Program |
| ----------------- | -------- | -------- | ---------------- |
| Tanpa limit       | Maksimal | Bebas    | Cepat & stabil   |
| Limit CPU         | Terbatas | Normal   | Lebih lambat     |
| Limit Memori      | Normal   | Terbatas | Error / OOM      |

---

## Kesimpulan
Docker mampu membatasi penggunaan CPU dan memori pada container secara efektif menggunakan mekanisme kernel Linux (cgroups), sehingga penggunaan resource dapat dikendalikan sesuai kebutuhan.
Pembatasan resource berpengaruh langsung terhadap perilaku aplikasi, di mana limit CPU menyebabkan eksekusi program menjadi lebih lambat, sedangkan limit memori dapat menghentikan aplikasi yang melebihi batas penggunaan RAM (Out of Memory).
Penerapan resource limit pada container penting untuk menjaga stabilitas, efisiensi, dan keamanan sistem, terutama ketika menjalankan banyak aplikasi secara bersamaan dalam satu host.

---

## Tugas & Quiz
### Tugas
1. Buat Dockerfile sederhana dan program uji di folder `code/`.
2. Build image dan jalankan container **tanpa limit**.
3. Jalankan container dengan limit **CPU** dan **memori**.
4. Sajikan hasil pengamatan dalam tabel/uraian singkat di `laporan.md`.
**JAWABAN**
Berdasarkan hasil eksekusi program uji dan monitoring menggunakan perintah docker stats, diperoleh pengamatan sebagai berikut:
- Saat container dijalankan tanpa limit resource, program dapat menggunakan CPU dan memori secara bebas. Memory stress test berhasil mengalokasikan memori hingga sekitar 500 MB tanpa dihentikan oleh sistem, menunjukkan bahwa container memanfaatkan resource host secara penuh.
- Saat container dijalankan dengan limit CPU 0.5 core dan memori 256 MB, eksekusi program menunjukkan pembatasan yang jelas. Penggunaan CPU dibatasi sekitar 50%, dan penggunaan memori tidak dapat melebihi 256 MB sesuai konfigurasi. Hal ini terlihat pada output docker stats yang menampilkan nilai MEM USAGE / LIMIT = 4.609MiB / 256MiB dan CPU usage sekitar 49–50%.
- Container tetap berjalan dalam kondisi aktif hingga dihentikan secara manual (Ctrl+C), menunjukkan bahwa kernel berhasil mengontrol resource tanpa menyebabkan sistem host terganggu.

Tabel Perbandingan Hasil Eksekusi
| Aspek Pengamatan            | Tanpa Limit Resource                              | Dengan Limit CPU & Memori                |
| --------------------------- | ------------------------------------------------- | ---------------------------------------- |
| Penggunaan CPU              | Bebas, dapat menggunakan CPU host secara penuh    | Dibatasi ±50% sesuai `--cpus="0.5"`      |
| Penggunaan Memori           | Meningkat hingga ±500 MB                          | Dibatasi maksimal 256 MB                 |
| Perilaku Program            | CPU stress berjalan cepat, memori terus bertambah | CPU stress lebih lambat, memori dibatasi |
| Status Container            | Berjalan normal                                   | Berjalan normal dengan pembatasan        |
| Monitoring (`docker stats`) | Tidak ada batas jelas                             | MEM USAGE / LIMIT terlihat jelas         |
| Dampak ke Sistem Host       | Berpotensi membebani host                         | Lebih stabil dan terkendali              |


### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Mengapa container perlu dibatasi CPU dan memori?
**Jawaban:** Container perlu dibatasi CPU dan memori agar satu aplikasi tidak menghabiskan seluruh sumber daya sistem. Tanpa pembatasan, container yang boros resource dapat menyebabkan aplikasi lain melambat, sistem menjadi tidak stabil, bahkan crash. Pembatasan resource membantu menjaga stabilitas, keadilan pemakaian resource, dan keamanan sistem host.
2. Apa perbedaan VM dan container dalam konteks isolasi resource?
**Jawaban:** Virtual Machine (VM) melakukan isolasi resource dengan menjalankan sistem operasi lengkap di atas hypervisor, sehingga setiap VM memiliki kernel sendiri dan resource yang dialokasikan bersifat tetap.
Sebaliknya, container hanya mengisolasi proses aplikasi dan berbagi kernel host, sehingga penggunaan resource lebih ringan, cepat, dan efisien, namun tingkat isolasinya lebih rendah dibandingkan VM.
3. Apa dampak limit memori terhadap aplikasi yang boros memori?
**Jawaban:** Jika aplikasi boros memori dijalankan dengan limit memori, maka ketika penggunaan RAM melebihi batas yang ditentukan, kernel akan menghentikan proses tersebut (Out of Memory / OOM). Akibatnya, aplikasi dapat berhenti tiba-tiba atau mengalami error. Hal ini mendorong pengembang untuk membuat aplikasi lebih efisien dan mencegah gangguan pada sistem secara keseluruhan.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
