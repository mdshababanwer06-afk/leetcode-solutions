class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        up = [[0] * n for _ in range(LOG)]

        # Iterative DFS to avoid recursion depth issues.
        timer = 0
        stack = [(0, 0, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                timer += 1
                tin[u] = timer
                up[0][u] = p

                for k in range(1, LOG):
                    up[k][u] = up[k - 1][up[k - 1][u]]

                stack.append((u, p, 1))

                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            k = 0
            while diff:
                if diff & 1:
                    u = up[k][u]
                diff >>= 1
                k += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return up[0][u]

        # Fenwick tree: range XOR update, point query.
        bit = [0] * (n + 2)

        def add(i: int, val: int) -> None:
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def range_xor(l: int, r: int, val: int) -> None:
            add(l, val)
            add(r + 1, val)

        def point_query(i: int) -> int:
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        char_mask = [1 << (ord(c) - ord('a')) for c in s]

        for u in range(n):
            range_xor(tin[u], tout[u], char_mask[u])

        ans = []

        for q in queries:
            parts = q.split()
            typ = parts[0]
            u = int(parts[1])

            if typ == "update":
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))
                delta = char_mask[u] ^ new_mask

                if delta:
                    range_xor(tin[u], tout[u], delta)
                    char_mask[u] = new_mask

            else:
                v = int(parts[2])
                w = lca(u, v)

                mask = (
                    point_query(tin[u])
                    ^ point_query(tin[v])
                    ^ char_mask[w]
                )

                # At most one character may have an odd frequency.
                ans.append((mask & (mask - 1)) == 0)

        return ans