import os
from PIL import Image
from pathlib import Path
import pyguetzli as pg

def show_file_size(size_in_bytes , format='auto'):
    unit = {'gb' : 1024 ** 3,
            'mb' : 1024 ** 2,
            'kb' : 1024}
    
    for key , val in unit.items():
        cal_val = size_in_bytes / val
        if(cal_val >= 1):
            return [cal_val , key]

#print(show_file_size(17897))

def compress_jpg(src_file_path , target_file_path):
    optimized_bytes = None
    try:
        with open(src_file_path,'rb') as image:
            optimized_bytes = pg.process_jpeg_bytes(image.read())

        with open(target_file_path,'wb') as image:
            image.write(optimized_bytes)
            return True
    except ValueError as e:
        print(f'[Error] : {e}')
        return False

def compress_png(src_file_path , target_file_path):
    optimized_bytes = None
    try:
        with Image.open(src_file_path) as image:
            optimized_bytes = pg.process_pil_image(image)
        with open(target_file_path , 'wb') as image:
            image.write(optimized_bytes)
            
    except ValueError as e:
        print(f'[Error] : {e}')
        return False


def batch_compress(directory , extra=''):
    if not os.path.isdir(directory):
        print(f'[Error] : `{directory}` is not a directory')
        return

    files = os.listdir(directory)
    file_counter = 1
    total_file_count = len(files)
    total_file_size = 0
    total_converted_file_size = 0
    
    for file in os.listdir(directory):
        src_file_path = os.path.join(directory,file)
        file_name , file_extention = file.split('.')
        file_extention = '.' + file_extention
        
        target_file_path = os.path.join(directory,file_name+extra+'.jpeg')

        print(f'[{file_counter} / {total_file_count}] File : {file_name+file_extention}')
        if file_extention in ['.jpg','.jpeg']:
            print('Compressing...')
            src_file_size = show_file_size(os.stat(src_file_path).st_size)
            if compress_jpg(src_file_path , target_file_path) :
                target_file_size = show_file_size(os.stat(target_file_path).st_size)
                total_file_size += src_file_size[0]
                total_converted_file_size += target_file_size[0]
                print(f'Done [{round(src_file_size[0],2)}{src_file_size[1].upper()} -> {round(target_file_size[0],2)}{target_file_size[1].upper()}]')
        elif file_extention == '.png':
            print('Compressing...')
            src_file_size = show_file_size(os.stat(src_file_path).st_size)
            if compress_png(src_file_path , target_file_path) :
                target_file_size = show_file_size(os.stat(target_file_path).st_size)
                total_file_size += src_file_size[0]
                total_converted_file_size += target_file_size[0]
                print(f'Done [{round(src_file_size[0],2)}{src_file_size[1].upper()} -> {round(target_file_size[0],2)}{target_file_size[1].upper()}]')
        else:
            print('File is not a valid image')

        file_counter += 1


def main():
    #directory = input('Enter the folder path :: ') 
    #directory = Path(directory)
    directory = Path(r'C:\Users\Rohan\Coding\Automation\Gutezli Photo Compressor')
    batch_compress(directory, '_compressed')

main()













    
    

    
# Alternatively, you can use double backslashes
# directory = Path("C:\\Users\\Rohan\\Pictures\\Screenshots")
# file_path = os.path.join('C:\\Users\\Rohan\\Coding\\Automation\\Gutezli Photo Compressor', 'test_image.jpg')
# # Open the file
# input_jpeg_bytes = open(file_path, "rb").read()
# optimized_output = pg.process_jpeg_bytes(input_jpeg_bytes)
# output_file_path = os.path.join('C:\\Users\\Rohan\\Coding\\Automation\\Gutezli Photo Compressor', 'test_image_output.jpg')
# output = open(output_file_path, "wb")
# output.write(optimized_output)