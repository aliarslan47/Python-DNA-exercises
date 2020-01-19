#counting Nucleotide frequency of a given DNA sample
DNA = open("sequence.fasta", "r")
content = DNA.read()

A = content.count("A")
T = content.count("T")
C = content.count("C")
G = content.count("G")
print("number of A in your sequance is : ", A)
print("number of A in your sequance is : ", T)
print("number of A in your sequance is : ", C)
print("number of A in your sequance is : ", G)
print("the GC ratio of your DNA sequence is : ", (G+C)/(G+C+T+A))
