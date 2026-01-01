from sqlite3 import IntegrityError
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import Customer
from app.extensions import db

customer_bp = Blueprint("customer", __name__, url_prefix="/customer")

@customer_bp.route("/add", methods=["GET", "POST"])
def add_customer():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        email = request.form["email"]

        if Customer.query.filter_by(email=email).first():
            flash("Customer already exists", "error")
            return render_template("customers/form.html", action="Add")

        customer = Customer(
            name=request.form["name"],
            email=email,
            phone=request.form["phone"]
        )

        db.session.add(customer)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("Email already exists", "error")
            return render_template("customers/form.html", action="Add")

    return render_template("customers/form.html", action="Add")


# Edit Customer
@customer_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_customer(id):
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    customer = Customer.query.get_or_404(id)

    if request.method == "POST":
        customer.name = request.form["name"]
        customer.email = request.form["email"]
        customer.phone = request.form["phone"]
        db.session.commit()
        flash("Customer updated successfully", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("customers/form.html", action="Edit", customer=customer)

@customer_bp.route("/delete/<int:id>", methods=["POST"])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    if customer.repair_orders:  # assuming relationship
        flash("Cannot delete customer with existing repair orders", "error")
        return redirect(url_for("customer.view_customers"))

    db.session.delete(customer)
    db.session.commit()
    flash("Customer deleted successfully", "success")
    return redirect(url_for("customer.view_customers"))


#view customers route
@customer_bp.route("/view", methods=["GET"])
def view_customers():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    customers = Customer.query.all()
    return render_template("customers/list.html", customers=customers)


# Customer Details
@customer_bp.route("/details/<int:id>", methods=["GET"])
def customer_details(id):
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    customer = Customer.query.get_or_404(id)
    return render_template("customers/detail.html", customer=customer)