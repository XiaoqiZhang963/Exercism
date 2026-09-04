def to_rna(dna_strand):
    mapping = {'G':'C','C':'G','T':'A','A':'U'}
    rna = ''.join([mapping.get(letter,'') for letter in dna_strand])
    return rna
