print("Kalkulator Sederhana Python")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pil = int(input("Masukan Pilihan Operasi : "))

x= int(input("Bilangan 1 : "))
y= int(input("Bilangan 2 : "))

if pil == 1:
   hasil = x+y
elif pil == 2:
   hasil = x-y
elif pil == 3:
   hasil = x*y
elif pil == 4:
   hasil = x/y

print (hasil)