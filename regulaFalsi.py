import numpy as np 

# definisi fungsi 
def fx(x):
    return x*np.exp(-x)+1

# memasukkan batas bawah, atas, toleransi, error, dan jumlah iterasi
p = float(input("Masukkan batas bawah : "))
q = float(input("Masukkan batas atas : "))
r = float(input("Masukkan batas toleransi error : "))
s = float(input("Masukkan jumlah iterasi : "))

iterasi = 0
y1 = fx(p)
y2 = fx(q)
xr = ((fx(q)*p-(fx(p)*q))//(fx(q))-fx(p))

if (y1*y2>0):
    print("\nf(p) x f(x) > 0, maka tidak ada akar")

else:
    print("\niterasi\t\t\t p\t\t xr \t\t q \t\t f(p)\t \tf(b)")
    while (iterasi <= s and abs ((fx(xr))>r)):
        iterasi = iterasi+1
        xr = ((fx(q)*p)-(fx(p)*q))/(fx(q)-fx(p))
        y3 = fx(xr)
        print("%f\t%f\t%f\t%f\t%f\t%f\t%f\t" %(iterasi,p,xr,q,fx(p),fx(q), abs(fx(xr))))
        if (fx(xr)*fx(p)<0):
            q = xr
            y2 = y3
        else:
            p = xr
            y1 = y3
    if (iterasi<=s):
        print("penyesaiannya adalah x =%f dengan error %f" %(xr,abs(fx(xr))))
    else:
        print("penyelesaiannya tidak ditemukan")