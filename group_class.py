from constants import PRODUCE_RELATORS

class Word: #models words. inputs will actually be integers. see group class for explanations.
    def __init__(self, iterable):
        l = list(iterable)
        if not all(isinstance(x, int) for x in l):
            raise TypeError("Word letters must be integers")
        t = [x for x in l if x != 0]
        self.word = tuple(t)
        self.length = len(t)
        self.gens = max(abs(n) for n in t) #number of generators used
        self.str = "".join([str(x) for x in t]) #useful for subword calculations

    def __repr__(self):
        return self.word.__repr__()

    def __mul__(self, other): #performs the free product of both elements
        length = min(len(self.word), len(other.word))
        x, y = self.word, other.word
        for i in range(0,length):
            if self.word[-i-1] == -other.word[i]:
                x, y = x[:-1], y[1:]
            else:
                return Word(x+y)
        return Word(x+y)
            
    def inv(self): #inverses
        return Word([-self.word[self.length-1-i] for i in range(0,self.length)])
    
    def conj(self, other): #conjugates self by other
        return other.inv() * self * other
    
    def is_subword(self,other): #checks if self is subword of other
        return self.str in other.str


class Group: #This group class is defined from a presentation
    def __init__(self, num_gens: int, relations: list):
        # The identity will be represented by 0, the first generator by 1, the second by 2, and so on...
        # The inverse of a generator is represented by the negative of the generator
        # For example, the inverse of the first generator is represented by -1
        if not all(isinstance(r, Word) for r in relations):
            raise TypeError("Relations must be in the Word class")
        for r in relations:
            if r.gens > num_gens:
                raise ValueError("One or more relations you included uses more generators than there actually are!")
        self.generators = num_gens
        self.relations = relations
        self.more_relations = relations #this will have more relations if we choose to produce them

    def is_valid_element(self, element: Word):
        if type(element) != Word: #e.g. abab^(-1) is represented as [1,2,1,-2]
            return False
        last_value = 0
        for x in element.word:
            if abs(x) > self.generators:
                return False
            elif x in [0,-last_value]: #we don't want un-freely-reduced
                return False
            last_value = x
        return True 

    def produce_relators(self):
        pass

    def is_relator(self, r): #checks if r is a relator
        #this is the word problem, unsolvable in general lol, but we can get partial detections by using the partial relation generator
        pass

    def reduce(self, element):
        #removes substrings that are in self.more_relations
        pass

    def mu(self, elem1, elem2): 
        #without a suitable 
        result = elem1 * elem2 
    
    def inv(self, element):
        result = element.inv()


    # Tietze Operations; to be finished
    def add_generator(self):
        self.generators.append(len(self.generators))

    def add_generators(self, n):
        for i in range(0, n):
            self.add_generator()
    
    def add_relation(self, relation):
        self.relations.append(relation)
    
