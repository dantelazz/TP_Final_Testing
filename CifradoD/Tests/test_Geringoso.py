from ..Geringoso import encriptarGeringoso,desencriptarGeringoso
import unittest

def test_encriptarGeringoso():
    h1 = encriptarGeringoso("test")
    assert h1 == "tepest"
    h2 = encriptarGeringoso("ho la")
    assert h2 == "hopo lapa"
    h3 = encriptarGeringoso("sala,do")
    assert h3 == "sapalapa,dopo"
    h4 = encriptarGeringoso(" ")
    assert h4 == " "
    h5 = encriptarGeringoso("")
    assert h5 == ""
    h6 = encriptarGeringoso (6)
    assert h6 == ""
    h7 = encriptarGeringoso("#")
    assert h7 == "#"
    h8 = encriptarGeringoso(3,4)
    assert h8 == ""
    h9 = encriptarGeringoso(None)
    assert h9 == None
    h10 = encriptarGeringoso("oa")
    assert h10 == "opolapa"
    h11 = encriptarGeringoso ("oo")
    assert h11 == "opoopo"
    h12 = encriptarGeringoso ("ho6la")
    assert h12 == "hopo6lapa"


def test_desencriptarGeringoso():
    l1 = desencriptarGeringoso("hopolapa")
    assert l1 == "hola"
    l2= desencriptarGeringoso("hopo lapa")
    assert l2 == "ho la"
    l3 = desencriptarGeringoso(None)
    assert l3 == None
    l4 = desencriptarGeringoso(" ")
    assert l4 == " "
    l5 = desencriptarGeringoso("")
    assert l5 == ""
    l6 = desencriptarGeringoso(6)
    assert l6 == ""
    l7 = desencriptarGeringoso("#")
    assert l7 == "#"
    l8 = desencriptarGeringoso(3,4)
    assert l8 == ""
    l9 = desencriptarGeringoso("bapa8lapa")
    assert l9 == "ba8la"
    l10 = desencriptarGeringoso("apaapa")
    assert l10 == "aa"