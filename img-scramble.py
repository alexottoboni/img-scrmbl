import sys
import argparse
from PIL import Image

class ImageScrambler:
    
    def __init__(self, img_file):
        """
            Accepts an image file to manipulate
            @img_file: The image file to manipulate
        """
        self.img = img_file

    def __str__(self):
        return str(self.img)
    
    def __repr__(self):
        return str(self.img)

    def write(self, location = './altered_img.jpeg'):
        """
            Writes the current image to a file called
        """
        img_file = open(location, 'w+')
        self.img.save(img_file)        

    def get_pixel_list(self):
        """
            Gets a list of pixel triples for the current image
        """
        return list(self.img.getdata())

    def get_flat_pixel_list(self):
        """
            Gets a list of R, G, and B values for the image.
        """
        pixel_values = list(self.img.getdata())
        pixel_values_flat = [x for sets in pixel_values for x in sets]
        return pixel_values_flat
   
    def scramble(self):
        """
        
        """
        first_half = []
        second_half = []
        pixel_values = self.get_pixel_list()
        for i in range(len(pixel_values)):
            if (i < len(pixel_values)/2):
                first_half.append(pixel_values[i])
            else:
                second_half.append(pixel_values[i])
        combined = []        
        while first_half and second_half:
            combined.append(first_half.pop())
            combined.append(second_half.pop())
        self.img = Image.new(self.img.mode, self.img.size)
        self.img.putdata(combined) 
        
        return None    
       
    def unscramble(self):
        """

        """
        pixel_values = self.get_pixel_list()
        first_half = []
        second_half = []
        for i in range(len(pixel_values)):
            if not (i % 2):
                first_half.append(pixel_values[i])
            else:
                second_half.append(pixel_values[i])
        combined = []
        while first_half:
            combined.append(first_half.pop())
        while second_half:    
            combined.append(second_half.pop())
        self.img = Image.new(self.img.mode, self.img.size)
        self.img.putdata(combined)

        return None
    
    def make_white(self):
        """
            Makes every pixel in the image white
        """
        pixel_values = self.get_pixel_list()
        for i in range(len(pixel_values)):
            pixel_values[i] = (255,255,255)
        self.img.putdata(pixel_values)
        return None

    def make_black(self):
        """
            Makes every pixel in the image black
        """
        pixel_values = self.get_pixel_list()
        for i in range(len(pixel_values)):
            pixel_values[i] = (0,0,0)
        self.img.putdata(pixel_values)
        return None

    def increase_color(self, color_value):
        pixel_values = self.get_pixel_list()
        for i in range(len(pixel_values)):
            r_value = pixel_values[i][0]
            g_value = pixel_values[i][1]
            b_value = pixel_values[i][2]
            if (color_value.upper() == 'R'):
                r_value += 50
            elif (color_value.upper() == 'G'):
                g_value += 50
            elif (color_value.upper() == 'B'):
                b_value += 50
            else:
                print "Not a valid color value"
            pixel_values[i] = (r_value, g_value, b_value)
        self.img.putdata(pixel_values)   
        return None

    def blur(self):
        return None

if __name__ == "__main__":

    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument('-f', nargs = 1, default = "my_image.jpg")
    arg_parse.add_argument('-s', nargs='?', const="false", default = False)
    arg_parse.add_argument('-u', nargs='?', const="false", default = False)

    options = arg_parse.parse_args()    

    if isinstance(options.f, list):
        my_image = Image.open(options.f[0], 'r')
    else:
        my_image = Image.open(options.f, 'r')
    img_scrmbler = ImageScrambler(my_image)

    if options.u:
        img_scrmbler.unscramble()
    if options.s:
        img_scrmbler.scramble()
    
    img_scrmbler.write()
