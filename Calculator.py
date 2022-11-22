from ComplexNumer import ComplexNumer
import re


class Calculator(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super( Calculator, cls).__new__(cls)
        return cls.instance

    def sum(self, complexName: str, a: ComplexNumer, b: ComplexNumer,
            verbose=False) -> ComplexNumer:
        result = ComplexNumer(complexName, a.value+b.value)
        if verbose:
            print(f"{result.name} = {a.name} + {b.name}")
            print(f"{result.name} = {a.toRect()} + {b.toRect()}")
            print(f"{result.name} = {result.value:.2f}")
            print("\n\n")
        return result

    def diff(self, complexName: str, a: ComplexNumer, b: ComplexNumer,
             verbose=False) -> ComplexNumer:

        result = ComplexNumer(complexName, a.value-b.value)

        if verbose:
            print(f"{result.name} = {a.name} - {b.name}")
            print(f"{result.name} = {a.toRect()} - {b.toRect()}")
            print(f"{result.name} = {result.value:.2f}")
            print("\n\n")
        return result

    def product(self, complexName: str, a: ComplexNumer, b: ComplexNumer,
                verbose=False) -> ComplexNumer:
        result = ComplexNumer(complexName, a.value*b.value)

        if verbose:
            print(f"{result.name} = {a.value} * {b.value}")
            print(f"{result.name} = {a.toRect()} * {b.toRect()}")
            print(f"{result.name} = {result.value:.2f}")
            print("\n\n")
        return result

    def division(self, complexName: str, a: ComplexNumer, b: ComplexNumer,
                 verbose=False) -> ComplexNumer:
        result = ComplexNumer(complexName, a.value/b.value)
        if verbose:
            print(f"{self.toSpaces(result.name)}   {a.name}   {a.toExp()}")
            
            print(f"{result.name} = {self.toHyphen(max(a.name,b.name))} = {self.toHyphen(max(a.toExp(),b.toExp()))} = {result.toExp()}")
            
            print(f"{self.toSpaces(result.name)}   {b.name}   {b.toExp()}")

            print("\n\n")

        return result

    def toSpaces(self, txt: str) -> str:
        return re.sub('.', ' ', txt)

    def toHyphen(self, txt: str) -> str:
        return re.sub('.', '-', txt)

    def paralel(self, complexName: str, a: ComplexNumer, b: ComplexNumer, verbose=False) -> ComplexNumer:
        result = ComplexNumer(
            complexName, (a.value * b.value) / (a.value + b.value))
        if verbose:
            n1 = a.name + " * " + b.name
            d1 = a.name + " + " + b.name
            n2 = a.toExp() + " * " + b.toExp()
            d2 = a.toRect() + " + " + b.toRect()
            n3 = self.product("", a, b).toExp()
            d3 = self.sum("", a, b).toExp()
            w2 = len(max(n2,d2))
            w3 = len(max(n3,d3))
            print(
                f"{self.toSpaces(result.name)}   {n1}   {n2:{w2}}   {n3:{w3}}")
            print(
                f"{result.name} = {self.toHyphen(max(n1,d1))} = {self.toHyphen(max(n2,d2))} = {self.toHyphen(max(n3,d3))} = {result.toExp()}")
            print(
                f"{self.toSpaces(result.name)}   {d1}   {d2:{w2}}   {d3:{w3}}")
            print("\n\n")
        return result

    def voltageDivider(self, complexName: str, v: ComplexNumer,
                       z1: ComplexNumer, z2: ComplexNumer, verbose=False) -> ComplexNumer:
        if verbose:
            result = ComplexNumer(complexName, v.value * (z1.value / (z1.value + z2.value)))
            d1 = z1.name + " + " + z2.name
            d2 = z1.toRect() + " + " + z2.toRect()
            d3 = self.sum("",z1,z2).toExp()
            n3 = z1.toExp()
            division = self.division("", z1, self.sum("", z1, z2))
            print(
                f"{self.toSpaces(result.name)}   {self.toSpaces(v.name)}   {z1.name:{len(d1)}}    {self.toSpaces(v.toExp())}  {z1.toExp():{len(d2)}} {self.toSpaces(v.toExp())}     {n3:{len(n3)}}")
            
            print(
                f"{result.name} = {v.name} * {self.toHyphen(d1)} = {v.toExp()} * {self.toHyphen(d2)} = {v.toExp()} * {self.toHyphen(max(n3,d3))} = {v.toExp()} * {division.toExp()} = {result.toExp()}")
            
            print(
                f"{self.toSpaces(result.name)}   {self.toSpaces(v.name)}   {d1}    {self.toSpaces(v.toExp())}  {d2} {self.toSpaces(v.toExp())}     {d3}")
            print("\n\n")
        return result

    def currentDivider(self, complexName: str, i: ComplexNumer,
                       z1: ComplexNumer, z2: ComplexNumer, verbose=False) -> ComplexNumer:
        
        result = ComplexNumer(complexName, i.value * (z2.value / (z1.value + z2.value)))
        
        if verbose:
            d1 = z1.name + " + " + z2.name
            d2 = z1.toRect() + " + " + z2.toRect()
            d3 = self.sum("",z1,z2).toExp()
            division = self.division("", z2, self.sum("", z1, z2))
            print(
                f"{self.toSpaces(result.name)}   {self.toSpaces(i.name)}   {z2.name:{len(d1)}}    {self.toSpaces(i.toExp())}  {z2.toExp():{len(d2)}} {self.toSpaces(i.toExp())}     {z2.toExp():{len(d2)}}")
            
            print(
                f"{result.name} = {i.name} * {self.toHyphen(d1)} = {i.toExp()} * {self.toHyphen(d2)} = {i.toExp()} * {self.toHyphen(d3)} = {i.toExp()} * {division.toExp()} = {result.toExp()}")
            
            print(
                f"{self.toSpaces(result.name)}   {self.toSpaces(i.name)}   {d1}    {self.toSpaces(i.toExp())}  {d2} {self.toSpaces(i.toExp())}     {d3}")
            print("\n\n")
        return result

    def power(self, complexName: str, v: ComplexNumer, i: ComplexNumer,
              verbose=False) -> ComplexNumer:

        result = ComplexNumer(complexName, 1/2 * v.value * i.value.conjugate())
        if verbose:
            iConj = ComplexNumer("",i.value.conjugate())
            print(f"{result.name} = 1/2 * {v.toExp()} * ~({i.toExp()}) = 1/2 * {v.toExp()} * {iConj.toExp()}")
            print(f"{result.name} = {result.toExp()}")
            print(f"S* = {result.toExp()}")
            print(f"S = {abs(result.value)}[V.A]")
            print(f"P = {result.value.real:.2f}[W]")
            print(f"Q = {result.value.imag:.2f}[V.A.R]")
            print("\n\n")
        return result


calc = Calculator()
