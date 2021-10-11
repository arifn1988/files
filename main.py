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

	if(len(files)!=0):\
		clean_cache()

	file.extractall(dir_path+'/cache')

def cached_files():
	files= os.listdir(dir_path+'/cache') 
	absolute_files=[]

	for file in files:
		absolute_files.append(dir_path+'\\cache\\'+file) 

	return absolute_files

def find_password(dir_files):
	letters=''
	for file in dir_files:
		text= open(file,'r').read()
		if('password' in text):
			letters=text

	words=letters.split()
	password=''

	for x in range(len(words)):
		if('password' in words[x]):
			password=words[x+1]

	return password



clean_cache()
cache_zip(dir_path+'/data.zip',dir_path+'/cache')
print(find_password(cached_files()))