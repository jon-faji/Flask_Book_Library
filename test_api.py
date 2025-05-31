import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_books_json(client):
    rv = client.get('/books/json')
    assert rv.status_code == 200
    assert 'books' in rv.json
    assert isinstance(rv.json['books'], list)

def test_create_book(client):
    new_book = {
        'name': 'Test Book',
        'author': 'Test Author',
        'year_published': 2024,
        'book_type': 'Fiction'
    }
    rv = client.post('/books/create', json=new_book)
    assert rv.status_code == 302  # Because it redirects

def test_get_book_details(client):
    # Ensure the book exists first
    new_book = {
        'name': 'Lookup Book',
        'author': 'Author',
        'year_published': 2023,
        'book_type': 'Non-fiction'
    }
    client.post('/books/create', json=new_book)

    rv = client.get('/books/details/Lookup Book')
    assert rv.status_code == 200
    assert rv.json['book']['name'] == 'Lookup Book'

def test_update_book(client):
    # First, create a book
    new_book = {
        'name': 'Editable Book',
        'author': 'Author',
        'year_published': 2020,
        'book_type': 'Mystery'
    }
    client.post('/books/create', json=new_book)

    # Get book id from JSON list
    books = client.get('/books/json').json['books']
    book_id = next((i for i, b in enumerate(books) if b['name'] == 'Editable Book'), None)
    
    assert book_id is not None

    # Update the book
    update_data = {
        'name': 'Edited Book',
        'author': 'Updated Author'
    }
    rv = client.post(f'/books/{book_id}/edit', json=update_data)
    assert rv.status_code == 200
    assert rv.json['message'] == 'Book updated successfully'

def test_delete_book(client):
    new_book = {
        'name': 'Delete Me',
        'author': 'Author',
        'year_published': 2019,
        'book_type': 'Drama'
    }
    client.post('/books/create', json=new_book)

    # Get book id
    books = client.get('/books/json').json['books']
    book_id = next((i for i, b in enumerate(books) if b['name'] == 'Delete Me'), None)

    assert book_id is not None

    rv = client.post(f'/books/{book_id}/delete')
    assert rv.status_code == 302  # Redirect on success
