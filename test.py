import argparse
import collections
import json
import logging
import os
import subprocess
import sys
import time

from code2flow import engine



def test_load_all_processors():
    from code2flow.loader import load_all_processors
    res = load_all_processors()
    print(res)


def test_python_processor():
    engine.code2flow(raw_source_paths='code2flow', output_file='ex1.dot', language='py')


test_python_processor()
