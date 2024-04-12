from storage_covert import convert_ascii, convert_10_bit

def test_convert_ascii_method_7():
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
    assert convert_ascii(['d-w-r--', 'dr--r-x','drw--wx','drw-r--', '-r-----', '-rw----', '-rw--w-'
                          ]) ==['T','e','s','t',' ','0','2']
    
def test_convert_ascii_method_10():
    assert convert_ascii(['d--xr-xrw-' , 'drwxrwx-w-' , '-rw-r--rwx' , 'd-wx-wx---' , '-rwxr-x--x' , 'd-w--wxr-x', 
                          'drwxr-xrw-' , '-r-----rw-' , 'd--xrwx--x' , 'd-w-----wx' , 'd-wxrwx-w-' , '--wx----wx',
                          'dr-x---r--' , '---xr--rwx' , 'dr--r-xrwx' , '-r--rwx--x' , 'd-w-----wx' , 'dr--rwx-wx',
                          'drwxr-x-w-' , 'd-----xrw-' , '-rwxrw-r--' , 'dr----xrwx' , '--w-rwx-w-' , '-rw--w-rwx',
                          '--w---x-wx' , 'd--x------' , 'd-----x--x' , '---xr----x' , 'dr---w-rw-' , 'd--xrwx-w-',  
                          '--w-----wx' , '-r--rwxr--' , 'dr-x-----x' , 'dr-xrwxr-x' , '---xr----x' , 'drw-r---w-',
                          '----rw-r-x' , 'drw--w-rwx' , '--w-rwxr--' , '--wxr--rw-' , 'd-----xrwx' , '--wxr-xrwx',
                          'drw-r-x-w-' , '----rw--wx' , 'drw-rwxrwx' , '-r--rwx-wx' , 'd-wx--xrw-' , 'd-wxr--r--',
                          '----r-xr-x' , '-r-xr-x-w-' , '----r--r-x' , '-rw-r--rwx' , '-rw-r-x---' , '--w-r--r-x',
                          'd-wxrwxr-x' , '---xr-xrw-']) == ['M','o','t','i','v','a','t','i','o','n',' ','i','s',
                            ' ','w','h','a','t','g','e','t','s',' ','y','o','u',' ','s','t','a','r','t','e',
                            'd','.',' ',' ','H','a','b','i','t',' ','i','s',' ','w','h','a','t',' ','k',
                            'e','e','p','s',' ','y','o','u',' ','g','o','i','n','g','.',' ','-','-',' ','J',
                            'i','m',' ','R','o','h','n']
    

if __name__ == "__main__":
    test_convert_ascii_method_7()
    test_convert_ascii_method_10()