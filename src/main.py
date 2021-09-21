import os
import tak_path_utils as path_utils

fileUtils = path_utils.TakPathUtils()

file_path = __file__
dir_path = os.path.dirname(__file__)

print("getFileName()        : ", fileUtils.getFileName(file_path))
print("hasExtension(file)   : ", fileUtils.hasExtension(file_path))
print("hasExtension(dir)    : ", fileUtils.hasExtension(dir_path))
print("getExtension()       : ", fileUtils.getExtension(file_path))
print("getExtensionWithoutExtension()   : ",
      fileUtils.getExtensionWithoutExtension(file_path))
print("getDirectoryName()   : ", fileUtils.getDirectoryName(file_path))
print("combine()            : ", fileUtils.combine(
    *[dir_path, "dir1", "dir2", "test.txt"]))
