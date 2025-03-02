discount = 10
class Brick:
    """Класс, описывающий объект Кирпич, который будет использоваться, как товар в магазине строительных материалов"""

    def __init__(self, volume: int, material: str, price: int):
        """
        Создание объекта Кирпич

                :param volume: Объем изделия
                :param material: РњР°С‚РµСЂРёР°Р» РёР·РґРµР»РёСЏ
                :param price: Р¦РµРЅР° РёР·РґРµР»РёСЏ
                """

        self._volume = volume
        self._material = material
        self._price = price
    @property
    def volume(self) -> int:
        """Возвращает объем изделия."""

        return self._volume

    @volume.setter
    def volume(self, new_volume: int) -> None:
        """Устанавливает другой объем изделия."""

        self._volume = new_volume

    @property
    def material(self) -> str:
        """Возвращает материал изделия."""

        return self._material

    @material.setter
    def material(self, new_material: str) -> None:
        """Устанавливает новый материал изделия."""

        self._material = new_material

    @property
    def price(self) -> int:
        """Возвращает цену изделия."""

        return self._price

    @price.setter
    def price(self, new_price: int) -> None:
        """Устанавливает новую цену изделия."""

        self._price = new_price

    def __str__(self) -> str:
        return f'Кирпич объемом {self.volume}, {self.material}, {self.price}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.volume!r}, {self.material!r}, {self.price!r})'


class Red(Brick):
    """Класс, описывающий объект Красный кирпич."""

    def __init__(self, volume: int, material: str, price: int, color: int):
        """
        Создание объекта Красный кирпич

        :param volume: Объем изделия
        :param material: Материал изделия
        :param price: Цена изделия
        :param color: Цвет изделия в цифровом коде
        """

        super().__init__(volume, material, price)
        self._color = color
        self._price = None #Для учета скидки
        self.price = price

    @property
    def color(self) -> int:
        """Возвращает цвет кирпича."""

        return self._color

    @color.setter
    def color(self, new_color: int) -> None:
        """Устанавливает новый увет кирпича."""

        self._color = new_color

    @property
    def price(self) -> int:
        """Возвращает цену изделия."""

        return self._price

    @price.setter
    def price(self, new_price: int) -> None:
        """Устанавливает новую цену изделия с учетом скидки."""

        self._price = round(new_price - (new_price * discount / 100))

    def __str__(self) -> str:
        """Перезагружаем метод str, меняем название на "Красный кирпич" и добавляем характеристику: цвет кирпича."""

        return f'Красный кирпич № {self.volume}, {self.material}, {self.price}, цвета {self.color} RGB'

    def __repr__(self) -> str:
        """Перезагружаем метод repr, добавляем новую характеристику: цвет изделия."""

        return f'{self.__class__.__name__}({self.volume!r}, {self.material!r}, {self.price!r}, {self.color!r})'