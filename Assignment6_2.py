class Circle:
	PI = 3.14;
	def __init__(self):
		self.radius=0.0;
		self.area=0.0;
		self.circumference=0.0;

	def Accept(self,n1):
		self.radius=n1;

	def CalculateArea(self):
		self.area = self.PI*self.radius*self.radius;

	def CalculateCircumference(self):
		self.circumference=2*self.PI*self.radius;

	def Display(self):
		print("Radius",self.radius);
		print("Area",self.area);
		print("Circumference",self.circumference);

def main():
	c = Circle();
	x = int(input("Enter the radius"));
	c.Accept(x);
	c.CalculateArea();
	c.CalculateCircumference();
	c.Display();

	d = Circle();
	y = int(input("Enter the radius"));
	d.Accept(y);
	d.CalculateArea();
	d.CalculateCircumference();
	d.Display();


if __name__ == '__main__':
	main();



