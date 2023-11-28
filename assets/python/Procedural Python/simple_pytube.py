from pytube import YouTube
link = input("Digite a URL do video do YouTube: ")
video = YouTube(link)
video.streams.get_highest_resolution().download(output_path = "C:\\Users\\isaac\\Downloads\\pytube", filename = "download")
