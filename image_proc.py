from cImage import *

def flip_horizontal(img):
    """Flip the specified image left to right and return the modified image"""
    return img

def sepia_tone(img):
    """Apply the sepia tone transformation to the specified image, and return the modified image"""
    width = img.getWidth()
    height = img.getHeight()
    new_img = EmptyImage(width, height)
    
    for x in range(width):
        for y in range(height):
            p = img.getPixel(x, y)
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()
            
            new_red = min(round(red * 0.393 + green * 0.769 + blue * 0.189), 255)
            new_green = min(round(red * 0.349 + green * 0.686 + blue * 0.168), 255)
            new_blue = min(round(red * 0.272 + green * 0.534 + blue * 0.131), 255)
            
            new_pixel = Pixel(new_red, new_green, new_blue)
            new_img.setPixel(x, y, new_pixel)
    return new_img

def convert_to_gray_scale(img):
    """Apply the gray scale transformation to the specified image, and return the modified image"""
    width = img.getWidth()
    height = img.getHeight()
    new_img = EmptyImage(width, height)
    
    for x in range(width):
        for y in range(height):
            p = img.getPixel(x, y)
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()
            
            new_pixel_color = min(round(red * 0.21 + green * 0.71 + blue * 0.07), 255)
            
            new_pixel = Pixel(new_pixel_color, new_pixel_color, new_pixel_color,)
            new_img.setPixel(x, y, new_pixel)
    return new_img

def flip_vertical(img):
    """Flip the specified image upside down and return the modified image"""
    width = img.getWidth()
    height = img.getHeight()
    new_img = EmptyImage(width, height)
    
    for y in range(height // 2):
        for x in range(width):
            tmp_pixel = img.getPixel(x, y)
            
            new_img.setPixel(x, y, img.getPixel(x, height - y - 1))
            new_img.setPixel(x, height - y - 1, tmp_pixel)
    return new_img

def rotate_right_90(img):
    """Rotate the specified image 90 degrees to the right and return the modified image"""
    
    return img

#construct a new image that
#is a copy of img in which
#each pixel retains all the red
#and loses the green and blue components.
#the function returns the modified image
def red_filter(img):
    """Apply the red filter transformation to the specified image, and return the modified image"""
    
    w = img.getWidth()
    h = img.getHeight()

    newimg = EmptyImage(w,h)
    
    for y in range(h):
        for  x in range(w):
           p = img.getPixel(x,y)


           newpixel = Pixel(p.getRed(),0,0)

           newimg.setPixel(x,y,newpixel)

    return newimg

#construct a new image that
#is a copy of img in which
#each pixel's red, green, and blue
#components are replaced with their complement with respect to 255
#the function returns the modified image
def negative(img):
    """Apply the negative transformation to the specified image, and return the modified image"""
    
    w = img.getWidth()
    h = img.getHeight()

    newimg = EmptyImage(w,h)
    
    for y in range(h):
        for  x in range(w):
           p = img.getPixel(x,y)


           newpixel = Pixel(255-p.getRed(),255-p.getGreen(),255 - p.getBlue())

           newimg.setPixel(x,y,newpixel)

    return newimg

##DO NOT MODIFY THE FUNCTIONS BELOW
##THEY ARE USED FOR TESTING YOUR FUNCTIONS
##AND DISPLAYING IMAGES

#display the specified image in a window
def display_image(img, t):
    """Display the specified image in a window"""
    win = ImageWin(title = t, width = img.getWidth(), height = img.getHeight())
    img.draw(win)
    
#don't modify this function    
def test_one(transform, filename):
    transformName = str(transform).split()[1]
    print("Starting "+ transformName)
    
    try:
        #create an image corresponding to the specified file
        img = Image(filename)
        
        #apply the specified transformation to the image
        img = transform(img)
        
        #show the transformed image
        display_image(img, transformName)
    except:
        print("\t"+transformName + ":Error")
        import sys, traceback
        traceback.print_exc()

#don't modify this function
#I will use it to test all your functions
def test_all():
    transforms = [flip_horizontal, sepia_tone, convert_to_gray_scale, flip_vertical, rotate_right_90]
    for t in transforms:
        test_one(t, "penguins.gif")
        
test_one(red_filter, "penguins.gif")
#test_all()
