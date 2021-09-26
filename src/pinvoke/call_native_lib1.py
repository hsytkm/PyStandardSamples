# [PythonのctypesでDLLの関数から様々な戻り値を受け取る その１ - MRが楽しい](https://bluebirdofoz.hatenablog.com/entry/2019/11/17/232435)
# [PythonのctypesでDLLの関数から様々な戻り値を受け取る その２（参照渡し） - MRが楽しい](https://bluebirdofoz.hatenablog.com/entry/2019/11/18/093343)
#
# Cython の プリミティブ型（c_bool, c_int など）の一覧は以下に書いてある。
#   https://docs.python.org/3/library/ctypes.html
#
from ctypes import *

# DLLをロード
dll = cdll.LoadLibrary(R"cpp\x64\Release\MyNativeLib.dll")

# int型 を値渡し+戻り値
print("--- Invoke C++ library function : by Value ---")
ix1 = c_int(1)
iy1 = c_int(2)
print(ix1, "+", iy1, "=", dll.sum_int(ix1, iy1))
print(ix1.value, "+", iy1.value, "=", dll.sum_int(ix1.value, iy1.value))

# int型 を参照渡し
print("--- Invoke C++ library function : by Reference ---")
ix2 = c_int()
dll.get_int_max(byref(ix2))
print("int max value = ", ix2.value)

# メモリを渡して文字列を設定してもらう
print("--- Invoke C++ library function : return string ---")
buffer_length = 256
str_buffer = create_string_buffer(buffer_length)
dll.get_string(str_buffer, str_buffer._length_)
# print(str_buffer.value)             # バイト列なので C++ で設定した "xxx" が b'xxx' と表示される。
print(str_buffer.value.decode())    # バイト列を文字列にデコードすれば、中身のみ表示される。"xxx"
