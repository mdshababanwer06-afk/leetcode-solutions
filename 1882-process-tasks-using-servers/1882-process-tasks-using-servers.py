class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []
        time = 0

        for i, task in enumerate(tasks):

            time = max(time, i)

            # Release completed servers
            while busy and busy[0][0] <= time:
                free, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # If no server is available, jump forward in time
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    free, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Select the server with minimum weight and index
            weight, idx = heapq.heappop(available)

            ans.append(idx)

            # Calculate actual finishing time
            heapq.heappush(
                busy,
                (time + task, weight, idx)
            )

        return ans