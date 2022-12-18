import time

from pylsl import *
def main():
    streamInfo = StreamInfo("StreamStart","Markers",1,0,'string', 'myuidw43536')
    outlet = StreamOutlet(streamInfo)
    while True:
        outlet.push_sample(['Start'])
        time.sleep(2)

if __name__ == "__main__":
    main()