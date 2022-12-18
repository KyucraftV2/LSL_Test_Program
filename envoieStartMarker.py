from pylsl import *
def main():
    streamInfo = StreamInfo("StreamStart","Markers",1,0,'string', 'myuidw43536')
    outlet = StreamOutlet(streamInfo)
    outlet.push_sample("Start")

if __name__ == "__main__":
    main()