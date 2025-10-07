class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        store1 = {}
        store2 = {}

        for i in range(len(s)):
            x = s[i]
            y = t[i]
            if x in store1:
                store1[x] += 1
            else:
                store1[x] = 0

            if y in store2:
                store2[y] += 1
            else:
                store2[y] = 0

        for i in range(len(s)):
            key = s[i]
            value = store1.get(key)
            valuet = store2.get(key)

            if valuet == None:
                return False
            
            if valuet != value:
                return False

        return True
