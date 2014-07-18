# All Rights Reserved.
# Copyright (C) 2014
# ======================================================================================================================
import os
from struct import unpack
import struct

from id3.media import is_text_frame
from id3.util.utility import to_string, parse_encoding


# ======================================================================================================================
__author__ = 'Vijay Shanker Dubey'
__project__ = 'metapy'
__Timestamp__ = '29-Jun-14 : 08:41'


# ======================================================================================================================
class MediaSource:
    def __init__(self, filename):
        # read full content of the file.
        file_size = os.path.getsize(filename)

        with open(filename, 'rb') as source:
            self.content = source.read(file_size)

    def consume(self, size):
        data = self.content[0: size]

        # Remove the consumed data
        self.content = self.content[size:]
        return data


# ======================================================================================================================
class MediaFile:
    """
    Represent a media file. Contains MP3 file metadata
    """

    def __init__(self, filename):
        """
        created media file
        @param filename: media file name
        """
        self.tag_header = None
        self.frames = []
        self.filename = filename

        MediaFile.create_media(filename, self)

    @staticmethod
    def create_media(filename, media):
        source = MediaSource(filename=filename)

        # Read file header : first 10 char of the file.
        media.tag_header = TagHeader(source.consume(10))
        if media.tag_header.identifier == 'ID3':
            # Parse ID3 tags;
            if media.tag_header.major_version == 3:
                # reading version ID3V2.3.0
                frame_data = source.consume(media.tag_header.size)
                MediaFile.read_id3_v2_3_0_tags(frame_data, media)
            else:
                print("Unknown media version : {0}".format(media.tag_header))
        else:
            print("Unknown media version : Tag version not identified")

    @staticmethod
    def read_id3_v2_3_0_tags(frame_data, media):
        # Read frames
        while frame_data:
            frame_header = frame_data[0:10]
            frame_data = frame_data[10:]

            try:
                name, size, flags = unpack('>4sLH', frame_header)
                # Check for the empty tags
                if name.strip(b'\x00') == b'':
                    continue

                frame_id = to_string(name, encoding='UTF-8')
                body = frame_data[0:size]
                media.frames.append(Frame(frame_id=frame_id, flags=flags, content=body))

                frame_data = frame_data[size:]
            except struct.error:
                return  # not enough header

    def show(self):
        content = list()
        content.append("Media File :- {0}".format(self.filename))
        content.append("\t" + str(self.tag_header))
        for frame in self.frames:
            content.append("\t {0}".format(str(frame)))

        return '\n'.join(content)


# ======================================================================================================================
class Frame:
    """
    contents a frame data. The frame is created from the input bytes with frame data.
    """

    def __init__(self, frame_id, flags, content):
        self.header = None
        self.id = frame_id
        self.flags = flags
        self.content = content

    def __str__(self):
        text = self.content
        if is_text_frame(self.id):
            encoding = parse_encoding(text[0])
            text = to_string(text[1:], encoding=encoding)

        return 'Frame Info : {0} : {1} : {2}'.format(self.id, self.flags, text)


# ======================================================================================================================
class TagHeader:
    """
    As per the standards an ID3v2 file has first 10 bytes of header information
    """

    def __init__(self, content):
        """
        parse the source content and create tag header.
        @rtype : content - Bytes for the header data
        """
        if content:
            self.identifier = to_string(content[0:3])
            self.major_version = content[3]
            self.revision_version = content[4]
            self.flags = []
            self.size = (content[6] << 21) + (content[7] << 14) + (content[8] << 7) + content[9]

            self.parse_flags(content[5])

    def parse_flags(self, flag):
        """
        By ID3 specification; there are three types of flags defined.
        """
        if (flag & 0x80) != 0:
            self.flags.append("unsynchronised")

        if (flag & 0x40) != 0:
            self.flags.append("extended")

        if (flag & 0x20) != 0:
            self.flags.append("experimental")

    def has_flag(self, flag_to_check):
        """
        Checks for a flag in the header.
        """
        is_available = False
        for flag in self.flags:
            if flag == flag_to_check:
                is_available = True
                break

        return is_available

    def __str__(self):
        message = "Tag Version : {0}v2.{1}.{2}"
        return message.format(self.identifier,
                              self.major_version,
                              self.revision_version,
                              self.flags)

# ======================================================================================================================
if __name__ == '__main__':
    folder = 'D:\\usr\\Music\\download\\'

    files = os.listdir(folder)
    for file in files:
        # file is valid mp3 file?
        extension = os.path.splitext(file)[1]
        if extension.upper() == '.MP3':
            file_path = folder + file
            intent = ''
            print(intent + "Cleaning mp3 file : {0}".format(file_path))
            media = MediaFile(filename=folder + file)
            print_content = media.show()
            print(print_content)