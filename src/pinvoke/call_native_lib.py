from ctypes import *

# DLLをロード
dll = cdll.LoadLibrary(R"cpp\x64\Release\MyNativeLib.dll")

# int型のクラスを作成
ix = c_int(1)
iy = c_int(2)

print("--- Invoke sum_int() from C++ library ---")
print(ix, "+", iy, "=", dll.sum_int(ix, iy))
print(ix.value, "+", iy.value, "=", dll.sum_int(ix.value, iy.value))
