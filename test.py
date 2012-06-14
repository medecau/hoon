# -*- coding: utf8 -*-

import unittest
import hashlib
import difflib
from worm import crypto
from worm import diff
from worm import mathkit
from worm import stringutil

class testCrypto(unittest.TestCase):
    test_str = 'abc'*100
    
    def test_default(self):
        a = crypto.digest(self.test_str)
        b = hashlib.sha1(self.test_str).digest()
        self.assertEqual(a, b)
    
    def test_md5(self):
        a = crypto.digest(self.test_str, 'md5')
        b = hashlib.md5(self.test_str).digest()
        self.assertEqual(a, b)
    
    def test_sha1(self):
        a = crypto.digest(self.test_str, 'sha1')
        b = hashlib.sha1(self.test_str).digest()
        self.assertEqual(a, b)

class testDiff(unittest.TestCase):
    s1 = 'aeou'
    s2 = 'eio'
    a = diff.sm(s1, s2)
    b = difflib.SequenceMatcher(None, s1, s2)
    
    def test_constructor(self):
        self.assertEqual(diff.sm(self.s1, self.s2).get_opcodes(), self.b.get_opcodes())
    
    def test_qratio(self):
        self.assertEqual(diff.qratio(self.s1, self.s2), self.b.real_quick_ratio())
    
        '''This helps test qmatch'''
        qr = diff.qratio(self.s1, self.s2)
        self.assertTrue(qr<0.9 and qr>0.7)
    
    def test_ratio(self):
        self.assertEqual(diff.ratio(self.s1, self.s2), self.b.ratio())
    
    def test_qmatch(self):
        self.assertFalse(diff.qmatch(self.s1, self.s2, 0.9))
        self.assertFalse(diff.qmatch(self.s1, self.s2, 0.7))
        self.assertTrue(diff.qmatch(self.s1, self.s2, 0.5))

class testStringutil(unittest.TestCase):
    s = 'aeiou'
    u = '\xc3aeiouáàâãéèâãíìîióòôõúùûucç'
    
    def test_translate(self):
        self.assertEqual(stringutil.translate(self.s, 'aiu', 'bcd'), 'becod')
    
    def test_to_ascii(self):
        self.assertEqual(stringutil.to_ascii(self.u), 'aeiouiuc')



class testMathkit(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_prime(self):
        self.assertTrue(mathkit.is_prime(2))
        self.assertTrue(mathkit.is_prime(11))
        self.assertFalse(mathkit.is_prime(0))
        self.assertFalse(mathkit.is_prime(1))
        self.assertFalse(mathkit.is_prime(-1))
        self.assertFalse(mathkit.is_prime(9))

    def test_next_prime(self):
        self.assertEqual(mathkit.next_prime(-1), 2)
        self.assertEqual(mathkit.next_prime(1), 2)
        self.assertEqual(mathkit.next_prime(2), 3)
        self.assertEqual(mathkit.next_prime(3), 5)
        self.assertEqual(mathkit.next_prime(9), 11)

    def test_get_factors(self):
        factors=mathkit.get_factors(1)
        self.assertEqual(factors, [1])
        
        factors=mathkit.get_factors(2)
        self.assertEqual(factors, [1,2])

        factors=mathkit.get_factors(3)
        self.assertEqual(factors, [1,3])

        factors=mathkit.get_factors(8)
        factors.sort()
        self.assertEqual(factors, [1,2,4,8])

        factors=mathkit.get_factors(25)
        factors.sort()
        self.assertEqual(factors, [1,5,25])

        factors=mathkit.get_factors(8, True)
        factors.sort()
        self.assertEqual(factors, [2,4])

        factors=mathkit.get_factors(25, True)
        factors.sort()
        self.assertEqual(factors, [5])

    def test_fibonacci(self):
        fibonacci_nums=mathkit.fib_seq(10)
        self.assertEqual(fibonacci_nums, [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

if __name__ == '__main__':
    unittest.main()
