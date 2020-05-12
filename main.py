from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os
import time
folder_track = 'C:/Users/VencPC/Downloads' # Папка за которой следим
folder_dest = 'C:/Users/VencPC/Desktop/test' # Куда кидаем все что не подошло по критериям
folder_dest_photo = 'C:/Users/VencPC/Desktop/test/photo'
folder_dest_text = 'C:/Users/VencPC/Desktop/test/text'
folder_dest_app = 'C:/Users/VencPC/Desktop/test/app'
folder_dest_audio = 'C:/Users/VencPC/Desktop/test/music'
folder_dest_video = 'C:/Users/VencPC/Desktop/test/video'
folder_dest_table = 'C:/Users/VencPC/Desktop/test/table'
folder_dest_7z = 'C:/Users/VencPC/Desktop/test/7z'
folder_dest_torrent = 'C:/Users/VencPC/Desktop/test/torrent'
folder_dest_scan = 'C:/Users/VencPC/Desktop/test/scan'



listphoto = ['jpg','jpeg', 'png'] # Список форматов фото
listtext = ['doc','txt','docx', 'epub', 'fb2']
listapp = ['exe', 'apk', 'com', 'jar']
listaudio = ['mp3','aac','ogg', 'wav', 'flac', 'ac3', 'aa', 'wma', 'm4a']
listvideo = ['mpg','avi', 'wmv', 'mov', 'mkv', 'mp4', 'mpeg']
listtable = []
list7z = ['rar','7z','zip', 'iso', 'dmg', 'gz']
listscan = ['pdf']
listtorrent = ['torrent']



class Handler(FileSystemEventHandler):

    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split('.')
            print(extension)
            if len(extension) > 1 and (extension[-1].lower() == 'ini'):
                pass
            elif len(extension) > 1 and (extension[-1].lower() in listphoto):
                file = folder_track + "/" + filename
                new_path = folder_dest_photo + '/' + filename
                os.rename(file, new_path)
            elif len(extension) > 1 and (extension[-1].lower() in listtext):
                file = folder_track + "/" + filename
                new_path = folder_dest_text + '/' + filename
                os.rename(file, new_path)
            elif len(extension) > 1 and (extension[-1].lower() in listapp):
                file = folder_track + "/" + filename
                new_path = folder_dest_app + '/' + filename
                os.rename(file, new_path)
            elif len(extension) > 1 and (extension[-1].lower() in listvideo):
                file = folder_track + "/" + filename
                new_path = folder_dest_video + '/' + filename
                os.rename(file, new_path)
            elif len(extension) > 1 and (extension[-1].lower() in listaudio):
                file = folder_track + "/" + filename
                new_path = folder_dest_audio + '/' + filename
                os.rename(file, new_path)
            elif len(extension) > 1 and (extension[-1].lower() in listtorrent):
                file = folder_track + "/" + filename
                new_path = folder_dest_torrent + '/' + filename
                os.rename(file, new_path)
            elif len(extension) > 1 and (extension[-1].lower() in list7z):
                file = folder_track + "/" + filename
                new_path = folder_dest_7z + '/' + filename
                os.rename(file, new_path)
            elif len(extension) > 1 and (extension[-1].lower() in listtable):
                file = folder_track + "/" + filename
                new_path = folder_dest_table + '/' + filename
                os.rename(file, new_path)
            elif len(extension) > 1 and (extension[-1].lower() in listscan):
                file = folder_track + "/" + filename
                new_path = folder_dest_scan + '/' + filename
                os.rename(file, new_path)
            else:
                file = folder_track +"/" +filename
                new_path = folder_dest + '/' + filename
                os.rename(file,new_path)
handle = Handler()
observer = Observer()
observer.schedule(handle,folder_track, recursive=True)
observer.start()


try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    print('Ошибка ну и пофиг')
    # observer.stop()

observer.join()
