from zigzag import zigzag


def test_example1():
    assert zigzag("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"


def test_example2():
    assert zigzag("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"


def test_example3():
    assert zigzag("A", 1) == "A"


def test_example4():
    assert zigzag("ABCDEF", 2) == "ACEBDF"
