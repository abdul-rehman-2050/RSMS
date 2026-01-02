from faker import Faker
import random
from app.extensions import db
from app.models import User, Customer, RepairOrder



fake = Faker()

def seed_users(n=5):
    roles = ["admin", "staff", "technician", "customer"]
    for _ in range(n):
        user = User(
            email=fake.unique.email(),
            role=random.choice(roles)
        )
        user.set_password("123456")
        db.session.add(user)
    db.session.commit()

def seed_customers(n=20):
    customers = []
    for _ in range(n):
        customer = Customer(
            name=fake.name(),
            email=fake.unique.email(),
            phone=fake.phone_number()
        )
        db.session.add(customer)
        customers.append(customer)
    db.session.commit()
    return customers

def seed_repairs(customers, n=50):
    statuses = ["Received", "Diagnosing", "Waiting Parts", "In Repair", "Completed", "Delivered"]
    devices = ["iPhone 11", "Samsung A51", "Laptop", "iPad", "MacBook"]
    for _ in range(n):
        repair = RepairOrder(
            customer_id=random.choice(customers).id,
            device=random.choice(devices),
            issue_description=fake.sentence(),
            status=random.choice(statuses)
        )
        db.session.add(repair)
    db.session.commit()


 

def seed_all():
    try:
        with db.session.begin():
            # --- Users ---
            roles = ["admin", "staff", "technician", "customer"]
            for _ in range(5):
                u = User(email=fake.unique.email(), role=random.choice(roles))
                u.set_password("123456")
                db.session.add(u)

            # --- Customers ---
            customers = []
            for _ in range(20):
                c = Customer(
                    name=fake.name(),
                    email=fake.unique.email(),
                    phone=fake.phone_number()
                )
                db.session.add(c)
                customers.append(c)

            # Flush to get IDs without committing yet
            db.session.flush()  # now c.id is available for RepairOrder

            # --- Repairs ---
            statuses = ["Received", "Diagnosing", "Waiting Parts", "In Repair", "Completed", "Delivered"]
            devices = ["iPhone 11", "Samsung A51", "Laptop", "iPad", "MacBook"]

            for _ in range(50):
                r = RepairOrder(
                    customer_id=random.choice(customers).id,  # IDs now exist
                    device=random.choice(devices),
                    issue_description=fake.sentence(),
                    status=random.choice(statuses)
                )
                db.session.add(r)

        print("Database seeded successfully!")

    except Exception as e:
        db.session.rollback()
        print("Seeding failed, rolled back!", e)
