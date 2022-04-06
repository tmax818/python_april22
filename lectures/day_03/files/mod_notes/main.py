# main.py
from operator import mod

import pkg_resources
import module
from pkg_demo.cool_functions import python_info, webpage
from pkg_demo.cool_functions import *
import pkg_demo
python_info()
webpage()

print(dir(pkg_demo))

print("from main.py", __name__)