def parse_version(s: str) -> tuple[int, ...]:
    """Parse a dotted version, optionally prefixed by one lowercase v."""
    if s.startswith("v"):
        s = s[1:]
    return tuple(int(part) for part in s.split("."))
