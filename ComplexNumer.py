import cmath


class ComplexNumer:
    value = complex()
    name = ""

    def __init__(self, name: str, complex: complex):
        self.name = name
        self.value = complex

    # def getName(self):
    #     return f'{self=}'.split('=')[0]

    def toExp(self) -> str:
        phase = cmath.phase(self.value) 
        phaseStr = ""
        if phase == cmath.pi/2:
            phaseStr = "pi/2"
        elif phase == -(cmath.pi/2):
            phaseStr = "- pi/2"
        elif phase == (cmath.pi):
            phaseStr = "pi"
        else:
            phaseStr = cmath.phase(self.value).__round__(2)
        
        return f"{self.value.__abs__().__round__(2)} e j({phaseStr})"

    def toRect(self) -> str:
        return f"{self.value.real.__round__(2)} {'+' if self.value.imag > 0 else '-'} {abs(self.value.imag.__round__(2))}j"
