import sys
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
        new_pixel_values = []
        pixel_values = self.get_pixel_list()
        for i in range(0, len(pixel_values), 2):
            if (i == len(pixel_values) - 1):
                new_pixel_values.append(pixel_values[i])
            else:
                curR = pixel_values[i][0]
                curG = pixel_values[i][1]
                curB = pixel_values[i][2]
            
                nextR = pixel_values[i+1][0]
                nextG = pixel_values[i+1][1]
                nextB = pixel_values[i+1][2]
            
                new_pixel_values.append((nextR, nextG, nextB))
                new_pixel_values.append((curR, curG, curB))

        self.img = Image.new(self.img.mode, self.img.size)
        self.img.putdata(new_pixel_values)
            
        return None    
       
    def unscramble(self):
        """

        """
        return None
    
    def make_white(self):
        """
            Makes every pixel in the image white
        """
        pixel_values = self.get_pixel_list()
        for i in range(len(pixel_values)):
            pixel_values[i] = (255,255,255)
        self.img = Image.new(self.img.mode, self.img.size)
        self.img.putdata(pixel_values)
        return None

    def make_black(self):
        """
            Makes every pixel in the image black
        """
        pixel_values = self.get_pixel_list()
        for i in range(len(pixel_values)):
            pixel_values[i] = (0,0,0)
        self.img = Image.new(self.img.mode, self.img.size)
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
        self.img = Image.new(self.img.mode, self.img.size)
        self.img.putdata(pixel_values)   
        return None

    def blur(self):
        return None

if __name__ == "__main__":

    if len(sys.argv) == 1:
         my_image = Image.open('my_image.jpg', 'r')
    elif len(sys.argv) == 2:
        my_image = Image.open(sys.argv[1])
    else:
        raise ValueError()
    my_image = Image.open('my_image.jpg', 'r')
    img_scrmbler = ImageScrambler(my_image)
    img_scrmbler.scramble()
    img_scrmbler.write()
