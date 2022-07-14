class Fight:

    # this method takes in two knights as attacker and defender and returns the same two knights as winner and loser
    # after fight between them
    @staticmethod
    def fight(attacker, defender):
        attacker_score = attacker.attack + 0.5
        defender_score = defender.defence
        if attacker.item:
            attacker_score += attacker.item.attack
        if defender.item:
            defender_score += defender.item.defence
        return (attacker, defender) if attacker_score > defender_score else (defender, attacker)
