from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.extensions import db
from app.models import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Login route (updated)
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session["user_id"] = user.id
            return redirect(url_for("main.dashboard"))
        else:
            flash("Invalid email or password", "error")

    return render_template("login.html")


# Registration route
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if User.query.filter_by(email=email).first():
            flash("Email already exists", "error")
            return redirect(url_for("auth.register"))

        user = User(email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()
        session["user_id"] = user.id
        return redirect(url_for("main.dashboard"))

    return render_template("register.html")


# Logout
@auth_bp.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("main.home"))
