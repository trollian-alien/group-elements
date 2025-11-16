from group_class import Word, Group, FreeGroup

def presentation_to_group_class(gens, relators): #example input: n, [x1xn^2, x1^2xn^-1]
    if type(gens) != int:
        if gens <= 0:
            raise TypeError("number of generators must be a positive integer") 
    try:
        relators = list(relators)
    except:
        raise TypeError("realtors should be a list of strings")
    
    if not relators: #first we'll recognize if we don't need to do any conversion
        return FreeGroup(n) #freedom motif
    
    conv_relators = []
    for r in relators:
        for i in r:
            if i == "x":
                continue
            elif type(i) == int:
                pass #you know what, I think here is a good place to use regex!!!

    


def group_class_to_presentation(gens, relators):
    pass

def main():
    print("Given a group presentation that you will imput, this program will be able to perform some calculations with it")
    print("Please input the number of generators of your group")