# Pertemuan 06 Nested Loop Python

Nama: Erna Hidayanti Nur Falah 
NIM: 2225250036 
Kelas: 3B

## Tujuan

Menggunakan nested loop, membuat pola, melakukan akumulasi, dan pencacahan menggunakan Python.

## Cara Menjalankan

```bash
python3 tugas/tabel_perkalian_dan_statistik.py
```

Untuk Windows, program juga dapat dijalankan dengan perintah:

```powershell
py tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

- **Loop luar (`i`):** menentukan baris tabel perkalian dari 1 sampai n.
- **Loop dalam (`j`):** menentukan kolom dan menghitung hasil perkalian pada setiap baris.
- **Akumulator `total_baris`:** menjumlahkan hasil perkalian pada satu baris dan direset setiap memulai baris baru.
- **Akumulator `total_semua`:** menjumlahkan seluruh hasil perkalian dari semua baris.
- **Counter `count_genap`:** menghitung banyaknya hasil perkalian yang genap.
- **Validasi `while`:** meminta input kembali jika n kurang dari atau sama dengan nol.

## Hasil Pengujian

| Input n | Jumlah pasangan | Total semua | Banyak hasil genap | Status |
|---|---:|---:|---:|---|
| 1 | 1 | 1 | 0 | Sesuai |
| 2 | 4 | 9 | 3 | Sesuai |
| 3 | 9 | 36 | 5 | Sesuai |

## Analisis Efisiensi

Loop luar berjalan sebanyak n kali. Untuk setiap iterasi loop luar, loop dalam berjalan sebanyak n kali. Oleh karena itu, pernyataan perkalian dieksekusi sebanyak n × n atau n² kali. Kompleksitas waktu program adalah O(n²).

## Refleksi

Kesalahan yang dapat terjadi pada nested loop adalah kesalahan indentasi sehingga loop dalam tidak berjalan sesuai struktur yang diharapkan. Kesalahan diperbaiki dengan memastikan indentasi benar dan melakukan pengujian menggunakan beberapa nilai n.

## Refleksi Teknis

1. **Mengapa `total_baris` direset di setiap iterasi loop luar?**  
   Agar jumlah setiap baris dihitung secara terpisah dan tidak tercampur dengan baris sebelumnya.

2. **Mengapa `total_semua` tidak direset di setiap baris?**  
   Karena variabel tersebut menyimpan jumlah seluruh hasil perkalian dari semua baris.

3. **Untuk n, berapa kali pernyataan `hasil = i * j` dieksekusi?**  
   Sebanyak n² kali.

4. **Bagaimana membuktikan `count_genap` benar?**  
   Dengan memeriksa setiap hasil perkalian dan menambah counter hanya jika `hasil % 2 == 0`, lalu membandingkannya dengan perhitungan manual.

5. **Apa bagian program yang paling banyak melakukan operasi ketika n membesar?**  
   Nested loop, karena perhitungan perkalian, penjumlahan, dan pemeriksaan kondisi dilakukan sebanyak n² kali.
