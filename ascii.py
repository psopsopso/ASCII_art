from PIL import Image
import sys

# print(sys.argv[1])
# im = Image.open(f"{sys.argv[1]}")

img = Image.open("img.jpeg")

if img:
    print("Image succesfully loaded!")
    print(f"Size : {img.size[0]}x{img.size[1]}")

def get_matrix(img):
    pixels = list(img.getdata())
    matrix = [pixels[i:i+img.width] for i in range(0,len(pixels), img.width)]
    return matrix

def get_grey_matrix(matrix):
    temp_matrix = []
    for x in range(len(matrix)):
        for y in range(img.width):
            pixel = matrix[x][y]
            pixel_avg = int(sum(pixel)/3)
            temp_matrix.append(pixel_avg)
    grey_matrix = [temp_matrix[i:i+img.width] for i in range(0,len(temp_matrix), img.width)]
    return grey_matrix

matrix = get_matrix(img)
grey_matrix = get_grey_matrix(matrix)
print(grey_matrix)












    







    




