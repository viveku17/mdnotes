import os
import git
import subprocess
import multiprocessing as mp
import tkinter as tk
from tkinter import filedialog

from src.data import get_data, set_data


def run_command(command, **kwargs):
    return subprocess.run(command.split(" "), **kwargs)


def is_valid_directory(path):
    return os.path.isdir(path)
