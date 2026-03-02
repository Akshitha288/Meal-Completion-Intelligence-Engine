"""
Intent Detection Module
Detects meal intent based on cuisine in cart.
"""

def detect_intent(cart_cuisines):
    """
    Detect meal intent using dominant cuisine in cart.
    
    Parameters:
        cart_cuisines (list): List of cuisines in current cart
    
    Returns:
        str: Detected meal intent
    """

    if not cart_cuisines:
        return None

    # Get most frequent cuisine
    dominant_cuisine = max(set(cart_cuisines), key=cart_cuisines.count)

    if dominant_cuisine == "North Indian":
        return "North Indian Meal"
    elif dominant_cuisine == "Fast Food":
        return "Fast Food Combo"
    elif dominant_cuisine == "South Indian":
        return "South Indian Breakfast"
    else:
        return None