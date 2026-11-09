class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        count = [0] * k
        
        # Min-heap of (finish_time, server_id)
        busy = []
        
        # SortedList of available server IDs
        free = SortedList(range(k))
        
        for i, (start, duration) in enumerate(zip(arrival, load)):
            # 1. Release all servers that finished before or at current arrival time
            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                free.add(server)
            
            # 2. If no servers are free, drop this request
            if not free:
                continue
            
            target = i % k
            # 3. Find the first available server >= target
            idx = free.bisect_left(target)
            
            # If no server >= target, wrap around to the first available server
            if idx == len(free):
                idx = 0
            
            assigned_server = free[idx]
            
            # 4. Assign request
            count[assigned_server] += 1
            heapq.heappush(busy, (start + duration, assigned_server))
            free.remove(assigned_server)
        
        # Return all servers that processed the maximum count
        max_requests = max(count)
        return [i for i, c in enumerate(count) if c == max_requests]