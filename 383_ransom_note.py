class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False 
        
        lst1 = [ransomNote[i] for i in range(0, len(ransomNote))]
        lst2 = [magazine[i] for i in range(0, len(magazine))]
        
        # lst1.sort()
        # lst2.sort()
        # Sorting not needed
        
        print(lst1)
        print(lst2)

        for i in lst2:
            if i in lst1:
                lst1.remove(i)
                print(lst1)
        lstx = []
        print(lstx.__len__())
        
        # return lst1.__len__ == 0 # missing ()
        # NOTE TO SELF: Never forget the () when calling a method !
        #  

sol = Solution()        # This is how we create an instance of a class
print(sol.canConstruct("aa", "aab"))