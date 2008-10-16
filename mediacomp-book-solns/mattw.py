from media import *

class BlankPicture(Picture):
    def __init__(self,x=0,y=0):
      self.__class__ = Picture
      self.pic=JavaPicture()
      self.pic.blankImage(x,y)  
      self.pic.setFilename('blank.jpg')   


#!!
#takes an image and changes it into a image of 4x4 blocks of pixels
def mosaicExample():
	img = Picture(pickAFile())
	new = mosaic(img)
	show(new)
	return new

def mosaic(src):
	for y in range(4,src.getHeight(),4):
		for x in range(4,src.getWidth(),4):
			p1 = getPixel(src,x,y)
			p2 = getPixel(src,x-1,y)
			p3 = getPixel(src,x,y-1)
			p4 = getPixel(src,x-1,y-1)
			#red = (getRed(p1) + getRed(p2) + getRed(p3) + getRed(p4))/4
			#blue = (getBlue(p1) + getBlue(p2) + getBlue(p3) + getBlue(p4))/4
			#green = (getGreen(p1) + getGreen(p2) + getGreen(p3) + getGreen(p4))/4
			#newColor = Color(red,green,blue)
			newColor = getColor(p1)
			#setColor(p1,newColor)
			setColor(p2,newColor)
			setColor(p3,newColor)
			setColor(p4,newColor)
	return src
	
#!!
#shift red->green->blue down one
def shiftExample():
	img = Picture(pickAFile())
	new = shiftColors(img)
	new = shiftColors(img)
	show(new)
	return new

def shiftColors(src):
	for x in range(1,src.getHeight()):
		for y in range(1,src.getWidth()):
			p = getPixel(src,y,x)
			setColor(p,Color(getBlue(p),getRed(p),getGreen(p)))
	return src
#!!
#the negative of the image
def negativeExample():
	img = Picture(pickAFile())
	new = negative(img)	
	show(new)
	return new

def negative(src):
	for x in range(1,src.getHeight()):
		for y in range(1,src.getWidth()):
			p = getPixel(src,y,x)
			setColor(p,Color(255-getRed(p),255-getGreen(p),255-getBlue(p)))
	return src
#!!
#splits the image in half vertically and fills in the right half with the mirror image of the left half
def mirrorVertExample():
	img = Picture(pickAFile())
	new = mirrorVert(img)	
	show(new)
	return new

def mirrorVert(src):
	for y in range(1,src.getHeight()):
		for x in range((src.getWidth()/2)+1,src.getWidth()):
			p = getPixel(src,x,y)
			p2 = getPixel(src,((src.getWidth()/2)-(x-(src.getWidth()/2))),y)
			setColor(p,Color(getRed(p2),getGreen(p2),getBlue(p2)))
	return src
#!!
#splits the image in half horizontally and fills in the bottom half with the mirror image of the top half
def mirrorHorizExample():
	img = Picture(pickAFile())
	new = mirrorHoriz(img)	
	show(new)
	return new

def mirrorHoriz(src):
	for x in range(1,src.getWidth()):
		for y in range((src.getHeight()/2)+1,src.getHeight()):
			p = getPixel(src,x,y)
			p2 = getPixel(src,x,((src.getHeight()/2)-(y-(src.getHeight()/2))))
			setColor(p,Color(getRed(p2),getGreen(p2),getBlue(p2)))
	return src
#!!
#computes the image in grey scale 
def greyScaleExample():
	img = Picture(pickAFile())	
	new = greyScale(img)
	show(new)
	return new

def greyScale(src):
	for x in range(1,src.getHeight()):
		for y in range(1,src.getWidth()):
			p = getPixel(src,y,x)
			nC =( getRed(p)+getGreen(p)+getBlue(p) )/ 3
			setColor(p,Color(nC,nC,nC))
	return src
#!!
#selects the blue channel(i also have functions that also select the red and green channels )
def channelExample():
	img = Picture(pickAFile())	
	new = blueChannel(img) #different channels can go here
	show(new)
	return new

def blueRedChannel(src):
	for x in range(1,src.getHeight()):
		for y in range(1,src.getWidth()):
			p = getPixel(src,y,x)			
			setColor(p,Color(getRed(p),0,getBlue(p)))
	return src

def greenRedChannel(src):
	for x in range(1,src.getHeight()):
		for y in range(1,src.getWidth()):
			p = getPixel(src,y,x)			
			setColor(p,Color(getRed(p),getGreen(p),0))
	return src

def greenBlueChannel(src):
	for x in range(1,src.getHeight()):
		for y in range(1,src.getWidth()):
			p = getPixel(src,y,x)			
			setColor(p,Color(0,getGreen(p),getBlue(p)))
	return src

