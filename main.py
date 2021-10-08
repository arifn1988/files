import os
from os import path
import zipfile
import pathlib

__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

dir_path = str(pathlib.Path(__file__).parent.absolute())

def clean_dir(dir):
	files = os.listdir(dir)
	if(len(files)!=0):
		for file in files:
			os.unlink(os.path.join(dir, file))

def clean_cache():
	folder_path=dir_path+'/cache'
	if(path.exists(folder_path)):
		clean_dir(folder_path)
	else:
		os.mkdir(folder_path)


def cache_zip(zip_file,cache_dir):
	file =  zipfile.ZipFile(zip_file)
	files= os.listdir(cache_dir)

	if(len(files)==0):
		file.extractall(dir_path+'/cache')
	else:
		print("Cache directory needs to be empty to extract files to it.")

def cached_files():
	files= os.listdir('C:/Users/gebruiker/Desktop/winc/files/cache') 
	absolute_files=[]

	for file in files:
		absolute_files.append(dir_path+'\\cache\\'+file) 

	return absolute_files

def find_password(dir_files):
	for x in dir_files:
		print(x)

clean_cache()
cache_zip('C:/Users/gebruiker/Desktop/winc/files/data.zip','C:/Users/gebruiker/Desktop/winc/files/cache')
#find_password(cached_files())

