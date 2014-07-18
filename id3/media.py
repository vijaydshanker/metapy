# All Rights Reserved.
# Copyright (C) 2014

# ======================================================================================================================

__author__ = 'Vijay Shanker Dubey'
__project__ = 'metapy'
__Timestamp__ = '29-Jun-14 : 08:41'


# ======================================================================================================================
def is_text_frame(frame_id):
    check = False

    for (key, value) in globals().items():

        if isinstance(value, type) and issubclass(value, TextFrame):
            try:
                if value.name == frame_id:
                    check = True
                    # break the loop; as  matched
                    break
            except AttributeError as error:
                pass

    return check


# ======================================================================================================================
def is_comment_frame(frame_id):
    return frame_id == 'COMM'


# ======================================================================================================================
def is_picture_frame(frame_id):
    return frame_id == 'APIC'


# ======================================================================================================================
class Frame:
    def __init__(self):
        pass


# ======================================================================================================================
class TextFrame(Frame):
    def __init__(self):
        super(Frame, self).__init__()


# ======================================================================================================================
class AlbumFrame(TextFrame):
    name = 'TALB'
    detail = 'Album'

    def __init__(self):
        super(TextFrame, self).__init__()


# ======================================================================================================================
class BeatsPerMinuteFrame(TextFrame):
    name = 'TBPM'
    detail = 'Beats per minute (BPM)'

    def __init__(self):
        super(TextFrame, self).__init__()


# ======================================================================================================================
class ComposerFrame(TextFrame):
    name = 'TCOM'
    detail = 'Composer'

    def __init__(self):
        super(TextFrame, self).__init__()


# ======================================================================================================================
class ContentTypeFrame(TextFrame):
    name = 'TCON'
    detail = 'Content type'

    def __init__(self):
        super(TextFrame, self).__init__()


# ======================================================================================================================
class CopyrightFrame(TextFrame):
    name = 'TCOP'
    detail = 'Copyright message'

    def __init__(self):
        super(TextFrame, self).__init__()


# ======================================================================================================================
class DateFrame(TextFrame):
    name = 'TDAT'
    detail = 'Date'

    def __init__(self):
        super(TextFrame, self).__init__()


# ======================================================================================================================
class PlaylistDelayFrame(TextFrame):
    name = 'TDLY'
    detail = 'Playlist delay'

    def __init__(self):
        super(TextFrame, self).__init__()


# ======================================================================================================================
class EncodedByFrame(TextFrame):
    name = 'TENC'
    detail = 'Encoded by'

    def __init__(self):
        super(TextFrame, self).__init__()


# ======================================================================================================================
class LyricistFrame(TextFrame):
    name = 'TEXT'
    detail = 'Lyricist/Text writer'

    def __init__(self):
        super(TextFrame, self).__init__()


# ======================================================================================================================
class TimeFrame(TextFrame):
    name = 'TIME'
    detail = 'Time'

    def __init__(self):
        super(TextFrame, self).__init__()


# =======================================================================================================================
class FileTypeFrame(TextFrame):
    name = 'TFLT'
    detail = 'File type'

    def __init__(self):
        super(TextFrame, self).__init__()


# =======================================================================================================================
class ContentGroupFrame(TextFrame):
    name = 'TIT1'
    detail = 'Content group description'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class TitleFrame(TextFrame):
    name = 'TIT2'
    detail = 'Title'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class SubtitleFrame(TextFrame):
    name = 'TIT3'
    detail = 'Subtitle'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class InitialKeyFrame(TextFrame):
    name = 'TKEY'
    detail = 'Initial key'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class AudioLanguageFrame(TextFrame):
    name = 'TLAN'
    detail = 'Initial key'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class LengthFrame(TextFrame):
    name = 'TLAN'
    detail = 'Length'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class MediaTypeFrame(TextFrame):
    name = 'TLAN'
    detail = 'Media type'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class OriginalAlbumFrame(TextFrame):
    name = 'TOAL'
    detail = 'Original album'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class OriginalFilenameFrame(TextFrame):
    name = 'TOFN'
    detail = 'Original filename'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class OriginalLyricistFrame(TextFrame):
    name = 'TOLY'
    detail = 'Original lyricist'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class OriginalArtistFrame(TextFrame):
    name = 'TOPE'
    detail = 'Original artist'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class OriginalReleaseYearFrame(TextFrame):
    name = 'TORY'
    detail = 'Original release year'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class LeadPerformerFrame(TextFrame):
    name = 'TPE1'
    detail = 'Lead performer'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class BandFrame(TextFrame):
    name = 'TOWN'
    detail = 'Band'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class ConductorFrame(TextFrame):
    name = 'TOWN'
    detail = 'Conductor'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class RemixedFrame(TextFrame):
    name = 'TPE4'
    detail = 'Remixed'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class PartOfSetFrame(TextFrame):
    name = 'TPOS'
    detail = 'Part of a set'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class PublisherFrame(TextFrame):
    name = 'TPUB'
    detail = 'Publisher'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class TrackNumberFrame(TextFrame):
    name = 'TRCK'
    detail = 'Track number'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class RecordingDateFrame(TextFrame):
    name = 'TRDA'
    detail = 'Recording dates'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class InternetRadioStationNameFrame(TextFrame):
    name = 'TRSN'
    detail = 'Internet radio station name'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class InternetRadioStationOwnerFrame(TextFrame):
    name = 'TRSN'
    detail = 'Internet radio station owner'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class SizeFrame(TextFrame):
    name = 'TSIZ'
    detail = 'Size'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class StandardRecordingCodeFrame(TextFrame):
    name = 'TSRC'
    detail = 'International Standard Recording Code'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class SoftwareSettingsFrame(TextFrame):
    name = 'TSIZ'
    detail = 'Software/Hardware and settings'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class YearFrame(TextFrame):
    name = 'TSIZ'
    detail = 'Year'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class ExtraTextFrame(TextFrame):
    name = 'TSIZ'
    detail = 'User defined text'

    def __init__(self):
        super(TextFrame, self).__init__()


#=======================================================================================================================
class AlbumArtPictureFrame(Frame):
    name = 'APIC'
    detail = 'Album Art'

    def __init__(self):
        super(TextFrame, self).__init__()


class URLFrames:
    valid_frames = dict()
    valid_frames['WOAF'] = {'name': 'WOAF', 'detail': 'Official audio file webpage'}
    valid_frames['WOAR'] = {'name': 'WOAR', 'detail': 'Official artist/performer webpage'}
    valid_frames['WOAS'] = {'name': 'WOAS', 'detail': 'Official audio source webpage'}
    valid_frames['WORS'] = {'name': 'WORS', 'detail': 'Official internet radio station homepage'}
    valid_frames['WPUB'] = {'name': 'WPUB', 'detail': 'Publishers official webpage'}
    valid_frames['WXXX'] = {'name': 'WXXX', 'detail': 'User defined URL link frame'}
