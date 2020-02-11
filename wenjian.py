import os,re

rootdir = '/Volumes/MSDOS/pics/'
# new_dir = '壁纸'

for dir2 in os.listdir(rootdir):
	if os.path.isdir(os.path.join(rootdir,dir2)):
		for dir3 in os.listdir(os.path.join(rootdir,dir2)):

			if os.path.isdir(os.path.join(rootdir,dir2,dir3)) and len(os.listdir(os.path.join(rootdir,dir2,dir3))) < 10:
				print(dir3)
				for files in os.listdir(os.path.join(rootdir,dir2,dir3)):
					# print(files)
					if os.path.isfile(rootdir+dir2+'/'+dir3+'/'+files):
						print(files)
						# os.remove(rootdir+dir2+'/'+dir3+'/'+files)

				# os.removedirs(os.path.join(rootdir,dir2,dir3))
# os.removedirs('/Volumes/MSDOS/pics/meizi/.DS_Store')


	# if len(os.listdir(rootdir +'/'+dir2)) < 6:
# 		for file in os.listdir(rootdir +'/'+dir2):
# 			os.rename(os.path.join(rootdir, dir2, file), os.path.join(rootdir, new_dir, file))

# 		os.removedirs(rootdir +'/'+dir2)
# pattern = re.compile(r'(\[\d+?\]).*?')
# rootdir = '/Volumes/MSDOS/pics/meitulu/'
# for  dir in os.listdir(rootdir):
# 	# oldname = os.path.dirname(dir)
# 	# print(type(dir))
# 	newname = re.sub(pattern,'',dir) 
# 	print(newname)
# 	os.rename(os.path.join(rootdir,dir),os.path.join(rootdir,newname))




