#!/usr/bin/env python2
import unittest
import hashlib
import os

from youtube_dl.FileDownloader import FileDownloader
from youtube_dl.InfoExtractors  import YoutubeIE, DailymotionIE
from youtube_dl.InfoExtractors import  MetacafeIE, PhotobucketIE
from youtube_dl.InfoExtractors import FacebookIE

class DownloadTest(unittest.TestCase):
	#calculated with md5sum:
	#	md5sum (GNU coreutils) 8.19
	YOUTUBE_MD5 = "8547978241cb87dd6782b10b8e90acc3"
	YOUTUBE_URL = "http://www.youtube.com/watch?v=BaW_jenozKc"
	YOUTUBE_FILE = "BaW_jenozKc.flv"


	DAILYMOTION_MD5 = ""
	DAILYMOTION_URL = "http://www.dailymotion.com/video/x33vw9_tutoriel-de-youtubeur-dl-des-video_tech"
	DAILYMOTION_FILE = ""


	METACAFE_MD5 = ""
	METACAFE_URL = "http://www.metacafe.com/watch/yt-bV9L5Ht9LgY/download_youtube_playlist_with_youtube_dl/"
	METACAFE_FILE = ""


	PHOTOBUCKET_MD5 = ""
	PHOTOBUCKET_URL = "http://www.metacafe.com/watch/yt-bV9L5Ht9LgY/download_youtube_playlist_with_youtube_dl/"
	PHOTOBUCKET_FILE = ""


	FACEBOOK_MD5 = ""
	FACEBOOK_URL = "https://www.facebook.com/video/video.php?v=207446242657384"
	FACEBOOK_FILE = ""


	def test_youtube(self):
		#let's download a file from youtube
		fd = FileDownloader({})
		fd.add_info_extractor(YoutubeIE())
		fd.download([DownloadTest.YOUTUBE_URL])
		self.assertTrue(os.path.exists(DownloadTest.YOUTUBE_FILE))
		md5_down_file = md5_for_file(DownloadTest.YOUTUBE_FILE)
		self.assertEqual(md5_down_file, DownloadTest.YOUTUBE_MD5)

	def test_dailymotion(self):
		fd = FileDownloader({})
		fd.add_info_extractor(DailymotionIE())
		fd.download([DownloadTest.DAILYMOTION_URL])
		self.assertTrue(os.path.exists(DownloadTest.DAILYMOTION_FILE))
		md5_down_file = md5_for_file(DownloadTest.DAILYMOTION_FILE)
		self.assertEqual(md5_down_file, DownloadTest.DAILYMOTION_MD5)


	def test_metacafe(self):
		fd = FileDownloader({})
		fd.add_info_extractor(MetacafeIE())
		fd.download([DownloadTest.METACAFE_URL])
		self.assertTrue(os.path.exists(DownloadTest.METACAFE_FILE))
		md5_down_file = md5_for_file(DownloadTest.METACAFE_FILE)
		self.assertEqual(md5_down_file, DownloadTest.METACAFE_MD5)

	def test_photobucket(self):
		fd = FileDownloader({})
		fd.add_info_extractor(PhotobucketIE())
		fd.download([DownloadTest.PHOTOBUCKET_URL])
		self.assertTrue(os.path.exists(DownloadTest.PHOTOBUCKET_FILE))
		md5_down_file = md5_for_file(DownloadTest.PHOTOBUCKET_FILE)
		self.assertEqual(md5_down_file, DownloadTest.PHOTOBUCKET_MD5)


	def test_facebook(self):
		fd = FileDownloader({})
		fd.add_info_extractor(FacebookIE())
		fd.download([DownloadTest.FACEBOOK_URL])
		self.assertTrue(os.path.exists(DownloadTest.FACEBOOK_FILE))
		md5_down_file = md5_for_file(DownloadTest.FACEBOOK_FILE)
		self.assertEqual(md5_down_file, DownloadTest.FACEBOOK_MD5)

	def cleanUp(self):
		if os.path.exists(DownloadTest.YOUTUBE_FILE):
			os.remove(DownloadTest.YOUTUBE_FILE)
		if os.path.exists(DownloadTest.DAILYMOTION_FILE):
			os.remove(DownloadTest.DAILYMOTION_FILE)
		if os.path.exists(DownloadTest.METACAFE_FILE):
			os.remove(DownloadTest.METACAFE_FILE)
		if os.path.exists(DownloadTest.PHOTOBUCKET_FILE):
			os.remove(DownloadTest.PHOTOBUCKET_FILE)
		if os.path.exists(DownloadTest.FACEBOOK_FILE):
			os.remove(DownloadTest.FACEBOOK_FILE)

def md5_for_file(f, block_size=2**20):
	md5 = hashlib.md5()
	while True:
		data = f.read(block_size)
		if not data:
			break
		md5.update(data)
		return md5.digest()
