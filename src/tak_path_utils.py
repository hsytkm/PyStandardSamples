import os
from os.path import abspath, join, split

# [python備忘録 - Qiita](https://qiita.com/ymdymd/items/d758110d429f72bc10fb)


class TakPathUtils:
    """ System.IO.Path の一部を実装してみます。
    （標準でありそうやけど探せへんほど Python力が低いっていうのもあります…）
    何れも簡単なコードやけど、めっちゃ勉強なる。"""

    def getFileName(self, path):
        """ ファイルPATH から ファイル名 を返します """
        if os.path.isfile(path):
            return os.path.basename(path)
        return None

    def hasExtension(self, path):
        """ ファイルPATH が 拡張子 を含むかを判定します """
        for i in range(len(path)):
            if i == 0:      # ループ先頭(最終文字)を飛ばします
                continue
            if "." == path[-1 - i]:
                return True
        return False

    def getExtension(self, path):
        """ ファイルPATH から 拡張子 を返します """
        name = self.getFileName(path)
        if name is None:
            return None
        return os.path.splitext(name)[-1]

    def getExtensionWithoutExtension(self, path):
        """ ファイルPATH から 拡張子を除いたファイル名 を返します """
        name = self.getFileName(path)
        if name is None:
            return None
        return os.path.splitext(name)[0]

    def getDirectoryName(self, path):
        """ ファイルPATH から ディレクトリPATH を返します """
        if os.path.isfile(path):
            return os.path.dirname(path)
        elif os.path.isdir(path):
            return path
        return None

    def combine(self, path, *paths):
        """ 可変長引数 を PATH区切り で連結して返します """
        return os.path.join(path, *paths)
