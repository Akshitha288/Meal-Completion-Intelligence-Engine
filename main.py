from src.intent.intent_detection import detect_intent
from src.engine.missing_component import get_missing_components


def test_meal_completion():

    # Example cart
    cart_cuisines = ["North Indian", "North Indian"]
    cart_categories = ["Main"]  # Only main dish added

    # Step 1: Detect intent
    intent = detect_intent(cart_cuisines)

    print("Detected Intent:", intent)

    # Step 2: Get missing components
    missing = get_missing_components(intent, cart_categories)

    print("Missing Components:", missing)


if __name__ == "__main__":
    test_meal_completion()