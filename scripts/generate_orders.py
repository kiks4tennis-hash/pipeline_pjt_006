from pathlib import Path
from datetime import datetime, timedelta
import random

import pandas as pd

# -----------------------------
# Settings
# -----------------------------
NUM_RECORDS = 1000
OUTPUT_DIR = Path("data")
OUTPUT_FILE = OUTPUT_DIR / "orders.csv"

random.seed(42)

# -----------------------------
# Master Data
# -----------------------------
categories = {
    "Tops": (2500, 9000),
    "Bottoms": (4000, 12000),
    "Shoes": (6000, 25000),
    "Bag": (5000, 30000),
    "Accessory": (1000, 8000),
}

products = {
    "Tops": [
        "T-shirt",
        "Shirt",
        "Hoodie",
        "Sweater",
    ],
    "Bottoms": [
        "Jeans",
        "Shorts",
        "Slacks",
        "Skirt",
    ],
    "Shoes": [
        "Sneakers",
        "Boots",
        "Sandals",
    ],
    "Bag": [
        "Backpack",
        "Shoulder Bag",
        "Tote Bag",
    ],
    "Accessory": [
        "Cap",
        "Belt",
        "Wallet",
        "Necklace",
    ],
}

# -----------------------------
# Generate Data
# -----------------------------
rows = []

today = datetime.now()

for order_id in range(1, NUM_RECORDS + 1):

    category = random.choice(list(categories.keys()))
    product = random.choice(products[category])

    min_price, max_price = categories[category]

    price = random.randint(min_price, max_price)
    quantity = random.randint(1, 3)

    customer_id = random.randint(10000, 10250)

    order_date = today - timedelta(
        days=random.randint(0, 180),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
    )

    rows.append(
        {
            "order_id": order_id,
            "customer_id": customer_id,
            "category": category,
            "product": product,
            "price": price,
            "quantity": quantity,
            "sales": price * quantity,
            "order_date": order_date.strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

# -----------------------------
# Save CSV
# -----------------------------
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.DataFrame(rows)

df.to_csv(OUTPUT_FILE, index=False)

print(f"{len(df)} records generated.")
print(f"Saved to {OUTPUT_FILE.resolve()}")

print(df.head())