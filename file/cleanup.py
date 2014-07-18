# All Rights Reserved.
# Copyright (C) 2014
import os
import re
import shutil
import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from id3.model import MediaFile
from id3.util.utility import parse_encoding, to_string

__author__ = 'Vijay Shanker Dubey'
__project__ = 'metapy'
__Timestamp__ = '30-Jun-14 : 17:44'


# ======================================================================================================================
def create_replacement_rule():
    replacement_rules = [ReplacementRule('-(Muskurahat.Com)'), ReplacementRule('(DesiTape.Com)'),
                         ReplacementRule('DesiWEB.net'),
                         ReplacementRule('('), ReplacementRule(')'),
                         ReplacementRule(' [www.DJLUV.in]'), ReplacementRule('_', ' ')]

    return replacement_rules


# ======================================================================================================================
class CleanupRule:
    def __init__(self, rule_name):
        self.rule_name = rule_name


# ======================================================================================================================
class MediaTagCleanupRule(CleanupRule):

    def __init__(self):
        super().__init__("Media Tag Cleanup Rule")

    @staticmethod
    def apply(self, media_file):

        media = MediaFile(filename=media_file)

        album = None
        for frame in media.frames:

            if frame.id == 'TALB':
                encoding = parse_encoding(frame.content[0])
                album = to_string(frame.content[1:len(frame.content)], encoding=encoding)
                break

        if album:
            out_path = 'D:/usr/Music/finale/' + album
            if not os.path.exists(out_path):
                os.makedirs(out_path)

            #shutil.copy(media_file, out_path)
        else:
            print('No album found : {0}'.format(media_file), file=open('tag.log', 'a'))

    def __str__(self):
        return "Rule : Media Tag Cleanup Rule"


# ======================================================================================================================
class ReplacementRule(CleanupRule):

    def __init__(self, rule_name, replacement=''):
        super().__init__("Replacement Rule")
        self.value = rule_name
        self.replacement = replacement

    def apply(self, input_value):

        new_name = input_value

        if input_value.find(self.value) >= 0:
            new_name = input_value.replace(self.value, self.replacement)

        return new_name

    def __str__(self):
        return "Rule : Replace {0} with {1}".format(self.value, self.replacement)


# ======================================================================================================================
class WhiteSpaceCleanup(CleanupRule):

    def __init__(self):
        super().__init__("White Space Rule")

    def apply(self, input_value):

        #strip input value
        new_name = input_value.strip()

        # replace more then one consecutive whitespaces
        new_name = re.sub('\\s{2,}', '', new_name)

        return new_name

    def __str__(self):
        return "White Space Cleanup"


# ======================================================================================================================
class FileNameCleanup:

    def __init__(self, filename, logger):
        self.rules = create_replacement_rule()
        self.rules.append(WhiteSpaceCleanup())

        self.filename = filename
        self.logger = logger

    def execute(self):
        self.logger.print("Executing filename cleanup")

        new_name = self.filename
        for rule in self.rules:
            self.logger.print("Checking for rule : {0}".format(rule))
            new_name = rule.apply(new_name)

        if new_name is self.filename:
            self.logger.print("File name is clean")
        else:
            new_name = new_name.strip()
            self.logger.print("Renaming file name to : {0}".format(new_name))

        return new_name