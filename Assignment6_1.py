class Demo:
	value=0;

	def __init__(self,val1,val2):
		self.no1=val1;
		self.no2=val2;

	def fun(self):
		print("inside fun");
		print(self.no1);
		print(self.no2);

	def gun(self):
		print("inside gun");
		print(self.no1);
		print(self.no2);		

def main():
	x=int(input("Enter a number"));
	y=int(input("Enter a number"));
	a=int(input("Enter a number"));
	b=int(input("Enter a number"));
	obj1 = Demo(x,y);
	obj2 = Demo(a,b);
	obj1.fun();
	obj2.fun();
	obj1.gun();
	obj2.gun();

if __name__ == '__main__':
		main();