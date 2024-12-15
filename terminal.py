def hitung_tarif_parkir(durasi_jam):
    # Tarif dasar
    tarif_awal = 3000
    
    # Tarif per jam setelah 2 jam
    tarif_per_jam = 1500
    
    # Biaya tambahan jika melebihi 24 jam
    biaya_tambahan_24_jam = 10000
    
    # Hitung biaya
    if durasi_jam <= 2:
        total_biaya = tarif_awal
    else:
        total_biaya = tarif_awal + (durasi_jam - 2) * tarif_per_jam
    
    # Tambahkan biaya tambahan jika melebihi 24 jam
    if durasi_jam > 24:
        total_biaya += biaya_tambahan_24_jam
    
    return total_biaya


# Program utama
print("Selamat datang di sistem perhitungan tarif parkir terminal!")
durasi_jam = int(input("Masukkan durasi parkir dalam jam: "))

# Hitung tarif
total_biaya = hitung_tarif_parkir(durasi_jam)

# Output hasil
print(f"Total biaya parkir untuk durasi {durasi_jam} jam adalah Rp{total_biaya},-")