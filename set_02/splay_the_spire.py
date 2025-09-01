import sys

def apply_card(card, atli_hp, enemy_hp, strength, enemy_strength):
    instant_win = False
    if card == "Lay into":
        enemy_hp -= 4 * strength
    elif card == "Power up":
        strength += 2
    elif card == "Whack":
        enemy_hp -= 6
    elif card == "Haymaker":
        enemy_hp -= 10
        atli_hp -= 3
    elif card == "Surpass limits":
        strength *= 2
    elif card == "Dirty tactics":
        enemy_strength -= 2
    elif card == "Bandages":
        atli_hp += 8
    elif card == "Xzodiac":
        if strength > 2 * atli_hp:
            instant_win = True
    return atli_hp, enemy_hp, strength, enemy_strength, instant_win

def simulate(i, atli_hp, enemy_hp, strength, enemy_strength, cards, path):
    # Check win/loss before Atli's move
    if atli_hp <= 0: 
        return None
    if enemy_hp <= 0: 
        return path
    
    if i >= len(cards): 
        return None
    
    card = cards[i]
    a_hp, e_hp, stren, e_str, instant_win = apply_card(card, atli_hp, enemy_hp, strength, enemy_strength)
    new_path = path + [card]

    if instant_win or e_hp <= 0:
        return new_path

    # Enemy attacks if alive
    if e_hp > 0:
        dmg = d + e_str
        if dmg < 0: dmg = 0
        a_hp -= dmg
        if a_hp <= 0:  # Atli dies
            return None

    # Continue recursion
    res = simulate(i + 1, a_hp, e_hp, stren, e_str, cards, new_path)
    if res is not None:
        return res
    
    # Option: skip the card (don’t play it) and move on
    return simulate(i + 1, atli_hp, enemy_hp, strength, enemy_strength, cards, path)

if __name__ == "__main__":
    h_a, h_e, d = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    cards = [sys.stdin.readline().strip() for _ in range(n)]
    
    result = simulate(0, h_a, h_e, 0, 0, cards, [])
    
    if result is None:
        print("Engin vinningsleið!")
    else:
        print(len(result))
        for card in result:
            print(card)
