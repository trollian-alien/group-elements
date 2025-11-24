from word_class import Word
import unittest

class TestWord(unittest.TestCase):

    def test_init(self):
        word = Word(((1,4),(2,6),(0,2),(1,0),(1,-5)))
        self.assertEqual(word.word, ((1,4),(2,6),(1,-5)))
        self.assertEqual(word, Word(((1,4),(2,6),(1,-5))))
        self.assertEqual(word.length, 4+6+5)
        self.assertEqual(word.gens, 2)
        with self.assertRaises(TypeError):
            Word(((-1,2),(3,1)))

    def test_reduce(self):
        word = Word(((1,2),(1,-2),(3,5),(3,6),(2,1),(2,-4),(2,2)))
        self.assertEqual(word.reduce().word, ((3,11),(2,-1)))

    def test_subword(self):
        word = Word(((1,2),(2,-3),(6,-7),(3,1),(4,7)))
        subword1 = Word(((6,-7),(3,1)))
        subword2 = Word(((2,-3),))
        self.assertTrue(subword1.is_subword(word))
        self.assertTrue(subword2.is_subword(word))
        self.assertFalse(subword2.is_subword(subword1))

    def test_mul(self):
        word1 = Word(((1,2),(2,-3)))
        word2 = Word(((2, 3), (1,1)))
        self.assertEqual(word1 * word2, Word(((1,3),)))

    def test_inv(self):
        word = Word(((1,2),(2,1),(1,-3)))
        self.assertEqual(word.inv(), Word(((1,3),(2,-1),(1,-2))))

    def test_pow(self):
        word = Word(((1,2),(2,1),(1,-3)))
        self.assertEqual(word.pow(3), Word(((1,2),(2,1),(1,-1),(2,1),(1,-1),(2,1),(1,-3))))
        self.assertEqual(word.pow(-3), Word(((1,2),(2,1),(1,-1),(2,1),(1,-1),(2,1),(1,-3))).inv())


if __name__ == '__main__':
    unittest.main()