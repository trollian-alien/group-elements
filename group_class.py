from constants import PRODUCE_RELATORS

def is_ordered_pair(x): #helper function to check that the Words have correct syntax
    return (
        isinstance(x, tuple) and
        len(x) == 2 and
        isinstance(x[0], int) and x[0] >= 0 and
        isinstance(x[1], int)
    )

class Word: #models words. inputs will actually be integers. see group class for explanations.
    def __init__(self, iterable): #iterable consists of ordered pairs of integers (the first non-negative), the first is the generator, the second the exponent
        try:
            l = list(iterable)
        except:
            raise TypeError("Please list the elements of the word in a list or tuple")
        if not all(is_ordered_pair(x) for x in l):
            raise TypeError("Invalid word. Please write words as a list of (generator, exponent) integer pair, where the generator int is >=0")

        t = [x for x in l if x[0] != 0 and x[1]!= 0]
        self.word = tuple(t)
        self.length = sum(abs(x[1]) for x in t)
        self.gens = max(n[0] for n in t) #number of generators used

    def __eq__(self, other):
        return self.reduce().word == other.reduce().word

    def __repr__(self):
        return self.word.__repr__()
    
    def reduce(self): #turns the word into a reduced one. used in other operations too.
        reduced_self = []
        i = 0
        for x in self.word:
            if reduced_self and reduced_self[-1][0] == x[0]:
                reduced_self[-1] = (x[0], x[1] + reduced_self[-1][1]) #the __init__ method gets rid of (n, 0)s so we can keep them here
            else:
                reduced_self.append(x)
        return Word(reduced_self)
    
    def is_subword(self,other): #checks if self is subword of other by first reducing them
        self, other = self.reduce(), other.reduce()
        if other.length < self.length:
            return False
        for i in range(0, len(other.word) - len(self.word) + 1):
            if self.word == other.word[i: i + len(self.word)]:
                return True #match found
        return False #all subwords don't match
                
    def __mul__(self, other): #performs the free product of both elements, result is reduced if self and other are reduced
        return Word(self.word+other.word).reduce()
    
            
    def inv(self): #inverses.
        return Word([(self.word[len(self.word)-1-i][0], -self.word[len(self.word)-1-i][1]) for i in range(0,len(self.word))])
    
    def conj(self, other): #conjugates self by other
        return other.inv() * self * other
    
    def pow(self, n: int):
        power = tuple()
        if n == 0:
            return Word([])
        elif n > 0:
            for i in range(0,n):
                power += self.word
        elif n < 0:
             for i in range(0,-n):
                power += self.inv().word
        return Word(power).reduce()


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
        pass

    def add_generators(self, n):
        for i in range(0, n):
            self.add_generator()
    
    def add_relation(self, relation):
        self.relations.append(relation)
    
class FreeGroup(Group):
    def __init__(self, num_gens):
        super.__init__(num_gens, [])