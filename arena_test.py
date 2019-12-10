import pytest
import io
import sys
import superhero
import math
import random

def capture_console_output(function_body):
    # _io.StringIO object
    string_io = io.StringIO()
    sys.stdout = string_io
    function_body()
    sys.stdout = sys.__stdout__
    return string_io.getvalue()

def test_create_ability():
    input_values = ["Amazing Ability", '200']
    # output = []

    def mock_input(s):
        # output.append(s)
        return input_values.pop(0)
    superhero.input = mock_input
    # superheroes.print = lambda s: output.append(s)

    arena = superhero.Arena()
    ability = arena.create_ability()

    assert ['Amazing Ability', 200] == [ability.name, ability.max_damage]

def test_create_weapon():
    input_values = ["Amazing Weapon", '200']

    def mock_input(s):
        return input_values.pop(0)
    superhero.input = mock_input

    arena = superhero.Arena()
    weapon = arena.create_weapon()

    assert ['Amazing Weapon', 200] == [weapon.name, weapon.max_damage]

def test_create_armor():
    input_values = ["Amazing Armor", '300']

    def mock_input(s):
        return input_values.pop(0)
    superhero.input = mock_input

    arena = superhero.Arena()
    armor = arena.create_armor()

    assert ['Amazing Armor', 300] == [armor.name, armor.max_block]


# testing create hero, could break based off of how you built this function so could be ignorable
def test_create_hero():
    # These are the values needed to create a hero. Could be different from application to application
    # due to implementation
    input_values = ['Ben', '1', 'Amazing Ability', '100', '1',
                     'Amazing Weapon', '200', '1', 'God Armor', '500']

    def mock_input(s):
        return input_values.pop(0)
    superhero.input = mock_input

    arena = superhero.Arena()
    hero = arena.create_hero()

    assert ['Ben', 1, True, 0, 0] == [hero.name, hero.current_health, hero.is_alive(), hero.kills, hero.deaths]