"""
Missing Component Engine
Determines which meal components are missing.
"""

from src.graph.meal_graph import get_expected_structure


def get_missing_components(intent, cart_categories):
    """
    Compare expected meal structure with current cart categories.

    Parameters:
        intent (str): Detected meal intent
        cart_categories (list): Categories present in cart

    Returns:
        list: Missing categories
    """

    if not intent:
        return []

    expected_categories = get_expected_structure(intent)

    missing = [
        category
        for category in expected_categories
        if category not in cart_categories
    ]

    return missing