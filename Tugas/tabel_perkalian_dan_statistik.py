
# Tugas 3: Tabel Perkalian dan Statistik

print("Tabel Perkalian dan Statistik")

# Validasi: n harus berupa bilangan bulat positif
n = int(input("n: "))
while n <= 0:
    print("n harus bilangan bulat positif!")
    n = int(input("Masukkan n kembali: "))

# Akumulator total dan counter hasil genap
total_semua = 0
count_genap = 0

# Loop luar: menentukan baris tabel
for i in range(1, n + 1):
    total_baris = 0

    # Loop dalam: menentukan kolom tabel
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end="")

        # Menghitung jumlah setiap baris dan total keseluruhan
        total_baris += hasil
        total_semua += hasil

        # Counter bertambah jika hasil perkalian genap
        if hasil % 2 == 0:
            count_genap += 1

    # Menampilkan jumlah setelah satu baris selesai
    print(f" | Jumlah baris {i} = {total_baris}")

# Statistik akhir
print(f"Total semua = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
