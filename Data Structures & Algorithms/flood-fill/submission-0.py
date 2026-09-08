from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m, n = len(image), len(image[0])
        curr = image[sr][sc]
        
        # The emergency brake
        if curr == color:
            return image 
            
        # Properly initialize the deque with our starting pixel
        queue = deque([(sr, sc)])
        
        # Paint the starting pixel right away
        image[sr][sc] = color
        
        while queue:
            # Pop the current position
            r, c = queue.popleft()
            
            # The 4 directions (dr, dc = delta row, delta col)
            check = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            for dr, dc in check:
                # Calculate the exact coordinates of the neighbor
                nr, nc = r + dr, c + dc
                
                # Check bounds AND if the neighbor matches our ORIGINAL color
                if nr < 0 or nc < 0 or nr == m or nc == n or image[nr][nc] != curr:
                    continue
                
                # If it's valid, paint it instantly so we don't queue it twice
                image[nr][nc] = color
                
                # Toss the neighbor into the back of the queue
                queue.append((nr, nc))
                
        return image
