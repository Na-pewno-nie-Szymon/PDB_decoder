import numpy as np
import pandas as pd

pdbPath = 'PDB_decoder\\1azw.pdb'
csvPath = 'PDB_decoder\\1azw.csv'

data = {
    'id':[],
    'aminokwas':[],
    'nazwa pierwiastka':[],
    'atom centralny':[],
    'helisa/wstarzka/tubka':[],
    'dl helisy':[],
    'x':[],
    'y':[],
    'z':[]
}

def HeavyRamEater():
    with open(pdbPath, 'r') as f:
        file = f.readlines()
    
    pdbData = []
    for i in file:
        pdbData.append(i)
    
    return pdbData

def AtomSlicer():
    atomATOMSlice = slice(0,4)
    idSlice = slice(6,11)
    aminokwasSlice = slice(17,20)
    pierwiastekSlice = slice(76,78)
    atomCentralnySlice = slice(12,16)
    xSlice = slice(30,38)
    ySlice = slice(38,46)
    zSlice = slice(46,54)


def main():
    pdbData = HeavyRamEater()
    dataFrame = pd.DataFrame(data=data)

if __name__ == '__main__': main()



