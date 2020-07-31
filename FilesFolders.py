from pathlib import Path
import shutil
import os


class FolderFunc:
    def __init__(self, src, dst=''):
        self.src = str(Path(src))
        self.dst = str(Path(dst))

    def make(self):
        p = Path(self.src)
        p.mkdir()

    def mov(self):
        shutil.move(self.src, self.dst)

    def backup(self):
        shutil.copytree(self.src, self.dst, )

    def archive(self, mode):
        shutil.make_archive(self.src, mode, self.dst)

    def unpack(self):
        shutil.unpack_archive(self.src, self.dst)

    def All_fol_fil(self):
        for dir_path, dir_names, files in os.walk(self.src):
            print(f'Found directory: {dir_path}')
            for file_name in files:
                print(file_name)


class FileFunc(FolderFunc):
    def __init__(self, src, dst="", ext=""):
        super().__init__(src, dst)
        self.ext = str(Path(ext))

    def make(self):
        with open(self.src, 'w') as f:
            f.write(f'{self.src}')

    def rename(self, name):
        s_path = Path(self.src)
        for count, file in enumerate(s_path.rglob(f"*{self.ext}")):
            nw_nme = Path(f"{s_path}/{name}{count}{self.ext}")
            file.rename(nw_nme)

    def move_ext_file(self):
        s_path = Path(self.src)
        d_path = Path(self.dst)
        if not d_path.is_dir():
            d_path.mkdir()
        for file in s_path.rglob(f'*{self.ext}'):
            shutil.move(str(file), str(d_path))
