from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import RepairOrder, Customer
from app.extensions import db

repair_bp = Blueprint("repair", __name__, url_prefix="/repairs")

@repair_bp.route("/")
def list_repairs():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    repairs = RepairOrder.query.order_by(RepairOrder.created_at.desc()).all()
    return render_template("repairs/list.html", repairs=repairs)

@repair_bp.route("/add", methods=["GET", "POST"])
def add_repair():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    customers = Customer.query.all()

    if request.method == "POST":
        repair = RepairOrder(
            customer_id=request.form["customer_id"],
            device=request.form["device"],
            issue_description=request.form["issue_description"],
            status=request.form.get("status", "Pending")
        )
        db.session.add(repair)
        db.session.commit()
        flash("Repair order created", "success")
        return redirect(url_for("repair.list_repairs"))

    return render_template("repairs/form.html", customers=customers, action="Add")

@repair_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_repair(id):
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    repair = RepairOrder.query.get_or_404(id)
    customers = Customer.query.all()

    if request.method == "POST":
        repair.customer_id = request.form["customer_id"]
        repair.device = request.form["device"]
        repair.issue_description = request.form["issue_description"]
        repair.status = request.form["status"]
        db.session.commit()
        flash("Repair order updated", "success")
        return redirect(url_for("repair.list_repairs"))

    return render_template("repairs/form.html", repair=repair, customers=customers, action="Edit")

@repair_bp.route("/delete/<int:id>", methods=["POST"])
def delete_repair(id):
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    repair = RepairOrder.query.get_or_404(id)
    db.session.delete(repair)
    db.session.commit()
    flash("Repair order deleted", "success")
    return redirect(url_for("repair.list_repairs"))
