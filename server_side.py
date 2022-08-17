from urllib.request import urlretrieve
from threading import Thread
import requests
import argparse
parser = argparse.ArgumentParser()
class DownloadThread():
    def __init__(self, Thread, parent, url, vid_code, fsize):
        """Constructor"""
        Thread.__init__(self)
        self.fsize = fsize
        self.url = url
        self.parent = parent
        self.vid_code = vid_code
        self.run()
        self.reporthook()

    def run(self):
        local_fname = self.vid_code + ".mp4"
        try:
            urlretrieve(self.url, local_fname, self.reporthook)
        except:
            urlretrieve(self.url, "default.mp4", self.reporthook)

    def reporthook(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = int((readsofar / totalsize) * 100)
        else:  # total size is unknown
            percent = 0
        # Initial call to print 0% progress
        print(percent)
class MainPanel():
    def __init__(self, url, vid_code):
        self.url = url
        self.vid_code = vid_code
        self.download_number = 8
        self.onDownload()

    def onDownload(self):

        """
        Update display with downloading gauges
        """
        try:

            header = requests.head(self.url, allow_redirects=True)
            fsize = int(header.headers["content-length"]) / 1024
            # start thread
            DownloadThread(Thread, self.download_number, self.url, self.vid_code, fsize)
        except Exception as e:
            print()
if __name__ == "__main__":
    parser.add_argument("-url", "--url_video", help="Video URL")
    parser.add_argument("-code", "--video_code", help="Video Code")
    args = parser.parse_args()

    url_video = args.url_video
    video_code = args.video_code
    MainPanel(url_video, video_code)
