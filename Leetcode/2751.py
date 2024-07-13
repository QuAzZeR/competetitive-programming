from typing import List
import unittest


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)
        robots = [
            {
                "position": positions[i],
                "health": healths[i],
                "direction": directions[i],
                "index": i,
            }
            for i in range(n)
        ]
        robots.sort(key=lambda x: x["position"])
        s = []
        for robot in robots:
            if robot["direction"] == "R" or not s or s[-1]["direction"] == "L":
                s.append(robot)
                continue
            if robot["direction"] == "L":
                is_added = True
                while s and s[-1]["direction"] == "R" and is_added:
                    h = s[-1]["health"]
                    if robot["health"] > h:
                        s.pop()
                        robot["health"] -= 1
                    elif robot["health"] < h:
                        s[-1]["health"] -= 1
                        is_added = False
                    else:
                        s.pop()
                        is_added = False
                if is_added:
                    s.append(robot)

        return [robot["health"] for robot in sorted(s, key=lambda x: x["index"])]


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(
            s.survivedRobotsHealths(
                positions=[5, 4, 3, 2, 1],
                healths=[2, 17, 9, 15, 10],
                directions="RRRRR",
            ),
            [2, 17, 9, 15, 10],
        )
        self.assertEqual(
            s.survivedRobotsHealths(
                positions=[3, 5, 2, 6], healths=[10, 10, 15, 12], directions="RLRL"
            ),
            [14],
        )
        self.assertEqual(
            s.survivedRobotsHealths(
                positions=[1, 2, 5, 6], healths=[10, 10, 11, 11], directions="RLRL"
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()
