#By Kisothan Suthakaran
#The mass_mol function could compute the mass of molecule if you input 2 things, a string  representing the chemical formula
#of the molecule and a dictionnary assigning the molar mass of each of the atoms present in the molecule. 


def count_chars(string):
    dict_={}
    for char in string[:]:
        if char in dict_:
            dict_[char]+=1
        else:
            dict_[char]=1
    return(dict_)

def mass_mol(table, mol): 
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tup_alpha=tuple(alphabet)
    occur_dict_=count_chars(mol)
    count_dict={}
    M=0
    for atom in mol: 
        i=0
        if mol.index(atom)!=len(mol)-1:
            if mol[mol.index(atom)+1] not in tup_alpha:
                if mol.index(atom)+1!=len(mol)-1:
                    while mol[mol.index(atom)+1+i] not in tup_alpha:
                        i+=1
                        if mol.index(atom)+i==len(mol)-1:
                            break    
                else:
                    i=1
            else:
                if atom in tup_alpha and mol.index(atom)!=len(mol)-1:
                    if mol[mol.index(atom)+1] in tup_alpha :
                        if atom not in count_dict: 
                            M+=occur_dict_[atom]*table[atom]
                            count_dict[atom]=1 
                    elif mol[mol.index(atom)+1] not in tup_alpha:
                        M+=table[atom]*int(mol[mol.index(atom)+1])
                elif atom in tup_alpha and mol.index(atom)==len(mol)-1:
                    M+=occur_dict_[atom]*table[atom]
                elif atom not in tup_alpha:
                    continue 
                
        if atom in tup_alpha and mol.index(atom)!=len(mol)-1:
            if mol[mol.index(atom)+i] in tup_alpha :
                if atom not in count_dict: 
                    M+=occur_dict_[atom]*table[atom]
                    count_dict[atom]=1 
            elif mol[mol.index(atom)+i] not in tup_alpha:
                add=""
                for k in range(1,i+1):
                    add+=mol[mol.index(atom)+k]
                M+=table[atom]*int(add)
        elif atom in tup_alpha and mol.index(atom)==len(mol)-1:
            M+=occur_dict_[atom]*table[atom]
        elif atom not in tup_alpha:
            continue
    return(M)

#TEST

print(mass_mol({"H":1,"C":12,"N":14,"O":16},"C18H2452O"))  

  