import numpy as np
from bayes.tensor.tensor import Tensor


class Parameter(Tensor):
    """
    parameter to be optimized
    """

    def __init__(self, array, prior=None):
        super().__init__(array, function=None)
        self.grad = None
        self.prior = prior

    def _backward(self, delta, **kwargs):
        if self.grad is None:
            self.grad = delta
        else:
            self.grad += delta

    def cleargrad(self):
        self.grad = None
        if self.prior is not None:
            loss = -self.prior.log_pdf(self)
            loss.backward()
