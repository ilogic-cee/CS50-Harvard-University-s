import pytest
from jar import Jar

def test_init():
    # Test initializing with default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test initializing with specific capacity
    jar = Jar(10)
    assert jar.capacity == 10

    # Test initializing with invalid capacity
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    # Test string representation for empty jar
    jar = Jar()
    assert str(jar) == ""

    # Test string representation after depositing cookies
    jar.deposit(1)
    assert str(jar) == "🍪"

    # Test string representation at full capacity
    jar.deposit(11)
    assert str(jar) == "🍪" * 12

def test_deposit():
    # Test depositing cookies within capacity
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1

    # Test exceeding capacity
    with pytest.raises(ValueError):
        jar.deposit(20)

def test_withdraw():
    # Test withdrawing cookies
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3

    # Test withdrawing more than available
    with pytest.raises(ValueError):
        jar.withdraw(100)

def test_capacity_and_size_properties():
    # Test capacity and size properties
    jar = Jar(5)
    assert jar.capacity == 5
    jar.deposit(2)
    assert jar.size == 2

    # Test modifying size beyond capacity
    with pytest.raises(ValueError):
        jar.size = 6

    # Test modifying size to negative number
    with pytest.raises(ValueError):
        jar.size = -1
