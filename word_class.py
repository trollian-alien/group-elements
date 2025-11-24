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

