[![pytest](https://github.com/fortitudo-tech/entropy-pooling/actions/workflows/tests.yml/badge.svg)](https://github.com/fortitudo-tech/entropy-pooling/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/fortitudo-tech/entropy-pooling/graph/badge.svg?token=XGIQ78ZLDN)](https://codecov.io/gh/fortitudo-tech/entropy-pooling)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fortitudo-tech/entropy-pooling/HEAD?labpath=example)

Entropy Pooling in Python
=========================

Due to popular demand from developers, this package contains the Entropy Pooling
implementation from the [fortitudo.tech Python package](https://github.com/fortitudo-tech/fortitudo.tech)
with a more permissive BSD 3-Clause license.

This package contains only one function called ep and has minimal dependencies
with just scipy. See [this example](https://github.com/fortitudo-tech/entropy-pooling/blob/main/example/EntropyPooling.ipynb)
for how you can import and use the ep function.

You can explore the example without local installations using
[Binder](https://mybinder.org/v2/gh/fortitudo-tech/entropy-pooling/HEAD?labpath=example).

Installation instructions
-------------------------

Installation can be done via pip:

    pip install entropy-pooling

Theory
------
Entropy Pooling is a powerful method for implementing subjective views and
performing stress-tests for fully general Monte Carlo distributions. It was first
introduced by [Meucci (2008)](https://ssrn.com/abstract=1213325) and refined
with sequential algorithms by [Vorobets (2021)](https://ssrn.com/abstract=3936392).

The original Entropy Pooling approach solves the minimum relative entropy problem

$$q=\underset{x}{\text{argmin}}\lbrace x^{T}\left(\ln x-\ln p\right)\rbrace$$

subject to the constraints

$$Gx\leq h \quad \text{and} \quad Ax=b.$$

The constraints matrices $A$ and $G$ contain transformations of the Monte Carlo
simulation that allow you to implement subjective views and stress-tests by
changing the joint scenario probabilities from a prior probability vector $p$
to a posterior probability vector $q$.

A useful statistic when working with Entropy Pooling is the effective number of
scenarios introduced by [Meucci (2012)](https://ssrn.com/abstract=1971808). For
a causal Bayesian nets overlay on top of Entropy Pooling, see
[Vorobets (2023)](https://ssrn.com/abstract=4444291).

Video walkthroughs
------------------

Video walkthroughs of the two notebook examples for this package are available here
https://youtu.be/hDt103zEML8 and here https://youtu.be/DK1Pv5tuLgo. The videos give
additional insights into the Entropy Pooling theory and its sequential refinements.
It is highly encouraged to watch these two quickly increase your understanding.