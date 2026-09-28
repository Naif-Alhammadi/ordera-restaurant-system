class Address:
    """" Represent an address with city, country, and street """

    def __init__(self, city: str, country: str, street: str):
        self.__city = city
        self.__country = country
        self.__street = street

    def __str__(self):
        return f"City: {self.__city}, Conutry: {self.__country}, Street: {self.__street}"