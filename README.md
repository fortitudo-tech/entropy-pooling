[![pytest](https://github.com/fortitudo-tech/entropy-pooling/actions/workflows/tests.yml/badge.svg)](https://github.com/fortitudo-tech/entropy-pooling/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/fortitudo-tech/entropy-pooling/graph/badge.svg?token=XGIQ78ZLDN)](https://codecov.io/gh/fortitudo-tech/entropy-pooling)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fortitudo-tech/entropy-pooling/HEAD?labpath=examples)

Entropy Pooling in Python
=========================

Due to popular demand from developers, this package contains the Entropy Pooling
implementation from the [fortitudo.tech Python package](https://github.com/fortitudo-tech/fortitudo.tech)
with a more permissive BSD 3-Clause license.

This package contains only one function called ep and has minimal dependencies
with just scipy. See [the examples](https://github.com/fortitudo-tech/entropy-pooling/tree/main/examples)
for how you can import and use the ep function.

You can explore the examples without local installations using
[Binder](https://mybinder.org/v2/gh/fortitudo-tech/entropy-pooling/HEAD?labpath=examples).

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

[You can loosely think about Entropy Pooling as a generalization of the Black-Litterman model](https://antonvorobets.substack.com/p/entropy-pooling-vs-black-litterman-abb608b810cd) without all the oversimplifying assumptions. Entropy Pooling operates directly on 
[the next generation market representation](https://youtu.be/4ESigySdGf8?si=yWYuP9te1K1RBU7j&t=46)
defined by the simulation matrix $R\in \mathbb{R}^{S\times I}$ and associated joint
scenario probability vector $p\in \mathbb{R}^{S}$.

For a quick introduction to Entropy Pooling intuition, watch [this YouTube video](https://youtu.be/qk_5l4ICXfY).
For a collection of Entropy Pooling resources, see this [Substack post](https://antonvorobets.substack.com/p/entropy-pooling-collection).

The original Entropy Pooling approach solves the minimum relative entropy problem

$$q=\underset{x}{\text{argmin}}\lbrace x^{T}\left(\ln x-\ln p\right)\rbrace$$

subject to linear constraints on the posterior probabilities

$$Gx\leq h \quad \text{and} \quad Ax=b.$$

The constraints matrices $A$ and $G$ contain functions of the Monte Carlo
simulation $R$ that allow you to implement subjective views and stress-tests by
changing the joint scenario probabilities from a prior probability vector $p$
to a posterior probability vector $q$.

A useful statistic when working with Entropy Pooling is the effective number of
scenarios introduced by [Meucci (2012)](https://ssrn.com/abstract=1971808).

For a causal Bayesian network overlay on top of Entropy Pooling, see
[Vorobets (2023)](https://ssrn.com/abstract=4444291).

Video walkthroughs
------------------

Video walkthroughs of the two notebook examples are available [here](https://youtu.be/hDt103zEML8)
and [here](https://youtu.be/DK1Pv5tuLgo). The videos give additional insights into
Entropy Pooling theory and its sequential refinements. It is highly recommended
to watch these videos to quickly increase your understanding.

Portfolio Construction and Risk Management Book
-----------------------------------------------

Entropy Pooling is a core part of the next generation investment framework that
also utilizes fully general Monte Carlo distributions and CVaR analysis, see
[this YouTube video](https://youtu.be/4ESigySdGf8?si) for an introduction. To
get a pedagogical and deep presentation of all the possibilities Entropy Pooling
offers, see the [Portfolio Construction and Risk Management Book](https://igg.me/at/pcrm-book).
