

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        width = len(dungeon)
        height = len(dungeon[0])
        goal = (width - 1, height - 1)

        def minimal_damage(x, y):
            base = dungeon[x][y]
            if (x, y) == goal:
                return base
            elif x == goal[0]:
                value = minimal_damage(x, y + 1)
            elif y == goal[1]:
                value = minimal_damage(x + 1, y)
            else:
                value = max(
                    minimal_damage(x, y + 1),
                    minimal_damage(x + 1, y)
                )
            return base + min(0, value)
        return max([1, 1 - minimal_damage(0, 0)])
