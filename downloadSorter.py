
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("Searching downloads....")
        for filename in os.listdir(folder_to_track):

            src = folder_to_track + "/" + filename
            if "ICA" in filename:
                new_destination = STT180_destination + "/" + filename
                print("==== Moving Filename: ", filename)
                print("==== New Destination: ", new_destination)
                print("--------------------------------------------------------")
                os.rename(src, new_destination)
            elif ("pre-class-assignment" in filename or "in-class-assignment" in filename or "_STUDENT" in filename) and ".ipynb" in filename:
                new_destination = MTH314_destination + "/" + filename
                print("==== Moving Filename: ", filename)
                print("==== New Destination: ", new_destination)
                print("--------------------------------------------------------")
                os.rename(src, new_destination)
            elif ("CC" in filename or "Project" in filename) and ".zip" in filename:
                new_destination = CSE331_destination+ "/" + filename
                print("==== Moving Filename: ", filename)
                print("==== New Destination: ", new_destination)
                print("--------------------------------------------------------")
                os.rename(src, new_destination)



folder_to_track = "/Users/willdiamond/Downloads"
STT180_destination = "/Users/willdiamond/Desktop/Classes/STT180"
MTH314_destination = "/Users/willdiamond/Desktop/Classes/MTH314"
CSE331_destination = "/Users/willdiamond/Desktop/Classes/CSE331"


print("#################################################")
print("####### Running Automated Download Sorter #######")
print("#################################################")
print()
print()
print("==== Downloads path: ", folder_to_track)
print("==== STT180 path: ", STT180_destination)
print("==== MTH314 path: ", MTH314_destination)
print("==== CSE331 path: ", CSE331_destination)
print()
print()
print()
print("--------------------------------------------------------")
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
