import vigenere

def test_encrypt():
    assert vigenere.encrypt_v0_2("apple", "test") == "tthex"
    assert vigenere.encrypt_v0_2("sponge", "hello") == "ztzyul"
    assert vigenere.encrypt_v0_2("message longer than key", "small") == "eqsdlyq lzyyqr essz kpj"
    assert vigenere.encrypt_v0_2("small", "keylongerthanmsg") == "cqywz"
