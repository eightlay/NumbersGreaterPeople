from topic import Topic
from storage.concrete_storages import *

STORAGES = {
    Topic("fibonacci", 11): FibonacciStorage,
    Topic("primes", 17): PrimesStorage,
    Topic("odds", 275): OddsStorage,
    Topic("evens", 274): EvensStorage,
}
