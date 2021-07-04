!pip install pytube
from pytube import YouTube
url =input("Enter url of the youtube video")
myvid=YouTube(url)
print("Details of the video as follows")
print("Title: ",myvid.title)
print("Thumbnail url:",myvid.thumbnail_url)
print("If you wanna download enter the following numbers:\n1.Highest resolution\n2.lowest resolution\n3.only audio")
choice= int(input("Enter your choice: "))
streams = myvid.streams
if choice==1:
  streams.get_highest_resolution().download()
elif choice==2:
  streams.get_lowest_resolution().download()
elif choice==3:
  streams.get_audio_only().download()
