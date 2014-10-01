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

    def increase_reds(self):
        """
            Increases the value of the reds in the image
        """    
        return None
 
    def increase_greens(self):
        """
            Increases the value of the greens in the image
        """
        return None

    def increase_blues(self):
        """
            Increases the value of the blues in the image
        """
        return None

if __name__ == "__main__":

    my_image = Image.open('my_image.jpg', 'r')
    img_scrmbler = ImageScrambler(my_image)
    img_scrmbler.make_black()

