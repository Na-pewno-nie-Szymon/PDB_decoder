import numpy as np
import pandas as pd
import time as t

starttime = t.time()

pdbPath = 'PDB_decoder\\1phm.pdb'
csvPath = 'PDB_decoder\\koniec.csv'

data = {
    'id':[],
    'aminokwas':[],
    'id-lancucha':[],
    'id-aminokwasu':[],
    'nazwa pierwiastka':[],
    'atom centralny':[],
    'helisa/wstazka/tubka':[],
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

def AtomSlicer(new_data):
    atomATOMSlice = slice(0,4)
    structureSlice = slice(0,6)
    idSlice = slice(6,11)
    aminokwasSlice = slice(17,20)
    pierwiastekSlice = slice(76,78)
    atomCentralnySlice = slice(12,16)
    xSlice = slice(30,38)
    ySlice = slice(38,46)
    zSlice = slice(46,54)
    nrIdAmin = slice(22,26)
    idLancucha = slice(21,22)

    for line in new_data:
        if line[atomATOMSlice] == 'ATOM':
            data['id'].append(line[idSlice])
            data['aminokwas'].append(line[aminokwasSlice])
            data['nazwa pierwiastka'].append(line[pierwiastekSlice])
            data['x'].append(line[xSlice])
            data['y'].append(line[ySlice])
            data['z'].append(line[zSlice])
            data['id-lancucha'].append(line[idLancucha])
            data['id-aminokwasu'].append(line[nrIdAmin])
            data['helisa/wstazka/tubka'].append('T')
            data['dl helisy'].append('0')

            if 'CA' in line[atomCentralnySlice]:    
                data['atom centralny'].append('1')
            else:
                data['atom centralny'].append('0')    


    for line in new_data:        
        if 'HELIX' in line[structureSlice]:
            for idx, val in enumerate(data['id-aminokwasu']):
                if int(line[21:25]) <= int(val) and int(line[33:37]) >= int(val) and data['id-lancucha'][idx] ==  line[19]:
                    data['helisa/wstazka/tubka'][idx] = 'H'
                    data['dl helisy'][idx] = line[71:76]
        elif 'SHEET' in line[structureSlice]:
            for idx, val in enumerate(data['id-aminokwasu']):
                if int(line[22:26]) <= int(val) and int(line[33:37]) >= int(val) and data['id-lancucha'][idx] == line[21]:
                    data['helisa/wstazka/tubka'][idx] = 'S'
        elif 'TURN' in line[structureSlice]:
            for idx, val in enumerate(data['id-aminokwasu']):
                if int(line[20:24]) <= int(val) and int(line[31:35]) >= int(val) and data['id-lancucha'][idx] == line[19]:
                    data['helisa/wstazka/tubka'][idx] = 'T'

def main():
    pdbData = HeavyRamEater()
    AtomSlicer(new_data=pdbData)
    dataFrame = pd.DataFrame(data=data)

    dataFrame.to_csv(csvPath, index=False)

if __name__ == '__main__': 
    main()
    print(t.time() - starttime)
