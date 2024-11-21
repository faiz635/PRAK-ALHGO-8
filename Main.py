# def rekursif(jumlah, i=1):
#     if jumlah <= 0:
#         return 0
#     else:
#        angka = float(input(f"Masukan bil ke-{i}: "))
#     return angka + rekursif(jumlah - 1, i + 1)
        
# angka = float(input("Masukan Angka : "))
# nilai = rekursif(angka)
# print(f"Hasil: {nilai}")


def pangkat_rekursif(x,y):
   if y == 0:
      return 1
   else:
      return x * pangkat_rekursif(x,y-1)

x = int(input("Masukan Angkanya : "))
y = int(input("Masukan Pangkatnya  : "))

print("%d dipangkatkan %d = %d" % (x,y,pangkat_rekursif(x,y)))