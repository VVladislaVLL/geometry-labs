from math import *

from classes.Point import Point


class Vector3d:
  def __init__(self, point1, point2, point3):
    if type(point1) == Point:
      self.x = point2.x - point1.x
      self.y = point2.y - point1.y
      self.z = point2.z - point1.z
    else:
      self.x = point1
      self.y = point2
      self.z = point3

  def __str__(self):
    return '[' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ']'

  @staticmethod
  def get_length(p1, p2):
    return sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 + (p2.z - p1.z) ** 2)

  @staticmethod
  def scalar_product(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

  #
  # @staticmethod
  # def get_vector(alpha, speed=1):
  #   return Vector3d(speed * cos(alpha), speed * sin(alpha)), speed

  @staticmethod
  def s_mult(v, scalar):
    new_vector = Vector3d(v.x * scalar, v.y * scalar, v.z * scalar)
    return new_vector

  @staticmethod
  def s_minus(v1, v2):
    new_vector = Vector3d(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
    return new_vector

  @staticmethod
  def vect_product(v1, v2):
    return Vector3d(v1.y * v2.z - v2.y * v1.z, v2.x * v1.z - v1.x * v2.z, v1.x * v2.y - v2.x * v1.y)
