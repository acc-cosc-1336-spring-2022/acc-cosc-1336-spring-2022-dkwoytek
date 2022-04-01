
def get_dna1_sequence():
    dna1 = []
    another_dna_base = "Y"
    while another_dna_base == "Y":
        dna_base = str(input('Enter a DNA base: '))
        dna1.append(dna_base)
        print('Do you want to add another DNA base?')
        another_dna_base = input("Y = yes, anything else = no: ")
        print()
    return dna1

def get_dna2_sequence():
    dna2 = []
    another_dna_base = "Y"
    while another_dna_base == "Y":
        dna_base = str(input('Enter a DNA base: '))
        dna2.append(dna_base)
        print('Do you want to add another DNA base?')
        another_dna_base = input("Y = yes, anything else = no: ")
        print()
    return dna2

def get_hamming_distance(dna1, dna2):
    index = 0
    ham = 0
    while index < len(dna1):
        if dna1[index] != dna2[index]:
            ham += 1
        index += 1
    return ham
        
def get_dna_seqence():
    dna = []
    another_dna_base = "Y"
    while another_dna_base == "Y":
        dna_base = str(input("Enter a DNA base: "))
        dna.append(dna_base)
        print('Do you want to add another DNA base?')
        another_dna_base = input("Y = yes, anything else = no: ")
        print()
    return dna

def get_dna_complement(dna):
    dna.reverse()
    index = 0
    while index < len(dna):
        if dna[index] == 'A':
            dna[index] = 'T'
        elif dna[index] == 'T':
            dna[index] = 'A'
        elif dna[index] == 'C':
            dna[index] = 'G'
        else:
            dna[index] = 'C'
        
        index += 1
    
    return dna



