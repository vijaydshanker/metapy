import socket
from urllib.error import URLError

__project__ = "metapy"
__author__ = 'Vijay Shanker Dubey'

import urllib.request
import urllib.response
import cgi

########################################################################################################################
# The launcher program for the downloader


class ConsiderateGrabber:

    def __init__(self):
        self.web_url_template = 'http://www.djluv.in/music/index.php?option=com_muscol&view=file&format=raw&id={0}'
        self.last_check_counter = 21231
        self.download_location = 'D:/usr/Music/downloads/'

    def get_url_template(self, song_id):
        return self.web_url_template.format(song_id)

    def create_download_location(self, filename):
        return self.download_location + filename

# create instance of the class for global usage
grabber = ConsiderateGrabber()

########################################################################################################################


class DownloadContainer:
    def __init__(self):
        self.downloadable_songs = dict()
        self.save_to_database = True

    def add(self, key, value):
        self.downloadable_songs[key] = value
        # output dir
        if self.save_to_database is True:
            with open("result.out", 'a') as logfile:
                message = 'song id = {0}, song name = {1}'.format(key, value)
                print(message, file=logfile)

    def fetch_songs(self):
        self._do_fetch()
        #pass

    def _do_fetch(self):
        for song in self.downloadable_songs:
            song_id = song
            filename = self.downloadable_songs[song]

            song_url = grabber.get_url_template(song_id)

            urllib.request.urlretrieve(song_url, grabber.create_download_location(filename))

    def clean_tags(self):
        pass

# create instance of the class for global usage
container = DownloadContainer()


########################################################################################################################
# Define the music resource to download.


class MusicResource:

    def __init__(self, song_id, logger):
        self.logger = logger
        self.song_id = song_id
        self.filename = None

    def get_music_filename(self):
        """
        # check the created resource for validity.
        """
        filename = None

        try:
            target = grabber.get_url_template(self.song_id)
            response = urllib.request.urlopen(target)

            filename = self.process_response(response)

        except urllib.request.HTTPError as err:
            pass
        except socket.gaierror as err:
            pass
        except URLError as err:
            pass

        return filename

    def process_response(self, response):
        filename = None

        if response.status is 200:

            disposition_header = response.getheader('Content-Disposition')

            _, pa = cgi.parse_header(disposition_header)
            filename = pa['filename']

        return filename


def main():
    
    # status check and update database
    exists =[]
    does_not_exists = []
    #last checked status : 21724, 21890
    for song_id in range(21890, 21890):
        logger = TreeLogger()

        song_exists, filename = check_status(song_id, logger.branch_out())

        if song_exists:
            exists.append(song_id);
            container.add(song_id, filename)
        else:
            does_not_exists.append(song_id);

    logger.debug(exists)
    logger.debug(does_not_exists)

    logger.purge()

    #download songs found at the server; read song ids from container
    container.fetch_songs()

    #once songs downloaded; clean mp3 tags on the downloaded files.
    #container.clean_tags()


def check_status(song_id, logger):
    mr = MusicResource(song_id, logger)
    filename = mr.get_music_filename()

    song_exists = False

    if filename is not None:
        song_exists = True

    return song_exists, filename


if __name__ == '__main__': main()