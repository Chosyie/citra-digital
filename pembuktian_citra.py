import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. MEMBACA GAMBAR ---
image_path = 'test_image.jpg'
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("="*50)
print("🔍 ANALISIS MENDALAM CITRA DIGITAL")
print("="*50)

# --- 2. BUKTI LEVEL 1: FISIK FILE (HEXADECIMAL) ---
with open(image_path, 'rb') as file:
    raw_bytes = file.read(40) # Membaca 40 byte pertama langsung dari hardisk
    hex_data = raw_bytes.hex()
    
print("\n[BUKTI 1: FISIK FILE DI HARDISK]")
print("Sebelum dirender layar, file gambar hanyalah susunan angka Hexadecimal/Biner:")
print(f"Isi mentah (40 karakter pertama): {hex_data[:40]}...\n")

# --- 3. BUKTI LEVEL 2: STRUKTUR DATA MATRIKS ---
print("[BUKTI 2: BENTUK MATRIKS SAAT MASUK KE RAM]")
print(f"Dimensi (Lebar x Tinggi) : {img_rgb.shape[1]} x {img_rgb.shape[0]} piksel")
print(f"Total jumlah piksel      : {img_rgb.shape[1] * img_rgb.shape[0]:,} kotak")
print(f"Satu piksel di koordinat ujung kiri atas berisi 3 angka (Red, Green, Blue): {img_rgb[0,0]}")

# --- 4. BUKTI LEVEL 3: ARITMATIKA (Ubah Kecerahan dengan Matematika) ---
# Menambahkan angka 75 ke semua matriks. Jika gambar adalah angka, maka nilainya naik = makin terang.
matrix_brighter = cv2.add(img_rgb, np.array([75.0]))

# --- 5. VISUALISASI KE LAYAR ---
print("\n[PROSES] Membuka 3 jendela grafik pembuktian visual... (Simpan gambar dan tutup jendela untuk mengakhiri)")

# Visualisasi 1: Grid Matriks 2D
crop_size = 8
crop_gray = img_gray[150:150+crop_size, 150:150+crop_size] # Memotong 8x8 piksel di tengah

fig1, ax1 = plt.subplots(figsize=(6, 6))
ax1.imshow(crop_gray, cmap='gray')
for i in range(crop_size):
    for j in range(crop_size):
        # Menuliskan angka intensitas (0-255) di atas setiap kotak piksel
        ax1.text(j, i, str(crop_gray[i, j]), color='red', ha='center', va='center', fontsize=9, fontweight='bold')
ax1.set_title("Bukti 2D: Setiap kotak piksel = 1 Angka Intensitas (0-255)")
ax1.axis('off')

# Visualisasi 2: Grafik Topografi 3D (Z-axis = Angka Intensitas)
X, Y = np.meshgrid(range(crop_size), range(crop_size))
Z = crop_gray

fig2 = plt.figure(figsize=(8, 6))
ax2 = fig2.add_subplot(111, projection='3d')
surf = ax2.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
fig2.colorbar(surf, ax=ax2, shrink=0.5, aspect=5)
ax2.set_title("Bukti 3D: Grafik Piksel (Semakin tinggi grafik = Angka makin besar/terang)")

# Visualisasi 3: Efek Penjumlahan Aritmatika
fig3, (ax3a, ax3b) = plt.subplots(1, 2, figsize=(10, 5))
ax3a.imshow(img_rgb)
ax3a.set_title("Matriks Asli")
ax3a.axis('off')

ax3b.imshow(matrix_brighter.astype(np.uint8))
ax3b.set_title("Matriks + Angka 75 (Menjadi Terang)")
ax3b.axis('off')

# Menampilkan semua jendela
plt.show()