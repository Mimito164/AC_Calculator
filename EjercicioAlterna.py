import cmath
from Calculator import calc
from ComplexNumer import ComplexNumer


omega = 100
V = ComplexNumer("V", complex(cmath.rect(20, 1)))
R = ComplexNumer("R", complex(220, 0))
C = ComplexNumer("C", complex(0, -(1/(omega * 100e-3))))
L = ComplexNumer("L", complex(0, omega * 25e-3))

if __name__ == "__main__":
    zp = calc.paralel("Zp", L, R, True)
    zt = calc.sum("Zt", zp, C, True)
    it = calc.division("It", V, zt, True)

    vc = calc.voltageDivider("Vc", V, C, zp, True)
    vp = calc.voltageDivider("Vp", V, zp, C, True)
    ir = calc.division("Ir", vp, R, True)
    il = calc.division("Ir", vp, L, True)
    powersV = calc.power("S*", V, it, True)