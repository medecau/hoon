# -*- coding: utf8 -*-

import unittest
import hashlib
import difflib
import hoon


class TestHoon(unittest.TestCase):
    test_str = 'abc' * 100
    s1 = 'aeou'
    s2 = 'eio'
    a = hoon.sequence_matcher(s1, s2)
    b = difflib.SequenceMatcher(None, s1, s2)
    s = 'aeiou'
    u = '\xc3aeiouáàâãéèâãíìîióòôõúùûucç'

    def test_default(self):
        a = hoon.binhash(self.test_str)
        b = hashlib.sha1(self.test_str).digest()
        self.assertEqual(a, b)

    def test_md5(self):
        a = hoon.binhash(self.test_str, 'md5')
        b = hashlib.md5(self.test_str).digest()
        self.assertEqual(a, b)

    def test_sha1(self):
        a = hoon.binhash(self.test_str, 'sha1')
        b = hashlib.sha1(self.test_str).digest()
        self.assertEqual(a, b)

    def test_constructor(self):
        self.assertEqual(hoon.sequence_matcher(self.s1, self.s2).get_opcodes(),
                         self.b.get_opcodes())

    def test_qratio(self):
        self.assertEqual(hoon.qratio(self.s1, self.s2),
                         self.b.real_quick_ratio())

        '''This helps test qmatch'''
        qr = hoon.qratio(self.s1, self.s2)
        self.assertTrue(qr < 0.9 and qr > 0.7)

    def test_ratio(self):
        self.assertEqual(hoon.ratio(self.s1, self.s2), self.b.ratio())

    def test_qmatch(self):
        self.assertFalse(hoon.qmatch(self.s1, self.s2, 0.9))
        self.assertFalse(hoon.qmatch(self.s1, self.s2, 0.7))
        self.assertTrue(hoon.qmatch(self.s1, self.s2, 0.5))

    def test_translate(self):
        self.assertEqual(hoon.translate(self.s, 'aiu', 'bcd'), 'becod')


if __name__ == '__main__':
    unittest.main()
