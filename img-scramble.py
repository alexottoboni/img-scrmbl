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

    def write_img(self):
        """
            Writes the current image to a file called
        """
        img_file = open('./altered_img.jpeg', 'w+')
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
        self.write_img()
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
        self.write_img()
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
        self.write_img()   
        return None

    def blur(self):
        return None

if __name__ == "__main__":

    my_image = Image.open('my_image.jpg', 'r')
    img_scrmbler = ImageScrambler(my_image)
    img_scrmbler.increase_color("B")
    img_scrmbler.make_white()
