class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map = {}
        for i in range(len(list1)):
            map[list1[i]] = i
        
        res = []
        min_sum = float("inf")
        
        for j in range(len(list2)):
            if list2[j] in map:
                sum = j + map[list2[j]]
                
                if sum < min_sum:
                    res.clear()
                    res.append(list2[j])
                    min_sum = sum
                elif sum == min_sum:
                    res.append(list2[j])
                    
        return res