class Road:

    def __init__(self, _length, _width, _weight, _thickness):
        self.length = _length
        self.width = _width
        self.weight = _weight
        self.thickness = _thickness

    def intake(self):

        intake = self.length * self.width * self.weight * self.thickness / 1000
        print(f'Для данного проетка требуется {intake} т асфальта.')


road_to_village = Road(20000, 5, 25, 4)
road_to_village.intake()
