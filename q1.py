import math
class Circle:
	def __init__(self,radius):
		self.radius=radius

	def areaofcircle(self):
		area = math.pi * self.radius
		return round(area,2)

circle1 = Circle(5)
print(circle1.areaofcircle())
