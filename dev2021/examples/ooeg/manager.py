import sys
import os
from zip_processor import ZipProcessor


class ZipReplace:
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        """Perform a search and replace on all files in the temporary
        directory."""
        for filename in self.temp_directory.iterdir():
            with filename.open as file:
                contents = file.read()

            contents = contents.replace(self.search_string,
                                        self.replace_string)

            with filename.open("w") as file:
                file.write(contents)


if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).process_zip()


# ==== ====
import os
import shutil
import zipfile
from pathlib import Path


class ZipProcessor:
    """We'll start by demonstrating an inheritance-based solution to this
    problem. First we'll modify our original `ZipReplace` class into a
    superclass for processing generic ZIP files.
    """
    """A program that does a find and replace action for text files stored
    in a compressed ZIP file.

    1. Unzipping the compressed file.
    2. Performing the find and replace action.
    3. Zipping up the new files.
    """
    def __init__(self, filename, search_string, replace_string):
        """Test init"""
        pass

    def __init__(self, zipname):
        """"""
        self.zipname = zipname
        self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))

        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path("unzipped-{}".format(filename))

    def zip_find_replace(self):
        """An overall 'manager' method for each the three steps. This method
        delegates responsibility to other methods.
        """
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def process_zip(self):
        """"""
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        """"""
        self.temp_directory.mkdir()
        # with zipfile.ZipFile(self.filename) as zip:
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def find_replace(self):
        """"""
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string,
                                        self.replace_string)
            with filename.open('w') as file:
                file.write(contents)

    def zip_files(self):
        """"""
        # with zipfile.ZipFile(self.filename, 'w') as file:
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))


def main():
    ZipReplace(*sys.argv[1:4]).zip_find_replace()


if __name__ == "__main__":
    main()

# === ===
from zip_processor import ZipProcessor
import sys
from PIL import Image  #  pip install pillow


class ScaleZip(ZipProcessor):

    def process_files(self):
        """Scale each image in the directory to 640*480"""
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((640, 480))
            scaled.save(str(filename))


def main():
    ScaleZip(*sys.argv[1:4]).process_zip()


if __name__ == "__main__":
    main()
