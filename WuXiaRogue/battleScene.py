from game import Soldier, maximizedWindow
import ctypes
import sys
import os
import keyboard
import time

maximizedWindow()
os.system('cls')
time.sleep(0.5)
dummy = Soldier("JC", 100, 120, 3, 15)
# dummy.displayInfo()
enemy = Soldier("XXX", 110, 50, 2, 10)


class battleInterface:
    def __init__(self):
        self.terminal_width = os.get_terminal_size().columns
        self.terminal_height = os.get_terminal_size().lines
        # print(terminal_width, terminal_height)
    
    def displayEnemy(self, name, maxHealth, maxMana, speed, basicDamage):
        self.name = name
        self.maxHeatlh = maxHealth
        self.maxMana = maxMana
        self.speed = speed
        self.basicDamage = basicDamage

        self.health = maxHealth
        self.mana = maxMana
        print('\n'*(self.terminal_height//6))
        print(' '*(self.terminal_width*5//6-len(self.name)), self.name)
        print(' '*(self.terminal_width*5//6-len(self.name)-20), "Health:", self.health, '\\', self.maxHeatlh)
        print(' '*(self.terminal_width*5//6-len(self.name)-20), "Mana  :", self.mana, '\\', self.maxMana)

    def displaySelf(self, name, maxHealth, maxMana, speed, basicDamage):
        self.name = name
        self.maxHeatlh = maxHealth
        self.maxMana = maxMana
        self.speed = speed
        self.basicDamage = basicDamage

        self.health = maxHealth
        self.mana = maxMana
        print('\n'*(self.terminal_height//6))
        print(' '*(self.terminal_width//6), self.name)
        print(' '*(self.terminal_width//6+len(self.name)+3), "Health:", self.health, '\\', self.maxHeatlh)
        print(' '*(self.terminal_width//6+len(self.name)+3), "Mana  :", self.mana, '\\', self.maxMana)
    
    def displayChoice(self, cursor):
        self.cursor = cursor
        print(' '*(self.terminal_width//6), '-'*(self.terminal_width*2//3), ' '*(self.terminal_width//6))
        choice = ["A: Attack", "I: Items", "S: Switch", "E: Escape"]
        
        print(' '*(self.terminal_width//6), '\t', end="")
        for i in range(len(choice)):
            print(self.cursor[i], choice[i], '\t'*2, end="")
        print('\n')
    
    def attackInfo(self, cursor, att:list, show=False):
        if show:
            self.att = att
            self.cursor = cursor
            print(' '*(self.terminal_width//6), '-'*(self.terminal_width*2//3), ' '*(self.terminal_width//6))
            print(' '*(self.terminal_width//6), '\t', end="")
            for i in range(len(self.att)):
                print(self.cursor[i], self.att[i], '\t'*2, end="")
            print('\n')

        else:
            pass
    
    def itemInfo(self, cursor, item:list, show=False):
        if show:
            self.item = item
            self.cursor = cursor
            x = 0
            print(' '*(self.terminal_width//6), '-'*(self.terminal_width*2//3), ' '*(self.terminal_width//6))
            while 4*x < len(self.item):
                if 4*x+4 < len(self.item):
                    lastItm = 4*x+4
                else:
                    lastItm = len(self.item)
                print(' '*(self.terminal_width//6), '\t'*2, end="")
                for i in range(4*x, lastItm):
                    print(self.cursor[i], self.item[i], '\t'*2, end="")
                print('\n')
                x += 1
            

def returnCursor(x):
    global csr, csrCount, attCsr, attCsrCount, attShow, itmCsr, itmCsrCount, itmShow, switchShow
    if x == 'right' and csrCount<3 and not max(attShow, itmShow, switchShow):
        csrCount += 1
        for i in range(4):
            csr[i] = ' '
        csr[csrCount] = '~>'

    elif x == 'left' and csrCount>0 and not max(attShow, itmShow, switchShow):
        csrCount -= 1
        for i in range(4):
            csr[i] = ' '
        csr[csrCount] = '~>'
        
    elif x == 'right' and attCsrCount<3 and attShow:
        attCsrCount += 1
        for i in range(4):
            attCsr[i] = ' '
        attCsr[attCsrCount] = '~>'

    elif x == 'left' and attCsrCount>0 and attShow:
        attCsrCount -= 1
        for i in range(4):
            attCsr[i] = ' '
        attCsr[attCsrCount] = '~>'

    elif x == 'right' and itmCsrCount<len(itmCsr)-1 and itmShow:
        itmCsr[itmCsrCount] = ' '
        itmCsrCount += 1
        itmCsr[itmCsrCount] = '~>'

    elif x == 'left' and itmCsrCount>0 and itmShow:
        itmCsr[itmCsrCount] = ' '
        itmCsrCount -= 1
        itmCsr[itmCsrCount] = '~>'

    elif x == 'down' and itmCsrCount<len(itmCsr)-1 and itmShow:
        itmCsr[itmCsrCount] = ' '
        if itmCsrCount+4 <= len(itmCsr)-1:
            itmCsrCount += 4
            itmCsr[itmCsrCount] = '~>'
        else:
            itmCsrCount = len(itmCsr)-1
            itmCsr[itmCsrCount] = '~>'

    elif x == 'up' and itmCsrCount>0 and itmShow:
        itmCsr[itmCsrCount] = ' '
        if itmCsrCount-4 >= 0:
            itmCsrCount -= 4
            itmCsr[itmCsrCount] = '~>'
        else:
            itmCsrCount = 0
            itmCsr[itmCsrCount] = '~>'
    
    if x == 'z':
        if csrCount == 0:
            attShow = True
        if csrCount == 1:
            itmShow = True
        if csrCount == 2:
            switchShow = True
        if csrCount == 3:
            pass
    if x == 'x':
        attShow, itmShow, switchShow = False, False, False


scene = battleInterface()
csrCount = 0
csr = ['~>', ' ', ' ', ' ']
attCsrCount = 0
attCsr = ['~>', ' ', ' ', ' ']
itmCsrCount = 0
# itmCsrCount2 = 0
itmCsr = []
lastLst = []
itm = ['apple', 'banana', 'sword', 'knife', 'bow', 'arrow', 'sniper', 'jingshi', 'yupei', 'xianglian', 'ababa', 'aaa', 'sadasd']
for i in range(len(itm)):
    itmCsr.append(' ')
itmCsr[0] = '~>'
#  for i in range(len(itm)//4):
#     itmCsr.append([' ', ' ', ' ', ' '])
#     itmCsr[0][0] = '~>'
# if len(itm)%4:
#     for j in range(len(itm)%4):
#         lastLst.append(' ')
#     itmCsr.append(lastLst)

attShow, itmShow, switchShow = False, False, False


while True:
    os.system('cls')
    scene.displayEnemy("WuDang Disciple", 110, 50, 2, 10)
    scene.displaySelf("TaoHua Disciple", 100, 100, 3, 15)
    scene.displayChoice(csr)
    scene.attackInfo(attCsr, ["QiShangQuan", "XiangLongShiBaZhang", "JiuYinBaiGuZhua", "TieShaZhang"], attShow)
    scene.itemInfo(itmCsr, itm, itmShow)
    # print(x)
    x = keyboard.read_key()
    time.sleep(0.2)
    returnCursor(x)
