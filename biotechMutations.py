#Computational Biology and Mutations Code

#Rajesh Balasamy

#ABE227 3:30 Period

#Stores DNA sequence inputs and makes them into lists

DNA1a = str(input('Enter the first DNA Sequence: '))

DNA2a = str(input('Enter the second DNA Sequence: '))

DNA1 = list(DNA1a)

DNA2 = list(DNA2a)

lengthDNA = len(DNA1)

#Counters for information that will be printed/returned at the end of the program

mutations = 0

mutationLocations = []

mutationsType = []

transitions = 0

transversions = 0

synonymousMutations = 0

synonymousMutationLocations = []

nonsynonymousMutations = 0

rawCodons1 = []

rawCodons2 = []

codonList1 = []

codonList2 = []

#This function goes throughout each DNA sequence and splits them up into groups of three base pairs. These three base pairs get appended to

#a list called rawCodons(1/2), which will then be processed below.

for l in range(0, lengthDNA, 3):

    rawCodons1.append(DNA1[l : l + 3])

    rawCodons2.append(DNA2[l : l + 3])

#This function takes the list of rawCodons and uses nested if/elif/else loops to determine what codon the specific group of three is. For example, if

#the codon from rawCodons is TTC, it would return yes on the first if loop, yes on the second if loop, no on the third if loop, and yes on the second elif loop.

#This means that TTC is the codon for amino acid Phe. The string Phe is then appended to another list called codonList(1/2). This function is repeated twice, one for

#the first DNA sequence, and one for the second DNA sequence. An alternate way to code this would be to keep this function in a main function, and call it twice,

#once for the first DNA sequence, and one for the second DNA sequence.

for k in range(len(rawCodons1)):

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


for h in range(len(rawCodons2)):

    if rawCodons2[h][0] == 'T':

        if rawCodons2[h][1] == 'T':

            if rawCodons2[h][2] == 'T':

                codonList2.append('Phe')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Phe')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Leu')

            else:

                codonList2.append('Leu')

        elif rawCodons2[h][1] == 'C':

            if rawCodons2[h][2] == 'T':

                codonList2.append('Ser')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Ser')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Ser')

            else:

                codonList2.append('Ser')

        elif rawCodons2[h][1] == 'A':

            if rawCodons2[h][2] == 'T':

                codonList2.append('Tyr')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Tyr')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('STOP')

            else:

                codonList2.append('STOP')

        else:

            if rawCodons2[h][2] == 'T':

                codonList2.append('Cys')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Cys')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('STOP')

            else:

                codonList2.append('Trp')

    elif rawCodons2[h][0] == 'C':

        if rawCodons2[h][1] == 'T':

            if rawCodons2[h][2] == 'T':

                codonList2.append('Leu')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Leu')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Leu')

            else:

                codonList2.append('Leu')

        elif rawCodons2[h][1] == 'C':

            if rawCodons2[h][2] == 'T':

                codonList2.append('Pro')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Pro')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Pro')

            else:
                codonList2.append('Pro')

        elif rawCodons2[h][1] == 'A':

            if rawCodons2[h][2] == 'T':

                codonList2.append('His')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('His')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Gin')

            else:

                codonList2.append('Gin')

        else:

            if rawCodons2[h][2] == 'T':

                codonList2.append('Arg')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Arg')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Arg')

            else:

                codonList2.append('Arg')

    elif rawCodons2[h][0] == 'A':

        if rawCodons2[h][1] == 'T':

            if rawCodons2[h][2] == 'T':

                codonList2.append('Ile')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Ile')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Ile')

            else:

                codonList2.append('Met')

        elif rawCodons2[h][1] == 'C':

            if rawCodons2[h][2] == 'T':

                codonList2.append('Thr')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Thr')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Thr')

            else:

                codonList2.append('Thr')

        elif rawCodons2[h][1] == 'A':

            if rawCodons2[h][2] == 'T':

                codonList2.append('Asn')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Asn')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Lys')

            else:

                codonList2.append('Lys')

        else:

            if rawCodons2[h][2] == 'T':

                codonList2.append('Ser')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Ser')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Arg')

            else:

                codonList2.append('Arg')

    else:
    
        if rawCodons2[h][1] == 'T':

            if rawCodons2[h][2] == 'T':

                codonList2.append('Val')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Val')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Val')

            else:

                codonList2.append('Val')

        elif rawCodons2[h][1] == 'C':

            if rawCodons2[h][2] == 'T':

                codonList2.append('Ala')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Ala')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Ala')

            else:

                codonList2.append('Ala')

        elif rawCodons2[h][1] == 'A':

            if rawCodons2[h][2] == 'T':

                codonList2.append('Asp')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Asp')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Glu')

            else:

                codonList2.append('Glu')

        else:

            if rawCodons2[h][2] == 'T':

                codonList2.append('Gly')

            elif rawCodons2[h][2] == 'C':

                codonList2.append('Gly')

            elif rawCodons2[h][2] == 'A':

                codonList2.append('Gly')

            else:

                codonList2.append('Gly')


