import json

new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}

def get_inventory():
    with open('inventory.json', 'r') as book:
        inventory = json.load(book)
    print(f"Number of books in the inventory: {len(inventory)}")
    return inventory

def save_new_entry(new_book, inventory):
    inventory.append(new_book)
    with open('inventory.json', 'w') as books:
        json.dump(inventory, books, indent=4)

def display_inventory(inventory):
    for book in inventory:
        print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")

save_new_entry(new_book, get_inventory())
display_inventory(get_inventory())