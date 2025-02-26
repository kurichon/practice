class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  #prefix sum of 0 is even
        prefix_sum = 0
        result = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 0: #if prefix sum is even
                result += odd_count 
                even_count += 1
            else: #otherwise if odd
                result += even_count  
                odd_count += 1
            
            result %= MOD  # modulo constraint
        
        return result
