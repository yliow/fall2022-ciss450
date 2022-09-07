# file: x.py
#
# To look for site-packages directory use find command:
# find /usr -name 'site-packages' -print 2>/dev/null
#
# import A -- look for A.py in current directory
# ... or  /usr/lib*/python*/site-packages
# ... or check sys.path
#
# If ABC.py in /home/student/, then execute
#
# import sys
# sys.path.append('/home/student/')
#
# Above is about python modules (files)
# Check "python packages".

a = 42

def f(x):
    return x + 1

class C:
    def __init__(self):
        print("C")
        return
