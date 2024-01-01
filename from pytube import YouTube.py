from pytube import YouTube
from moviepy.editor import *

# YouTube video URL'si
video_url = 'https://youtu.be/qgn_Wngf4wM'  # İndirmek istediğiniz video URL'sini buraya yazın

# YouTube nesnesi oluştur
yt = YouTube(video_url)

# En yüksek kalitedeki sesi seç
video = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

# İndirme klasörü yolu
download_folder = r'C:\Users\ekinz\OneDrive\Masaüstü\python indirilenler'  

# Dosya adı (MP4 uzantısı ile)
download_file = video.download(download_folder)

# MP4 dosyasının adını al (MP3'e dönüştürmek için)
base, ext = os.path.splitext(download_file)
new_file = base + '.mp3'

# MP4 dosyasını MP3'e dönüştür
clip = AudioFileClip(download_file)
clip.write_audiofile(new_file)

# Orijinal MP4 dosyasını sil
os.remove(download_file)

print(f"Video başarıyla indirildi ve MP3'e dönüştürüldü: {new_file}")
