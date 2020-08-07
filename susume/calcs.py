
def calc_magic_damage(d=1,mtdr=1,staff=1,affinity=1,sdt=0,resist=0,mb=0,mbb=1,day=1,weather=1,mabmdb=1,tmda=1,potency=1):
    # Damage Dealt = D × MTDR × Staff × Affinity × SDT × Resist × MB × MBB × Day & Weather × MAB/MDB × TMDA × Potency Multipliers

    #D: INT-adjusted base spell damage
    #MTDR: Multiple-Target Damage Reduction (for area of effect spells)
    #Staff: Elemental staff hidden damage bonus multiplier
    #Affinity: Elemental affinity damage bonus muliplier (from staff and/or atma/atmacite)
    #SDT: Species Damage Taken
    #Resist: Reduction of spell damage due to resist states.
    #MB: Magic Burst
    #MBB: Magic Burst Bonus
    #Day & Weather: Day and Weather multipliers, including Iridescence and equipment modifiers
    #MAB / MDB: Caster Magic Attack Bonus factor divided by target's Magic Defense Bonus factor
    #TMDA: Target Magic Damage Adjustment (Magic Damage Taken reduction)
    #Potency Multipliers: e.g. Ebullience, Klimaform Bonus, Goetia +2 Set Bonus, etc.
    if sdt == 0: sdt = 1
    if resist == 0: resist = 1
    if mb == 0: mb = 1
    return(d * mtdr * staff * affinity * sdt * resist * mb * mbb * day * weather * mabmdb * tmda * potency)

def calc_magic_d(mdmg=1,v=0,dint=1,m=0):
    # D = mDMG + V + (dINT × M)

    #V: Every individual damage-dealing magic spell has a base damage value denoted as V.
    #dINT: dINT represents the difference between caster and target INT: (Caster's INT - Target's INT).
    #M: Every individual damage-dealing magic spell has several INT multiplier values denoted as M for different dINT ranges.
    #Note: For offensive white magic, substitute dMND for dINT (Caster's MND - Target's MND)
    #mDMG: mDMG represents the "Magic Damage" statistic obtained from equipped weapons and armor.
    #D: INT and "Magic Damage" adjusted base spell damage calculated from the terms above.
    m,v = lookup_dint_mv(dint)
    print("d: mdmg {} v {} dint {} m {}".
        format(mdmg,v,dint,m))
    return(mdmg + v + (dint-v * m))
def lookup_dint_mv(dint=1):
    if dint > 0 and dint <= 49:
        return 2,10 # stone1
    elif dint > 49 and dint <= 99:
        return 1,110 # stone1
    elif dint > 99 and dint <= 199:
        return 0,160 # stone1
    elif dint > 199:
        return 0,160 # stone1 has no 200+ tier
    else:
        return -1

def calc_phys_damage():
    #Physical Damage = Base Damage * pDIF
    #Critical ranged pDIF = Normal Ranged pDIF × 1.25

    #For normal attack: Base Damage = D + (aD) + fSTR
    #For weapon skill: Base Damage = floor((D + (aD) + fSTR + WSC)* fTP)
    # THF #
    #base damage on a Sneak Attacked normal hit is calculated as Base Damage = floor(D + fSTR) + Total DEX.
    #base damage on a Trick Attacked normal hit is calculated as Base Damage = floor(D + fSTR) + Total AGI
    #base damage on a Sneak Attacked weapon skill is calculated as Base Damage = floor((D + fSTR + WSC)* fTP) + Total DEX
    #base damage on a Trick Attacked weapon skill is calculated as Base Damage = floor((D + fSTR + WSC)* fTP) + Total AGI

    pass

print(calc_magic_damage(mabmdb=10))
print(calc_magic_d(dint=100))