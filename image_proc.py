########################################################
########################################################
#
#Your name: Jude Vargas
#
#Names of people you consulted
#for this assignment(if None, say None): None
#
#I affirm that I have not violated the
#Academic Integrity policies detailed in the syllabus
#
########################################################
########################################################

from cImage import *

def flip_horizontal(img):
    """Flip the specified image left to right and return the modified image"""
    
    # Create an empty image to copy each pixel over
    width = img.getWidth()
    height = img.getHeight()
    new_img = EmptyImage(width, height)
    
    # Go halfway across the image and swap each column of pixels with their complimentary column on the other side
    for x in range(width // 2):
        for y in range(height):
            tmp_pixel = img.getPixel(x, y)
            
            new_img.setPixel(x, y, img.getPixel(width - x - 1, y))
            new_img.setPixel(width - x - 1, y, tmp_pixel)

    return new_img

def sepia_tone(img):
    """Apply the sepia tone transformation to the specified image, and return the modified image"""
    
    # Create an empty image to copy each pixel over
    width = img.getWidth()
    height = img.getHeight()
    new_img = EmptyImage(width, height)
    
    # Iterate through each pixel in the image and apply the filter
    for x in range(width):
        for y in range(height):

            # Get the values for each color in a pixel
            p = img.getPixel(x, y)
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()
            
            # Calculate the color for the pixel with the filter
            new_red = min(round(red * 0.393 + green * 0.769 + blue * 0.189), 255)
            new_green = min(round(red * 0.349 + green * 0.686 + blue * 0.168), 255)
            new_blue = min(round(red * 0.272 + green * 0.534 + blue * 0.131), 255)
            
            # Apply the pixel with the filter to the new image
            new_pixel = Pixel(new_red, new_green, new_blue)
            new_img.setPixel(x, y, new_pixel)

    return new_img

def convert_to_gray_scale(img):
    """Apply the gray scale transformation to the specified image, and return the modified image"""
    
    # Create an empty image to copy each pixel over
    width = img.getWidth()
    height = img.getHeight()
    new_img = EmptyImage(width, height)
    
    # Iterate through each pixel in the image and apply the filter
    for x in range(width):
        for y in range(height):
            # Get the values for each color in a pixel
            p = img.getPixel(x, y)
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()
            
            # Create a new grayscale picture and add it to the new image
            new_pixel_color = min(round(red * 0.21 + green * 0.71 + blue * 0.07), 255)
            new_pixel = Pixel(new_pixel_color, new_pixel_color, new_pixel_color)

            new_img.setPixel(x, y, new_pixel)

    return new_img

def flip_vertical(img):
    """Flip the specified image upside down and return the modified image"""
    
    # Create an empty image to copy each pixel over
    width = img.getWidth()
    height = img.getHeight()
    new_img = EmptyImage(width, height)
    
    # Go halfway down the image and swap each row of pixels with their complimentary row on the other side
    for y in range(height // 2):
        for x in range(width):
            tmp_pixel = img.getPixel(x, y)
            
            new_img.setPixel(x, y, img.getPixel(x, height - y - 1))
            new_img.setPixel(x, height - y - 1, tmp_pixel)

    return new_img

def rotate_right_90(img):
    """Rotate the specified image 90 degrees to the right and return the modified image"""
   
    # Create an empty image with inverted width & height to allow for the rotation
    width = img.getWidth()
    height = img.getHeight()
    new_img = EmptyImage(height, width)

    # Get each pixel from the given image and alter its position in the new image to rotate it
    for x in range(width):
        for y in range(height):
            p = img.getPixel(x, y)

            new_img.setPixel(height - y - 1, x, p)

    return new_img

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
        
#test_one(red_filter, "penguins.gif")
test_all()