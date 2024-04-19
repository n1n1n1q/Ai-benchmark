"""Cafeteroum"""


RECIPE = {
        "espresso": {
            'espresso': 30},
        "latte": {
            'espresso': 60,
            'steamed_milk': 120, 
            'foamed_milk': 15},
        "macchiato": {
            'espresso': 60,
            'foamed_milk': 15},
        "flat white": {
            'espresso': 60,
            'steamed_milk': 120},
        "dopio": {
            'espresso': 60},
        "cappuccino": {
            'espresso': 60,
            'steamed_milk': 60, 
            'foamed_milk': 60},
        "lungo": {
            'espresso': 90},
        "cortado": {
            'espresso': 60,
            'steamed_milk': 60}
            }


class Coffee:
    """Coffee object"""
    __recipe = {}

    def __init__(self, name: str, count: int = 1) -> None:
        """Initialize coffee"""
        self.name = name
        self.count = count
        if name in self.__recipe:
            self.is_paid = False

    @classmethod
    def set_recipe(cls, recipe: dict) -> None:
        """Set recipe for coffees"""
        cls.__recipe = recipe

    @property
    def espresso(self):
        """Return quantity of espresso in coffee"""
        return self.__recipe.get(self.name, {}).get('espresso', 0) * self.count

    @property
    def beans(self) -> int:
        """Return number of beans to prepare this coffee"""
        espresso_per_shot = self.__recipe.get('espresso', {}).get('espresso', 0)
        return (self.espresso // espresso_per_shot) * 6

    @property
    def milk(self):
        """Return quantity of milk in coffee"""
        recipe = self.__recipe.get(self.name, {})
        milk_for_one_coffee = recipe.get("steamed_milk", 0) + recipe.get("foamed_milk", 0)
        return milk_for_one_coffee * self.count

    def __str__(self) -> str:
        """Return a string representation of object"""
        if not self.__recipe:
            return "Order cannot be created. Recipe has not been set."
        if self.name not in self.__recipe:
            return "Order cannot be created. We don't have recipe for it."
        if not self.is_paid:
            return f'Order "{self.__repr__()}" is created.'
        return f"Preparing {self.count} {self.name}..."

    def __repr__(self) -> str:
        """Return repr string of Coffee"""
        return f"{self.count} {self.name}"

    def __eq__(self, other: "Coffee") -> bool:
        """Compare two coffees"""
        return self.name == other.name and self.count == other.count


class FlavorMixin:
    """Flavor mixin object"""

    def add_flavor(self, sugar: int, cinammon: bool, syrup: str) -> str:
        """Add flavor to coffe"""
        if not getattr(self, 'is_paid', False):
            return "Please, pay for it."

        self.sugar = self.count * sugar
        self.cinammon = cinammon
        self.syrup = syrup

        if sugar or cinammon or syrup:
            self.flavor = True

        return "Done!"


class CustomCoffee(Coffee, FlavorMixin):
    """Custom coffee object"""

    def __init__(self, name: str, count: int = 1):
        super().__init__(name=name, count=count)
        FlavorMixin.__init__(self)
        self.flavor = False

    def __str__(self) -> str:
        """Return string representation of CustomCoffee"""
        if not self.flavor:
            return super().__str__()
        flavors = []
        if getattr(self, 'sugar', 0):
            flavors.append(f"{self.sugar} stickers of sugar")
        if getattr(self, 'cinammon', False):
            flavors.append("cinammon")
        if getattr(self, 'syrup', ""):
            flavors.append(f"{self.syrup} syrup")
        return f"Your best {self.name} is ready! It has: {', '.join(flavors)}."

    def __repr__(self) -> str:
        """Return repr of the Custom coffee"""
        return f"{self.count} custom {self.name}"

    def __eq__(self, other: "CustomCoffee") -> bool:
        """Compare two custom coffees"""
        flavor_eq = getattr(self, 'sugar', 0) == getattr(other, 'sugar', 0) and \
                    getattr(self, 'cinammon', False) == getattr(other, 'cinammon', False) and \
                    getattr(self, 'syrup', '') == getattr(other, 'syrup', '')
        return super().__eq__(other) and flavor_eq


class Track:
    """Daily orders tracker"""
    MENU = {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60
    }

    __beans = 5000
    __milk = 20000
    safety = True

    def __init__(self, date: str) -> None:
        """Initialize tracker"""
        self.date = date
        self.orders = []

        self.milk = self.__milk
        self.beans = self.__beans

    @classmethod
    def set_limit_milk(cls, value: int) -> None:
        """change milk limit"""
        cls.__milk = value

    @classmethod
    def change_air_state(cls) -> None:
        """Change air safety state"""
        if cls.safety:
            cls.safety = False
        else:
            cls.safety = True

    def milk_spoil(self, value: int) -> None:
        """Spoil some milk"""
        self.milk = max(0, self.milk - value)

    def place_order(self, order: Coffee) -> str:
        """Start"""

        if not isinstance(order, Coffee):
            return "We can't create anything that is not a Coffee instance."

        if order.name not in self.MENU:
            return "Unfortunately, we don't have such kind of coffee in the menu."

        if not self.safety:
            return "Unfortunately, now it is not safe to make coffee."

        if self.beans < order.beans or self.milk < order.milk:
            return "Unfortunately, we don't have enough ingredients."

        order.price = self.MENU[order.name] * order.count

        order.is_paid = True

        self.beans -= order.beans
        self.milk -= order.milk

        self.orders.append(order)

        return "Done!"

    def total_revenue(self) -> int:
        """Return total revenue of day"""
        return sum(order.price for order in self.orders)

    def total_milk(self) -> int:
        """Return total milk consumption of day"""
        return sum(order.milk for order in self.orders)

    def total_beans(self) -> int:
        """Return total coffe bean consumption of day"""
        return sum(order.beans for order in self.orders)

