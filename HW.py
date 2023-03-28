import random


class Character:

    def __init__(self, name, hp, mp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.mp = mp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def magic_attack(self, other):
        damage = random.randint(self.power*2 - 2, self.power*2 + 2)
        if self.mp <= 0:
            print("mp가 없어서 가만히 있었다.")
            return True
        self.mp = max(self.mp - 3, 0)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 마법 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} MP {self.mp}")


class Monster:

    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


Character_name = input("플레이어의 이름을 입력하세요\n")
character = Character(Character_name, hp=100, mp=40, power=10)

monster = {
    Monster("언데드 아처", hp=50, power=7),
    Monster("언데드 워리어", hp=80, power=7),
    Monster("언데드 나이트", hp=100, power=7)
}


mon_select = input("누구와 싸우시겠습니까?\n 1. 언데드 아처, 2. 언데드 워리어, 3.언데드 나이트\n")
print(type(mon_select))
if mon_select == "1":
    undead_acher = Monster("언데드 아처", hp=50, power=7)
    print(f'{undead_acher.name}가 나타남')
    while True:
        character.show_status()
        undead_acher.show_status()
        atk_type = input("무엇을 할 것인가?\n 1. 일반공격 2. 마법공격\n")
        if atk_type == "1":
            character.attack(other=undead_acher)
            undead_acher.attack(other=character)
            character.show_status()
            undead_acher.show_status()
        elif atk_type == "2":
            character.magic_attack(other=undead_acher)
            undead_acher.attack(other=character)
            character.show_status()
            undead_acher.show_status()
        if character.hp <= 0:
            print("당신은 죽었습니다.")
            break
        elif undead_acher.hp <= 0:
            print("승리하셨습니다.")
            break

if mon_select == "2":
    undead_warrior = Monster("언데드 워리어", hp=80, power=7)
    print(f'{undead_warrior.name}가 나타남')
    while True:
        character.show_status()
        undead_warrior.show_status()
        atk_type = input("무엇을 할 것인가?\n 1. 일반공격 2. 마법공격\n")
        if atk_type == "1":
            character.attack(other=undead_warrior)
            undead_warrior.attack(other=character)
            character.show_status()
            undead_warrior.show_status()
        elif atk_type == "2":
            character.magic_attack(other=undead_warrior)
            undead_warrior.attack(other=character)
            character.show_status()
            undead_warrior.show_status()
        if character.hp <= 0:
            print("당신은 죽었습니다.")
            break
        elif undead_warrior.hp <= 0:
            print("승리하셨습니다.")
            break

if mon_select == "3":
    undead_knight = Monster("언데드 나이트", hp=100, power=7)
    print(f'{undead_knight.name}가 나타남')
    while True:
        character.show_status()
        undead_knight.show_status()
        atk_type = input("무엇을 할 것인가?\n 1. 일반공격 2. 마법공격\n")
        if atk_type == "1":
            character.attack(other=undead_knight)
            undead_knight.attack(other=character)
            character.show_status()
            undead_knight.show_status()
        elif atk_type == "2":
            character.magic_attack(other=undead_knight)
            undead_knight.attack(other=character)
            character.show_status()
            undead_knight.show_status()
        if character.hp <= 0:
            print("당신은 죽었습니다.")
            break
        elif undead_knight.hp <= 0:
            print("승리하셨습니다.")
            break
