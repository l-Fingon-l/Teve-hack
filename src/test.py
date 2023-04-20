from tevehack import ProfessionRank, load_smart, save, load, Item, HeroCodeFields

# hero = load('[XE<-ZU3!-hLMg-!LYS-]T&a')
# for i in range(0x34):
#     hero.heroID = i + 1
#     print('-load ' + save(hero))

hero = HeroCodeFields(int1=2, int2=1, food=1, professionLvl = 0, hasFishingRod = 0, professionRank='Never caught a fish',
    revivalLocation=0, imp5Stage=0, int3=1, heroID='Acolyte (Male)', heroXP=0, locationX=0, locationY=0)
print('-load ' + save(hero))
print('-load ' + save(hero, ''))
exit()
# hero = load('3PxA-a)Ek-U*o)-<O7n-vf)T-wA.q-skAO-7V4t-C<Z')
# hero = load('[XE<-ZU3!-hLMg-!LYS-]T&a')
# hero = load_smart(' 3PxA-a)Ek-U*6[-WQnm-d7Qa-yFpU-<PU3-Z5ep-q<C')
# hero = load_smart('   ')
# hero = load('-load Y9..-k_!F-K7_S-U2H5->]t>-9Wz8-Zhj?-xs')
# hero = load('b3R8')
# hero = load('Y8b')
# hero = load('3PxA-a)Ek-U*6[-WQnm-d7Qa-yFpU-<PU3-Z5ep-q<C')
# hero = load('3PxA-a)Ek-U*6[-WQnm234234-d7Qa-yFpU-<PU3-Z5ep-q<C')
# hero = load('123adeqqweqwe$#!@!%$!$#@#*(_*}{')
# hero = load('FkmK-9R88-yu7)-[](_-Hu7e-c!)]-BGA>-#Gaw-<+#[-.]g&-8qYe-WqC!-q!NE-H')
if hero:
    hero.heroXP = 99999999
    hero.locationX = -10000
    hero.locationY = 8000
    # code = save(hero, 'Fingon')
    code = save(hero)
    if code: print('-load ' + code)

hero = load('3PxA-a)Ek-U*6[-WQnm234234-d7Qa-yFpU-<PU3-Z5ep-q<C')
if hero:
    hero.heroXP = 99999999
    hero.locationX = -10000
    hero.locationY = 8000
    code = save(hero, 'Fingon')
    if code: print('-load ' + code)


res = load2('kEF5-2d+d-o2<L-hW<T-R>D?-faQV-wU>U->]Bh-(Q*x-r<)N-TQX')
# res = load2('_kEF5-2d+d-o2<L-hW<T-R>D?----faQV-wU>U->]Bh-(Q*x-r<)N-TQX')
res.gold = 9999999
res.lumber = 300
code2 = save(res, 'Fingon')
if code2: print('-load2 ' + code2)
