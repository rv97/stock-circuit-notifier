from nsetools import Nse
from pprint import pprint
from datetime import datetime

nse = Nse()

q = nse.get_quote('JISLDVREQS')

print(datetime.now())