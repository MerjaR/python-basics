# Find gene in genome, not overlapping
def find_gene_positions(gene: str, genome: str):
    result = []
    i = 0
    found = False
    for i in range(0, len(genome)-len(gene)+1):
        current_letter = gene[0]
        if genome[i] == current_letter:
            position = i
            for j in range(0,len(gene)):
                if genome[i+j] == gene[j]:
                    found = True
                else:
                    found = False
                    break
            if found:
                result.append(position)
    k = 1
    while k <= len(result)-1:
        value = result[k]
        end_position = result[k-1] + len(gene) - 2
        if value <= end_position:
            result.remove(result[k])
        k = k + 1
    if result:       
        return result
            
                
if __name__ == "__main__":
    genome = "ATCGAGATCGACGATCGTAGCTAGCTAGCTAGCGATCGA"
    gene1 = "TAGCTA"
    gene2 = "ATCGA"
    gene3 = "X"

    print(find_gene_positions(gene1, genome))
    print(find_gene_positions(gene2, genome))
    print(find_gene_positions(gene3, genome))
    print(type((find_gene_positions(gene3, genome))))


        
