

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        goal = (len(dungeon) - 1, len(dungeon[0]) - 1)

        def minimal_damage(x, y, hp):
            hp += dungeon[x][y]
            if (x, y) == goal:
                return hp
            elif x == goal[0]:
                value = minimal_damage(x, y + 1, hp)
            elif y == goal[1]:
                value = minimal_damage(x + 1, y, hp)
            else:
                value = max(
                    minimal_damage(x, y + 1, hp),
                    minimal_damage(x + 1, y, hp)
                )
            return min(hp, value)
        return max([1, 1 - minimal_damage(0, 0, 0)])
