# INI TANDA AIR (Watermark)

print("=== Program Kalkulator Sederhana ===")
print("1. Penjumlahan")
print("2. Pengurangan")

pilihan = input("Pilih operasi (1/2): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    hasil = angka1 + angka2
    print(f"Hasil penjumlahan: {angka1} + {angka2} = {hasil}")
elif pilihan == '2':
    hasil = angka1 - angka2
    print(f"Hasil pengurangan: {angka1} - {angka2} = {hasil}")
else:
    print("Pilihan tidak valid.")