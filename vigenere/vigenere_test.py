import vigenere

def test_encrypt():
    assert vigenere.encrypt_v0_2("apple", "test") == "tthex"
    assert vigenere.encrypt_v0_2("sponge", "hello") == "ztzyul"
    assert vigenere.encrypt_v0_2("message longer than key", "small") == "eqsdlyq lzyyqr essz kpj"
    assert vigenere.encrypt_v0_2("small", "keylongerthanmsg") == "cqywz"

def test_decrypt():
    assert vigenere.decrypt("tthex", "test") == "apple"
    assert vigenere.decrypt("ztzyul", "hello") == "sponge"
    assert vigenere.decrypt("eqsdlyq lzyyqr essz kpj", "small") == "message longer than key"
    assert vigenere.decrypt("cqywz", "keylongerthanmsg") == "small"
