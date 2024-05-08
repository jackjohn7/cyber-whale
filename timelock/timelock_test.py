from timelock import retrieve_code, get_time_elapsed
import datetime
import pytz

def test_valid_hash_string():
    assert retrieve_code('3ee1df13bc19a968b89629c749fee39d') == 'ee93'
    assert retrieve_code('wsf79534hfrf984592139fjk') == 'ws93'
    assert retrieve_code('ab93') == 'ab39'
# 1999 12 31 23 59 59
# '2013 05 06 07 43 25'
# datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
def test_time_elapsed():
    assert get_time_elapsed(datetime(year=1999, month=12, day=31, hour=23, minute=59, second=59, tzinfo = pytz.UTC), 
                            datetime(year=2013, month=5, day=6, hour=7, minute=43, second=25, tzinfo = pytz.UTC)) == 421141380
    
