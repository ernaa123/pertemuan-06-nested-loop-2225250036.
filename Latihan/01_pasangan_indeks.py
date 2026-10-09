
# Program: Pasangan Indeks

count = 0  # Menghitung banyak pasangan

# Loop luar: mengatur nilai i dari 1 sampai 3
for i in range(1, 4):

    # Loop dalam: mengatur nilai j dari 1 sampai 4
    for j in range(1, 5):

        # Output: menampilkan pasangan indeks
        print(i, j)

        # Counter: bertambah setiap pasangan ditampilkan
        count += 1

# Output: menampilkan jumlah seluruh pasangan
print(f"Banyak pasangan = {count}")
