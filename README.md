# Python-DNA-exercises
#counting Nucleotide frequency of a given DNA sample
DNA = input("please enter your DNA sequance below:\n")
A = DNA.count("A")
T = DNA.count("T")
C = DNA.count("C")
G = DNA.count("G")
print("the number of A in your DNA sequance is : ", A)
print("the number of T in your DNA sequance is : ", T)
print("the number of C in your DNA sequance is : ", C)
print("the number of G in your DNA sequance is : ", G)
print("the GC ratio of your DNA sequence is : ", (G+C)/(G+C+T+A))
