import os
import tak_path as path_util

path = path_util.TakPath()

file_path = __file__
dir_path = os.path.dirname(__file__)

print("is_file(file)           : ", path.is_file(file_path))
print("is_file(dir)            : ", path.is_file(dir_path))
print("is_directory(file)      : ", path.is_directory(file_path))
print("is_directory(dir)       : ", path.is_directory(dir_path))
print("get_filename(file)      : ", path.get_filename(file_path))
print("get_filename(dir)       : ", path.get_filename(dir_path))
print("has_extension(file)     : ", path.has_extension(file_path))
print("has_extension(dir)      : ", path.has_extension(dir_path))
print("get_extension(file)     : ", path.get_extension(file_path))
print("get_extension(dir)      : ", path.get_extension(dir_path))
print("get_filename_without_extension(file) : ",
      path.get_filename_without_extension(file_path))
print("get_filename_without_extension(dir)  : ",
      path.get_filename_without_extension(dir_path))
print("get_directory_name(file) : ", path.get_directory_name(file_path))
print("get_directory_name(dir)  : ", path.get_directory_name(dir_path))
print("combine()              : ", path.combine(
    *[dir_path, "dir1", "dir2", "file1.txt"]))
