#!/usr/bin/python3
from models.human import human


class child(human):
    def __init__(self, fstName: str, lstName: str, age: int):
        super().__init__(fstName, lstName, age)
        self.health = 100
        self.saludo = f"Hola, mi nombre es {self.name} y soy un niño"
