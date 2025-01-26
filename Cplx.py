import math

def sumcplx(a, b):
    return(a[0]+b[0], a[1]+b[1])

def prodcplx(a, b):
    return((a[0]*b[0] - a[1]*b[1]) , (a[0]*b[1] + a[1]*b[0]))

def rescplx(a, b):
    return(a[0]-b[0], a[1]-b[1])

def divcplx(a, b):
    denominator = ((b[0]**2) + (b[1]**2))
    return(((a[0]*b[0] + a[1]*b[1]) / denominator , (a[1]*b[0] - a[0]*b[1] ) / denominator))

def modcplx(a):
    return ((a[0]**2) + (a[1]**2)**0.5, 0)

def conjcplx(a):
    return(a[0], -a[1])

def polcplx(a):
    r = (a[0]**2 + a[1]**2)**0.5
    #Calcula el ángulo en radianes teniendo en cuenta el cuadrante
    ang = math.atan2(a[1], a[0])
    return (r, ang)


def carcplx(a):
    real = a[0] * math.cos(a[1])
    imag = a[0] * math.sin(a[1])
    return (real, imag)

def fasecplx(a):
    ang = math.atan2(a[1], a[0])
    return ang

if __name__ == "__main__":
    print(sumcplx((3.5, 6),(-6.7,2)))
    print(prodcplx((3.5, 6),(-6.7,2)))
    print(rescplx((3.5, 6),(-6.7,2)))
    print(divcplx((3.5, 6),(-6.7,2)))
    print(modcplx((3.5, 6)))
    print(conjcplx((3.5, 6)))
    print(polcplx((3.5, 6)))
    print(carcplx((7.11, math.pi/4)))
    print(fasecplx((3.5 , 6)))