def blueChannel(src):
	for x in range(1,src.getHeight()):
		for y in range(1,src.getWidth()):
			p = getPixel(src,y,x)			
			setColor(p,Color(0,0,getBlue(p)))
	return src

def greenChannel(src):
	for x in range(1,src.getHeight()):
		for y in range(1,src.getWidth()):
			p = getPixel(src,y,x)			
			setColor(p,Color(0,getGreen(p),0))
	return src

def redChannel(src):
	for x in range(1,src.getHeight()):
		for y in range(1,src.getWidth()):
			p = getPixel(src,y,x)			
			setColor(p,Color(getRed(p),0,0))
	return src
#!!
#adds horizontal and vertical lines
def lineExample():
	img = Picture(pickAFile())
	new = verticalLines(img)
	new2 = horizontalLines(img)
	show(new2)
	return new2

def horizontalLines(src):
	for x in range(1,src.getHeight(),5):
		for y in range(1,src.getWidth()):
			setColor(getPixel(src,y,x),black())
	return src

def verticalLines(src):
	for x in range(1,src.getWidth(),5):
		for y in range(1,src.getHeight()):
			setColor(getPixel(src,x,y),black())
	return src

def negGrey():
    pic = Picture(pickAFile())
    greyScale(pic)
    negative(pic)
    show(pic)
    
def blurExample(size):
    pic = Picture(pickAFile())
    newPic = blur(pic,size)
    show(newPic)
    show(pic)
    
def blur(pic,size):
    new = BlankPicture(pic.getWidth(),pic.getHeight())
    for x in range(1,pic.getWidth()):
        print 'On x> ', x
        for y in range(1,pic.getHeight()):
            newClr = blurHelper(pic,size,x-size,y-size)
            setColor(getPixel(new,x,y),newClr)
    return new
    
def blurHelper(pic,size,x,y):
    red,green,blue = 0,0,0
    cnt = 0
    for x2 in range(0,(1+(size*2))):
        if(x+x2 >= 0):       
            if(x+x2 < pic.getWidth()):
                for y2 in range(0,(1+(size*2))):
                    if(y+y2 >= 0):
                        if(y+y2 < pic.getHeight()):
#                            print '---------'
#                            print x
#                            print y
#                            print x2
#                            print y2
#                            print pic.getWidth()
#                            print pic.getHeight()
                            p = getPixel(pic,(x+x2),(y+y2))
                            blue  += getBlue(p)
                            red   += getRed(p)
                            green += getGreen(p)
                            cnt   += 1
    return Color(red/cnt,green/cnt,blue/cnt)                    

#!!
#first rendetion, does not check size of orig and/or dest
def copyPic(orig,dest):
    for x in range(1,orig.getWidth()):
        for y in range(1,orig.getHeight()):
            setColor(getPixel(dest,x,y),getColor(getPixel(orig,x,y)))
            
    
#!!
#Filters only a defined square of the image    
def squareAlter(x,y,w,h,pic):
    new = BlankPicture(pic.getWidth(),pic.getHeight())
    copyPic(pic,new)
    print 'copied'
    for a in range(1,w+1):
        print 'at ',x+a
        for b in range(1,h+1):
            p = getPixel(pic,a+w,b+h)
            nC =( getRed(p)+getGreen(p)+getBlue(p) )/ 3
            setColor(getPixel(new,a+w,b+h),Color(nC,nC,nC))
    return new
                
def findCommon(prcnt,colors):
    lenth = len(colors)
    holder = []
    for o in range(0,lenth):
        holder.append([])
        for i in range(0,lenth):
            if(abs(distance(colors[i],colors[o])) <= 144):#defaults to 10%
                holder[o].append(colors[i])
    max = 0
    for a in range(0,lenth):
        if(len(holder[a]) > len(holder[max])):
            max = a 
    return max
    

            
def oilHelper(pic,size,x,y):
    red,green,blue = 0,0,0
    cnt = 0
    clrs = []
    for x2 in range(0,(1+(size*2))):
        if(x+x2 >= 0):       
            if(x+x2 < pic.getWidth()):
                for y2 in range(0,(1+(size*2))):
                    if(y+y2 >= 0):
                        if(y+y2 < pic.getHeight()):
                            clrs.append(getColor(getPixel(pic,x+x2,y+y2)))
    pClr = findCommon('bla',clrs)                           
    return clrs[pClr]
    
