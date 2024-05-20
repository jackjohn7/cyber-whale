from steg import StegByte, StegBit

def test_byte_retrieve():
    # testing Canvas examples
    # create experimental
    wrapper_file = open("./steg/provided_files/stegged-byte.bmp", "rb")
    wrapper = bytearray(wrapper_file.read())
    wrapper_file.close()
    hidden = bytearray()
    s = StegByte(wrapper, hidden, 1024, 8)
    result1 = s.retrieve()

    # read expected
    expected_file1 = open("./steg/provided_files/unstegged-byte1.bmp", "rb")
    expected1 = bytearray(expected_file1.read())
    expected_file1.close()

    assert expected1 == result1

    s = StegByte(wrapper, hidden, 1025, 2)
    result2 = s.retrieve()

    # read expected
    expected_file2 = open("./steg/provided_files/unstegged-byte2.txt", "rb")
    expected2 = bytearray(expected_file2.read())
    expected_file2.close()

    assert expected2 == result2

def test_byte_store():
    # storing ruff.toml inside apple.bmp
    wrapper_file = open("./steg/provided_files/apple.bmp", "rb")
    wrapper = bytearray(wrapper_file.read())
    wrapper_file.close()

    hidden_file = open("./ruff.toml", "rb")
    hidden = bytearray(hidden_file.read())
    hidden_file.close()

    s = StegByte(wrapper, hidden, 812, 12)
    result = s.store()

    # read expected
    expected_file = open("./steg/provided_files/ruff_in_apple.bmp", "rb")
    expected = bytearray(expected_file.read())
    expected_file.close()

    assert result == expected

def test_bit_retrieve():
    # testing Canvas example
    wrapper_file = open("./steg/provided_files/stegged-bit.bmp", "rb")
    wrapper = bytearray(wrapper_file.read())
    wrapper_file.close()
    hidden = bytearray()
    s = StegBit(wrapper, hidden, 1024, 1)
    result = s.retrieve()

    # read expected
    expected_file = open("./steg/provided_files/unstegged-bit.bmp", "rb")
    expected = bytearray(expected_file.read())
    expected_file.close()

    assert expected == result

def test_bit_store():
    # store README.md inside apple.bmp
    wrapper_file = open("./steg/provided_files/apple.bmp", "rb")
    wrapper = bytearray(wrapper_file.read())
    wrapper_file.close()

    hidden_file = open("./README.md", "rb")
    hidden = bytearray(hidden_file.read())
    hidden_file.close()

    s = StegBit(wrapper, hidden, 1026, 6)
    result = s.store()

    # read expected
    expected_file = open("./steg/provided_files/README_in_apple.bmp", "rb")
    expected = bytearray(expected_file.read())
    expected_file.close()

    assert result == expected


