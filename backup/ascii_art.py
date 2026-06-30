# ascii_art.py

# -----------------------------
# Default Bunny Art (your original creature)
# -----------------------------
DEFAULT_ART = {
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

# -----------------------------
# Dragon ASCII Art (all moods)
# -----------------------------
DRAGON_ART = {
    "happy": r"""
          /\_/\ 
         ( ^.^ )
          > ^ <    My roar commands generations!
    """,

    "hungry": r"""
          /\_/\ 
         ( •.• )
        <  🔥  >   My belly rumbles for embers...
    """,

    "tired": r"""
          /\_/\ 
         ( -.- )
        zz🔥zz    I need to sleep on my pile of gold...
    """,

    "dirty": r"""
          /\_/\ 
         ( x.x )
        <  🧼  >   My scales are bloody from fallen adventurers...
    """,

    "sad": r"""
          /\_/\ 
         ( ;.; )
          > ^ <    I wish I had more gold...
    """,

    "ecstatic": r"""
          /\_/\ 
         ( ☆o☆ )
        <🔥🎉🔥>   I could burn down a village!
    """,

    "fiery": r"""
          /\_/\ 
         ( >.< )
        <🔥🔥🔥>   My hunger fuels my flames!
    """,

    "irritated": r"""
          /\_/\ 
         ( -_- )
        <  🔥  >   My scales itch... do not test me.
    """,

    "neutral": r"""
          /\_/\ 
         ( •.• )
          > ^ <    Just guarding my hoards of gold.
    """
}

SLIME_ART = {
    "happy": r"""
        .-.
      _(   )_
     (  ^_^  )   *blorp!*
      '-----'
    """,

    "hungry": r"""
        .-.
      _(   )_
     (  •_•  )   *glorp... feed me?*
      '-----'
    """,

    "tired": r"""
        .-.
      _(   )_
     ( -.- )   *sloooosh...*
      '-----'
    """,

    "dirty": r"""
        .-.
      _(   )_
     ( x_x )   *covered in dirt!!!*
      '-----'
    """,

    "sad": r"""
        .-.
      _(   )_
     ( ;_; )   *bluuurp...life is a lie*
      '-----'
    """,

    "ecstatic": r"""
        .-.
      _(   )_
     ( ☆o☆ )   *BLOOOORP!! I just won the lottery*
      '-----'
    """,

    "gooey": r"""
        .-.
      _(   )_
     ( >.< )   *too sticky... help...*
      '-----'
    """,

    "bubbly": r"""
        .-.
      _(   )_
     ( ^o^ )   *bubble bubble!*
      '-----'
    """,

    "neutral": r"""
        .-.
      _(   )_
     ( •.• )   *blorp.*
      '-----'
    """
}


# -----------------------------
# Art Selector
# -----------------------------
def get_art(mood, species="Pet"):
    if species == "Dragon":
        return DRAGON_ART.get(mood, DRAGON_ART["neutral"])
    if species == "Slime":
        return SLIME_ART.get(mood, SLIME_ART["neutral"])
    return DEFAULT_ART.get(mood, DEFAULT_ART["neutral"])

    
