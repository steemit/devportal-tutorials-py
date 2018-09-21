import pprint
import math
from pick import pick

# initialize Steem class
from steem import Steem


s = Steem()

title = 'Please choose account: '
options = ["steemitblog","esteemapp","busy.org","demo"]

# get index and selected filter name
option, index = pick(options, title)

# option is printed as reference
pprint.pprint("Selected: "+option)

user = s.get_accounts([option])

def rep_log10(rep):
    """Convert raw steemd rep into a UI-ready value centered at 25."""
    def log10(string):
        leading_digits = int(string[0:4])
        log = math.log10(leading_digits) + 0.00000001
        num = len(string) - 1
        return num + (log - int(log))

    rep = str(rep)
    if rep == "0":
        return 25

    sign = -1 if rep[0] == '-' else 1
    if sign < 0:
        rep = rep[1:]

    out = log10(rep)
    out = max(out - 9, 0) * sign  # @ -9, $1 earned is approx magnitude 1
    out = (out * 9) + 25          # 9 points per magnitude. center at 25
    return round(out, 2)



# print specified account's reputation
pprint.pprint(rep_log10(user[0]['reputation']))