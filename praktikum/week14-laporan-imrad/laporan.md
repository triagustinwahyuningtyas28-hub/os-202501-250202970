
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD

---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas 
- **NIM**   : 250202970 
- **Kelas** : 1IKRA

---

## Pendahuluan
Sistem operasi bertanggung jawab mengelola sumber daya agar dapat digunakan secara optimal oleh berbagai proses. Dalam kondisi tertentu, pengelolaan sumber daya dapat menimbulkan permasalahan serius yang dikenal sebagai deadlock. Deadlock terjadi ketika dua atau lebih proses saling menunggu sumber daya yang tidak akan pernah dilepaskan.

Deadlock sulit dihindari sepenuhnya dalam sistem yang dinamis karena proses dan kebutuhan resource dapat berubah sewaktu-waktu. Oleh karena itu, salah satu pendekatan yang digunakan adalah deteksi deadlock, yaitu membiarkan sistem berjalan normal lalu mendeteksi adanya kondisi deadlock secara periodik.

Praktikum ini dilakukan untuk memahami konsep deadlock secara praktis melalui simulasi program. Fokus utama adalah mendeteksi deadlock dengan membangun Wait-For Graph dan menganalisis keberadaan siklus sebagai indikator deadlock.

---

## Methods
Metode yang digunakan dalam praktikum ini meliputi beberapa tahapan berikut:

## 1. Penyusunan Dataset

Dataset disusun dalam bentuk tabel yang berisi daftar proses, resource yang sedang dialokasikan (Allocation), dan resource yang diminta (Request). Dataset ini merepresentasikan kondisi sistem nyata secara sederhana.

Contoh struktur dataset:

| Proses | Allocation | Request |
|--------|------------|---------|
| P1     | R1         | R2      |
| P2     | R2         | R3      |
| P3     | R3         | R1      |

## 2. Pembangunan Wait-For Graph (WFG)

Wait-For Graph dibangun berdasarkan hubungan antar proses. Jika suatu proses meminta resource yang sedang dialokasikan oleh proses lain, maka dibuat sisi dari proses peminta ke proses pemegang resource.

## 3. Algoritma Deteksi Deadlock

Deteksi deadlock dilakukan menggunakan algoritma Depth First Search (DFS). DFS digunakan untuk menelusuri graf dan mendeteksi adanya siklus. Jika ditemukan siklus, maka proses-proses yang terlibat dalam siklus tersebut dinyatakan mengalami deadlock.

## 4. Implementasi Program

Program diimplementasikan menggunakan bahasa Python dengan memanfaatkan struktur data dictionary dan list untuk merepresentasikan graf serta DFS untuk pendeteksian siklus.

---

## Results
Program berhasil dijalankan menggunakan dataset uji dan menghasilkan deteksi deadlock berdasarkan siklus pada Wait-For Graph. Hasil eksekusi menunjukkan bahwa tidak semua proses berada dalam kondisi deadlock.

Hasil deteksi deadlock disajikan dalam tabel berikut:

| Proses | Status          |
|--------|-----------------|
| P1     | Deadlock        |
| P2     | Deadlock        |
| P3     | Tidak Deadlock  |
| P4     | Tidak Deadlock  |

Proses P1 dan P2 teridentifikasi mengalami deadlock karena saling menunggu resource satu sama lain, sedangkan proses P3 dan P4 tidak terlibat dalam siklus ketergantungan.

---

## Discussion
Hasil praktikum menunjukkan bahwa deadlock terjadi ketika terdapat siklus dalam Wait-For Graph. Siklus tersebut menandakan adanya circular wait antar proses, yang merupakan salah satu dari empat kondisi Coffman.

Analisis berdasarkan teori deadlock menunjukkan bahwa:

 ## 1. Mutual Exclusion
 
  terpenuhi karena resource hanya dapat digunakan oleh satu proses dalam satu waktu.

## 2. Hold and Wait
 terpenuhi karena setiap proses menahan resource sambil menunggu resource lain.

## 3. No Preemption 
terpenuhi karena resource tidak dapat direbut secara paksa oleh sistem.

## 4. Circular Wait
 terpenuhi ketika terdapat siklus pada WFG, yang terdeteksi langsung oleh algoritma DFS.

 Proses yang tidak berada dalam siklus tetap dapat berjalan karena rantai tunggu tidak kembali ke proses awal. Hal ini menegaskan bahwa keberadaan siklus merupakan indikator utama terjadinya deadlock dalam metode deteksi.

---

## Conclusion
Praktikum simulasi dan deteksi deadlock berhasil dilaksanakan dengan baik. Program mampu mendeteksi deadlock melalui pembangunan Wait-For Graph dan pendeteksian siklus menggunakan algoritma DFS. Hasil menunjukkan bahwa deadlock terjadi ketika keempat kondisi Coffman terpenuhi secara bersamaan, terutama kondisi circular wait.

Melalui praktikum ini, pemahaman mengenai konsep deadlock, deteksi deadlock, serta analisis permasalahan sinkronisasi dalam sistem operasi dapat ditingkatkan secara logis dan sistematis.

---

## Refleksi Diri
Bagian paling menantang dalam praktikum ini adalah memahami logika pembentukan Wait-For Graph dan pendeteksian siklus menggunakan DFS. Tantangan tersebut diatasi dengan mempelajari kembali teori deadlock dan mencoba menelusuri alur program secara bertahap hingga memahami hubungan antar proses dan resource.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
