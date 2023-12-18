in_to_cm = 2.45
cm_to_in = 0.3937

class InchMeasurement(float):
    def __add__(self, other):
        if not isinstance(other, InchMeasurement):
            raise TypeError('You can only add inch measurements to other inch measurements')

        return InchMeasurement(float(self) + float(other))

    def __sub__(self, other):
        if not isinstance(other, InchMeasurement):
            raise TypeError('You can only subtract inch measurements to other inch measurements')

        return InchMeasurement(float(self) - float(other))

    def to_cm(self):
        return CentimeterMeasurement(float(self) * in_to_cm)

class CentimeterMeasurement(float):
    def __add__(self, other):
        if not isinstance(other, CentimeterMeasurement):
            raise TypeError('You can only add centimeter measurements to other centimeter measurements')

        return CentimeterMeasurement(float(self) + float(other))

    def __sub__(self, other):
        if not isinstance(other, CentimeterMeasurement):
            raise TypeError('You can only subtract centimeter measurements to other centimeter measurements')

        return CentimeterMeasurement(float(self) - float(other))
    
    def to_in(self):
        return InchMeasurement(float(self) * cm_to_in)

x = InchMeasurement(5)
y = CentimeterMeasurement(10)
z = InchMeasurement(12)

# print(x + y)

print(x.to_cm() + y)
print(y.to_in())