# -*- coding: utf8 -*-

import unittest
import hashlib
import difflib
import worm

class testWorm(unittest.TestCase):
    test_str = 'abc'*100
    s1 = 'aeou'
    s2 = 'eio'
    a = worm.sm(s1, s2)
    b = difflib.SequenceMatcher(None, s1, s2)
    s = 'aeiou'
    u = '\xc3aeiouáàâãéèâãíìîióòôõúùûucç'
    
    def test_default(self):
        a = worm.digest(self.test_str)
        b = hashlib.sha1(self.test_str).digest()
        self.assertEqual(a, b)
    
    def test_md5(self):
        a = worm.digest(self.test_str, 'md5')
        b = hashlib.md5(self.test_str).digest()
        self.assertEqual(a, b)
    
    def test_sha1(self):
        a = worm.digest(self.test_str, 'sha1')
        b = hashlib.sha1(self.test_str).digest()
        self.assertEqual(a, b)
    
    def test_constructor(self):
        self.assertEqual(worm.sm(self.s1, self.s2).get_opcodes(), self.b.get_opcodes())
    
    def test_qratio(self):
        self.assertEqual(worm.qratio(self.s1, self.s2), self.b.real_quick_ratio())
    
        '''This helps test qmatch'''
        qr = worm.qratio(self.s1, self.s2)
        self.assertTrue(qr<0.9 and qr>0.7)
    
    def test_ratio(self):
        self.assertEqual(worm.ratio(self.s1, self.s2), self.b.ratio())
    
    def test_qmatch(self):
        self.assertFalse(worm.qmatch(self.s1, self.s2, 0.9))
        self.assertFalse(worm.qmatch(self.s1, self.s2, 0.7))
        self.assertTrue(worm.qmatch(self.s1, self.s2, 0.5))
    
    def test_translate(self):
        self.assertEqual(worm.translate(self.s, 'aiu', 'bcd'), 'becod')
    
    def test_to_ascii(self):
        self.assertEqual(worm.to_ascii(self.u), 'aeiouiuc')
    
    def test_is_prime(self):
        self.assertTrue(worm.is_prime(2))
        self.assertTrue(worm.is_prime(11))
        self.assertFalse(worm.is_prime(0))
        self.assertFalse(worm.is_prime(1))
        self.assertFalse(worm.is_prime(-1))
        self.assertFalse(worm.is_prime(9))

    def test_next_prime(self):
        self.assertEqual(worm.next_prime(-1), 2)
        self.assertEqual(worm.next_prime(1), 2)
        self.assertEqual(worm.next_prime(2), 3)
        self.assertEqual(worm.next_prime(3), 5)
        self.assertEqual(worm.next_prime(9), 11)

    def test_get_factors(self):
        factors=worm.get_factors(1)
        self.assertEqual(factors, [1])
        
        factors=worm.get_factors(2)
        self.assertEqual(factors, [1,2])

        factors=worm.get_factors(3)
        self.assertEqual(factors, [1,3])

        factors=worm.get_factors(8)
        factors.sort()
        self.assertEqual(factors, [1,2,4,8])

        factors=worm.get_factors(25)
        factors.sort()
        self.assertEqual(factors, [1,5,25])

        factors=worm.get_factors(8, True)
        factors.sort()
        self.assertEqual(factors, [2,4])

        factors=worm.get_factors(25, True)
        factors.sort()
        self.assertEqual(factors, [5])

    def test_fibonacci(self):
        fibonacci_nums=worm.fib_seq(10)
        self.assertEqual(fibonacci_nums, [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

if __name__ == '__main__':
    unittest.main()
