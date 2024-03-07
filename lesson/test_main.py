import pytest
from main import Category, Product


def test_category_initialization():
    category = Category("Фрукты", "Вкусные и полезные фрукты")
    assert category.name == "Фрукты"
    assert category.description == "Вкусные и полезные фрукты"


def test_product_initialization():
    product = Product("Яблоко", "Сладкое и хрустящее яблоко", 100, 50)
    assert product.name == "Яблоко"
    assert product.description == "Сладкое и хрустящее яблоко"
    assert product.price == 100
    assert product.quantity == 50


def test_category_product_count():
    category = Category("Фрукты", "Вкусные и полезные фрукты")
    product1 = Product("Яблоко", "Сладкое и хрустящее яблоко", 100, 50)
    product2 = Product("Банан", "Желтый и питательный банан", 80, 30)
    assert category.total_unique_products == 3


def test_category_count():
    category1 = Category("Фрукты", "Вкусные и полезные фрукты")
    category2 = Category("Овощи", "Свежие и хрустящие овощи")
    assert Category.total_categories == 4
