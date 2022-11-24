import cmath



class ComplexNumer:
    omega = 0

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
    
    def setOmega(self, newOmega):
        self.omega = newOmega
    
    def getOmega(self):
        return self.omega

class Resistor(ComplexNumer):
    def __init__(self, name: str, resistorValue: float):
        if resistorValue < 0: raise ValueError("Resistor value provided can't be negative.")
        super().__init__(name, complex(resistorValue, 0))

class Inductor(ComplexNumer):
    def __init__(self, name: str, inductorValue: float):
        if inductorValue < 0: raise ValueError("Inductor value provided can't be negative.")
        super().__init__(name, complex(0, self.getOmega() * inductorValue))

class Capacitor(ComplexNumer):
    def __init__(self, name: str, capacitorValue: float, omega: float):
        if capacitorValue < 0: raise ValueError("Capacitor value provided can't be negative.")
        super().__init__(name, complex(0, -(1 / self.getOmega() * capacitorValue)))

class VoltajeSource(ComplexNumer):
    def __init__(self, name: str, voltage:float, phase:float):
        if voltage < 0: raise ValueError("Voltage provided can't be negative.")
        super().__init__(name, complex(cmath.rect(voltage,phase)))
    
