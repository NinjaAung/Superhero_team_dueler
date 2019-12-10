import random

class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
        '''
       # TODO: Instantiate the variables listed in the docstring with then
       # values passed in
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value.
      return random.randint(0,self.max_damage)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack()) 
