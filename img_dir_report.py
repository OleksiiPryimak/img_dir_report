# python (dir location)/img_dir_report.py

import os
from PIL import Image
import PIL.ExifTags
from PIL.ExifTags import TAGS
import glob 


DIR_PATH = '(dir location)'
images = []


def count_all_files():
    all_files_counter = len([name for name in os.listdir(DIR_PATH) if os.path.isfile(os.path.join(DIR_PATH, name))])
    print('ALL files:', all_files_counter)


def count_jpg_files():
    jpg_counter = len(glob.glob1(DIR_PATH,"*.jpg"))
    print('JPG files:',jpg_counter)


def count_png_files():
    png_counter = len(glob.glob1(DIR_PATH,"*.png"))
    print('PNG files:',png_counter)


def count_tiff_files():
    tiff_counter = len(glob.glob1(DIR_PATH,"*.tiff"))
    print('TIFF files:',tiff_counter)


def png_files_report():
    for png_image in os.listdir(DIR_PATH):
        if png_image.endswith(".png"):
            print('PNG:', os.path.basename(png_image))


def tiff_files_report():
    for tiff_image in os.listdir(DIR_PATH):
        if tiff_image.endswith(".tiff"):
            print('TIFF:', os.path.basename(tiff_image))


def jpg_files_report():
    for jpg_image in os.listdir(DIR_PATH):
        if jpg_image.endswith((".jpg", ".JPG", ".JPEG")):

            img_path, extension = os.path.splitext(jpg_image)
            extension=extension.replace('.','')
            images = Image.open(os.path.join(DIR_PATH, jpg_image))          
            width, height = images.size          

            print('JPG file:', os.path.basename(jpg_image))
            print('Dim.:', width, 'x', height, 'Ext.:', extension)


def dir_filenames():
    filenames = os.listdir(DIR_PATH)
    # print(filenames[0]) # - only one file
    print(filenames)


def main():
    print('---Count files in the directory---')
    count_all_files()
    count_jpg_files()
    count_png_files()
    count_tiff_files()
    print('-------')
    png_files_report()
    tiff_files_report()
    print('-------')
    jpg_files_report()
    print('---End of the report---')  

if __name__ == "__main__":
    main()