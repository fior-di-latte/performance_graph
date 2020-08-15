#
""" sheeesh"""

## mm
import argparse
import time
from tests.sub_dir.subsub_dir.helper import  goodnight
import pandas

df = pandas.DataFrame([[3,4,5]*100, [5,2,1]*100])
df.apply(lambda x: x**3)
def foo():
    time.sleep(0.1)

def bar():
    time.sleep(0.4)

goodnight()

for i in range(10):
    foo()
bar()

def foo():
    time.sleep(2)

foo()

parser = argparse.ArgumentParser(description='Testing.')
parser.add_argument('-w', action='store_true')
args = parser.parse_args()
print(args.w)