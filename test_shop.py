"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(product.quantity) is True
        assert product.check_quantity(1000)

    def test_product_buy(self, product):
        product.buy(8)
        assert product.quantity == 992

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            assert product.buy(1009)


class TestCart:

    def test_add_product(self, product, cart):
        cart.add_product(buy_count=1, product=product)
        assert cart.products[product] == 1
        cart.add_product(buy_count=1000, product=product)
        assert cart.products[product] == 1001

    def test_remove_product(self, product, cart):
        cart.add_product(buy_count=100, product=product)
        cart.remove_product(remove_count=100, product=product)
        assert len(cart.products) == 0

    def test_clear(self, product, cart):
        cart.add_product(buy_count=100, product=product)
        cart.clear()
        assert len(cart.products) == 0

    def test_total_price(self, product, cart):
        cart.add_product(buy_count=2, product=product)
        assert cart.get_total_price() == 200

    def test_product_buy_more_than_available(self, cart, product):
        cart.add_product(product, 1999)
        with pytest.raises(ValueError):
            cart.buy()
        assert product.quantity == 1000
