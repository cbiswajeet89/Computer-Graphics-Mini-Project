import numpy as np
import matplotlib.pyplot as plt
import math

def midpoint_ellipse(xc,yc,rx_1,ry_1):
	rx=rx_1/2
	ry=ry_1/2
	X=[0]
	Y=[ry]
	x=0
	y=ry
	dx=2*pow(ry,2)*x
	dy=2*pow(rx,2)*y
	p1=pow(ry,2)-(pow(rx,2)*ry)+(pow(rx,2)/4)
	while dx<dy:
		if p1<0:
			x=x+1
			dx=2*x*pow(ry,2)
			p1=p1+dx+pow(ry,2)
			X.append(x)
			Y.append(y)
		else:
			x=x+1
			y=y-1
			dx=2*x*pow(ry,2)
			dy=2*y*pow(rx,2)
			p1=p1+dx+pow(ry,2)-dy
			X.append(x)
			Y.append(y)
	p2=(pow(ry,2)*pow((X[-1]+0.5),2))+(pow(rx,2)*pow((Y[-1]-1),2))-(pow(rx,2)*pow(ry,2))
	while(y>0):
		if p2>0:
			y=y-1
			dy=2*y*pow(rx,2)
			p2=p2-dy+pow(rx,2)
			if(y<0):
				break
			else:
				X.append(x)
				Y.append(y)
		else:
			x=x+1
			y=y-1
			dx=2*x*pow(ry,2)
			dy=2*y*pow(rx,2)
			p2=p2+dx-dy+pow(rx,2)
			if(y<0):
				break
			else:
				X.append(x)
				Y.append(y)
	X_1=[]
	Y_1=[]
	X_neg = list(map(lambda x:-x, X))
	Y_neg = list(map(lambda x:-x, Y))
	X_new = [X,X,X_neg,X_neg]
	Y_new = [Y,Y_neg,Y_neg,Y]
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
	rx_1=int(input("Enter major axis of the ellipse : "))
	ry_1=int(input("Enter minor axis of the ellipse : "))

