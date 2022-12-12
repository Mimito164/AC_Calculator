from Calculator import calc
from ComplexNumer import *


ComplexNumer.setOmega(ComplexNumer, 100)

V = VoltageSource("V", 20, 1)
R = Resistor("R", 220)
C = Capacitor("C", 100e-3)
L = Inductor("L", 25e-3)

if __name__ == "__main__":
    zp = calc.paralel("Zp", L, R, True)
    zt = calc.sum("Zt", zp, C, True)
    it = calc.division("It", V, zt, True)

    vc = calc.voltageDivider("Vc", V, C, zp, True)
    vp = calc.voltageDivider("Vp", V, zp, C, True)
    ir = calc.division("Ir", vp, R, True)
    il = calc.division("Ir", vp, L, True)
    powersV = calc.power("S*", V, it, True)
