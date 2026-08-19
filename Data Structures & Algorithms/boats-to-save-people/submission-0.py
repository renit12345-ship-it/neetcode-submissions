class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
    
        while left <= right:
        # If the lightest and heaviest can share
            if people[left] + people[right] <= limit:
                left += 1
        
        # The heaviest person always gets a boat
            right -= 1
            boats += 1
        
        return boats


        