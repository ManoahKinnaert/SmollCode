from constants import *
import os 
import re

def render_title_logo():
    print(f"{BOLD}{RED}{LOGO}{RESET}\n")

def render_separator():
    print(f"{DIM}{'─' * min(os.get_terminal_size().columns, 90)}{RESET}")

def render_markdown(markdown: str, other: str=""):
    print(other + re.sub(r"\*\*(.+?)\*\*", rf"{BOLD}\1{RESET}", markdown))