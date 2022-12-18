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
        print("Les flux arrivent")


if __name__ == "__main__":
    main()