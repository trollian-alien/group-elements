from constants import PRODUCE_RELATORS
from word_class import Word

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