stages = [
    # Final state: head, torso, both arms, both legs (dead - 0 lives)
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    # 1 life left: head, torso, both arms, one leg
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    # 2 lives left: head, torso, both arms
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    # 3 lives left: head, torso, one arm
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    # 4 lives left: head and torso
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    # 5 lives left: head only
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    # Initial state: empty gallows (6 lives)
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]