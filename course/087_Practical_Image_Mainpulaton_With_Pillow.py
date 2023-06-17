# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------
print("=" * 40)

from PIL import Image

# Open The Image
myImage = Image.open(r"C:\khouba\Elzero\Python\Python-course-with-zero\course\RainbowSkies_Banner.jpg")

# Show The Image
myImage.show()

# My Cropped Image
myBox = (300, 300, 800, 800)
myNewImage = myImage.crop(myBox)

# Show The New Image
myNewImage.show()

# My Convirted Mode Image 
myConverted = myImage.convert("L")
myConverted.show()
