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
    assert e4 == ""
    e5 = encriptarX(" ")
    assert e5 == ""
    e6 = encriptarX("holá")
    assert e6 == ("ho4á")
    e7 = encriptarX(True)
    assert e7 == ()
    e8 = encriptarX("va,so")
    assert e8 == ("va,so")
    e9 = encriptarX("#")
    assert e9 == "#"
    e10 = encriptarX(1323)
    assert e10== ""
    e11 = encriptarX(1,5)
    assert e11 == ""
    e12 = encriptarX(" k ")
    assert e12 == ("k")





def test_desencriptarX():
    a1 = desencriptarX(" frase ")
    assert a1 == ("frase")
    a2 = desencriptarX("pa8a")
    assert a2 ==("pala")
    a4 = desencriptarX(1)
    assert a4 == ""
    a5 = desencriptarX(" ")
    assert a5 == ""
    a7 = desencriptarX(True)
    assert a7 == ()
    a8 = desencriptarX("b3,lon")
    assert a8 == ("ba,lon")
    a9 = desencriptarX("#")
    assert a9 == "#"
    a10 = desencriptarX(1323)
    assert a10 == ""
    a11 = desencriptarX(1, 5)
    assert a11 == ""
