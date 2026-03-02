"""
Meal Ontology Graph
Defines expected structure for different meal intents.
"""

MEAL_GRAPH = {
    "North Indian Meal": ["Main", "Side", "Drink", "Dessert"],
    "Fast Food Combo": ["Main", "Side", "Drink"],
    "South Indian Breakfast": ["Main", "Side", "Drink"]
}


def get_expected_structure(intent):
    """
    Return expected categories for given meal intent.
    """
    return MEAL_GRAPH.get(intent, [])