#This is a for loop that iterates for the length of the DNA sequence. Given the background of this problem/program, both DNA sequences would be the exact same length.

#The inside if loop checks if the i-th entry for each sequence. If they are the same, it moves on to the next base pair in each sequence. If they aren't the same, the code

#moves inward in the if loop. First, a counter is incremented by one to show that there is a mutation present. The i value, which is the location of the differing base pairs,  

#is appended to a list that marks the locations of the mutations. Next is a series of if/elif/else loops. These loops use logic, with and/or checkers, to determine if the mutation

#is a transition of a transversion. An example for a transition mutation would be if DNA sequence 1's base pair is C, and DNA sequence 2's base pair is T. This would prove the logic in

#elif loop 1 correct, which would increment the transition counter by one, and also append a string called Transition to a list called mutationsType, that marks whether the

#mutation is a transition or transversion. This will be used later to return the specific type of mutation at a certain location. The last part of the if loop that is triggered if

#a mutation is found deals with synonymous versus nonsynonymous mutations. Since both synonymous and nonsynonymous mutatations occurs when there is a mutation, we add this code to the  

#end of this if loop instead of having it outside. Synonymous and nonsynonymous mutations differ based on whether the amino acids change or not, so this code will reference the 

#earlier function that translated the DNA sequences into raw codons into amino acids. The variable z is equal to i / 3. Since i is our position in the DNA sequence, this divided by 

#three, rounded down as its casted as an integer, would return the position of the amino acid in the list from the code referenced above. The next if loop checks whether the z-th codon

#in DNA sequence 1 and 2 are the same. If they are the same, the synonymous counter is incremented by one; if they aren't, the nonsynonymous counter is increased by one. The last part  

#of the synonymous mutation code appends synonymous or nonsynonymous mutation to a list. This will be used later similar to the transition/transversion lists.
                
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
            
        z = int(i / 3)

        if codonList1[z] == codonList2[z]:

            synonymousMutations += 1

            synonymousMutationLocations.append('Synonymous Mutation.')

        else:

            nonsynonymousMutations += 1

            synonymousMutationLocations.append('Nonsynonymous Mutation.')


#This last portion deals with returning the values that have been processed above. The first line deals with similarity, and returns the percentage of base pairs that

#aren't mutated. There are several print statements that print the values of the variables, such as similarity, number of mutations, and the ratios. The last  print

#statement print the locations of the mutations, and the locations of the synonymous and nonsynonymous mutations in two seperate statements. They use for loops to iterate

#through the mutationLocations list and print the values appended to the list with it's specific location number.     


similarity = (1 - (mutations / lengthDNA))*100

print('The percent similarity is: ', similarity, '%')

print('The number of mutations is: ', mutations)

print('The number of transitions is: ', transitions)

print('The number of transversions is: ', transversions)

print('The ratio of transition mutations to tranversion mutations is: ', transitions,':',transversions)

print('The ratio of synonymous mutations to nonsynonymous mutations is: ', synonymousMutations,':',nonsynonymousMutations)

print('The locations of the mutations are: ', str(mutationLocations)[1:-1])

for j in range(len(mutationLocations)):

               print('The mutation at location', mutationLocations[j], 'is a', mutationsType[j], 'mutation.')

               print('The mutation at location',mutationLocations[j], 'is a', synonymousMutationLocations[j])



               






            
