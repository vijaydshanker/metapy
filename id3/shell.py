# All Rights Reserved.
# Copyright (C) 2014
import os
import shutil
from mutagen.mp3 import MP3

from file.cleanup import FileNameCleanup, MediaTagCleanupRule
from id3.model import MediaFile
from log.Logger import TreeLogger


__author__ = 'Vijay Shanker Dubey'
__project__ = 'metapy'
__Timestamp__ = '29-Jun-14 : 15:50'


def main():
    file_name = 'D:\\usr\\Music\\Water [2005]\\01 - Water (2005) - Aayo Re Sakhi [www.DJLUV.in].mp3'

    media = MediaFile(filename=file_name)

    media.show()

def cleanup():
    logger = TreeLogger()

    folder = 'D:\\usr\\Music\\download\\'
    logger.print("Reading mp3 tags from : {0}".format(folder))

    output = 'D:\\usr\\Music\\test\\result\\'
    files = os.listdir(folder)
    for file in files:
        # file is valid mp3 file?
        extension = os.path.splitext(file)[1]
        if extension.upper() == '.MP3':
            file_path = folder + file

            logger.print("Cleaning mp3 file : {0}".format(file_path))

            # name clean up
            new_name = FileNameCleanup(file, logger.branch_out()).execute()
            shutil.copy(src=file_path, dst=output + new_name)

            MediaTagCleanupRule().apply(media_file=output + new_name)


if __name__ == '__main__':
    cleanup()
