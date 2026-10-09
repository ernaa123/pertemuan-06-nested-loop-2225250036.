
# Program: Pola Segitiga Bintang

n = int(input("n: "))

# Loop luar: menentukan jumlah baris
for i in range(1, n + 1):

    # Loop dalam: mencetak bintang pada setiap baris
    for j in range(i):
        print("*", end=" ")

    # Pindah ke baris berikutnya
    print()
