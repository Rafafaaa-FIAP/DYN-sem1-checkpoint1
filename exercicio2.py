
import unittest
from deque import Deque


def fibonacci_com_deque(n):
    d = Deque()

    if (n > 0):
        n += 1

    fibo = 0

    for i in range(n):
        if (d.is_empty()):
            d.enqueue_rear(fibo)
            fibo += 1
        else:
            fibo += d.peek_front()
            d.enqueue_rear(fibo)
            if (d.size() > 2):
                d.dequeue_front()

    return fibo

class TestFibonacciComDeque(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci_com_deque(0), 0)
    def test_fibonacci_um(self):
        self.assertEqual(fibonacci_com_deque(1), 1)
    def test_fibonacci_seis(self):
        self.assertEqual(fibonacci_com_deque(6), 8)
    def test_fibonacci_dez(self):
        self.assertEqual(fibonacci_com_deque(10), 55)
    def test_fibonacci_grande(self):
        self.assertEqual(fibonacci_com_deque(20), 6765)