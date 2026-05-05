def is_colliding(rect1, rect2):
    """
    Check if two rectangles are colliding.
    Each rect is a dict with: x, y, width, height

    Returns True if colliding, False if not overlapping.
    """
    return not (
        rect1['x'] + rect1['width']  <= rect2['x'] or   # rect1 is left of rect2
        rect2['x'] + rect2['width']  <= rect1['x'] or   # rect2 is left of rect1
        rect1['y'] + rect1['height'] <= rect2['y'] or   # rect1 is above rect2
        rect2['y'] + rect2['height'] <= rect1['y']      # rect2 is above rect1
    )