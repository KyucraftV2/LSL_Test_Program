import getopt
import sys
import time

from typing import List
from pylsl import *
from random import random

def main(argv: List[str]):
    name = "Flux de secondes"
    type = "EEG"
    help_string = 'SendData.py -s <sampling_rate> -n <stream_name> -t <stream_type>'
    opts = List[tuple]
    n_channels = 8
    srate = 100
    try:
        opts,args = getopt.getopt(argv,"hs:c:n:t:",["srate=", "channels=", "name=", "type"])
        #opts est une liste de tuple (option,value) et args est la liste d'arguments non utilisés par getopt
    except getopt.GetoptError: #une erreur peut etre levé a cause du dernier parametre de getopt
        print("Erreur bizarre faut que je cherche ce que c'est")

    for opt,arg in opts : #Va récupérer après la commande le taux de sample, nombre de channels par sample, le nom et enfin le type du stream
        if opt=="-h":
            print(help_string)
            sys.exit()
        elif opt in ("-s", "--srate"):
            srate = float(arg)
        elif opt in ("-c", "--channels"):
            n_channels = int(arg)
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-t", "--type"):
            type = arg

    #Créer le stream d'info qui contient tout ce qu'on vient de récupérer
    info = StreamInfo(name,type,n_channels,srate,'float32','miuid34234')

    #Création de l'outlet
    outlet = StreamOutlet(info)

    #Envoi des données
    print("Envoi des données")
    start_time = local_clock()
    sent_samples = 0
    while True:
        elapsed_time = local_clock()-start_time
        required_samples = int(srate*elapsed_time) - sent_samples
        for sample in range(required_samples):
            mysample = [random() for _ in range(n_channels)]
            outlet.push_sample(mysample)
        sent_samples += required_samples
        time.sleep(1)

if __name__ == '__main__':
    main(sys.argv[1:])