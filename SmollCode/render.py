from constants import *
import os, re, getpass

def render_title_logo():
    print(f"{BOLD}{RED}{LOGO}{RESET}\n")

def render_separator():
    print(f"{DIM}{'─' * min(os.get_terminal_size().columns, 90)}{RESET}")

def render_markdown(markdown: str):
    print(re.sub(r"\*\*(.+?)\*\*", rf"{BOLD}\1{RESET}", markdown))

def user_input(message: str=""):
    render_separator()
    user_input = input(f"{BOLD}{GREEN}{message} ❯{RESET} ").strip()
    render_separator()
    return user_input

def get_secure(message: str):
    render_separator()
    secret = getpass.getpass(f"{BOLD}{YELLOW}{message} ❯{RESET} ")
    render_separator()
    return secret

def green_message(message: str):
    print(f"{GREEN}⏺ {message}{RESET}")

def error(message: str):
    print(f"{RED}\u203C {message}{RESET}")

def cyan_message(message: str):
    print(f"{CYAN}{message}{RESET}")

def yellow_message(message: str):
    print(f"{YELLOW}{message}{RESET}")

def indicate_tool_use(tool_name: str, arg_preview: str):
    print(f"\n{GREEN}⏺ {tool_name.capitalize()}{RESET}({DIM}{arg_preview}{RESET})")
