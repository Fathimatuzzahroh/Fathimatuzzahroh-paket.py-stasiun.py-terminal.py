# Program menghitung biaya layanan ekspedisi

# Fungsi untuk menghitung biaya ekspedisi
def hitung_biaya(panjang, lebar, tinggi, berat):
    # Dimensi maksimum untuk kategori kecil
    batas_dimensi = 50  # dalam cm
    biaya_per_kg_kecil = 5000  # Rp
    biaya_per_kg_besar = 7000  # Rp
    biaya_tambahan_besar = 50000  # Rp
    biaya_minimal = 8000  # Rp

    # Hitung volume paket
    volume = panjang * lebar * tinggi

    # Cek berat minimal
    if berat < 1:
        berat = 1

    # Tentukan biaya berdasarkan dimensi
    if panjang <= batas_dimensi and lebar <= batas_dimensi and tinggi <= batas_dimensi:
        biaya = berat * biaya_per_kg_kecil
    else:
        biaya = berat * biaya_per_kg_besar + biaya_tambahan_besar

    # Pastikan biaya minimal
    if biaya < biaya_minimal:
        biaya = biaya_minimal

    return biaya

# Input data dari pengguna
print("=== Layanan Ekspedisi Kota dan Kabupaten Pasuruan ===")
panjang = float(input("Masukkan panjang paket (cm): "))
lebar = float(input("Masukkan lebar paket (cm): "))
tinggi = float(input("Masukkan tinggi paket (cm): "))
berat = float(input("Masukkan berat paket (kg): "))

# Hitung biaya
biaya = hitung_biaya(panjang, lebar, tinggi, berat)

# Tampilkan hasil
print(f"Biaya pengiriman paket Anda: Rp{biaya:,}")