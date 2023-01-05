import numpy as np

def bisection_v1(func, interval: np.array, Ilimit: int = 65536, tolerance: float = 0.00000000000000001):
	a = interval[0]
	b = interval[1] 
	if func(a)*func(b)>0:
		raise Exception("No hay una raíz en el intervalo dado")
	else:
		print("{:<6} {:<32} {:<32} {:<32} {:<32} {:<32} {:<32}".format("i","a","func(a)","b","func(b)","c","func(c)"))
		for i in range(Ilimit):
			c = (a+b)/2
			print("{:<6} {:<32} {:<32} {:<32} {:<32} {:<32} {:<32}".format(i,a,func(a),b,func(b),c,func(c)))
			if np.abs(func(c)) <= tolerance or func(c)==0:
				return c
			else:
				if func(a)*func(c) < 0:
					b = c
				else:
					a = c

def funcion(x):
	return (3*x**2)-(2*x)-(4)

if __name__ == "__main__":
	interval = np.array([-1,0])
	print(bisection_v1(funcion, interval))
