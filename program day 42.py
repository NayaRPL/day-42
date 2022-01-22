print("contoh menampilkan tabel perkalian")
print("contoh memakai perulangan atau foor")
num= int(input("multipication table off:"))
for i in range (1,11):
    print(num, 'x',i,'=',num*i)
print("contoh memakai fungsi atau fuction")
def perkalian(num):
    for i in range (1,11):
      print(num, 'x',i,'=',num*i)
perkalian(7)
print("contoh memakai fungsi rekursif")
nam=int(input("multipication table off:"))
def perkalian(batas,i=1):
      print(nam, 'x',i,'=',nam*i)
      if (i < batas):
          perkalian(batas,i+1)
perkalian(10)

