from flask import Blueprint, render_template, session, redirect, url_for

from app.models import Customer

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")


@main_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    customers = Customer.query.order_by(Customer.created_at.desc()).all()
    return render_template("dashboard.html", customers=customers)
    