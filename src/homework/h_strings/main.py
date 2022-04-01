
import strings


menu_selex = "Y"
while menu_selex == "Y":   #This is so that HW Menu is generated
    print('\nHomework 5 Menu\n1-Hamming Distance\n2-DNA Complement\n3-Exit')
    selex = int(input('Please select menu item 1, 2 or 3: ')) 

    if selex == 1:   #This is the Hamming distance part of the assignment
        print('Please enter the bases of your first DNA sequence. YOU MUST INPUT EACH BASE WITH ITS CAPITAL LETTER! (C-Cytosine; A-Adenine; T-Thymine; G-Guanine)')
        dna1 = strings.get_dna1_sequence()
        print('Please enter the bases of your second DNA sequence. NOTE THAT THE SECOND DNA SEQUENCE MUST HAVE THE SAME NUMBER OF BASES (aka, BE THE SAME LENGTH) AS THE FIRST DNA SEQUENCE!')
        dna2 = strings.get_dna1_sequence()
        hamming_distance = strings.get_hamming_distance(dna1,dna2)
        print('Hamming distance is:',hamming_distance)

    elif selex == 2:   #This is the DNA complement part of the assignment
        print('Please enter the bases of the original DNA sequence. YOU MUST INPUT EACH BASE WITH ITS CAPITAL LETTER! (C-Cytosine; A-Adenine; T-Thymine; G-Guanine)')
        dna = strings.get_dna_seqence()
        complement = strings.get_dna_complement(dna)
        print('This is the DNA complement of the original DNA sequence is:', complement)

    elif selex == 3:   #This is the exit from the menu part of the assignment
        print('You have chosen to exit.')
    
    else:
        print("Invalid entry")

    menu_selex = input('Do you want to continue with another menu selection (Enter "Y" for yes, n to exit from Homework 5 Menu): ')






