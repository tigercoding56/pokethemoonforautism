# plant,water,air,fire,ice,stone,technology
import pygame
powers = {
"plant":[0.6,2,1.2,0.3,1,1.2,0.4],
"water":[0.3,0.6,1,2,1,1.2,1.4],
"alien":[1.2,1.2,0.6,1.9,0.7,0.3,0.5],
"fire":[2,0.2,0.8,0.5,1.9,1,1.2],
"ice":[0.9,1.8,1,0.7,1,1.1,2],
"stone":[1,0.9,1.4,1,1.9,0.7,1.6],
"technology":[2,0.4,1.6,1,1.4,0.7,1] 
}

pokemonnames = ['Wallapod-a', 'shelby-s', 'glaze-w', 'spout-t', 'Gambroon-s', 'Wellee-p', 'Rapidash-t', 'Heatran-f', 'stoney-p', 'battera-t', 'doggy-p', 'mushroling-p', 'Flareon-s', 'Quilombo-p', 'Desk-t', 'splashycorn', 'icebird', 'jelly-p', 'Olystail-p', 'Scyther-p', 'Geocrawl-s', 'crisp-f', 'foxy-p', 'stonegolem-s', 'catleaf-p', 'flevilop', 'Volcanion-f', 'Senectitude-t', 'Phantasm-a', 'woofle-i']
import random
pokemons = []

class arena():
    def __init__(self,pk1,pk2):
        self.ani1 = 0
        self.ani2 = 0
        self.pk1 = pk1 # Player
        self.pk2 = pk2 # AI generated
class attack():
    def __init__(self,name,ptype,hp=10,strengthmap=[1,1,1,1,1,1,1],levelr=1,cost=50,auto=False):      
        global powers
        self.name = str(name)
        random.seed(str(name) + str(ptype) + "1028")
        if auto == True:
            levelr = random.randint(0,5)
            cost= random.randint(1,100)
            hp = (levelr * 190 ) + cost      # 2000 hp max health , a attack may only do about a bit less than half damage   
            etp = powers[self.type]
            foundst = False
            avg = 0
            for i in etp:
                avg = avg + 1
            avg = avg / 8
            avg =   avg + (0.4 * levelr)
            sa = 0
            tries = 0
            while not foundst :
                tries = tries + 1
                strengthmap = []
                sa = 0
                for i in etp:
                    x = random.randint(0,0.4 * levelr)
                    sa = sa + x
                    strengthmap.append( x+ i)
                if (sa/8 > (avg - 0.4) and sa < (avg + 0.4)) or (tries > 100):
                    foundst = True
            
        self.force = hp
        self.strength = strengthmap
        self.levelr = levelr
        self.cost = cost
        self.type = ptype
        
        def calc(self,enemy):
            global powers
            tp = powers[self.type]
            idx = ["plant","water","air","fire","ice","stone","technology"].index(enemy.type)
            return (self.force * self.strength[idx])
            

 
random.seed(1)    
pattacks = ["leaf age","jungle fire"," overgrowth","Petal Storm"," Grassy slide","Razor leaf","Seed Flare","Solar Beam","Trailblaze"," photosynthesis"," Magical forest"," flower power"," Vine flow","Bloom Doom","Sun's Energy","wooden bridge","breath of the wild"]
wattacks = ["trillion waves","Dive","tsunami"," wavy blast","Splishy Splash"," Surf","Waterfall ","Whirlpool","Soak","Oceanic Orchester "," symphony of the seas","Odyssea","Hydroflash","bubble beam","bouncy bubble","alure of the sea's"," kraken's dinner","lakeside"]
alienattacks = ["meteorite"," thousand stars"," starfall","moonrise","interstellar"," slimy suprise","ufo attack","endless skyes","world of Illuma","Hyperspeed","infinity and beyond","alienated","free worlds","galactica","supernova","starfield","void","planetary plummet "]
technologyattacks = [" cmatrix "," arch btw ","metal volley","thunder","sparks","short-circuit","gears of freedom ","nerdHack "," master control program"," the hivemind ","plan 9 ","opensource it","GPL-3","out of memory","USENET","gentoo","debugging c++ ","made in germany"] ##sorry but i have to include as many FOSS references as i can
fireattacks = [" Volcano","lava torpedo","magma","firestorm","fusion flare","inferno","mythical fire","greek fire","overheat","Flame wheel","fire blast","Eruption","embers of love","incinerate"]
iceattacks = [" icy peaks"," ice cavern","frost","freeze over"," hypersonic snowball"," below 0*  "," Ice spikes","Snow Fall","Glaciate"," Hail","Avalanche","Blizzard","Ice Shard","Icy Winds","Mist","Chilly reception","Aurora"]
stoneattacks = ["Dig","Drill in","Earthquake","boulder barrage"," Bulldoze","Mythical Ruins"," landslide","thousand stones","stone sworth","stones edge"," stone shards","rockslide","continental crush","Stone throw","Stone Fall","New Gem Cave","Cave in","crystalize","Yosemity","rocky peaks"]
def appendattacks(appendtolist,attacklist,atype):
    for i in attacklist:
        appendtolist.append(attack(i,atype,auto=True))
    return attacklist

