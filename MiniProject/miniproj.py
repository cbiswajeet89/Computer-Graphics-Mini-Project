import math
import matplotlib.pyplot as plt
import mcda as circle
import meda as ellipse
import bresenham as line

def entercircle():		#Input function for Circle
	xc=int(input("Enter x center coordinate: "))
	yc=int(input("Enter y center coordinate: "))
	r=int(input("Enter radius of the circle: "))
	return xc,yc,r
def enterellipse():		#Input function for ellipse
	xc=int(input("Enter x center coordinate: "))
	yc=int(input("Enter y center coordinate: "))
	rx_1=int(input("Enter major axis of the ellipse: "))
	ry_1=int(input("Enter minor axis of the ellipse: "))
	return xc,yc,rx_1,ry_1
def enterpolygon():
	x=[]
	y=[]
	n=int(input("Enter number of sides of the Polygon: "))
	print("Enter coordinates: ")
	for i in range(n):
		p,q=map(int,input().split())
		x.append(p)
		y.append(q)
	x.append(x[0])
	y.append(y[0])
	return x,y,n

def creatematrix(a,b,c,d,tx,ty,e,f):		#Creation of 3*3 homogenous matrix
	m=[[a,b,tx],[c,d,ty],[e,f,1]]
	return m

def multiply(a,b,r,c):		#Function for matrix multiplication
	res = [[0 for i in range(c)] for j in range(r)]
	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(b)):
				res[i][j]+=a[i][k]*b[k][j]
	return res

def translate(x,y,a,b,p,q,m):		#Translation function
	for i in range(len(x)):
		pxy=[[x[i]],[y[i]],[1]]
		res=multiply(m,pxy,3,1)
		x[i]=res[0][0]
		y[i]=res[1][0]
	for i in range(len(a)):
		pxy=[[a[i]],[b[i]],[1]]
		res=multiply(m,pxy,3,1)
		a[i]=res[0][0]
		b[i]=res[1][0]
	for i in range(len(p)):
		pxy=[[p[i]],[q[i]],[1]]
		res=multiply(m,pxy,3,1)
		p[i]=res[0][0]
		q[i]=res[1][0]
	return x,y,a,b,p,q

def scale(x,y,a,b,p,q,m):		#Scaling function
	for i in range(len(x)):
		pxy=[[x[i]],[y[i]],[1]]
		res=multiply(m,pxy,3,1)
		x[i]=res[0][0]
		y[i]=res[1][0]
	for i in range(len(a)):
		pxy=[[a[i]],[b[i]],[1]]
		res=multiply(m,pxy,3,1)
		a[i]=res[0][0]
		b[i]=res[1][0]
	for i in range(len(p)):
		pxy=[[p[i]],[q[i]],[1]]
		res=multiply(m,pxy,3,1)
		p[i]=res[0][0]
		q[i]=res[1][0]
	return x,y,a,b,p,q

def rotate(x,y,a,b,p,q,m):		#Rotation function
	for i in range(len(x)):
		pxy=[[x[i]],[y[i]],[1]]
		res=multiply(m,pxy,3,1)
		x[i]=res[0][0]
		y[i]=res[1][0]
	for i in range(len(a)):
		pxy=[[a[i]],[b[i]],[1]]
		res=multiply(m,pxy,3,1)
		a[i]=res[0][0]
		b[i]=res[1][0]
	for i in range(len(p)):
		pxy=[[p[i]],[q[i]],[1]]
		res=multiply(m,pxy,3,1)
		p[i]=res[0][0]
		q[i]=res[1][0]
	return x,y,a,b,p,q

def shear(x,y,a,b,p,q,m):		#Shearing function
	for i in range(len(x)):
		pxy=[[x[i]],[y[i]],[1]]
		res=multiply(m,pxy,3,1)
		x[i]=res[0][0]
		y[i]=res[1][0]
	for i in range(len(a)):
		pxy=[[a[i]],[b[i]],[1]]
		res=multiply(m,pxy,3,1)
		a[i]=res[0][0]
		b[i]=res[1][0]
	for i in range(len(p)):
		pxy=[[p[i]],[q[i]],[1]]
		res=multiply(m,pxy,3,1)
		p[i]=res[0][0]
		q[i]=res[1][0]
	return x,y,a,b,p,q

