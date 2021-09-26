# [PythonのctypesでDLLの関数から様々な戻り値を受け取る その３（構造体） - MRが楽しい](https://bluebirdofoz.hatenablog.com/entry/2019/11/19/090109)
from ctypes import *

# DLLをロード
dll = cdll.LoadLibrary(R"cpp\x64\Release\MyNativeLib.dll")


class Channels(Structure):
    _fields_ = [("b", c_ubyte), ("g", c_ubyte), ("r", c_ubyte)]

    def __str__(self):
        return "b=" + format(self.b, '#04x') + ", g=" + format(self.g, '#04x') + ", r=" + format(self.r, '#04x')


# 構造体を参照で渡して設定してもらう
print("--- Invoke C++ library function : return struct ---")
channels = Channels()
dll.get_struct(byref(channels))
print(channels)
