from PIL import Image

#ASCII chars
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

#resize image
def resize_image(image, new_width= 100):
    width, height = image.size
    ratio = height / width / 2
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)

#convert to greyscale
def grayscale(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

#convert pixels to a string of ASCII chars
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width=100):
    #open image file
    path = input("Enter a valid pathname to an image:\n")
    try:
        print("hi")
        image = Image.open(path)
    except:
        print(path, "is not a valid pathname to an image.")

    #convert to ascii
    new_image_data = pixels_to_ascii(grayscale(resize_image(image)))

    #format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    #print result
    print(ascii_image)

    #save result to file
    with open ("ascii_image.txt", "w") as f:
        f.write(ascii_image)

if __name__ == "__main__":
    main()
