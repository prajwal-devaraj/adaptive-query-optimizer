import random
from datetime import date, timedelta
from faker import Faker
import psycopg2

fake = Faker()

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "aqo_db",
    "user": "postgres",
    "password": "postgres"
}

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()


def random_date(start_days_ago=900):
    return date.today() - timedelta(days=random.randint(0, start_days_ago))


def insert_suppliers(n=500):
    data = []
    for _ in range(n):
        data.append((fake.company(), random.choice(["East", "West", "North", "South"]), random.randint(1, 5)))
    cur.executemany(
        "INSERT INTO suppliers (supplier_name, region, rating) VALUES (%s, %s, %s)",
        data,
    )
    conn.commit()


def insert_warehouses(n=50):
    data = []
    for i in range(n):
        data.append((f"Warehouse_{i+1}", fake.city(), random.randint(5000, 50000)))
    cur.executemany(
        "INSERT INTO warehouses (warehouse_name, city, capacity) VALUES (%s, %s, %s)",
        data,
    )
    conn.commit()


def insert_customers(n=50000):
    batch = []
    for _ in range(n):
        batch.append((
            fake.name(),
            fake.city(),
            fake.state(),
            random.choice(["Retail", "Corporate", "Home Office"]),
            random_date()
        ))
    cur.executemany(
        "INSERT INTO customers (full_name, city, state, segment, signup_date) VALUES (%s, %s, %s, %s, %s)",
        batch,
    )
    conn.commit()


def insert_products(n=20000):
    batch = []
    categories = ["Electronics", "Books", "Clothing", "Home", "Sports", "Beauty"]
    for i in range(n):
        batch.append((
            f"Product_{i+1}",
            random.choice(categories),
            round(random.uniform(5, 1500), 2),
            random.randint(1, 500),
            random.randint(1, 50),
            random.randint(0, 5000)
        ))
    cur.executemany(
        """
        INSERT INTO products (product_name, category, price, supplier_id, warehouse_id, stock)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        batch,
    )
    conn.commit()


def insert_orders(n=200000):
    statuses = ["pending", "shipped", "delivered", "cancelled"]
    batch = []
    for _ in range(n):
        batch.append((
            random.randint(1, 50000),
            random_date(),
            random.choice(statuses),
            round(random.uniform(20, 5000), 2)
        ))
    cur.executemany(
        "INSERT INTO orders (customer_id, order_date, order_status, total_amount) VALUES (%s, %s, %s, %s)",
        batch,
    )
    conn.commit()


def insert_order_items(n=600000):
    batch = []
    for _ in range(n):
        qty = random.randint(1, 10)
        price = round(random.uniform(5, 1500), 2)
        batch.append((
            random.randint(1, 200000),
            random.randint(1, 20000),
            qty,
            price
        ))
    cur.executemany(
        "INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (%s, %s, %s, %s)",
        batch,
    )
    conn.commit()


def insert_shipments(n=200000):
    batch = []
    for _ in range(n):
        batch.append((
            random.randint(1, 200000),
            random.randint(1, 50),
            random_date(),
            random.randint(1, 12),
            round(random.uniform(3, 100), 2)
        ))
    cur.executemany(
        "INSERT INTO shipments (order_id, warehouse_id, shipped_date, delivery_days, shipping_cost) VALUES (%s, %s, %s, %s, %s)",
        batch,
    )
    conn.commit()


def insert_reviews(n=150000):
    batch = []
    for _ in range(n):
        batch.append((
            random.randint(1, 50000),
            random.randint(1, 20000),
            random.randint(1, 5),
            random_date(),
            fake.sentence(nb_words=12)
        ))
    cur.executemany(
        "INSERT INTO reviews (customer_id, product_id, rating, review_date, review_text) VALUES (%s, %s, %s, %s, %s)",
        batch,
    )
    conn.commit()


if __name__ == "__main__":
    insert_suppliers()
    insert_warehouses()
    insert_customers()
    insert_products()
    insert_orders()
    insert_order_items()
    insert_shipments()
    insert_reviews()
    cur.close()
    conn.close()
    print("Large benchmark-style dataset inserted successfully.")