def reflect(x,y,a,b,p,q,m):		#Reflection function
    for i in range(len(x)):
        pxy=[[x[i]],[y[i]],[1]]
        res=multiply(m,pxy,3,1)
        x[i]=res[0][0]
        y[i]=res[1][0]
    for i in range(len(a)):
        pxy=[[a[i]],[b[i]],[1]]
        res=multiply(m,pxy,3,1)
        a[i]=res[0][0]
        b[i]=res[1][0]
    for i in range(len(p)):
    	pxy=[[p[i]],[q[i]],[1]]
    	res=multiply(m,pxy,3,1)
    	p[i]=res[0][0]
    	q[i]=res[1][0]
    return x,y,a,b,p,q

def composition(x,y,a,b,p,q,v):		#Composite function
	c=[]
	d=[]
	e=[]
	for i in range(len(x)):
		c.append([x[i],y[i],1])
	for i in range(len(a)):
		d.append([a[i],b[i],1])
	for i in range(len(p)):
		e.append([p[i],q[i],1])
	res=[[1,0,0],[0,1,0],[0,0,1]]
	for i in range(len(v)):
		res=multiply(res,v[i],3,3)
	res1=multiply(c,res,len(x),3)
	res2=multiply(d,res,len(a),3)
	res3=multiply(e,res,len(p),3)
	for i in range(len(x)):
		x[i]=res1[i][0]
		y[i]=res1[i][1]
	for i in range(len(a)):
		a[i]=res2[i][0]
		b[i]=res2[i][1]
	for i in range(len(p)):
		p[i]=res3[i][0]
		q[i]=res3[i][1]
	return x,y,a,b,p,q


