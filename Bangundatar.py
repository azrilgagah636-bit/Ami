import math

# ===== Fungsi perhitungan =====
def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

def lingkaran(jari):
    luas = math.pi * jari * jari
    keliling = 2 * math.pi * jari
    return luas, keliling

def segitiga(alas, tinggi, sisi):
    luas = 0.5 * alas * tinggi
    keliling = alas + tinggi + sisi
    return luas, keliling

# ===== Program utama =====
def main():
    print("=== Aplikasi Bangun Datar ===")

    nama = input("Masukkan nama anda: ")
    print(f"\nHalo, {nama}!\n")

    bangun_datar = ["Persegi", "Persegi Panjang", "Lingkaran", "Segitiga"]

    while True:
        print("Daftar Bangun Datar:")
        for i in range(len(bangun_datar)):
            print(f"{i+1}. {bangun_datar[i]}")

        pilihan = input("\nPilih bangun datar (1-4) atau 0 untuk keluar: ")

        if pilihan == "0":
            print("\nTerima kasih telah menggunakan aplikasi ini.")
            break

        elif pilihan == "1":
            sisi = float(input("Masukkan sisi: "))
            luas, keliling = persegi(sisi)

        elif pilihan == "2":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            luas, keliling = persegi_panjang(panjang, lebar)

        elif pilihan == "3":
            jari = float(input("Masukkan jari-jari: "))
            luas, keliling = lingkaran(jari)

        elif pilihan == "4":
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            sisi = float(input("Masukkan sisi miring: "))
            luas, keliling = segitiga(alas, tinggi, sisi)

        else:
            print("Pilihan tidak valid!\n")
            continue

        print("\nHasil Perhitungan:")
        print(f"Luas     = {luas:.2f}")
        print(f"Keliling = {keliling:.2f}")

        ulang = input("\nHitung lagi? (y/n): ")
        if ulang.lower() != "y":
            print("\nTerima kasih telah menggunakan aplikasi ini.")
            break


# ===== Jalankan program =====
if __name__ == "__main__":
    main()