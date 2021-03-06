import unittest
import numpy as np
import bayesnet as bn


class TestLaplace(unittest.TestCase):

    def test_laplace(self):
        obs = np.arange(3)
        loc = bn.Parameter(0)
        s = bn.Parameter(1)
        for _ in range(1000):
            loc.cleargrad()
            s.cleargrad()
            x = bn.random.Laplace(loc, bn.softplus(s), data=obs)
            x.log_pdf().sum().backward()
            loc.value += loc.grad * 0.01
            s.value += s.grad * 0.01
        self.assertAlmostEqual(x.loc.value, np.median(obs), places=1)
        self.assertAlmostEqual(x.scale.value, np.mean(np.abs(obs - x.loc.value)), places=1)


if __name__ == '__main__':
    unittest.main()
