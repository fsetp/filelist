import os

dir_path = "E:\\Workspace\\Computex\\LC_CJV50\\MainSystem"

def scan_depth(target_path, folder, level):
	paths = os.listdir(target_path)
	for path in paths:
		# except special path
		#
		if path[0] != '.':
			file_path = target_path + '\\' + path
			if folder == '':
				target_folder = path
			else:
				target_folder = folder + ', ' + path

			print(file_path)

			# folfer -> more dig
			#
			if os.path.isdir(file_path):
				level = level + 1
				level = scan_depth(file_path, target_folder, level)
				print(level)
#				return level

#			else:
#				max_level = level

	return level

def list_files(target_path, folder):
	paths = os.listdir(target_path)
	for path in paths:
		# except special path
		#
		if path[0] != '.':
			file_path = target_path + '\\' + path
			if folder == '':
				target_folder = path
			else:
				target_folder = folder + ', ' + path

			# folfer -> more dig
			#
			if os.path.isdir(file_path):
				list_files(file_path, target_folder)

			#
			else:
				print(f'{folder}, {path}')

level = scan_depth(dir_path, '', 0)
print(level)

#list_files(dir_path, '')
