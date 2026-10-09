
# Program: Menghitung Pasangan

n = int(input("n: "))
count = 0

# Loop luar menentukan nilai i
for i in range(1, n + 1):

    # Loop dalam memeriksa semua nilai j
    for j in range(1, n + 1):

        # Menghitung pasangan yang memenuhi kondisi
        if i + j <= n:
            count += 1

# Menampilkan jumlah pasangan
print(f"Banyak pasangan = {count}")
