skill = """1.碧凝神爪"""

clean = skill.split('\n')
imt = []
fnl = []
for j in clean:
    imt += j.split(' ')
for k in imt:
    fnl += k.split('.')
file = open("tiandihui.txt", 'a', encoding="utf-8")
for l in range(len(fnl)//2):
    # pass
    file.write(fnl[2*l+1]+'\n')
file.close()
# print(fnl)