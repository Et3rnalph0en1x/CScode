#Computational Biology and Mutations Code

#Rajesh Balasamy

#ABE227 3:30 Period

#Stores DNA sequence inputs and makes them into lists

DNA1a = str(input('Enter the first DNA Sequence: '))

DNA2a = str(input('Enter the second DNA Sequence: '))

DNA1 = list(DNA1a)

DNA2 = list(DNA2a)

lengthDNA = len(DNA1)

#Counters

mutations = 0

mutationLocations = []

mutationsType = []

transitions = 0

transversions = 0

synonymousMutations = 0

nonsynonymousMutations = 0

rawCodons1 = []

rawCodons2 = []

codonList1 = []

codonList2 = []


for l in range(0, lengthDNA, 3):

    rawCodons1.append(DNA1[l : l + 3])

    rawCodons2.append(DNA2[l : l + 3])

for k in range(rawCodons1):

    if rawCodons1[k][0] == 'T':

        if rawCodons1[k][1] == 'T':

            if rawCodons1[k][2] == 'T':

                codonList1.append('Phe')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Phe')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Leu')

            else:

                codonList1.append('Leu')

        elif rawCodons1[k][1] == 'C':

            if rawCodons1[k][2] == 'T':

                codonList1.append('Ser')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Ser')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Ser')

            else:

                codonList1.append('Ser')

        elif rawCodons1[k][1] == 'A':

            if rawCodons1[k][2] == 'T':

                codonList1.append('Tyr')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Tyr')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('STOP')

            else:

                codonList1.append('STOP')

        else:

            if rawCodons1[k][2] == 'T':

                codonList1.append('Cys')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Cys')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('STOP')

            else:

                codonList1.append('Trp')

    elif rawCodons1[k][0] == 'C':

        if rawCodons1[k][1] == 'T':

            if rawCodons1[k][2] == 'T':

                codonList1.append('Leu')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Leu')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Leu')

            else:

                codonList1.append('Leu')

        elif rawCodons1[k][1] == 'C':

            if rawCodons1[k][2] == 'T':

                codonList1.append('Pro')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Pro')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Pro')

            else:
                codonList1.append('Pro')

        elif rawCodons1[k][1] == 'A':

            if rawCodons1[k][2] == 'T':

                codonList1.append('His')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('His')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Gin')

            else:

                codonList1.append('Gin')

        else:

            if rawCodons1[k][2] == 'T':

                codonList1.append('Arg')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Arg')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Arg')

            else:

                codonList1.append('Arg')

    elif rawCodons1[k][0] == 'A':

        if rawCodons1[k][1] == 'T':

            if rawCodons1[k][2] == 'T':

                codonList1.append('Ile')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Ile')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Ile')

            else:

                codonList1.append('Met')

        elif rawCodons1[k][1] == 'C':

            if rawCodons1[k][2] == 'T':

                codonList1.append('Thr')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Thr')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Thr')

            else:

                codonList1.append('Thr')

        elif rawCodons1[k][1] == 'A':

            if rawCodons1[k][2] == 'T':

                codonList1.append('Asn')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Asn')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Lys')

            else:

                codonList1.append('Lys')

        else:

            if rawCodons1[k][2] == 'T':

                codonList1.append('Ser')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Ser')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Arg')

            else:

                codonList1.append('Arg')

    else:
    
        if rawCodons1[k][1] == 'T':

            if rawCodons1[k][2] == 'T':

                codonList1.append('Val')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Val')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Val')

            else:

                codonList1.append('Val')

        elif rawCodons1[k][1] == 'C':

            if rawCodons1[k][2] == 'T':

                codonList1.append('Ala')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Ala')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Ala')

            else:

                codonList1.append('Ala')

        elif rawCodons1[k][1] == 'A':

            if rawCodons1[k][2] == 'T':

                codonList1.append('Asp')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Asp')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Glu')

            else:

                codonList1.append('Glu')

        else:

            if rawCodons1[k][2] == 'T':

                codonList1.append('Gly')

            elif rawCodons1[k][2] == 'C':

                codonList1.append('Gly')

            elif rawCodons1[k][2] == 'A':

                codonList1.append('Gly')

            else:

                codonList1.append('Gly')


