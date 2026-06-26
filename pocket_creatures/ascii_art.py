# ascii_art.py

ART = {
    "happy": r"""
        (\_/)
        ( ^_^)
        / >🍪   Damn I feel good!
    """,

    "hungry": r"""
        (\_/)
        ( •_•)
        / >🥺   Spare me a slice of the cheese?
    """,

    "tired": r"""
        (\_/)
        (-_- zZ)
        / >💤   So EEPY...
    """,

    "dirty": r"""
        (\_/)
        ( x_x)
        / >🧼   Covered in grime!
    """,

    "sad": r"""
        (\_/)
        ( ;_;)
        / >💔   Sometimes I feel like no one cares about me...
    """,

    "ecstatic": r"""
        (\_/)
        ( ☆‿☆)
        / >🎉   Over the moon!
    """,

    "neutral": r"""
        (\_/)
        ( •‿•)
        / >   I have no strong feelings either way.
    """
}

def get_art(mood: str) -> str:
    """Return ASCII art for the given mood."""
    return ART.get(mood, ART["neutral"])
