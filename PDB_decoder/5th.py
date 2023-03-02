from Bio.PDB import PDBParser
import pandas as pd

pdb_file = "3dkc.pdb" #ścieżka dostępu do pdb
csv_file = "output.csv" #output csv

parser = PDBParser()

structure = parser.get_structure("structure", pdb_file)

with open(csv_file, "w") as f:
    #kolumny
    f.write("l.p,residue_name, symbol, CA, x_coord, y_coord, z_coord\n")
    #SMCRA - (Structure/Model/Chain/Residue/Atom)
    for model in structure: #model w strukturze
        for chain in model: #łańcuch w modelu
            for residue in chain: #reszta w łańcuchu (dla 3-literowego skrótu aminokwasu)
                for atom in residue: #dla atomu w reszcie
                    atom_serial = atom.get_serial_number() #numer atomu
                    residue_name = residue.get_resname() #3-literowy skrót aminokwasu
                    atom_name = atom.get_name() #symbol atomu w całości
                    x_coord, y_coord, z_coord = atom.get_coord() #koordynacja
                    CA = int(atom_name == "CA") #czy jest alfa węglęm

                    #wpisanie ostateczne danych do csv + utworzenie pliku
                    f.write(f"{atom_serial},{residue_name},{atom_name},{CA},{x_coord:.3f},{y_coord:.3f},{z_coord:.3f}\n")

pd.options.display.max_rows = 9999

df = pd.read_csv('output.csv')

print(df)
