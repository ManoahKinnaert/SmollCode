from render import *
from tools import *

def main():
    render_title_logo()
    render_separator()
    render_markdown(markdown="Version: ** 0.1 beta ** | Provider: ** ** | ** Model: **")
    render_separator()
    user_input()

if __name__ == "__main__":
    main()