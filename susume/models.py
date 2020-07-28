from django.db import models

# Create your models here.

class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, default='Cornelia')
    server = models.CharField(max_length=200, default='Server')

    def __str__(self):
        return self.en

     
class Server(models.Model):
    id = models.IntegerField(primary_key=True)
    en = models.CharField(max_length=255, default='Bahamut')
    
    def __str__(self):
        return self.en
##############################
# Meta Class. willnot create a table
##############################
class Item(models.Model):
    #{"id", "en", "ja", "enl", "jal", "category", "flags", "stack", "targets", "type", "cast_time", "jobs", "level", "races", "slots", "cast_delay", "max_charges", "recast_delay", "shield_size", "damage", "delay", "skill", "item_level", "superior_level"}
    #[16555] = {id=16555,en="Ridill",ja="リディル",enl="Ridill",jal="リディル",category="Weapon",damage=40,delay=236,flags=59508,jobs=6978,level=70,races=510,skill=3,slots=3,stack=1,targets=0,type=4},

    id = models.IntegerField(primary_key=True)
    en = models.CharField(max_length=255, default='Gil')

    ja = models.CharField(max_length=200, default='ギル')
    enl = models.CharField(max_length=255, default='Gil')
    jal = models.CharField(max_length=255, default='ギル')

    category = models.CharField(max_length=200,default='General')
    flags = models.IntegerField(default=0)
    stack = models.IntegerField(default=1)
    targets = models.IntegerField(default=1)
    item_type = models.IntegerField(default=1)
    cast_time = models.IntegerField(default=0)
    jobs = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    races = models.IntegerField(default=1)
    slots = models.IntegerField(default=1)

    cast_delay = models.IntegerField(default=0)
    max_charges = models.IntegerField(default=1)
    recast_delay = models.IntegerField(default=0)
    shield_size = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    delay = models.IntegerField(default=0)
    skill = models.IntegerField(default=1)
    item_level = models.IntegerField(default=1)
    superior_level = models.IntegerField(default=1)

    #desc_en = models.CharField(max_length=255, default='Money')
    #desc_ja = models.CharField(max_length=255, default='Money')
    
    desc_en = models.TextField(blank=True)
    desc_ja = models.TextField(blank=True)

    def __str__(self):
        return self.en

    class Meta:
        abstract = True
    pass

class Equipment(Item):
    #question_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    #votes = models.IntegerField(default=0)
    equipment_type = models.CharField(max_length=200,default='EquipmentType')

    pass

class AugmentedEquipment(Item):
    #question_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    #votes = models.IntegerField(default=0)

    pass

##############################

class Job(models.Model):
    #    [0] = {id=0,en="None",ja="なし",ens="NON",jas=""},
    #    [1] = {id=1,en="Warrior",ja="戦士",ens="WAR",jas="戦"},

    id = models.IntegerField(primary_key=True)
    en = models.CharField(max_length=200, default='None')
    ja = models.CharField(max_length=200, default='なし')
    ens = models.CharField(max_length=200, default='NON')
    jas = models.CharField(max_length=200, blank=True, null=True, default='')


    def __str__(self):
        return self.en
        
class Slot(models.Model):
    id = models.IntegerField(primary_key=True)
    en = models.CharField(max_length=200, default='Main')
    
    def __str__(self):
        return self.en
class Inventory(models.Model):
    pass

##############################

class Ability(models.Model):
    #{"id", "en", "ja", "duration", "element", "icon_id", "mp_cost", "prefix", "range", "recast_id", "targets", "tp_cost", "type"}
    #[35] = {id=35,en="Provoke",ja="挑発",element=1,icon_id=360,mp_cost=0,prefix="/jobability",range=11,recast_id=5,targets=32,tp_cost=0,type="JobAbility"},
    #[16] = {id=16,en="Mighty Strikes",ja="マイティストライク",duration=45,element=0,icon_id=66,mp_cost=0,prefix="/jobability",range=0,recast_id=0,targets=1,tp_cost=0,type="JobAbility"},

    id = models.IntegerField(primary_key=True)
    en = models.CharField(max_length=200, default='Provoke')

    ja = models.CharField(max_length=200, default='挑発')
    duration = models.IntegerField(default=0)
    element = models.IntegerField(default=0)
    icon_id = models.IntegerField(default=0)
    mp_cost = models.IntegerField(default=0)
    prefix = models.CharField(max_length=200,default='/jobability')
    ability_range = models.IntegerField(default=0)
    recast_id = models.IntegerField(default=0)
    targets = models.IntegerField(default=1)
    tp_cost = models.IntegerField(default=0)
    ability_type = models.CharField(max_length=200,default='JobAbility')

    def __str__(self):
        return self.en

class Weaponskill(models.Model):
    #{"id", "en", "ja", "element", "icon_id", "prefix", "range", "skill", "skillchain_a", "skillchain_b", "skillchain_c", "targets"}
    #[1] = {id=1,en="Combo",ja="コンボ",element=6,icon_id=590,prefix="/weaponskill",range=2,skill=1,skillchain_a="Impaction",skillchain_b="",skillchain_c="",targets=32},

    id = models.IntegerField(primary_key=True)
    en = models.CharField(max_length=200, default='Combo')

    ja = models.CharField(max_length=200, default='コンボ')
    element = models.IntegerField(default=0)
    icon_id = models.IntegerField(default=0)
    prefix = models.CharField(max_length=200,default='/weaponskill')
    ws_range = models.IntegerField(default=0)
    skill = models.IntegerField(default=0)
    targets = models.IntegerField(default=1)
    skillchain_a = models.CharField(max_length=200,default='')
    skillchain_b = models.CharField(max_length=200,default='')
    skillchain_c = models.CharField(max_length=200,default='')
    
    def __str__(self):
        return self.en
class Spell(models.Model):
    #[1] = {id=1,en="Cure",ja="ケアル",cast_time=2,element=6,icon_id=86,icon_id_nq=6,levels={[3]=1,[5]=3,[7]=5,[20]=5},mp_cost=8,prefix="/magic",range=12,recast=5,recast_id=1,requirements=1,skill=33,targets=63,type="WhiteMagic"},
    #{"id", "en", "ja", "cast_time", "element", "icon_id", "icon_id_nq", "levels", "mp_cost", "prefix", "range", "recast", "recast_id", "requirements", "skill", "targets", "type", "duration", "status", "overwrites", "unlearnable"}

    id = models.IntegerField(primary_key=True)
    en = models.CharField(max_length=200, default='Cure')
    ja = models.CharField(max_length=200, default='ケアル')
    cast_time = models.DecimalField(default=0,decimal_places=2,max_digits=5)
    element = models.IntegerField(default=0)
    icon_id = models.IntegerField(default=0)
    icon_id_nq= models.IntegerField(default=0)
    #levels
    mp_cost = models.IntegerField(default=1)
    prefix = models.CharField(max_length=200,default='/magic')
    spell_range = models.IntegerField(default=0)
    recast = models.DecimalField(default=1,decimal_places=2,max_digits=5)
    recast_id = models.IntegerField(default=0)
    requirements = models.IntegerField(default=0)
    skill = models.IntegerField(default=1)
    targets = models.IntegerField(default=1)
    spell_type = models.CharField(max_length=200,default='WhiteMagic')
    duration = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    #overwrites
    unlearnable = models.BooleanField(default=False)
    
    def __str__(self):
        return self.en
##############################

class Loadout(models.Model):
    pass