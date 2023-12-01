
dnastring = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
SymbolDictionary = {
    "A" : 0,
    "C" : 0,
    "G" : 0,
    "T" : 0
}
if not len(dnastring) > 1000:
    for Symbol in dnastring:
        SymbolDictionary[Symbol] +=1

    for entries in SymbolDictionary.values():
        print(entries, end=" ")
else:
    print("to many nucleotides")
    exit()