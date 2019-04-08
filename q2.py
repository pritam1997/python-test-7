class Rectangle:

	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area_of_rectangle(self):
		area = self.length * self.width
		return round(area,2)

o1 = Rectangle(5,3.123)
print(o1.area_of_rectangle())