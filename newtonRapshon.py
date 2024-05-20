def f(x,p,q,r,s):
    return p * x**3 + q * x**2 + r * x + s

def f_prime(x,p,q,r):
    return 3 * p * x**2 + 2 * q * x + r

def newton_raphson(p,q,r,s,x0, tol=1e-6, max_iter=100):
    iterasi = 0
    x = x0

    while iterasi < max_iter:
        x_new = x - f(x,p,q,r,s) / f_prime(x,p,q,r)

        if abs(x_new - x) < tol:
            print("Iterasi ke - ",iterasi, ": x =", x_new)
            break

        x = x_new
        iterasi += 1
        print("Iteraksi ke - ",iterasi,": x =",x_new)

    if iterasi == max_iter:
        print("Iterasi maksimum telah tercapai.")
    return x_new

p = float(input("Masukkan nilai p : "))
q = float(input("Masukkan nilai q : "))
r = float(input("Masukkan nilai r : "))
s = float(input("Masukkan nilai s : "))

x0 = float(input("Masukkan nilai x0 : "))

akar = newton_raphson(p,q,r,s,x0)
print("Akar persamaan : ",akar)
