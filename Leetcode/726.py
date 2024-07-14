import unittest


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        s = [{}]
        i = 0
        while i < n:
            if formula[i] == "(":
                s.append({})
                i += 1
            elif formula[i] == ")":
                t = s.pop()
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                m = int(formula[start:i] or 1)
                for e, c in t.items():
                    s[-1][e] = s[-1].get(e, 0) + c * m
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                e = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                c = int(formula[start:i] or 1)
                s[-1][e] = s[-1].get(e, 0) + int(c)
        r = s.pop()
        answer = sorted(r.keys())
        return "".join(f'{e}{(r[e] if r[e] > 1 else "")}' for e in answer)


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.countOfAtoms("H2O"), "H2O")
        self.assertEqual(s.countOfAtoms("Mg(OH)2"), "H2MgO2")
        self.assertEqual(s.countOfAtoms("K4(ON(SO3)2)2"), "K4N2O14S4")


if __name__ == "__main__":
    unittest.main()
