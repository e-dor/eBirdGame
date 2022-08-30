from google_images_search import GoogleImagesSearch
from io import BytesIO
from PIL import Image
from random_birds import bird_chosen

gis = GoogleImagesSearch('', '')

my_bytes_io = BytesIO()
def bird_image():
    
    gis.search({'q': bird_chosen, 'num': 1})
    for image in gis.results():
        # here we tell the BytesIO object to go back to address 0
        my_bytes_io.seek(0)

        # take raw image data
        raw_image_data = image.get_raw_data()

        # this function writes the raw image data to the object
        image.copy_to(my_bytes_io, raw_image_data)

        # or without the raw data which will be automatically taken
        # inside the copy_to() method
        image.copy_to(my_bytes_io)

        # we go back to address 0 again so PIL can read it from start to finish
        my_bytes_io.seek(0)

        # create a temporary image object
        temp_img = Image.open(my_bytes_io)
        
        # show it in the default system photo viewer
        temp_img.show()
        
