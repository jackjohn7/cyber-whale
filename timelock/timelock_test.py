from timelock import retrieve_code

def test_valid_hash_string():
    assert retrieve_code('3ee1df13bc19a968b89629c749fee39d') == 'ee93'
    assert retrieve_code('wsf79534hfrf984592139fjk') == 'ws93'
    assert retrieve_code('ab93') == 'ab39'

