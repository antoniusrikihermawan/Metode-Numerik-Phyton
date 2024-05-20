def fungsi(x,p,q,r,s):
    return p * x**3 + q * x**2 + r * x + s

def secant(x0,x1,p,q,r,s, toleransi=1e-6, max_iter=100):
    iterasi = 0
    while iterasi < max_iter:
        f_x0 = fungsi(x0,p,q,r,s)
        f_x1 = fungsi(x1,p,q,r,s)
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        print(f"Iterasi - {iterasi + 1}, x2 = {x2: .6f} dan f(x2) = {fungsi(x2,p,q,r,s):.6f}")

        if abs(f_x1) < toleransi :
            print(f"akar perkiraan : {x2:.6f} setelah {iterasi + 1}iterasi")
            break

        x0, x1 = x1, x2
        iterasi += 1
    else:
        print("Metode tidak konvergen setelah maksimum iterasi.")

x0 = float(input("Masukkan nilai x0 (tebakan awal) : "))
x1 = float(input("Masukkan nilai x1 (tebakan awal) : "))
p = float(input("Masukkan nilai p : "))
q = float(input("Masukkan nilai q : "))
r = float(input("Masukkan nilai r : "))
s = float(input("Masukkan nilai s : "))
toleransi = float(input("Masukkan nilai toleransi : "))

secant(x0,x1,p,q,r,s,toleransi)

if __name__ == "__main__":
    main()