def oil(pic,size=1):
    new = BlankPicture(pic.getWidth(),pic.getHeight())
    show(new)
    for x in range(110,220):
        print 'On x> ', x
        new.repaint()
        for y in range(94,174):
            newClr = oilHelper(pic,size,x-size,y-size)
            setColor(getPixel(new,x,y),newClr)
    return new                           
 
def oilExample():
    new = oil(Picture(pickAFile()),2)
    show(new)
    return new

HE = [[1,1,1],[1,1,1],[1,1,1]]

def convolutionExample():
    pic = Picture(pickAFile())
    show(pic)
    new = convolution(pic,HE)
    show(new)
    return new

def convolution(img,matrix):
    new = BlankPicture(img.getWidth(),img.getHeight())
    show(new)
    for x in range(0,img.getWidth()):
        print 'At x> ',x
        new.pic.repaint()
        for y in range(0,img.getHeight()):              
                pN = getPixel(new,x,y)
                if(len(matrix) == 3):
                    setColor(pN,get3x3Color(img,x,y,matrix))
                elif(len(matrix) == 5):
                    setColor(pN,get5x5Color(img,x,y,matrix))
    return new

def get3x3Color(img,x,y,matrix):
    x = x-1
    y = y-1
    lst = [[0]*3]*3
    for x2 in range(0,3):
        for y2 in range(0,3):     
            if( (x+x2 >= 0) and (y+y2 >= 0) and (x+x2 < img.getWidth()) and (y+y2 < img.getHeight()) ):              
                lst[x2][y2] = getPixel(img,x+x2,y+y2)
    return kernel3x3(lst,matrix)        
            
            
            
def get5x5Color(img,x,y,matrix):
    x -= 2
    y -= 2
    lst = [[0]*5]*5
    for x2 in range(0,3):
        for y2 in range(0,3):     
            if( (x+x2 > 0) and (y+y2 > 0) and (x+x2 < img.getWidth()) and (y+y2 < img.getHeight()) ):
                lst[x2][y2] = getPixel(img,x+x2,y+y2)
    return kernel5x5(lst,matrix)        
    
def kernel3x3(pixels,matrix):
    cnt, red, green, blue = (0,0,0,0)
    for x in range(0,3):
        for y in range(0,3):
            if(pixels[x][y].__class__ == Pixel):
                cnt +=1
                red += pixels[x][y].getColor().getRed() * matrix[x][y]
                green += pixels[x][y].getColor().getGreen() * matrix[x][y]
                blue += pixels[x][y].getColor().getBlue() * matrix[x][y]
         #       print red,' ',green,' ',blue
    return Color(red/cnt,green/cnt,blue/cnt)
    
def kernel5x5():
    cnt, red, green, blue = (0,0,0,0)
    for x in range(0,5):
        for y in range(0,5):
            if(pixels[x][y].__class__ == Pixel):
                cnt +=1
                red += pixels[x][y].getRed() * matrix[x][y]
                green += pixels[x][y].getGreen() * matrix[x][y]
                blue += pixels[x][y].getBlue() * matrix[x][y]
    return Color(red/cnt,green/cnt,blue/cnt)
    
def bluescreenMain():
    pic1 = pickAFile()
    newbg = pickAFile()
    ppic1 = Picture(pic1)
    pnewbg = Picture(newbg)
    newp1 = chromakey(ppic1,pnewbg)
    show(newp1)
    return newp1

def chromakey(source,bg):
    # source should have something in front of blue, bg is the new background
    for x in range(1,source.getWidth()):
        for y in range(1,source.getHeight()):
            p = getPixel(source,x,y)
            if (getRed(p) + getGreen(p) < getBlue(p)+100):            
                setColor(p,Color(255,255,255))
            else:
                setColor(p,Color(0,0,0))                
    return source

def chromakey2(source,bg):
    for p in pixels(source):
        if (getRed(p)+getGreen(p) < getBlue(p)):
            setColor(p,getColor(getPixel(bg,x(p),y(p))))
    return source

def maskExample():
    p = Picture(pickAFile())
    show(p)
    m = mask(p)
    show(m)
    
def mask(source):
    # source should have something in front of blue, bg is the new background
    new = BlankPicture(source.getWidth(),source.getHeight())
    for x in range(1,source.getWidth()):
        for y in range(1,source.getHeight()):
            p = getPixel(source,x,y)
            if (getRed(p) + getGreen(p) < getBlue(p)+100):            
                setColor(getPixel(new,x,y),Color(255,255,255))
            else:
                setColor(getPixel(new,x,y),Color(0,0,0))                
    return new

def chromakey2(source,bg):
    for p in pixels(source):
        if (getRed(p)+getGreen(p) < getBlue(p)):
            setColor(p,getColor(getPixel(bg,x(p),y(p))))
    return source