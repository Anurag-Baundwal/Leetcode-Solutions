class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {}
        d["U"] = d["D"] = d["L"] = d["R"] = 0
        for move in moves:
            d[move] += 1
        
        if d["U"] == d["D"] and d["L"] == d["R"]:
            return True
        else: 
            return False