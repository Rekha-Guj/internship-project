import sys
from behave.__main__ import main as behave_main

browser = "chrome"    # or "chrome" or "firefox"
headless = "false"      # or "false" or "true"

sys.argv = [
    "behave",
    "-D", f"browser={browser}",
    "-D", f"headless={headless}",
    "features"
]

behave_main()