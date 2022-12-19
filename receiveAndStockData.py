from pylsl import *

def main():
    print("En attente du début de l'enregistrement :")
    stream = resolve_stream('type','Markers')
    inlet = stream_inlet(stream[0])
    while True:
        sample,timestamp = inlet.pull_sample()
        if sample[0]=='Start':
            break

    while True:
        streams = resolve_stream('type', 'EEG')
        inlet = StreamInlet(streams[0])
        f = open("sauvegardeTest.txt", 'w')
        while True:
            sample, timestamp = inlet.pull_sample()
            print(timestamp, sample)
            for i in range(len(sample)):
                f.write(str(timestamp))
                f.write(" : ")
                f.write(str(sample[i]))
                f.write("\n")
            f.write("\n")
        f.close()

if __name__ == "__main__":
    main()