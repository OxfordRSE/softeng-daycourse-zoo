from zoo.elephant import Elephant
from zoo.kangaroo import Kangaroo


def test_elephant():
    assert Elephant().describe() == "Ellie the Elephant says toots and remembers everything!"


def test_kangaroo():
    assert Kangaroo().describe() == "Roo the Kangaroo says thumps and hops around happily."


def test_dog():
    assert Dog().describe() == "Leo the Dog says bark and is a good boy!"
