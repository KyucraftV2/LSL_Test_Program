import getopt
import sys
import time

from typing import List
from pylsl import *
from random import random

def main(argv: List[str]):
    nomFlux = "Flux de secondes"
    type = "EEG"
    helpString = 'SendData.py -s <sampling_rate> -n <stream_name> -t <stream_type>'
    nbChannels = 8
    tauxSample = 100
    try:
        opts,args = getopt.getopt(argv,"hs:c:n:t:",["srate=", "channels=", "name=", "type"])
        #opts est une liste de tuple (option,value) et args est la liste d'arguments non utilisés par getopt
    except getopt.GetoptError: #une erreur peut etre levé a cause du dernier parametre de getopt
        print("Erreur de getopt, vérifiez les paramètres")

    for opt,arg in opts : #Va récupérer après la commande le taux de sample, nombre de channels par sample, le nom et enfin le type du stream
        if opt=="-h":
            print(helpString)
            sys.exit()
        elif opt in ("-s", "--srate"):
            tauxSample = float(arg)
        elif opt in ("-c", "--channels"):
            nbChannels = int(arg)
        elif opt in ("-n", "--name"):
            nomFlux = arg
        elif opt in ("-t", "--type"):
            type = arg

    #Créer le stream d'info qui contient tout ce qu'on vient de récupérer
    streamInfo = StreamInfo(nomFlux,type,nbChannels,tauxSample,'float32','miuid34234')

    #Création de l'outlet
    outlet = StreamOutlet(streamInfo)

    #Envoi des données
    print("Envoi des données")
    startTime = local_clock()
    sentSamples = 0
    while True:
        elapsedTime = local_clock()-startTime
        requiredSamples = int(tauxSample*elapsedTime) - sentSamples
        for sample in range(requiredSamples):
            listeSampleEnvoie = [random() for _ in range(nbChannels)]
            outlet.push_sample(listeSampleEnvoie)
        sentSamples += requiredSamples
        time.sleep(1)

if __name__ == '__main__':
    main(sys.argv[1:])