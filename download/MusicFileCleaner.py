# #######################################################################################################################
# Import statements
import os
from id3.media import EncodedBy

from log.Logger import TreeLogger


# #######################################################################################################################
__project__ = 'metapy'
__author__ = 'Vijay Shanker Dubey'




########################################################################################################################
class FrameHeader:
    """
        Represents a music frame.
    """

    def __init__(self):
        content = []

        self.frameId = content[4]
        self.flags = content[5]
        self.size = content[6:10]


########################################################################################################################
class MusicFile:
    """
    Represents a music file as cleanup source
    """

    def __init__(self, file_name):
        self.is_mp3_file = False
        self.file_name = file_name
        self.logger = TreeLogger("Processing file : {0}".format(str(file_name)))
        basename, extension = os.path.splitext(file_name)

        if extension == '.mp3':
            self.is_mp3_file = True
            self.logger.debug('Input file is a valid mp3 file.')

    def list_tags(self):
        logger = self.logger.branch_out()

        if self.is_mp3_file:
            logger.debug('Cleaning Music file tags for : {0}'.format(self.file_name))

            try:
                music_source = open(self.file_name, "r+b", 0)
                try:
                    music_source.seek(0)

                    # Read Tag version
                    version_tag = music_source.read(3)
                    if to_string(version_tag) == 'ID3':
                        self.read_id3_tags(music_source, logger)

                finally:
                    music_source.close()
            except IOError as err:
                logger.debug(err)

    def read_id3_tags(self, file_source, logger):
        """
        Reads the ID3 tags from the file source.

        @param file_source: file to read tags
        @param logger: tree logger; used for logging in the execution context.
        """
        sub_version_tags = file_source.read(3)

        if sub_version_tags[0] == 3 and sub_version_tags[1] == 0:
            tag_version = "ID3v2.{0}.{1}".format(str(sub_version_tags[0]), str(sub_version_tags[1]))
            logger.debug("Music tag format : {0}".format(tag_version))

        data_flag = sub_version_tags[2]

        print(data_flag)


########################################################################################################################

def main():
    file_name = 'D:/usr/Music/downloads/03 - 2 States (2014) - Mast Magan [www.DJLUV.in].mp3'

    header = TagHeader(file_name)
    if not header.has_flag("extended"):
        # Read extended flag related data.
        print("extended flag does not exists in the file.")
    print(str(header))

    # Start to read frames in source file
    source = open(file_name, 'rb')
    # frames starts at 10th byte; if no extended header present. Other wise frame start is after the extended header.
    frame_start = 10
    if not header.has_flag("extended"):
        header_size = 10  # Calculate the header value
        frame_start = header_size

    #skip header bytes
    source.seek(frame_start)

if __name__ == '__main__':
    main()
