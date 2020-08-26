import os
import sys
file_path = os.path.join(os.path.dirname(__file__), '..')
file_dir = os.path.dirname(os.path.realpath('_file_'))
sys.path.insert(0, os.path.abspath(file_path))
