import time
from add import add
from sub import subtract_non_negative
from multi import multi
from div import div

print("=== ⚔️ 미니 RPG 전투 시뮬레이터 ⚔️ ===")
hp = 100
base_atk = 15

# 1. 장비 장착 (add 활용)
weapon_bonus = 10
total_atk = add(base_atk, weapon_bonus)
print(f"🗡️ 무기 장착! 공격력이 {total_atk}이 되었습니다.")

# 2. 버프 중첩 공격 (multi의 가변 인자 활용)
crit_damage = multi(total_atk, 2, 1.5)  # 기본공격력 * 치명타(2배) * 속성강화(1.5배)
print(f"💥 치명타 + 속성 버프 발동! 총 데미지: {crit_damage}")

# 3. 몬스터 피격 및 방어 (subtract_non_negative 활용 - 오버킬 방지)
monster_hp = 60
monster_hp = subtract_non_negative(monster_hp, crit_damage)
print(f"👾 몬스터 남은 HP: {monster_hp} (0 미만으로 떨어지지 않음!)")

# 4. 경험치 분배 (div 활용)
total_exp = 500
party_members = 4
exp_per_member = div(total_exp, party_members)
print(f"🎉 전투 승리! 파티원 {party_members}명이 각각 경험치 {exp_per_member}씩 획득했습니다.")