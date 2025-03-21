"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, p_name: str, p_type: str, price: int, mass: int):
        self.p_name = p_name
        self.p_type = p_type
        self.price = price
        self.mass = mass
    def __str__(self):
        return(f"{self.p_name}, {self.p_type}, {self.price}, {self.mass}")


def main():
    kokokola = Product("Ко-ко-ко-ла", "напиток", 100, 500)
    print(kokokola)
    # print(f"price of kokokola is {kokokola.price}")
    return 0

if __name__ == '__main__':
    res = main()
    exit(res)
