class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def __contains__(self, other):
        if isinstance(other, tuple):
            if len(other) == 2:
                if (other[0]-self.centre[0]) ** 2 + (other[1]-self.centre[1]) ** 2 <= self.radius:
                    return True
                else:
                    return False
            else:
                return NotImplemented
        else:
            return NotImplemented
