# -*- coding: utf-8 -*-
#
from __future__ import division

from math import sqrt

import numpy

from ..helpers import untangle, rd


class Stroud1969(object):
    '''
    A.H. Stroud,
    A Fifth Degree Integration Formula for the n-Simplex,
    SIAM J. Numer. Anal., 6(1), 90–98. (9 pages),
    <https://doi.org/10.1137/0706009>.
    '''
    # pylint: disable=too-many-locals
    def __init__(self, n):
        assert n >= 3
        self.dim = n
        self.degree = 5

        pm = numpy.array([+1, -1])
        sqrt15 = sqrt(15.0)

        t = 1/(n+1)
        r1, r2 = (n + 4 - pm * sqrt15) / (n**2 + 8*n + 1)
        s1, s2 = (4*n + 1 + pm * n * sqrt15) / (n**2 + 8*n + 1)
        u1, u2 = (n + 7 + pm * 2 * sqrt15) / (n**2 + 14*n - 11)
        v1, v2 = (4*n - 2 - pm * (n-1) * sqrt15) / (n**2 + 14*n - 11)

        A = {
            3: 16 / 135,
            4: 0.631521898883e-1,
            5: 0.235714285714,
            6: 0.791575476992,
            7: 0.185798728021e+1,
            8: 0.353666958042e+1,
            9: 0.1590844340844e+1,
            10: 0.903765432098e+1,
            11: 0.129758241758e+2,
            12: 0.177645108738e+2,
            13: 0.234375030259e+2,
            14: 0.300224941950e+2,
            15: 0.375423613501e+2,
            16: 0.460161454949e+2,
            }

        B1 = {
            3: (2665 + 14 * sqrt(15)) / 37800,
            4: 0.470456145702e-1,
            5: 0.333009774677e-1,
            6: 0.248633014592e-1,
            7: 0.192679696358e-1,
            8: 0.153322153879e-1,
            9: 0.124316229901e-1,
            10: 0.102112988361e-1,
            11: 0.845730697460e-2,
            12: 0.703433430999e-2,
            13: 0.585330520067e-2,
            14: 0.485356735291e-2,
            15: 0.399261092720e-2,
            16: 0.323988713017e-2,
            }

        B2 = {
            3: (2665 - 14 * sqrt(15)) / 37800,
            4: +0.371530185868e-1,
            5: -0.719253160920e-1,
            6: -0.264323879461,
            7: -0.537926779961,
            8: -0.886895605701,
            9: -0.130409181465e+1,
            10: -0.178227048964e+1,
            11: -06231462336314e+1,
            12: -0.289499045158e+1,
            13: -0.351790849765e+1,
            14: -0.417858310668e+1,
            15: -0.487282884913e+1,
            16: -0.559699944261e+1,
            }

        C1 = {
            3: 10 / 189,
            4: 0.261368740713e-1,
            5: 0.499020181331e-1,
            6: 0.782233395867e-1,
            7: 0.109041040862,
            8: 0.140874828568,
            9: 0.172735353396,
            10: 0.203992490408,
            11: 0.234263814181,
            12: .0253332763315,
            13: 0.291091849264,
            14: 0.317504208212,
            15: 0.342577872069,
            16: 0.366348654344,
            }

        C2 = {
            4: 0.254485903613e-1,
            5: 0.165000982690e-1,
            6: 0.115218303668e-1,
            7: 0.850478779483e-2,
            8: 0.655297510968e-2,
            9: 0.522372456259e-2,
            10: 0.428017828134e-2,
            11: 0.358722367033e-2,
            12: 0.306362964360e-2,
            13: 0.265836687133e-2,
            14: 0.233816221525e-2,
            15: 0.208061510846e-2,
            16: 0.187022027571e-2,
            }

        data = [
            (A[n], numpy.array([numpy.full(n+1, t)])),
            (B1[n], rd(n+1, [(r1, n), (s1, 1)])),
            (B2[n], rd(n+1, [(r2, n), (s2, 1)])),
            (C1[n], rd(n+1, [(u1, n-1), (v1, 2)])),
            ]
        if n > 3:
            data += [
                (C2[n], rd(n+1, [(u2, n-1), (v2, 2)]))
                ]

        self.bary, self.weights = untangle(data)
        self.points = self.bary[:, 1:]
        return
