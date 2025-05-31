### wishlist/forms.py (optional WTForms UI integration)
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class WishlistForm(FlaskForm):
    customer_id = IntegerField('Customer ID', validators=[DataRequired()])
    book_id = IntegerField('Book ID', validators=[DataRequired()])
    submit = SubmitField('Add to Wishlist')
