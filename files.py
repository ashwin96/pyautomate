import os
import shutil
os.chdir("/Users/ashwin/Downloads/")
lst = os.listdir(".");
#os.makedirs("/Users/ashwin/Downloads/pdfsfinal")
#addr = "/Users/ashwin/Downloads/pdfsfinal";
mp3addr = "/Users/ashwin/Downloads/Music"
mp4addr = "/Users/ashwin/Downloads/Movies"
toraddr = "/Users/ashwin/Downloads/Torrents"
picaddr = "/Users/ashwin/Downloads/Pics/pics"
if not os.path.exists(mp3addr):
	os.makedirs(mp3addr)
if not os.path.exists(mp4addr):
	os.makedirs(mp4addr)
if not os.path.exists(toraddr):
	os.makedirs(toraddr)
if not os.path.exists(picaddr):
	os.makedirs(picaddr)

for i in lst:
	if ".mp3" in i and os.path.isfile(i):
		shutil.move(i,mp3addr)
for i in lst:
	if ".mp4" in i and os.path.isfile(i):
		shutil.move(i,mp4addr)
for i in lst:
	if ".torrent" in i and os.path.isfile(i):
		shutil.move(i,toraddr)
for i in lst:
	if ".jpg" or ".jpeg" in i and os.path.isfile(i):
		shutil.move(i,picaddr)