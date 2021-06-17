from ..EncriptarX import encriptarX,desencriptarX
import unittest

def test_encriptarX():
    e1 = encriptarX("frase")
    assert e1 == "frase"
    e2 = encriptarX("")
    assert e2 == ""
    e3 = encriptarX("ho la")
    assert e3 == ("ho 5a")
    e4 = encriptarX(1)
    assert e4 == 1
    e5 = encriptarX(" ")
    assert e5 == ("")
    e6 = encriptarX("holá")
    assert e6 == ("ho4á")
    e7 = encriptarX(True)
    assert e7 == ()
    e8 = encriptarX("va,so")
    assert e8 == ("va,so")
    e9 = encriptarX(9)
    assert e9 == ""



def test_desencriptarX():
    a1 = desencriptarX("frase ")
    assert a1 == ("frase")
    a2 = desencriptarX("pa8a")
    assert a2 ==("pala")