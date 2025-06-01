# Search for an exact match, or a word with * or . notation for other letters to be included in acceptable matches.
def find_words(search_term: str):
    results = []
    with open("words.txt") as file:
        for line in file:
            word = line.strip()

            if "." not in search_term and "*" not in search_term:
                if word == search_term:
                    results.append(word)

            elif "." in search_term:
                if len(word) != len(search_term):
                    continue

                match = True
            
                for i in range(len(word)):
                    if search_term[i] != "." and search_term[i] != word[i]:
                        match = False
                        break
                
                if match:
                    results.append(word)

            elif "*" in search_term: 

                if search_term.startswith('*'):
                    suffix = search_term[1:]
                    if word.endswith(suffix):
                        results.append(word)   

                elif search_term.endswith('*'):
                    prefix = search_term[:-1]
                    if word.startswith(prefix):
                        results.append(word)   
    return results
            
