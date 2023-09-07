# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------

from PIL import Image

# Open The Image
myImage = Image.open(r"C:\khouba\image_elzero\rainbow_skies.jfif")

# Show The Image
myImage.show()

# My Cropped Image
myBox = (300, 300, 800, 800)
MyNewImage = myImage.crop(myBox)

# Show The New Image
MyNewImage.show()

# My Converted Mode Image 

myConverted = myImage.convert("L")
myConverted.show()

