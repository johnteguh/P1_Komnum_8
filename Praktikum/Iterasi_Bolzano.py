import numpy as np
import matplotlib.pyplot as plt
 
#Mendefinisikan fungsi
def f(x):
    return (x**3+x**2-3*x-3)
 
itr_max = 50 
teliti = 10E-6  
x1 = float(input("Masukkan x1: "))       
x2 = float(input("Masukkan x2: "))      
 
# Memeriksa apakah value x1 dan x2 sesuai syarat
if f(x1) * f(x2) > 0:
    print('Angka tidak memenuhi kriteria bolzano (bertanda sama)')
    exit()
 

print('----------------------------------------------------------------------------')
print('iterasi \t x1\t\t x2\t\t xt\t\t f(xt)        ')
print('----------------------------------------------------------------------------')

for i in range(itr_max):
    xt = (x1 + x2)/2

    # Output hasil sesuai iterasi
    print(str(i + 1)+'\t\t% 10.8f\t% 10.8f\t% 10.8f\t% 10.8f\t' %(x1, x2, xt, f(xt)))
 
    if np.abs(f(xt)) < teliti:
        print('----------------------------------------------------------------------------')
        print('Nilai akar: '+ str(xt))
        exit()

    if f(x1) * f(xt) < 0:
        x2 = xt

    else: 
        x1 = xt
 
print('----------------------------------------------------------------------------')
if i == iterasi_maks - 1:
    print('\n\nIterasi maksimum!!!')
    print('Nilai akar: '+ str(xt))

print("\n")
