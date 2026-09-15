"""
Opens a bookmarked link in the default browser.

The URL is read from the BOOKMARK_URL environment variable so the action can be
pointed at whatever the user wants without editing the code.
"""

import os
import webbrowser

DEFAULT_URL = "https://www.wikipedia.org/"


def launchBrowser():
    """Open the configured bookmark. Kept under the old name for compatibility."""
    open_bookmark()


def open_bookmark():
    url = os.environ.get("BOOKMARK_URL", DEFAULT_URL)
    webbrowser.open(url)