if __name__ == "__main__":

	print("Please Enter the shape or figure required ")
	choice=int(input(("1.Circle \n2.Ellipse \n3.N-Sided Polygon\n4.All\n")))
	x=[]
	y=[]
	a=[]
	b=[]
	p=[]
	q=[]
	if(choice==1):
		xc,yc,r=entercircle()
		x,y=circle.midpoint_circle(xc,yc,r)
		plt.scatter(x,y,color='red',label='Original figure')
	elif(choice==2):
		xc,yc,rx_1,ry_1=enterellipse()
		x,y=ellipse.midpoint_ellipse(xc,yc,rx_1,ry_1)		
		plt.scatter(x,y,color='red',label='Original figure')
	elif(choice==3):
		xl=[]
		yl=[]
		xl,yl,n=enterpolygon()
		for i in range(n):
			xc=[]
			yc=[]
			xc,yc=line.drawBresenham(xl[i],yl[i],xl[i+1],yl[i+1])
			x.extend(xc)
			y.extend(yc)
		plt.scatter(x,y,color='red',label='Original figure')
	elif(choice==4):
		print("\nEnter coordinates for circle\n")
		xc,yc,r=entercircle()
		x,y=circle.midpoint_circle(xc,yc,r)
		plt.scatter(x,y,color='red',label='Original figure')
		print("\nEnter coordinates for ellipse\n ")
		xc,yc,rx_1,ry_1=enterellipse()
		a,b=ellipse.midpoint_ellipse(xc,yc,rx_1,ry_1)	
		plt.scatter(a,b,color='red')
		print("\nEnter coordinates for Polygon\n ")
		xl=[]
		yl=[]
		xl,yl,n=enterpolygon()
		for i in range(n):
			xc=[]
			yc=[]
			xc,yc=line.drawBresenham(xl[i],yl[i],xl[i+1],yl[i+1])
			p.extend(xc)
			q.extend(yc)
		plt.scatter(p,q,color='red')
	print("Enter the Transformation required")
	choice=int(input(("1.Translation \n2.Scaling \n3.Rotation \n4.Shearing \n5.Reflection\n6.Composite\n")))
	if(choice==1):
		tx=int(input("Enter translation in x axis: "))
		ty=int(input("Enter translation in y axis: "))
		m=creatematrix(1,0,0,1,tx,ty,0,0)
		x,y,a,b,p,q=translate(x,y,a,b,p,q,m)
	elif(choice==2):
		sx=float(input("Enter the scale factor in x direction: "))
		sy=float(input("Enter the scale factor in y direction: "))
		m=creatematrix(sx,0,0,sy,0,0,0,0)
		x,y,a,b,p,q=scale(x,y,a,b,p,q,m)
	elif(choice==3):
		angle=float(input("Enter the rotation angle: "))
		ch=int(input("Enter \n1.Clockwise rotation \n2.Anti-Clockwise rotation\n"))
		c=math.cos(angle*math.pi/180)
		s=math.sin(angle*math.pi/180)
		if(ch==1):
			m=creatematrix(c,-s,s,c,0,0,0,0)
		elif(ch==2):
			m=creatematrix(c,s,-s,c,0,0,0,0)
		x,y,a,b,p,q=rotate(x,y,a,b,p,q,m)
	elif(choice==4):
		h=float(input("Enter shearing factor in x direction: "))
		g=float(input("Enter shearing factor in y direction: "))
		m=creatematrix(1,h,g,1,0,0,0,0)
		x,y,a,b,p,q=shear(x,y,a,b,p,q,m)
	elif(choice==5):
	    ch=int(input("1.Reflection about X-Axis\n2.Reflection about Y-Axis\n3.Reflection about an axis perpendicular to xy plane and passing through origin\n4.Reflection about line y=x\n"))
	    if(ch==1):
	        m=creatematrix(1,0,0,-1,0,0,0,0)
	        x,y,a,b,p,q=reflect(x,y,a,b,p,q,m)
	    elif(ch==2):
	        m=creatematrix(-1,0,0,1,0,0,0,0)
	        x,y,a,b,p,q=reflect(x,y,a,b,p,q,m)
	    elif(ch==3):
	        m=creatematrix(-1,0,0,-1,0,0,0,0)
	        x,y,a,b,p,q=reflect(x,y,a,b,p,q,m)
	    elif(ch==4):
	        m=creatematrix(0,1,1,0,0,0,0,0)
	        x,y,a,b,p,q=reflect(x,y,a,b,p,q,m)
	elif(choice==6):
		v=[]
		while True:
			ch=int(input("Enter choice (-1 to quit):\n1.Translation \t2.Scaling \t3.Rotation \t4.Shearing\n"))
			if(ch==-1):
				break
			elif(ch==1):
				tx=int(input("Enter translation in x axis: "))
				ty=int(input("Enter translation in y axis: "))
				m=creatematrix(1,0,0,1,0,0,tx,ty)
				v.append(m)
			elif(ch==2):
				sx=float(input("Enter the scale factor in x direction: "))
				sy=float(input("Enter the scale factor in y direction: "))
				m=creatematrix(sx,0,0,sy,0,0,0,0)
				v.append(m)
			elif(ch==3):
				angle=int(input("Enter the rotation angle: "))
				k=int(input("Enter \n1.Clockwise rotation \n2.Anti-Clockwise rotation\n"))
				c=math.cos(angle*math.pi/180)
				s=math.sin(angle*math.pi/180)
				if(k==1):
					m=creatematrix(c,-s,s,c,0,0,0,0)
				elif(k==2):
					m=creatematrix(c,s,-s,c,0,0,0,0)
				v.append(m)
			elif(ch==4):
				g=float(input("Enter shearing factor in x direction: "))
				h=float(input("Enter shearing factor in y direction: "))
				m=creatematrix(1,h,g,1,0,0,0,0)
				v.append(m)
		x,y,a,b,p,q=composition(x,y,a,b,p,q,v)
	plt.scatter(x,y,color='blue',label='Transformed figure')
	plt.scatter(a,b,color='blue')
	plt.scatter(p,q,color='blue')	
	plt.title("2-D Transformation")
	plt.xlabel("X-Axis")
	plt.ylabel("Y-Axis")
	plt.legend()
	plt.grid()
	plt.show()



