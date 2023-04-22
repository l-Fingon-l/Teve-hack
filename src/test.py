from tevehack import ProfessionRank, save, load, load_file, Item, HeroCodeFields, ItemCodeFields, print_code, load_item_code

# hero = load('[XE<-ZU3!-hLMg-!LYS-]T&a')
# for i in range(0x34):
#     hero.heroID = i + 1
#     print('-load ' + save(hero))
# load_item_code('ZRhL-?Jf)-77<5-?PO>-4]bk-,*L<-jFp?-JkKg-X7Wz-,pn]-Pagk')
# load_item_code(save(ItemCodeFields(gold=1, shards=0, pvpPoints=0, unlockedCritterTiers=0, numberOfItems=0)))
# ItemCode = ItemCodeFields(gold=1, shards=0, pvpPoints=0, unlockedCritterTiers=0, numberOfItems=0)
# save(ItemCode)

hero = load_file(
    '''
function PreloadFiles takes nothing returns nothing

	call PreloadStart()
	call Preload( "MAP: Twilight's Eve R4" )
	call Preload( "Brought to you by Donach#6231 and KryptonRazer#3935, developers for new Teve Community!" )
	call Preload( "Join us at discord.tever.xyz and visit tever.xyz" )
	call Preload( "Version: Teve_R4.18.4" )
	call Preload( "Recommended Wc3 Version: 1.33.0.19378 (classic)" )
	call Preload( "Player Name: KawerOrda" )
	call Preload( "   " )
	call Preload( "Hero: ArchTemplar [Lv.99]" )
	call Preload( "Load Type: Hero" )
	call Preload( "-load g!4E-C&9+-hR7Q-k6[A-C7MC-kVte-mQ" )
	call Preload( "PvP rank: None (Points: 0)" )
	call Preload( "Fishing profession: Master Fisherman (Points: 4)" )
	call Preload( "Imp5 Stage Finished: 0" )
	call Preload( "   " )
	call Preload( "Load Type: Item" )
	call Preload( "-load2 ZRhL-?Jf)-77<5-?PO>-4]bk-,*L<-jFp?-JkKg-X7Wz-,pn]-Pagk" )
	call Preload( "Gold: 284   Shards: 0" )
	call Preload( "Unlocked Critter Tiers: none" )
	call Preload( "Items Worn by Hero: " )
	call Preload( "Items in Stash: " )
	call Preload( "        " )
	call PreloadEnd( 1230815.1 )

endfunction

'''
)

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
