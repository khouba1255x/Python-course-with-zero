# assignment 1:
print("assignment 1:")

# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list, my_tuple):
#     my_data += data

# final_string = ""

# for alpha in my_data :
#     final_string += alpha

# print(final_string.capitalize())


print("=" * 40)
# assignment 2:
print("assignment 2:")

# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):

#     my_data.append(item1)

    
# # print(my_data)

# final_string = ""

# for alpha in my_data :
    
#     if isinstance(alpha, str) :
#         final_string += alpha
        

# print(final_string.capitalize())


print("=" * 40)
# assignment 3:
print("assignment 3:")

from PIL import Image 

# # open image and show it
# elzero_image = Image.open(r"C:\khouba\Elzero\Python\Python-course-with-zero\Tathkir\elzero_image_v2_assignment_86_89.png")
# elzero_image.show()

# # first image:
# # cut the image and show the lettre L black and white

# crop_L = (400, 0, 800, 400)
# update_image_elzero = elzero_image.crop(crop_L)
# convert_image_elzero = update_image_elzero.convert("L")
# convert_image_elzero.show()


# # second image:
# # cut the 3 low letters and show in form upturned and black and white

# crop_3_low_letters = (0, 400, 1200, 800)
# update_image_elzero2 = elzero_image.crop(crop_3_low_letters)
# convert_image_elzero2 = update_image_elzero2.convert("L")
# rotate_image_elzero2 = convert_image_elzero2.rotate(180)

# rotate_image_elzero2.show()

print("=" * 40)
# assignment 4:
print("assignment 4:")

# def say_hello_to(name) :
    
#     """
#     parameter(someone) => Person Name
#     Function To Say Hello To Anyone
#     """
    
#     print(f"Hello {name}")

# say_hello_to("Osama")
# print(say_hello_to.__doc__)


print("=" * 40)
# assignment 5:
print("assignment 5:")

myFriends = ["Ahmed", "Osama", "Sayed"]

def sayHello(SomePeoples) -> list:
  for Someone in SomePeoples:
    print(f"Hello {Someone}")

sayHello(myFriends)

# be9i famma il moshkil mta3 il pyilnt elli mey7ebbish ye5dem fil command line 