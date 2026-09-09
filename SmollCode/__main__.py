from display import *
from tools import *

def main():
    render_title_logo()
    render_separator()
    render_markdown(markdown="Version 0.1 beta | ** Model: **")
    render_separator()
    warning("test")

if __name__ == "__main__":
    main()