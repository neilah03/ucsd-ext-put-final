import counter
import pytest

def test_counter_inc():
    assert counter.inc(4) == 5
  
def test_counter_dec():
    assert counter.dec(5) == 4

def test_counter_prod():
    assert counter.prod(8, 8) == 64
    
def test_counter_square():
    assert counter.square(6) == 36

def test_counter_div():
    assert counter.div(8, 4) == 2
