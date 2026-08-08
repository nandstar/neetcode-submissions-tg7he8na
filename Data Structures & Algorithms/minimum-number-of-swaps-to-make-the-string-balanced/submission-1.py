class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_close = 0
        
        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1
            
            # If balance goes negative, we have an unmatched ']'
            if balance < 0:
                max_close = max(max_close, -balance)
                
        return (max_close + 1) // 2


        