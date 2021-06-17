from ..Cesar import encriptarCesar,desencriptarCesar
import unittest

def test_encriptarCesar():
    c1 = encriptarCesar("bala")
    assert c1 == "azkz"
    c2 = encriptarCesar("ba la")
    assert c2 == "az kz"
    c3 = encriptarCesar("ba45la")
    assert c3 == "az45kz"
    c4 = encriptarCesar("")
    assert c4 == ""
    c5 = encriptarCesar(" ")
    assert c5 == " "
    c6 = encriptarCesar(123432)
    assert c6 == ""
    c7 = encriptarCesar(2,1)
    assert c7 == ""
    c8 = encriptarCesar("@")
    assert c8 == "@"


def test_desencriptarCesar():
    m1 = desencriptarCesar("BGZXZMMD")
    assert m1 =="chayanne"
    m2 = desencriptarCesar("BGZX ZMMD")
    assert m2 == "chay anne"
    m3 = desencriptarCesar("zm3zmz ")
    assert m3 == "an3ana"
    m4 = desencriptarCesar("")
    assert m4 ==""
    m5 = desencriptarCesar(" ")
    assert m5 ==""
    m6 = desencriptarCesar(5)
    assert m6 == ""
    m7 = desencriptarCesar(1,5)
    assert m7 == ""
    m8 = desencriptarCesar("#")
    assert m8 =="#"

