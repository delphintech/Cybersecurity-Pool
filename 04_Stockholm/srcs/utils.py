import os


def get_all_files(file_list, path):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            get_all_files(file_list, full_path)
        elif os.path.isfile(full_path):
            file_list.append(full_path)


def get_file_list() -> list:
    file_list = []

    path = os.path.expanduser("~/infection")
    if not os.path.isdir(path):
        return file_list
    get_all_files(file_list, path)
    return file_list
