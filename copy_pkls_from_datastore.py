import glob
#import shutil
import os

cohort="_cohort2"
# good_list = glob.glob(f"unified_binned/{cohort}/*_50ms.pkl")
# done_list = []
# for folder in good_list:
# 	name = (folder.split('/')[-1]).split('_50ms.pkl')[0]
# 	done_list.append(name)
#print(done_list)
#exit()

for dir in glob.glob(f"/mnt/datastore/ActiveProjects/Sarah/Data/Ramp_project/OpenEphys/{cohort}/VirtualReality/*"):
	new_name=dir.split("/")[-1]
	if "." not in new_name:
		print(new_name)
		path_from=dir+'/MountainSort/DataFrames'
		#path_to=f"/home/ninelk/Documents/work/sarah_data/{cohort}/{new_name}"
		path_to=f"sarah_data/{cohort}/{new_name}"
		print(path_to)
		#shutil.copytree(path_from,path_to)
		if '245' in new_name:
			for file in ['position_data.pkl','spatial_firing.pkl']:
				os.system(f'scp -r {path_from}/{file} work-server:~/{path_to}/{file}')
	# else:
	# 	print('File ignored: ',new_name)
