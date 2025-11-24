from group_class import Word

def num_gens_used(words): #number of generators used by a list of Words
    return max([word.gens for word in words])

def normal_subgroup_generated_by_words(words, num_gens, limit): #input: list of Words and number of generators, and a limit to the length of the words in the resturned list
    if num_gens_used(words) > num_gens:
        raise ValueError(f"More generators used than inputted {num_gens} generators to be used")
    #We want to recursively enumerate all words of length 1, 2, 3, 4, ..., limit 
    ws, gs = [], []
    for i in range(1, limit+1):
        pass