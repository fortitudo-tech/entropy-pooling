# Copyright (c) 2021-2024, Fortitudo Technologies
# This work is licensed under BSD 3-Clause "New" or "Revised" License:
# https://github.com/fortitudo-tech/entropy-pooling/blob/main/LICENSE

import numpy as np
import pytest
from fortitudo.tech import load_pnl
import os
import sys
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entropy_pooling import ep


R = load_pnl().values
S = len(R)
A_base = np.ones((1, S))
b_base = np.ones((1, 1))
A = np.vstack((A_base, R[:, 0][np.newaxis, :]))
b = np.vstack((b_base, np.array([[0.075]])))
G = -R[:, 1][np.newaxis, :]
h = -np.array([[0.075]])
tol = 1e-5
p1 = np.ones((S, 1)) / S
p2 = np.random.randint(1, S, (S, 1))
p2 = p2 / np.sum(p2)


@pytest.mark.parametrize("p", [p1, p2])
def test_equality(p):
    q = ep(p, A, b)
    means = q.T @ R
    assert np.abs(means[0, 0] - b[1, 0]) <= tol
    assert np.abs(np.sum(q) - 1) <= tol
    assert np.all(q > 0)
    assert q.shape == (S, 1)


@pytest.mark.parametrize("p", [p1, p2])
def test_base_inequality(p):
    q = ep(p, A_base, b_base, G, h)
    means = q.T @ R
    assert means[0, 1] + h[0, 0] <= tol
    assert np.abs(np.sum(q) - 1) <= tol
    assert np.all(q > 0)
    assert q.shape == (S, 1)


@pytest.mark.parametrize("p", [p1, p2])
def test_equality_inequality(p):
    q = ep(p, A, b, G, h)
    means = q.T @ R
    assert np.abs(means[0, 0] - b[1, 0]) <= tol
    assert means[0, 1] + h[0, 0] <= tol
    assert np.abs(np.sum(q) - 1) <= tol
    assert np.all(q > 0)
    assert q.shape == (S, 1)


def test_method():
    with pytest.raises(ValueError):
        _ = ep(p1, A, b, method='X')
