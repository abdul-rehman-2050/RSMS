# app/commands.py
import click
from flask.cli import with_appcontext
from app.seed import seed_all, seed_users, seed_customers, seed_repairs

@click.command("seed-db")
@with_appcontext
def seed_db():
    seed_users()
    customers = seed_customers()
    seed_repairs(customers)
    click.echo("Database seeded with fake data!")

@click.command("seed-db-all")
@with_appcontext
def seed_db_all():
    seed_all()
    click.echo("Database seeded with fake data! Through single transaction.")