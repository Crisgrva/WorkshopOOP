#!/usr/bin/python3
"""
Driver program
"""

from models.human import human
from models.child import child
from models.young import young
from models.older import older

Jorge = child("Jorge", "Cepeda", 9)
Andres = young("Andrés", "Cepeda", 18)
Pedro = older("Pedro", "Capó", 75)

Jorge.jump(2)
Andres.jump(5)
Pedro.jump(1)

Jorge.feed(10)
Andres.feed(20)

human.save_to_file([Jorge, Andres, Pedro])