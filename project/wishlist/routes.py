### wishlist/routes.py
from flask import request, jsonify
from . import wishlist_bp
from .models import Wishlist
from project import db  


@wishlist_bp.route('/api/wishlist', methods=['GET'])
def get_wishlist():
    wishlists = Wishlist.query.all()
    return jsonify([w.to_dict() for w in wishlists]), 200

@wishlist_bp.route('/api/wishlist/<int:wishlist_id>', methods=['GET'])
def get_single_wishlist(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)
    if not wishlist:
        return jsonify({'error': 'Wishlist item not found'}), 404
    return jsonify(wishlist.to_dict()), 200

@wishlist_bp.route('/api/wishlist', methods=['POST'])
def create_wishlist():
    data = request.get_json()
    if not data or 'customer_id' not in data or 'book_id' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_item = Wishlist(
        customer_id=data['customer_id'],
        book_id=data['book_id']
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

@wishlist_bp.route('/api/wishlist/<int:wishlist_id>', methods=['PUT'])
def update_wishlist(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)
    if not wishlist:
        return jsonify({'error': 'Wishlist item not found'}), 404

    data = request.get_json()
    if 'customer_id' in data:
        wishlist.customer_id = data['customer_id']
    if 'book_id' in data:
        wishlist.book_id = data['book_id']

    db.session.commit()
    return jsonify(wishlist.to_dict()), 200

@wishlist_bp.route('/api/wishlist/<int:wishlist_id>', methods=['DELETE'])
def delete_wishlist(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)
    if not wishlist:
        return jsonify({'error': 'Wishlist item not found'}), 404

    db.session.delete(wishlist)
    db.session.commit()
    return jsonify({'message': 'Deleted successfully'}), 200
