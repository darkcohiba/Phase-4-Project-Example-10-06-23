#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import db, Gladiator, Arena, Fights



# Views go here!

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'


class Fighters(Resource):
        def get(self):
            fighters = [f.to_dict(rules=('-arena_field.fight_field', '-gladiator_field')) for f in Fights.query.all()]
            return fighters, 200
        def post(self):
            request_obj = request.get_json()
            try:
                print(request_obj["gladiator"], request_obj["arena"])
                new_fight = Fights(
                    gladiator_id =request_obj["gladiator"],
                    arena_id = request_obj["arena"],
                )
                db.session.add(new_fight)
                db.session.commit()

            except Exception as e:
                message = {'errors': [e.__str__()]}
                return message, 422
            
            return new_fight.to_dict(),200
        

api.add_resource(Fighters, '/fighters')

if __name__ == '__main__':
    app.run(port=5555, debug=True)




