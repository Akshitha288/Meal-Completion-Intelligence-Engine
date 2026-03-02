import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


def generate_synthetic_data(num_sessions=1000):
    """
    Generate synthetic food ordering session data.
    """

    users = range(1, 201)
    restaurants = range(1, 51)

    cuisines = ["North Indian", "Fast Food", "South Indian"]
    categories = ["Main", "Side", "Drink", "Dessert"]

    data = []

    start_date = datetime(2025, 1, 1)

    for session_id in range(1, num_sessions + 1):
        user_id = random.choice(users)
        restaurant_id = random.choice(restaurants)
        cuisine = random.choice(cuisines)

        num_items = random.randint(1, 4)

        for _ in range(num_items):
            item_id = random.randint(1, 200)
            category = random.choice(categories)
            price = random.randint(100, 500)

            timestamp = start_date + timedelta(
                minutes=random.randint(0, 100000)
            )

            data.append([
                session_id,
                user_id,
                restaurant_id,
                cuisine,
                item_id,
                category,
                price,
                timestamp
            ])

    columns = [
        "session_id",
        "user_id",
        "restaurant_id",
        "cuisine",
        "item_id",
        "category",
        "price",
        "timestamp"
    ]

    df = pd.DataFrame(data, columns=columns)

    return df


if __name__ == "__main__":
    df = generate_synthetic_data(1000)
    df.to_csv("data/synthetic_dataset.csv", index=False)
    print("Dataset generated successfully!")