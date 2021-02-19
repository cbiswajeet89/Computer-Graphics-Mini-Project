import numpy as np
import matplotlib.pyplot as plt

def midpoint_circle(xc,yc,r):
	X=[0]
	Y=[r]
	x,y=0,r
	p_c=(5/4)-r
	while x<=y:
		if p_c<0:
			p_c=p_c+(2*x)+3
			x=x+1
			if(x>y):
				break
			else:
				X.append(x)
				Y.append(y)
		else:
			p_c=p_c+(2*(x-y))+5
			y=y-1
			x=x+1
			if(x>y):
				break
			else:
				X.append(x)
				Y.append(y)
	X_1=[]
	Y_1=[]
	X_rev = []
	Y_rev = []
	X_rev.extend(Y)
	X_neg = list(map(lambda x:-x, X))
	X_rev_neg = list(map(lambda x:-x,X_rev))
	Y_rev.extend(X)
	Y_neg = list(map(lambda x:-x, Y))
	Y_rev_neg = list(map(lambda x:-x,Y_rev))
	X_new = [X,X_rev,X_rev,X,X_neg,X_rev_neg,X_rev_neg,X_neg]
	Y_new = [Y,Y_rev,Y_rev_neg,Y_neg,Y_neg,Y_rev_neg,Y_rev,Y]
	for i in X_new :		
		X_1.extend(i)
	for i in Y_new :		
		Y_1.extend(i)
	if xc==0 and yc==0 :
		"""for i in range(len(X_1)):
			print('x = ', X_1[i],'y = ', Y_1[i])
		plt.scatter(X_1,Y_1)
		plt.show()"""
		return X_1,Y_1
	elif xc!=0 or yc!=0 :
		X1 = list(map(lambda x:x+xc,X_1))
		Y1 = list(map(lambda x:x+yc,Y_1))
		"""for i in range(len(X1)):
			print('x = ', X1[i],'y = ', Y1[i])
		plt.scatter(X1,Y1)
		plt.show()"""
		return X1,Y1
if __name__ == "__main__":
	xc=int(input("Enter x center coordinate : "))
	yc=int(input("Enter y center coordinate : "))
	r=int(input("Enter radius of the circle : "))


