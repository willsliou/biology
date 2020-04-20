Nucleotides = ["A", "C", "G", "T"]

# Input Validation
def validateSequence(dna_seq):
    temp = dna_seq.upper()
    for i in temp:
        if i not in Nucleotides:
            return "Not a valid DNA sequence"
    return temp
