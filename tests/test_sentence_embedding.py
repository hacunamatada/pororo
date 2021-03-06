"""Test Sentence Embedding module"""

import unittest

import numpy as np

from pororo import Pororo


class PororoSentenceTester(unittest.TestCase):

    def test_modules(self):
        sentvec = Pororo(task="sentvec", lang="ko")
        sentvec_res = sentvec("나는 동물을 좋아하는 사람이야")
        self.assertIsInstance(sentvec_res, np.ndarray)


if __name__ == "__main__":
    unittest.main()
