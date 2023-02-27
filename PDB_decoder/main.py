import numpy as np
import pandas as pd

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
    with open('PDB_decoder\\1azw.pdb', 'r') as f:
        file = f.readlines()
    
    pdbData = []
    for i in file:
        pdbData.append(i)
    
    return pdbData

def AtomSlicer():
    idSlice = slice(6,11)
    aminokwasSlice = slice(17,20)
    pierwiastekSlice = slice(76,78)
    atomCentralnySlice = slice(12,16)
    


def main():
    pdbData = HeavyRamEater()
    dataFrame = pd.DataFrame(data=data)

if __name__ == '__main__': main()



