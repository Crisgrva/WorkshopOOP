#!/usr/bin/python3
"""
Base model
"""


import json
import time


class human():
    numpersonas = 0

    def __init__(self, fstName, lstName, age):
        self.name = fstName
        self.lstName = lstName
        self.age = age
        self.energy = 100
        self.health = 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("El tipo de nombre no es correcto")
        elif len(value) > 15:
            raise ValueError("El nombre es demasiado largo")
        elif len(value) < 2:
            raise ValueError("El nombre es demasiado corto")

        self.__name = value

    @property
    def lstName(self):
        return self.__lstName

    @lstName.setter
    def lstName(self, value):
        if not isinstance(value, str):
            raise TypeError("El tipo de apellido no es correcto")
        elif len(value) > 15:
            raise ValueError("El apellido es demasiado largo")
        elif len(value) < 2:
            raise ValueError("El apellido es demasiado corto")

        self.__lstName = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("El tipo de edad no es correcto")
        elif value > 100:
            raise ValueError("Estás viviendo demasiado")
        elif value < 1:
            raise ValueError("Aún no has nacido")

        self.__age = value

    def to_dictionary(self):
        dict = {
            "First name": self.name,
            "Last name": self.lstName,
            "Age": self.age,
            "Current Health": self.health,
            "Energy": self.energy,
            "Saludo": self.saludo
        }

        return dict

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return []
        elif list_dictionaries is None:
            return []

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        dicts = []
        if list_objs is not None:
            for obj in list_objs:
                dicts.append(obj.to_dictionary())
            dicts = human.to_json_string(dicts)
        else:
            dicts = str(dicts)

        with open("{}.json".format(cls.__name__), mode="w",
                  encoding="utf-8") as f:
            f.write(dicts)

    def jump(self, seconds):
        energyperseconds = 10

        if not isinstance(seconds, int):
            raise TypeError("No puedes saltar")
        if seconds == 0:
            raise ValueError("¿Realmente quieres saltar?")
        if seconds < 0:
            raise ValueError("No puedes devolver el tiempo")

        for second in range(1, seconds + 1):
            print(f"{self.name} is Jumping...{second}")
            time.sleep(1)

        self.energy -= energyperseconds * seconds

    def feed(self, food):
        if not isinstance(food, int):
            raise TypeError("No puedes comer esto")
        if food < 0:
            raise ValueError("No puedes comer esto")
        if self.energy + food > 100:
            raise ValueError("Es demasiada comida parea ti")

        self.energy += food
