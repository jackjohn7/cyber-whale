from storage_covert import convert_ascii, convert_10_bit

def test_convert_ascii():
    assert convert_ascii(['x-w-r--', 'xr-x---', 'xr--r-x', 'xrw--w-', 'xr--r-x', '-r-----', 'xr----x', 
                           'xrw--w-', 'xr--r-x', '-r-----', '-rw---x', '-rw----', '-r-----', 'xrw-r--', 
                           'xrwx--x', 'xrw----', 'xr--r-x', 'xrw--wx', '-r-----', 'xr-xrwx', 'xr--rw-', 
                           '-r-----', 'xrw----', 'xr--r-x', 'xr-xrwx', 'xrw----', 'xr-xr--', 'xr--r-x', 
                           '-rwx-w-', '-r-----', 'xrw-r--', 'xr-x---', 'xr-xrwx', 'xrw--wx', 'xr--r-x', 
                           '-r-----', 'xrw-rwx', 'xr-x---', 'xr-xrwx', '-r-----', 'xr-x-wx', 'xr-xrw-', 
                           'xr-xrwx', 'xrw-rwx', '-r-----', 'xr---w-', 'xr-x--x', 'xr-xrw-', 'xr----x', 
                           'xrw--w-', 'xrwx--x', '-r-xr--', '-r-----', 'xrw-r--', 'xr-x---', 'xr-xrwx', 
                           'xrw--wx', 'xr--r-x', '-r-----', 'xrw-rwx', 'xr-x---', 'xr-xrwx', '-r-----', 
                           'xr--r--', 'xr-xrwx', 'xr-xrw-', '-r--rwx', 'xrw-r--', '-r-xr--', '-r-----', 
                           'xr----x', 'xr-xrw-', 'xr--r--', '-r-----', 'xrw-r--', 'xr-x---', 'xr-xrwx', 
                           'xrw--wx', 'xr--r-x', '-r-----', 'xrw-rwx', 'xr-x---', 'xr-xrwx', '-r-----', 
                           'xrw-rwx', 'xr--r-x', 'xrw--w-', 'xr--r-x', 'xr-xrw-', '-r--rwx', 'xrw-r--', 
                           '-r-----', 'xr--r-x', 'xrwx---', 'xrw----', 'xr--r-x', 'xr---wx', 'xrw-r--', 
                           'xr-x--x', 'xr-xrw-', 'xr--rwx', '-r-----', 'xr-x--x', 'xrw-r--', '-r-----', 
                           'xr-x--x', 'xr-xrw-', '-r-----', 'xr---w-', 'xr----x', 'xrw--wx', 'xr--r-x', 
                           '-r-----', '-rw--wx', '-r-xrw-']) == ['T', 'h', 'e', 'r', 'e', ' ', 'a', 'r', 
                            'e', ' ', '1', '0', ' ', 't', 'y', 'p', 'e', 's', ' ', 'o', 'f', ' ', 'p', 
                            'e', 'o', 'p', 'l', 'e', ':', ' ', 't', 'h', 'o', 's', 'e', ' ', 'w', 'h', 
                            'o', ' ', 'k', 'n', 'o', 'w', ' ', 'b', 'i', 'n', 'a', 'r', 'y', ',', ' ', 
                            't', 'h', 'o', 's', 'e', ' ', 'w', 'h', 'o', ' ', 'd', 'o', 'n', "'", 't', 
                            ',', ' ', 'a', 'n', 'd', ' ', 't', 'h', 'o', 's', 'e', ' ', 'w', 'h', 'o', 
                            ' ', 'w', 'e', 'r', 'e', 'n', "'", 't', ' ', 'e', 'x', 'p', 'e', 'c', 't', 
                            'i', 'n', 'g', ' ', 'i', 't', ' ', 'i', 'n', ' ', 'b', 'a', 's', 'e', ' ', 
                            '3', '.']