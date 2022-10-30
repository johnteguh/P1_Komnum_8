import numpy as np
import matplotlib.pyplot as plt
 
#Menentuk fungsi yang akan dihitung
def f(x):
    return (x**3+x**2-3*x-3)
 
itr_max = 50 
teliti = 10E-6  
x1 = float(input("Masukkan x1: "))       
x2 = float(input("Masukkan x2: "))      
 
# Memeriksa apakah value x1 dan x2 sesuai syarat
if (f(x1) > 0 and f(x2) < 0) or (f(x1) < 0 and f(x2)>0):
    print('Angka Tidak sesuai karena x1 dan x2 bertanda sama')
    exit()

for i in range(itr_max):
    xt = (x1 + x2)/2
    # Output hasil sesuai iterasi
    print("i:"+str(i + 1)+".")
    print("x1: "+'%10.8f'%(x1)+"")
    print("x2: "+'%10.8f'%(x2)+"")
    print("xt: "+'%10.8f'%(xt)+"")
    print("f(xt):"+'%10.8f' %(f(xt))+"\n\n")
 
    if np.abs(f(xt)) < teliti:
        print('=========================')
        print('Nilai akar: '+ str(xt))
        exit()

    if f(x1) * f(xt) < 0:
        x2 = xt

    else: 
        x1 = xt
 
print('============================')
if i == itr_max - 1:
    print('\n\n Sudah Dilakukan Iterasi maksimum!!!')
    print('Didapatkan Nilai akar: '+ str(xt))

print("\n")
