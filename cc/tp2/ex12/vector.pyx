
# distutils: language=c++
# distutils: extra_compile_args=-fopenmp
# distutils: extra_link_args=-fopenmp


from cython.parallel import prange
import numpy as np
cimport numpy as cnp
import random

def vector_by_scalar(double[:] vetor, double scalar):
    cdef int i
    vetor_size = vetor.shape[0]
    cdef double[:] resultados = vetor
    cdef double soma = 0
    for i in prange(vetor_size,nogil=True):
        soma+=resultados[i]
    return soma


def old_somar_vet_aleatorio():
    cdef int i
    cdef double[:] vetor = np.random.rand(1000000)
    cdef double soma = 0
    for i in prange(1000000,nogil=True):
        soma+=vetor[i]
    return vetor,soma

def somar_vet_aleatorio():
    cdef double[:] vetor = [random.randint(1, 100000) for _ in range(10000)]
    cdef double soma = 0
    for i in prange(10000, nogil=True):
        soma += vetor[i]
    return vetor, soma