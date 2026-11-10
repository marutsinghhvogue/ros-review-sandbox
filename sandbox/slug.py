"""URL slugs: lower-case, words joined by single hyphens, no leading/trailing hyphens."""

import re

_NON_WORD = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Turn a title into a URL slug: "Hello, World!" -> "hello-world"."""
    return _NON_WORD.sub("-", text.lower()).strip("-")
