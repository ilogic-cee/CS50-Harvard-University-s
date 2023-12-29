import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("ten")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪" * 12

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(jar.capacity - 1)
    assert jar.size == jar.capacity
    with pytest.raises(ValueError):
        jar.deposit(1)
    with pytest.raises(ValueError):
        jar.deposit(-5)

def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3
    jar.withdraw(3)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
    with pytest.raises(ValueError):
        jar.withdraw(-1)

def test_capacity():
    jar = Jar(10)
    assert jar.capacity == 10
    jar2 = Jar()
    assert jar2.capacity == 12
