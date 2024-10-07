#menghitung perkalian matriks ordo 3x3
Orde_A = [[3, 5, 7],
          [7, 9, 6],
          [9, 8, 7]]
Orde_B = [[8, 17, -6],
          [18, 4, 9],
          [-15, 5, 28]]

# Memeriksa apakah orde matriks sesuai
if len(Orde_A) != 3 or len(Orde_B) != 3 or len(Orde_A[0]) != 3 or len(Orde_B[0]) != 3:
    print("Matriks tidak dapat dikalikan, pastikan kedua matriks berordo 3x3.")
else:
    # Inisialisasi matriks hasil
    hasil = [[0 for _ in range(3)] for _ in range(3)]

    # Mengalikan matriks A dan B
    for i in range(3):
        for j in range(3):
            hasil[i][j] = sum(Orde_A[i][k] * Orde_B[k][j] for k in range(3))

    # Menampilkan hasil perkalian
    print("Hasil perkalian matriks A dan B adalah:")
    for row in hasil:
        print(row)

print("Selesai")