allattacks = []
allattacks = appendattacks(allattacks,fireattacks,"fire")
allattacks = appendattacks(allattacks,technologyattacks,"technology")
allattacks = appendattacks(allattacks,pattacks,"plant")
allattacks = appendattacks(allattacks,wattacks,"water")
allattacks = appendattacks(allattacks,alienattacks,"alien")
allattacks = appendattacks(allattacks,stoneattacks,"stone")
allattacks = appendattacks(allattacks,iceattacks,"ice")
            
class pokemon():
    def __init__(self,name,ptype,autogen=True):
        self.name = name
        self.attacks = attacks
        self.type = ptype
        self.bns = []
        for i in range(1,9):
            self.bns.append(random.randint(0,0.2))
        if not autogen == True:
            self.img =  pygame.image.load('img/creatures/'+str(img) + str(i)+'.png')
    def calcdamage(enemy,attack):
        global powers      
        try:
            tp = powers[self.type]
            idx = ["plant","water","air","fire","ice","stone","technology"].index(enemy.type)
            pp = tp[idx] + self.bns[idx]
        except:
            pp = 0.9
        damage = 0
        damage = attack.calc(enemy) * pp
        return damage
    def draw(self,surface,arena,side):
            if side == 1:
                img = pygame.transform.flip(self.img.copy(),True,False)
                screen.blit(img, (50 + arena.ani1, 120))
            else:
                screen.blit(self.img, (190 + arena.ani2, 120))
            
def loadp():
    global pokemonnames, pokemons, allattacks
    for i in pokemonnames:
        ptype = "plant"
        if i.endswith("t"):
            ptype = "technology"
        if i.endswith("i"):
            ptype = "ice"
        if i.endswith("s"):
            ptype = "stone"
        if i.endswith("f"):
            ptype = "fire"
        if i.endswith("a"):
            ptype = "alien"
        if i.endswith("w"):
            ptype = "water"
        handledpokemon = pokemon(i,ptype,True)
        handledpokemon.name = i[:-2]
        handledpokemon.img =  pygame.image.load('img/crt/'+str(i) +'.png')
        handledpokemon.bns = []
        handledpokemon.attacks = []
        t = False
        while t == False:
            for i in allattacks:
                if i.type == ptype:
                    if i.levelr < 2 and random.randint(0,1) == 1:
                        handledpokemon.attacks.append(i)
                        if len(handledpokemon.attacks) > 2:
                            t = True
                        
        pokemons.append(handledpokemon)
def display(surface):
        i = 130
        pygame.draw.polygon(surface,(0,0,0),[(0,0),(i,0),(i + (overlap * 0.5) + 51,Y-height),(0,Y-height)],0)
        pygame.draw.polygon(surface,(255,255,255),[(320,Y-height),(320-i,Y-height),(320-(i + (overlap * 0.5) + 51),0),(320,0)],0)
        pygame.draw.polygon(surface,(55,55,110),[(0,320),(0,Y-(i*0.7692307692307693)),(320,Y-(i*0.7692307692307693)),(320,320)],0)
        pygame.display.flip()    
def transition(surface):
    for i in range(1,130):
        pygame.draw.polygon(surface,(0,0,0),[(0,0),(i,0),(i + (overlap * 0.5) + 51,Y-height),(0,Y-height)],0)
        pygame.draw.polygon(surface,(255,255,255),[(320,Y-height),(320-i,Y-height),(320-(i + (overlap * 0.5) + 51),0),(320,0)],0)
        pygame.draw.polygon(surface,(55,55,110),[(0,320),(0,Y-(i*0.7692307692307693)),(320,Y-(i*0.7692307692307693)),(320,320)],0)
        pygame.display.flip()
        time.sleep(0.01)
        
loadp()