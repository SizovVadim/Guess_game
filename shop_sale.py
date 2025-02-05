class Customer:
    def __init__(self, name: str):
        self.name = name
        self.__discount = 10
        # Добавьте сюда приватный атрибут "скидка"
        # со значением по умолчанию 10.

    # Метод set_discount() принимает на вход
    # новое значение для приватного атрибута "скидка".
    # Если new_value превышает 80 -
    # новое значение скидки должно стать 80.
    # Метод не должен ничего возвращать.
    def set_discount(self, new_value: int):
        if new_value <= 80:
            self.__discount = new_value
            return self.__discount
        else:
            self.__discount = 80
            return self.__discount

    # Метод get_price() получает на вход исходную стоимость товара
    # и должен вернуть новую цену товара с учётом
    # скидки покупателя.
    # Возвращаемое значение округлите до двух знаков после запятой.
    def get_price(self, price: int) -> float:
        self.price = price
        return round(self.price * (1 - self.__discount / 100), 2)



# Проверим работу программы.
# Создаём объект покупателя:
customer = Customer('Иван Иванович')

original_price = 85

print(
    f'С исходной скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)
# Изменим скидку до неприемлемого уровня.
# Метод set_discount() должен установить размер скидки равным 80.
customer.set_discount(90)
print(
    f'С новой скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)
