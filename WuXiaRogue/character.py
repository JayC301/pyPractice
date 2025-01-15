from mainMenu import *
class Soldier:
    def __init__(self, name, maxHealth, maxMana, speed, basicDamage, armor):
        self.name = name
        self.maxHealth = maxHealth
        self.oriMaxHealth = maxHealth
        self.maxMana = maxMana
        self.oriMaxMana = maxMana
        self.speed = speed
        self.orispeed = speed
        self.basicDamage = basicDamage
        self.oriBasicDamage = basicDamage
        self.armor = armor
        self.oriArmor = armor
        
        self.level = 1
        self.nextLevelExp = 300
        self.exp = 0

    def adjustStatus(self, changeStatus:list): #list from the equipment dictionary
        # [name, armorValue, damageIncrement, healthIncrement, manaIncrement, speedChange, specialEffects...]
        for i in changeStatus:
            if len(i) > 0:
                self.maxHealth += i[3]
                self.maxMana += i[4]
                self.speed += i[5]
                self.basicDamage += i[2]
                self.armor += i[1]
    
    def clearEquipmentEffect(self):
        self.maxHealth = self.oriMaxHealth
        self.maxMana = self.oriMaxMana
        self.speed = self.orispeed
        self.basicDamage = self.oriBasicDamage
        self.armor = self.oriArmor

    def levelUp(self):
        self.oriMaxHealth += 10
        self.oriMaxMana += 10
        self.orispeed += 1
        self.oriBasicDamage += 5
        self.oriArmor += 1

        self.level += 1
        self.nextLevelExp *= 2
        self.exp = 0
    
    def gainExp(self, exp):
        self.exp += exp
        if self.exp >= self.nextLevelExp:
            self.levelUp()


    def displayInfo(self):
        centralizedText(f"I am {self.name}, {self.maxHealth} HP, {self.maxMana} MP, {self.speed} speed, {self.basicDamage} damage")
    
class bag:
    def __init__(self, item, equipment, skill):
        self.item = item
        self.equipment = equipment
        self.skill = skill

    def displayInfo(self):
        print(f'item list {self.item} \nequipment {self.equipment} \nskill {self.skill}')
        # print(self.equipment['helmet'][0])

    def adjustItem(self, itemName, use=True):
        if use: #use item
            self.item[itemName] -= 1
            if self.item[itemName] == 0:
                self.item.pop(itemName)
        # has to make sure item number must be greater than 0 while displaying item
        # remove 0 item from dictionary
        else: #obtain item
            if itemName in self.item:
                self.item[itemName] += 1
            else:
                self.item[itemName] = 1

    def adjustEquipment(self, part, stats): #part indicates equipment dict keys; stats indicate equipment dict values
        #this code will remove original equipment and replace it with new equipment
        self.equipment[part] = stats
        
    def adjustSkill(self, selectedSkill, replacedSkill, replacedSkillStats):
        # remember not to allow user to put on the same skill. 
        # Check if selectedSkill is same as replacedSkill.
        # Or, remove selectedSkill from learntSkill. Add back selectedSkill while choosing replacedSkill (No redundant choice between skill and learntSkill)
        self.skill.pop(selectedSkill)
        self.skill[replacedSkill] = replacedSkillStats
        pass

item = {'ZhiXueSan':5, 'FeiBiao':10, 'TongQian':100}
# for listed values in equipment[name, armorValue, damageIncrement, healthIncrement, manaIncrement, speedChange, specialEffects...]
equipment = {'weapon':['TaoHuaJian', 0, 10, 0, 0, -2], 'helmet':['BuMao', 1, 0, 5, 0, 0], 'armor':['BuYi', 2, 0, 20, 0, 0],
             'boot':['BuXie', 1, 0, 5, 0, 1], 'ascrs1':[], 'ascrs2':[]}

# learntSkill must be more than skill
learntSkill = {'QiShangQuan':[1, 0, 15, 10], 'KongMingQuan':[1, 0, 20, 12], 'JingGangQuan':[1, 0, 20, 5]}
# skill always display maximum 4 only (chosen from learntSkill)
# for listed values in skill[level, numberofUses, damageDealt, manaNeeded, skillEffects]
skill = {'HuiQUan':[1, 0, 15, 0], 'ZhangJi':[1, 0, 10, 0], 'HengTi':[1, 0, 18, 0], 'ZhenQiQuan':[1, 0, 25, 0]}

dummy = Soldier("JC", 100, 120, 3, 15, 0)
dummyBag = bag(item, equipment, skill)
dummy.adjustStatus(dummyBag.equipment.values())
dummy.displayInfo()
# print(dummyBag.equipment.values())