import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        h = int(input_data[idx+1])
        idx += 2
        a = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        
        low = 1
        high = h 
        ans = h
        
        while low <= high:
            mid = (low + high) // 2
            
            damage = 0
            for i in range(n - 1):
                diff = a[i+1] - a[i]
                if mid < diff:
                    damage += mid
                else:
                    damage += diff
            
            damage += mid
            
            if damage >= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1 
                
        results.append(str(ans))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()