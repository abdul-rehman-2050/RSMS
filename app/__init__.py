from flask import Flask
from app.config import Config
from app.extensions import db,migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.customer import customer_bp
    from app.routes.repair_order import repair_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(repair_bp)
    # Uncomment the following lines to create database tables on app startup , currently we using flask-migrations 
    # Migrations will manage schema.
    # with app.app_context():  
    #     db.create_all()
    
    from app.commands import seed_db, seed_db_all
    app.cli.add_command(seed_db_all)
    app.cli.add_command(seed_db)

    return app
