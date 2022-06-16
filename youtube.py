from pytube import YouTube
link=input("enter the video link: ")

youtube_1 = YouTube(link)

#print(youtube_1.title) //For getting the Video Title
#print(youtube_1.thumbnail_url) // For getting the Thumbnail Link
video = youtube_1.streams.all()  #for getting full video and audio types
video=youtube_1.streams.filter(only_audio=True) #for getting only audio types 

vid = list(enumerate(video))
for i in vid:
	print(i)

strm = int(input("enter : "))
video[strm].download()
print('Sucessfully')

