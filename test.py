# -*- coding: utf8 -*-

import unittest
import crypto
import hashlib
import diff
import difflib
import stringutil

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
    
    def test_qratio_1(self):
        self.assertEqual(diff.qratio(self.s1, self.s2), self.b.real_quick_ratio())
    
    def test_qratio_2(self):
        '''This helps test qmatch'''
        qr = diff.qratio(self.s1, self.s2)
        self.assertTrue(qr<0.9 and qr>0.7)
    
    def test_ratio(self):
        self.assertEqual(diff.ratio(self.s1, self.s2), self.b.ratio())
    
    def test_qmatch_1(self):
        self.assertFalse(diff.qmatch(self.s1, self.s2, 0.9))
    
    def test_qmatch_2(self):
        self.assertFalse(diff.qmatch(self.s1, self.s2, 0.7))
    
    def test_qmatch_3(self):
        self.assertTrue(diff.qmatch(self.s1, self.s2, 0.5))

class testStringutil(unittest.TestCase):
    s = 'aeiou'
    u = '\xc3aeiouáàâãéèâãíìîióòôõúùûucç'
    
    def test_translate(self):
        self.assertEqual(stringutil.translate(self.s, 'aiu', 'bcd'), 'becod')
    
    def test_to_ascii(self):
        self.assertEqual(stringutil.to_ascii(self.u), 'aeiouiuc')


if __name__ == '__main__':
    unittest.main()
