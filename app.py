from project import app, db
from project.wishlist.models import Wishlist  # Import your Wishlist model

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the wishlist table if it doesn't exist yet
    app.run(debug=True)
