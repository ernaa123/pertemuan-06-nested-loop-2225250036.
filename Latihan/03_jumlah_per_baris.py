
# Program: Jumlah per Baris

# Loop luar: menentukan nilai i dari 1 sampai 4
for i in range(1, 5):

    # Akumulator: menyimpan jumlah pada setiap baris
    total_baris = 0

    # Loop dalam: menentukan nilai j dari 1 sampai 3
    for j in range(1, 4):

        # Menambahkan hasil perkalian ke jumlah baris
        total_baris += i * j

    # Output: menampilkan jumlah setiap baris
    print(f"Jumlah baris {i} = {total_baris}")
