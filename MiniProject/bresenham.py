def drawBresenham(x1, y1, x2, y2): 
    x_data = []
    y_data = []
    x_data.append(x1)
    y_data.append(y1)
    dx = abs(x2 - x1) 
    dy = abs(y2 - y1)  
    if (x2 > x1): 
        xs = 1
    else: 
        xs = -1
    if (y2 > y1): 
        ys = 1
    else: 
        ys = -1
  
    if (dx > dy):         
        p1 = 2 * dy - dx 
        while (x1 != x2): 
            x1 += xs 
            if (p1 >= 0): 
                y1 += ys 
                p1 -= 2 * dx 
            p1 += 2 * dy 
            x_data.append(x1)
            y_data.append(y1)
  
    elif (dy >= dx):        
        p1 = 2 * dx - dy 
        while (y1 != y2): 
            y1 += ys 
            if (p1 >= 0): 
                x1 += xs 
                p1 -= 2 * dy 
            p1 += 2 * dx 
            x_data.append(x1)
            y_data.append(y1)
    return x_data,y_data