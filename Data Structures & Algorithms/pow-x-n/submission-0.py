class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer=x**n
        return float(f"{answer:.5f}")