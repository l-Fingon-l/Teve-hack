from tevehack import ProfessionRank, save, load, save2, load2

# res = load('Y9..-vAKu-Rgj)-t4UD-eszA-Y&_t-DFf[-8J')
# print(res)
# print(load2('Sxwy-yrpD-FLaC-6H9[-!K2z-doZh-mRDy-B89d-Yt7s-+(QM-fDZA'))

# load('F(W2-ZPr(->NNK-vkvB-.<pF-wAVc-at4X-(wUJ-dnO')
# load2('ofa<-B.2s-MdWB-L]AZ-!cSz-s3ho-RKJo-!y5V-M6..-(AU9-cL*')

# load('F(W2-ZPr(->NNK-vkvB-.<pF-wAVc-at4X-(wUJ-dnO')
# load2('ofa<-B.2s-MdWB-L]AZ-!cSz-s3ho-RKJo-!y5V-M6..-(AU9-cL*')

# load('F(W2-ZPr(->NNK-vkvB-bjBC-WZxq-ORYw-Eat9-yt#')
# load2('ofa<-B._q-HchM-FAzN-Q9wM-v[th-E4b5-*AS+-FQ!j-*MTH-TbM')

# load('F(W2-ZPr(->NNK-vkvB-&kvJ-BR]6-c!vP-ug(#-w]E')

hero = load('3PxA-a)Ek-U*o)-<O7n-vf)T-wA.q-skAO-7V4t-C<Z')
hero.heroXP *= 20
hero.professionLvl *= 3
hero.professionRank = ProfessionRank[5]
print('-load ' + save(hero))

res = load2('ofa<-BTqm-(3kO-o)nK-ENaC-B7<E-2<rB-DMj7-_[Vk-j5y5-f9(')
res.gold = 999999
res.lumber = 200
print('-load2 ' + save2(res))
