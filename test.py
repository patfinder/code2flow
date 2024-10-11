import argparse
import collections
import json
import logging
import os
import subprocess
import sys
import time

from code2flow.loader import load_all_processors

res = load_all_processors()
print(res)
