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
    """Coffe object"""
    __recipe: dict = {}

    def __init__(self, name: str, count: int = 1) -> None:
        """Initialize coffe"""
        self.name = name
        self.count = count

        if name in self.__recipe:
            self.is_paid = False

    def __str__(self) -> str:
        """Return a string representation of object"""

        if not self.__recipe:
            return "Order cannot be created. Recipe has not been set."

        if self.name not in self.__recipe:
            return "Order cannot be created. We don't have recipe for it."

        if self.is_paid is False:
            return f'Order "{self.__repr__()}" is created.'

        return f"Preparing {self.count} {self.name}..."

    def __repr__(self) -> str:
        """Return repr string of Coffee"""
        return f"{self.count} {self.name}"

    def __eq__(self, other: "Coffee") -> bool:
        """Compare two coffees"""
        return self.name == other.name and self.count == other.count

    @classmethod
    def set_recipe(cls, recipe: dict) -> None:
        """Set recipe for coffees"""
        cls.__recipe = recipe

    @property
    def espresso(self):
        """Return quantity of espresso in coffee""" 
        return self.__recipe[self.name]['espresso'] * self.count

    @property
    def beans(self) -> int:
        """Return number of beans to prepare this coffee"""
        return self.espresso // self.__recipe['espresso']['espresso'] * 6

    @property
    def milk(self):
        """Return quantity of milk in coffee"""
        milk_for_one_coffee = self.__recipe[self.name].get("steamed_milk", 0) + \
               self.__recipe[self.name].get("foamed_milk", 0)
        return milk_for_one_coffee * self.count


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
    """Custom coffe object"""

    def __init__(self, name: str, count: int = 1):
        super().__init__(name=name, count=count)
        FlavorMixin.__init__(self)

        if hasattr(self, 'is_paid'):
            self.flavor = False

    def __eq__(self, other: Coffee) -> bool:
        flavor_eq = getattr(self, 'sugar', 0) == getattr(other, 'sugar', 0) and \
               getattr(self, 'cinammon', False) == getattr(other, 'cinammon', False) and \
               getattr(self, 'syrup', '') == getattr(other, 'syrup', '')
        return super().__eq__(other) and flavor_eq

    def __repr__(self) -> str:
        """Return repr of the Custom coffe"""
        return f"{self.count} custom {self.name}"

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


