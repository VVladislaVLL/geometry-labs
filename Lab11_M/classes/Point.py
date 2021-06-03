import copy


class Point:
  def __init__(self, x, y, z = 0):
    self.x = x
    self.y = y
    self.z = z

  def __str__(self):
    return f'''
        Point:
            x: {self.x}
            y: {self.y}
            z: {self.z}
        '''

  def __eq__(self, other):
    if not isinstance(other, Point):
      return NotImplemented
    return self.x == other.x and self.y == other.y and self.z == other.z

  def __hash__(self):
    return hash((self.x, self.y, self.z))

  def print(self):
    print('(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')')

  def reverse(self):
    return Point(-self.x, -self.y, -self.z)

  @staticmethod
  def get_center(p1, p2):
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2, 0)
