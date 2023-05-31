from topic import Topic
from storage.concrete_storages import *

STORAGES = {
    Topic("fibonacci", 11): FibonacciStorage,
    Topic("primes", 17): PrimesStorage,
}
