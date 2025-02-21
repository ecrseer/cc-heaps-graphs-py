
# distutils: language=c++
# distutils: extra_compile_args=-fopenmp
# distutils: extra_link_args=-fopenmp


from cython.parallel import prange
import numpy as np
cimport numpy as cnp
import random

def somar_vet_aleatorio():
    cdef double vetor[10000]
    cdef double soma = 0
    cdef int i

    for i in range(10000):
        vetor[i] = random.randint(1, 100000)

    for i in prange(10000, nogil=True):
        soma += vetor[i]

    return soma


def somar_vet_linear():
    cdef double vetor_linear[10000]
    cdef double soma = 0
    cdef int i

    for i in range(10000):
        vetor_linear[i] = i

    for i in prange(10000, nogil=True):
        soma += vetor_linear[i]

    return soma