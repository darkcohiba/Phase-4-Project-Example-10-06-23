#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Gladiator, Arena, Fights

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # db.create_all()

        # delete my previous data
        db.session.query(Gladiator).delete()
        db.session.query(Arena).delete()
        


        print("seeding gladiators")
        g1 = Gladiator(name="Ryan", number_of_fights=25, weapon="Shiv")
        g2 = Gladiator(name="Jake", number_of_fights=29, weapon="Bare Hands")
        g3 = Gladiator(name="Cristal", number_of_fights=50, weapon="Nails")
        glads= [g1,g2,g3]
        db.session.add_all(glads)
        db.session.commit()

        print("seeding arenas")


        a1 = Arena(title="Worchestire", location="France")
        a2 = Arena(title="A Random Divet on Mars", location="Mars")
        a3 = Arena(title="Mr.Beast's Private Island", location="Need to Know")
        arenas = [a1, a2, a3]
        db.session.add_all(arenas)
        db.session.commit()

        print("seeding fights")
        fights = []
        for arena in arenas:
            f1 = Fights(gladiator_id=rc(glads).id, arena_id=arena.id)
            fights.append(f1)
        db.session.add_all(fights)
        db.session.commit()







        # db.create_all()
        # Seed code goes here!
