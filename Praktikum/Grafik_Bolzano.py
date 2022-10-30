import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100) #Menentukan sumbu x pada grafik
y = (x**3+x**2-3*x-3) #fungsi yang akan dicari penyelesaian

# mengatur axis di pusat dan untuk mengubah menjadi grafik
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#Mengubah Grafik yang awalnya 1 daerah menjadi 4 daerah dengan sumbu x dan y
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, y, 'g')
plt.title("bolzano method") #Judul Grafik
# Menampilkan Grafik
plt.show()
