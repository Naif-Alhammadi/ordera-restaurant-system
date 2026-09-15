class Address:
    """" Represent an address with city, country, and street """

    def __init__(self, city: str, country: str, street: str):
        self.__city = city
        self.__country = country
        self.__street = street
