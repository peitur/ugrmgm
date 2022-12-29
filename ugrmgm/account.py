#!/usr/bin/env python3

import re
import datetime

import ugrmgm.command
import ugrmgm.util

def account_set_expiry( uname, days ):
    dt_days = ugrmgm.util.time_now_raw()+datetime.timedelta( days=int( days ) )
    cmd = "chage --expiredate %s %s" % ( dt_days.strftime("%Y-%m-%d"), uname )
    
    print( cmd )

def account_unset_expiry( uname ):
    cmd = "chage --expiredate -1 %s" % ( )


# $ sudo chage --expiredate $(date -d +90days +%Y-%m-%d) userxxx

# lock user usermod -L user1

# lock password passwd -l userxxxx 

if __name__ == "__main__":
    pass