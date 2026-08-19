class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1Count, s2Count = {}, {}
        
        # 1. Initialize the maps with the first window
        for i in range(len(s1)):
            s1Count[s1[i]] = 1 + s1Count.get(s1[i], 0)
            s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)
            
        if s1Count == s2Count: return True
        
        # 2. Start sliding!
        l = 0
        for r in range(len(s1), len(s2)):
            # Add the new character on the right
            s2Count[s2[r]] = 1 + s2Count.get(s2[r], 0)
            
            # Remove the character on the left (the one that just left the window)
            s2Count[s2[l]] -= 1
            if s2Count[s2[l]] == 0:
                s2Count.pop(s2[l]) # Keep dictionary clean for easy comparison
            
            l += 1
            
            # 3. Check if the new window matches
            if s1Count == s2Count:
                return True
                
        return False