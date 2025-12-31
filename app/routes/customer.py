from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import Customer
from app.extensions import db

customer_bp = Blueprint("customer", __name__, url_prefix="/customer")

# Add Customer
@customer_bp.route("/add", methods=["GET", "POST"])
def add_customer():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        customer = Customer(name=name, email=email, phone=phone)
        db.session.add(customer)
        db.session.commit()
        flash("Customer added successfully", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("customer_form.html", action="Add")

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

    return render_template("customer_form.html", action="Edit", customer=customer)

# Delete Customer
@customer_bp.route("/delete/<int:id>", methods=["POST"])
def delete_customer(id):
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    flash("Customer deleted successfully", "success")
    return redirect(url_for("main.dashboard"))
