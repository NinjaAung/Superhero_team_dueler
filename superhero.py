import random

class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
        '''
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      # Return an attack value between 0 and the full attack.
      return random.randint(0,self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block)

class Hero(Ability, Armor):
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        self.name = name
        self.max_health = starting_health
        self.current_health = self.max_health
        self.armors = list()
        self.abilities = list()

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
        '''
        damage = 0

        for ability in self.abilities: 
            new_damage = damage + ability.attack()
            damage = new_damage

        return damage

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        blocked = 0
        for armor in self.armors:
            new_block = armor.block() + blocked
            blocked = new_block 
        return blocked 

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense. '''
        blocked = self.defend()

        if damage - blocked > 0:
            damage_taken = damage - blocked
        else:
            damage_taken = 0

        self.current_health = self.current_health - damage_taken
         
        return self.current_health

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health <= 0:
            return False
        else:
            return True
        pass



        



if __name__ == "__main__":
    pass