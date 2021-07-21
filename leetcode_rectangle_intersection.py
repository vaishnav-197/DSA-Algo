def isRectangleOverlap(rec1 , rec2):



    # lower and upper limit of coord
    xl=rec1[0]
    xh=rec1[3]

    yl=rec1[1]
    yh=rec1[3]

    # all x and y values of second Rectangle

    r2x= [rec2[0],rec2[2]]
    r2y= [rec2[1],rec2[3]]

    # check if they overlap


    flagx=0
    flagy=0

    for i in r2x:
        if i < xh and i>xl:
            print(i)
            flagx=1 

    for i in r2y:
        if i < yh and i>yl:
            
            flagy=1

    if flagy ==1 and flagx ==1 :
        return True
    else:
        return False


print(isRectangleOverlap([7,8,13,15],[10,8,12,20]))