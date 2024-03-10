#pip install Pillow
import PIL.Image

#ascii character used to build the output text
ASCII_CHARS = ["N","@","#","W","9","8","7","6","5","4","3","2","1","0","?","!","a","b","c",";",":","+","=","-",",","_"]
#resize the image according to a new width 
def resize_image(image,new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int (new_width *ratio)
    resized_image = image.resize((new_width,new_height))
    return (resized_image)

#convert each pixel into grayscale
def grayify (image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

#convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[int(pixel / (256 / len(ASCII_CHARS)))] for pixel in pixels])

    return characters

# ...

def main(new_width=100):
    # Initialize the 'image' variable
    image = None

    # Attempt to open the image from user input
    path = input("Enter the valid path to the image:\n")
    try:
        image = PIL.Image.open(path)
    except Exception as e:
        print(f"{path} is not a valid pathname to an image. Error: {e}")
        return 

    #converting image into ASCII
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    #format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:i+new_width] for i in range(0, pixel_count, new_width))
    print(ascii_image)

    #now saving the result to ascii image text
    with open ("ascii_image.txt", "w") as f:
        f.write(ascii_image)
main()