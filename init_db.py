from app import app, db
from app.models import Task

# Push an application context
with app.app_context():
    # Create the database and the database table
    db.create_all()

    # Commit the changes
    db.session.commit()
