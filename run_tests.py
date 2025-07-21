import sys
from behave.__main__ import main as behave_main

browser = "firefox"    # or "chrome"
headless = "true"      # or "false"

sys.argv = [
    "behave",
    "-D", f"browser={browser}",
    "-D", f"headless={headless}",
    "features"
]

behave_main()