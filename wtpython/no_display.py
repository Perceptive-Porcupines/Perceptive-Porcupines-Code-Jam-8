"""
This module works to dump the information for the no-display option.

Each datasource should have it's own function while `dump_info` will
control the order in which they are displayed.
"""
from rich import print
from rich.markdown import HorizontalRule

from wtpython.search_engine import SearchEngine
from wtpython.settings import SEARCH_ENGINE
from wtpython.stackoverflow import StackOverflow


def _header(txt: str) -> str:
    """Format header for section."""
    print(HorizontalRule())
    return f"[yellow]{txt}:[/]\n"


def _stackoverflow(so: StackOverflow) -> None:
    """Dump Stackoverflow Questions list."""
    print(_header("Stack Overflow Results"))
    print(so.no_display())


def _searchengine(search_engine: SearchEngine) -> None:
    """Dump url for search engine."""
    print(_header(f"Search on {SEARCH_ENGINE}"))
    print(search_engine.url)


def dump_info(so_results: StackOverflow, search_engine: SearchEngine) -> None:
    """Dump information for no-display mode.

    The traceback message is dumped before display vs no-display is evaluated.
    """
    _stackoverflow(so_results)
    _searchengine(search_engine)
    print()
