# plant,water,air,fire,ice,stone,technology
powers = {
"plant":[0.6,2,1.2,0.3,1,1.2,0.4],
"water":[0.3,0.6,1,2,1,1.2,1.4],
"air":[1.2,1.2,0.6,1.9,0.7,0.3,0.5],
"fire":[2,0.2,0.8,0.5,1.9,1,1.2],
"ice":[0.9,1.8,1,0.7,1,1.1,2],
"stone":[1,0.9,1.4,1,1.9,0.7,1.6],
"technology":[2,0.4,1.6,1,1.4,0.7,1] 
}
import random
class attack():
    def __init__(self,name,hp,ptype,strengthmap=[1,1,1,1,1,1,1],levelr=1,cost=50):
        self.name = str(name)
        self.force = hp
        self.strength = strengthmap
        self.levelr = levelr
        self.cost = cost
        self.type = ptype
 
        
        
            
class enemy():
    def __init__(self,name,ptype,attacks):
        self.name = name
        self.attacks = attacks
        self.type = ptype
    def calcdamage(enemy,attack):
        global powers      
        try:
            tp = powers[self.type]
            pp = tp[["plant","water","air","fire","ice","stone","technology"].index(enemy.type)]
        except:
            pp = 0.9
        damage = 0
        damage = attack.force * pp
        return damage
        