import Binary

def test_numBits():
    assert Binary.numBits("1000001") == 7
    assert Binary.numBits("01000001") == 8
    assert Binary.numBits("10000011000001") == 7
    assert Binary.numBits("0100000101000001") == 8
    assert Binary.numBits("100000101000001") is None

def test_segments():
    assert Binary.segments("1000001", 7) == ["1000001"]
    assert Binary.segments("01000001", 8) == ["01000001"]
    assert Binary.segments("10000011000001", 7) == ["1000001", "1000001"]
    assert Binary.segments("0100000101000001", 8) == ["01000001", "01000001"]

def test_toASCII():
    assert Binary.toASCII(["1000001"]) == "A"
    assert Binary.toASCII(["1000010"]) == "B"
    assert Binary.toASCII(["01000001"]) == "A"
    assert Binary.toASCII(["01000010"]) == "B"
    assert Binary.toASCII(["1000010", "1000001"]) == "BA"
    assert Binary.toASCII(["01000010", "01000001"]) == "BA"

