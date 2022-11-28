import cmath


class ComplexNumer:
    omega = 0

    def __init__(self, name: str, complex: complex):
        self.name = name
        self.value = complex

    # def getName(self):
    #     return f'{self=}'.split('=')[0]

    def module(self):
        return abs(self.value)

    def phase(self):
        return cmath.phase(self.value)

    def toExp(self) -> str:
        phase = self.phase()
        COMMONPHASES = {
            cmath.pi/2: "pi/2",
            -(cmath.pi/2): "- pi/2",
            cmath.pi: "pi"
        }
        phaseStr = COMMONPHASES.get(phase, phase.__round__(2))
        return f"{self.module().__round__(2)} e j({phaseStr})"

    def toRect(self) -> str:
        return f"{self.value.real.__round__(2)} {'+' if self.value.imag > 0 else '-'} {abs(self.value.imag.__round__(2))}j"

    def setOmega(self, newOmega):
        self.omega = newOmega

    def getOmega(self):
        return self.omega


class Resistor(ComplexNumer):
    def __init__(self, name: str, resistorValue: float):
        if resistorValue < 0:
            raise ValueError("Resistor value provided can't be negative.")
        super().__init__(name, complex(resistorValue, 0))


class Inductor(ComplexNumer):
    def __init__(self, name: str, inductorValue: float):
        if inductorValue < 0:
            raise ValueError("Inductor value provided can't be negative.")
        super().__init__(name, complex(0, self.getOmega() * inductorValue))


class Capacitor(ComplexNumer):
    def __init__(self, name: str, capacitorValue: float):
        if capacitorValue < 0:
            raise ValueError("Capacitor value provided can't be negative.")
        super().__init__(name, complex(0, -(1 / self.getOmega() * capacitorValue)))


class Source(ComplexNumer):
    def __init__(self, name: str, module: float, phase: float):
        super().__init__(name, complex(cmath.rect(module, phase)))

    def toFunction(self):
        return f"{self.name}(t) = {self.module().__round__(2)}.sin( {self.getOmega().__round__(2)}.t + {self.phase().__round__(2)} )"


class VoltageSource(Source):
    def __init__(self, name: str, voltage: float, phase: float):
        if voltage < 0:
            raise ValueError("Voltage provided can't be negative.")
        super().__init__(name, voltage, phase)


class CurrentSource(Source):
    def __init__(self, name: str, current: float, phase: float):
        if current < 0:
            raise ValueError("Current provided can't be negative.")
        super().__init__(name, current, phase)