def test_cafeteria_class():
    """
    Print Done if all tests passed
    """
    print("Testing Cafeteria class...")
    # We track the orders during the day
    day_track = Track('07.02.2024')
    day_track.date = '07.02.2024'
    # Our cafeteria has a lot of different beverages in the menu and
    # all of them are connected to coffee.
    # The cafeteria use classical RECIPE that provided as a
    # constant.
    order1 = Coffee('latte')
    assert str(order1) == 'Order cannot be created. Recipe has not been set.'
    # We need to set the recipe before creating the instances.
    assert order1.__dict__ == {'name': 'latte', 'count': 1}
    Coffee.set_recipe(RECIPE)
    # A client can order only some kind of coffee.
    order1 = Coffee('latte', 2)
    assert order1.name == 'latte'
    assert order1.count == 2
    # also when the client ask for some order the is_paid attribute is
    # created and it is False from the start.
    assert order1.is_paid is False
    # Coffee have three main ingredients that provide variety of the drinks:
    # espresso, steamed milk and foamed milk. But on the side of the client we
    # provide only name of the drink and total amount of espresso
    # and milk in ml.
    assert order1.espresso == 120
    assert order1.milk == 270
    assert Coffee._Coffee__recipe[order1.name] == {'espresso': 60, 'steamed_milk': 120, 'foamed_milk': 15}
    assert str(order1) == 'Order "2 latte" is created.'

    #now we are ready to place this order
    assert Track.MENU == {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60}
    assert day_track.place_order(order1) == 'Done!'
    assert order1.price == 140
    assert order1.is_paid == True
    assert str(order1) == 'Preparing 2 latte...'
    assert len(day_track.orders) == 1

    # it is possible that we have a coffee in recipe but 
    # don't have in a menu
    order2 = Coffee("macchiato")
    assert str(order2) == 'Order "1 macchiato" is created.'
    assert order2.__dict__ == {'name': 'macchiato', 'count': 1, 'is_paid': False}
    assert day_track.place_order(order2) == "Unfortunately, we don't have such kind of coffee in the menu."
    assert len(day_track.orders) == 1

    order2 = Coffee("mocca")
    assert str(order2) == "Order cannot be created. We don't have recipe for it."
    assert order2.__dict__ == {'name': 'mocca', 'count': 1}
    # Each customer can ask for adding sugar, cinammon or syrup 
    # thus creating custom coffee.
    order2 = CustomCoffee('cappuccino')
    assert isinstance(order2, CustomCoffee)
    assert isinstance(order2, Coffee)
    assert isinstance(order2, FlavorMixin)
    assert not isinstance(order1, CustomCoffee)
    assert not isinstance(order1, FlavorMixin)

    assert order2.name == 'cappuccino'
    assert order2.count == 1
    assert order2.espresso == 60
    assert order2.milk == 120
    assert order2.flavor == False

    assert day_track.place_order(order2) == 'Done!'
    assert len(day_track.orders) == 2
    assert str(order2) == 'Preparing 1 cappuccino...'
    assert order2.price == 60

    assert order2.add_flavor(2, True, 'almond') == 'Done!'
    assert order2.sugar == 2 #number of stickers
    assert order2.cinammon == True #just to add some
    assert order2.syrup == 'almond' #type of syrup
    assert str(order2) == 'Your best cappuccino is ready! It has: 2 stickers of sugar, cinammon, almond syrup.'

    #of course we track the orders
    assert str(day_track.orders) == '[2 latte, 1 custom cappuccino]'
    assert day_track.total_revenue() == 200
    assert day_track.total_milk() == 390
    #we need approx 6 grams of coffee beans to prepare 
    # one espresso
    assert day_track.total_beans() == 36
    assert not isinstance(order2, Track)
    # of course we have some reserves of milk and beans
    # but they are limited. At the beginning of the day we usually
    #have 20 litres of milk and 5 kg of beans
    assert Track._Track__beans == 5000
    assert Track._Track__milk == 20000
    assert day_track.beans == 4964
    assert day_track.milk == 19610

    order3 = Coffee('Irish Coffee', 3)
    # unfortunately we don't have this kind of drinks
    # please let our customer know about it
    assert day_track.orders == [order1, order2]


    order3 = CustomCoffee('latte', 2)
    assert order3 == order1
    assert order3.add_flavor(3, False, 'green banana') == 'Please, pay for it.'
    assert day_track.place_order(order3) == 'Done!'
    assert order3.add_flavor(3, False, 'green banana') == 'Done!'
    assert order3.sugar == 6
    assert str(order3) == 'Your best latte is ready! It has: 6 stickers of sugar, green banana syrup.'
    assert order3 != order1
    
    # Sometimes we have situation when the milk spoiled
    # in grams
    day_track.milk_spoil(19340)
    assert day_track.milk == 0
    order4 = Coffee('latte', 2)
    assert day_track.place_order(order4) == "Unfortunately, we don't have enough ingredients."
    assert len(day_track.orders) == 3
    #oneday our founder bought new fridge
    # and we can store more milk
    Track.set_limit_milk(30000)
    assert Track._Track__milk == 30000


    order5 = "Coffee"
    assert not isinstance(order5, CustomCoffee)
    assert day_track.place_order(order5) == "We can't create anything that is not a Coffee instance."

    #and sure we don't work in air alert time
    Track.change_air_state()
    assert Track.safety == False
    order6 = CustomCoffee('lungo', 2)
    assert day_track.place_order(order6) == 'Unfortunately, now it is not safe to make coffee.'
    Track.change_air_state()
    assert Track.safety == True
    order6 = CustomCoffee('lungo')
    assert str(order6) == 'Order "1 custom lungo" is created.'
    assert day_track.place_order(order6) == 'Done!'
    assert day_track.total_revenue() ==  390
    assert day_track.total_milk() == 660
    assert day_track.total_beans() == 78
    print('Done!')


if __name__ == '__main__':
    test_cafeteria_class()

