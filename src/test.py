from tevehack import ProfessionRank, save, load, save2, load2, Item

hero = load('3PxA-a)Ek-U*6[-WQnm-d7Qa-yFpU-<PU3-Z5ep-q<C')
hero.heroXP = 99999999
hero.locationX = -10000
hero.locationY = 8000
print('-load ' + save(hero, 'Fingon'))

res = load2('kEF5-2d+d-o2<L-hW<T-R>D?-faQV-wU>U->]Bh-(Q*x-r<)N-TQX')
res.gold = 9999999
res.lumber = 300
print('-load2 ' + save2(res, 'Fingon'))
