class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][cnt] = minimum cost
        # cnt = consecutive occurrences of labels[node]
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Starting node contributes one character.
        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:
            cost, u, cnt = heapq.heappop(pq)

            if cost != dist[u][cnt]:
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:

                if labels[u] == labels[v]:
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                if new_cnt > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_cnt]:
                    dist[v][new_cnt] = new_cost
                    heapq.heappush(
                        pq, (new_cost, v, new_cnt)
                    )

        return -1