from group_class import Word

def num_gens_used(words): #number of generators used by a list of Words
    return max([word.gens for word in words])

def subtups(lst, length): #output: set of all lists of length up to length formed from elements of lst
    lists = [[x] for x in lst]
    for i in range(1, length):
        for l in lists:
            for x in lst:
                lists.append(l+[x])
    return set(lists)

def normal_subgroup_generated_by_words(words, num_gens, limit): #input: list of Words and number of generators, and a limit to the length of the words in the resturned list
    if num_gens_used(words) > num_gens:
        raise ValueError(f"More generators used than inputted {num_gens} generators to be used")
    #We want to recursively enumerate all words of length 1, 2, 3, 4, ..., limit 
    ws, gs = set(words), set(range(1,num_gens+1))
    for i in range(1, limit+1):
        for word in ws:
            for g in gs:
                ws.add(word.conj(g))