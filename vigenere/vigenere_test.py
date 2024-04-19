from vigenere import encrypt, decrypt

def test_encrypt():
    assert encrypt("apple", "test") == "tthex"
    assert encrypt("sponge", "hello") == "ztzyul"
    assert encrypt("message longer than key", "small") == "eqsdlyq lzyyqr essz kpj"
    assert encrypt("small", "keylongerthanmsg") == "cqywz"
    assert encrypt("small", "keylongerthanmsg") == "cqywz"
    assert encrypt(
        "Get ready for Cyber Storm! We’re going to turn your world upside down on May 17!",
        "This is my key"
    ) == "Zlb jmspw psp Vfjwz Kfmbq! Ux’ym ywaze ds rnyv qwmd uyvjw bxkqvq byal hu Usg 17!"

def test_decrypt():
    assert decrypt("tthex", "test") == "apple"
    assert decrypt("ztzyul", "hello") == "sponge"
    assert decrypt("eqsdlyq lzyyqr essz kpj", "small") == "message longer than key"
    assert decrypt("cqywz", "keylongerthanmsg") == "small"
    assert decrypt(
        "Zlb jmspw psp Vfjwz Kfmbq! Ux’ym ywaze ds rnyv qwmd uyvjw bxkqvq byal hu Usg 17!",
        "This is my key"
    ) == "Get ready for Cyber Storm! We’re going to turn your world upside down on May 17!"

def test_bijectivity():
    inputs: list[tuple[str, str]] = [
        ("Apple", "passkey"),
        ("baNana$$", "supersecret"),
        ("ankunda@)", "kiremire"),
        ("andrey2#", "timofeyev"),
        ("whales2", "cyber"),
        ("whales are goated123", "definitely"),
        ("whale$ wi1l win cyb3rst0rm!", "withoutasingledoubt"),
    ]

    for (raw, key) in inputs:
        assert decrypt(encrypt(raw, key), key) == raw
