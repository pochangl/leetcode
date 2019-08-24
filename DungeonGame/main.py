

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        goal = (len(dungeon) - 1, len(dungeon[0]) - 1)

        def minimal_damage(x, y):
            if (x, y) == goal:
                return dungeon[x][y]
            elif x == goal[x]:
                return minimal_damage(x, y + 1)
            elif y == goal[y]:
                return minimal_damage(x + 1, y)
            return max(
                minimal_damage(x, y + 1),
                minimal_damage(x + 1, y)
            )

        return max([1, 1 - minimal_damage(0, 0)])
