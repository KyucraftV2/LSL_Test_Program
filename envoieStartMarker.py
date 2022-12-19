import time

from pylsl import *

def main():
    global envoie
    streamInfo = StreamInfo("StreamStart","Markers",1,0,'string', 'myuidw43536')
    outlet = StreamOutlet(streamInfo)
    envoie = True
    while envoie:
        outlet.push_sample(['Start'])
        time.sleep(2)

if __name__ == "__main__":
    main()