for k in range(rawCodons2):

    if rawCodons2[k][0] == 'T':

        if rawCodons2[k][1] == 'T':

            if rawCodons2[k][2] == 'T':

                codonList2.append('Phe')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Phe')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Leu')

            else:

                codonList2.append('Leu')

        elif rawCodons2[k][1] == 'C':

            if rawCodons2[k][2] == 'T':

                codonList2.append('Ser')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Ser')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Ser')

            else:

                codonList2.append('Ser')

        elif rawCodons2[k][1] == 'A':

            if rawCodons2[k][2] == 'T':

                codonList2.append('Tyr')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Tyr')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('STOP')

            else:

                codonList2.append('STOP')

        else:

            if rawCodons2[k][2] == 'T':

                codonList2.append('Cys')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Cys')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('STOP')

            else:

                codonList2.append('Trp')

    elif rawCodons2[k][0] == 'C':

        if rawCodons2[k][1] == 'T':

            if rawCodons2[k][2] == 'T':

                codonList2.append('Leu')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Leu')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Leu')

            else:

                codonList2.append('Leu')

        elif rawCodons2[k][1] == 'C':

            if rawCodons2[k][2] == 'T':

                codonList2.append('Pro')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Pro')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Pro')

            else:
                codonList2.append('Pro')

        elif rawCodons2[k][1] == 'A':

            if rawCodons2[k][2] == 'T':

                codonList2.append('His')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('His')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Gin')

            else:

                codonList2.append('Gin')

        else:

            if rawCodons2[k][2] == 'T':

                codonList2.append('Arg')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Arg')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Arg')

            else:

                codonList2.append('Arg')

    elif rawCodons2[k][0] == 'A':

        if rawCodons2[k][1] == 'T':

            if rawCodons2[k][2] == 'T':

                codonList2.append('Ile')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Ile')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Ile')

            else:

                codonList2.append('Met')

        elif rawCodons2[k][1] == 'C':

            if rawCodons2[k][2] == 'T':

                codonList2.append('Thr')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Thr')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Thr')

            else:

                codonList2.append('Thr')

        elif rawCodons2[k][1] == 'A':

            if rawCodons2[k][2] == 'T':

                codonList2.append('Asn')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Asn')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Lys')

            else:

                codonList2.append('Lys')

        else:

            if rawCodons2[k][2] == 'T':

                codonList2.append('Ser')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Ser')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Arg')

            else:

                codonList2.append('Arg')

    else:
    
        if rawCodons2[k][1] == 'T':

            if rawCodons2[k][2] == 'T':

                codonList2.append('Val')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Val')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Val')

            else:

                codonList2.append('Val')

        elif rawCodons2[k][1] == 'C':

            if rawCodons2[k][2] == 'T':

                codonList2.append('Ala')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Ala')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Ala')

            else:

                codonList2.append('Ala')

        elif rawCodons2[k][1] == 'A':

            if rawCodons2[k][2] == 'T':

                codonList2.append('Asp')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Asp')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Glu')

            else:

                codonList2.append('Glu')

        else:

            if rawCodons2[k][2] == 'T':

                codonList2.append('Gly')

            elif rawCodons2[k][2] == 'C':

                codonList2.append('Gly')

            elif rawCodons2[k][2] == 'A':

                codonList2.append('Gly')

            else:

                codonList2.append('Gly')


#For loop that iterates through each DNA Sequence

for i in range(lengthDNA):
            
    if DNA1[i] != DNA2[i]:

        mutations += 1 

        mutationLocations.append(i)

        if ((DNA1[i] == 'A') and (DNA2[i] == 'G')) or ((DNA1[i] == 'G') and (DNA2[i] == 'A')):

            transitions += 1

            mutationsType.append('Transition')

        elif ((DNA1[i] == 'C') and (DNA2[i] == 'T')) or ((DNA1[i] == 'T') and (DNA2[i] == 'C')):

            transitions += 1

            mutationsType.append('Transition')
                
        elif ((DNA1[i] == 'A') and (DNA2[i] == 'C')) or ((DNA1[i] == 'A') and (DNA2[i] == 'T')):

            transversions += 1

            mutationsType.append('Transversion')

        elif ((DNA1[i] == 'C') and (DNA2[i] == 'A')) or ((DNA1[i] == 'C') and (DNA2[i] == 'G')):

            transversions += 1

            mutationsType.append('Transversion')

        elif ((DNA1[i] == 'T') and (DNA2[i] == 'A')) or ((DNA1[i] == 'T') and (DNA2[i] == 'G')):

            transversions += 1

            mutationsType.append('Transversion')

        else:

            transversions += 1

            mutationsType.append('Transversion')
            
        z = i / 3

        if codonList1[z] == codonList2[z]:

            synonymousMutations += 1

        else:

            nonsynonymousMutations += 1

    


        


similarity = (1 - (mutations / lengthDNA))*100

print('The percent similarity is: ', similarity, '%')

print('The number of transitions is: ', transitions)

print('The number of transversions is: ', transversions)

print('The ratio of transition mutations to tranversion mutations is: ', transitions,':',transversions)

print('The ratio of synonymous mutations to nonsynonymous mutations is: ', synonymousMutations,':',nonsynonymousMutations)

print('The locations of the mutations are: ', str(mutationLocations)[1:-1])

for j in range(len(mutationLocations)):

               print('The mutation at location', mutationLocations[j], 'is a', mutationsType[j], 'mutation.')






            
