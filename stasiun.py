def hitung_tarif_parkir(jenis_kendaraan, durasi_jam):
    # Tarif dasar
    tarif_awal = 3000
    
    # Tarif per jam setelah 2 jam
    tarif_motor_per_jam = 1000
    tarif_mobil_per_jam = 1500
    
    # Biaya tambahan jika melebihi 24 jam
    biaya_tambahan_24_jam = 10000
    
    # Hitung biaya
    if durasi_jam <= 2:
        total_biaya = tarif_awal
    else:
        if jenis_kendaraan == "motor":
            total_biaya = tarif_awal + (durasi_jam - 2) * tarif_motor_per_jam
        elif jenis_kendaraan == "mobil":
            total_biaya = tarif_awal + (durasi_jam - 2) * tarif_mobil_per_jam
        else:
            return "Jenis kendaraan tidak valid."
    
    # Tambahkan biaya tambahan jika melebihi 24 jam
    if durasi_jam > 24:
        total_biaya += biaya_tambahan_24_jam
    
    return total_biaya


# Program utama
print("Selamat datang di sistem perhitungan tarif parkir!")
jenis_kendaraan = input("Masukkan jenis kendaraan (motor/mobil): ").strip().lower()
durasi_jam = int(input("Masukkan durasi parkir dalam jam: "))

# Hitung tarif
total_biaya = hitung_tarif_parkir(jenis_kendaraan, durasi_jam)

if isinstance(total_biaya, str):
    print(total_biaya)
else:
    print(f"Total biaya parkir untuk {jenis_kendaraan} selama {durasi_jam} jam adalah Rp{total_biaya},-")