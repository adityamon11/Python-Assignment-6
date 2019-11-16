class Arithmetic:
	def __init__(self):
		self.value1=0;
		self.value2=0;

	def Accept(self,n1,n2):
		self.value1=n1;
		self.value2=n2;

	def Addition(self):
		return self.value1+self.value2;

	def Subtraction(self):
		return self.value1-self.value2;

	def Multiplication(self):
		return self.value1*self.value2;

	def Division(self):
		return self.value1/self.value2;

def main():
	a = Arithmetic();
	x=int(input("Enter a number"));
	y=int(input("Enter a number"));
	a.Accept(x,y);
	print("Addition is ",a.Addition());
	print("Subtraction is ",a.Subtraction());
	print("Multiplication is ",a.Multiplication());
	print("Division is ",a.Division());

	b = Arithmetic();
	x=int(input("Enter a number"));
	y=int(input("Enter a number"));
	b.Accept(x,y);
	print("Addition is ",b.Addition());
	print("Subtraction is ",b.Subtraction());
	print("Multiplication is ",b.Multiplication());
	print("Division is ",b.Division());

if __name__ == '__main__':
	main();