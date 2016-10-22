def jie(e, n):
    cipher_len = len(e)
    y = ''
    for k in range(n):
        cipher_len = len(e)
        j = 1
        for i in range(0, cipher_len, n - k):
            y += e[i]
        for i in range(0, cipher_len, n - k):
            e = e[:i + j - 1] + e[i + j:]
            j -= 1
    print y


e = 'ahseoni aw ef arbuoasohestp, t mlrnpa aapitoptwsiiy ha, mp  sne s epeaptlrneltydwsehav.y atoat isiahorleplfnelwepmneuoereg nydrotdealcisedwrcpec ueaaohe r ehwtpau  eaerstirded sie aa l ss artcirgyaah o el etya t  ondf es glc u y t pilcis  nmn lohapmnsaegae e afcnmghlr mgestrneret,ta sifaes tpaslhsyfhhaesc nal toaide rcicre nh esd ee  ii ali  pbhssyop,cdetyi,eltecoaveo msmr rito, ans snaap   eete,hjssnpnoat criehorsmcrdii hly   tpncmgmpetaitn  lcyr.sleafspecr  csiewuog smeu shfeassigetaap maceioe alhaeus mc.cran egeeeestee te sd rt eiaomont.coh s e p easdtaboslfhsrni.galcisro aot, imdhotmmn ctarletipfh hem  a cyewhgseddseepso tel ot  b.yslhwublseo  u ado, thoiscrepleais rgiei wufrogreeoe hmdhsmbaapa s mrtut itoakomvitwety lst  rnniomrdhslhaodeccrcmn ecsc eahi  sca s,rt hs sidtp o elrrnmeryt rgycicraecrt  oluw eoettts elaap anabft ame arhpeidehroy  ce ew   vrbei r ny l.ecs u tdacoapebay  s eesylpdpsalcr l ceewp henuydnp t in taesoar essnooeeeewuesltpciseeesitpentsmeet l hsifiosaecasmeo  s errvdha teicrh,htn ipim olas etoesaut roftlre sdes  eiyr,lci   i  uhrlt fnr  ,ouin,slhot le earpnbn  lcceseeb mb scrhmtneelsaa to do rh ctohilhgne intmcicrre  e lusia newrdinhw   l .yhhhon manrerntsts gpn  . es scohlccs ncbohxlt,esnhkeoett,nousqyl.esuwcicreea alercci i  himn'
elen = len(e)
l = []
for i in range(2, elen):
    if (elen % i == 0):
        l.append(i)
for n in l:
    jie(e, n)
while 1:
    n = input('Col:')
    jie(e, n)
