from bs4 import *
import re
import requests
import os

##Read HTML
def read_file():
	links=[]
	with open("hmtlstorage.txt") as f:
		for line in f:
			 if "td" in line:
			 	x=re.search("(?P<url>https?://[^\s]+)", line).group("url")
			 	x=x[:-8]
			 	links.append(x)
	return links

# CREATE FOLDER
def folder_create(images,num):
	try:
		#folder_name = input("Enter Folder Name:- ")
		folder_name = "Attack on Titan Chapter {}".format(num)
		# folder creation
		os.mkdir(folder_name)

	# if folder exists with that name, ask another name
	except:
		print("Folder Exist with that name!")
		folder_create()

	# image downloading start
	download_images(images, folder_name)


# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):
	
	# intitial count is zero
	count = 0

	# print total images found in URL
	print(f"Total {len(images)} Image Found!")

	# checking if images is not zero
	if len(images) != 0:
		for i, image in enumerate(images):
			# From image tag ,Fetch image Source URL

						# 1.data-srcset
						# 2.data-src
						# 3.data-fallback-src
						# 4.src

			# Here we will use exception handling

			# first we will search for "data-srcset" in img tag
			try:
				# In image tag ,searching for "data-srcset"
				image_link = image["data-srcset"]
				
			# then we will search for "data-src" in img
			# tag and so on..
			except:
				try:
					# In image tag ,searching for "data-src"
					image_link = image["data-src"]
				except:
					try:
						# In image tag ,searching for "data-fallback-src"
						image_link = image["data-fallback-src"]
					except:
						try:
							# In image tag ,searching for "src"
							image_link = image["src"]

						# if no Source URL found
						except:
							pass

			# After getting Image Source URL
			# We will try to get the content of image
			try:
				r = requests.get(image_link).content
				try:

					# possibility of decode
					r = str(r, 'utf-8')

				except UnicodeDecodeError:

					# After checking above condition, Image Download start
					with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
						f.write(r)

					# counting number of image downloaded
					count += 1
			except:
				pass

		# There might be possible, that all
		# images not download
		# if all images download
		if count == len(images):
			print("All Images Downloaded!")
			

# MAIN FUNCTION START
def main(url,num):
	
	# content of URL
	r = requests.get(url)

	# Parse HTML Code
	soup = BeautifulSoup(r.text, 'html.parser')

	# find all images in URL
	images = soup.findAll('img')

	# Call folder create function
	folder_create(images,num)

if __name__ == "__main__":
	list_links = read_file()
	#url = input("Enter URL:- ")
	num = 1

	# CALL MAIN FUNCTION
	for url in list_links:
		main(url,num)
		print("Chapter {} done".format(num))
		num = num+1
