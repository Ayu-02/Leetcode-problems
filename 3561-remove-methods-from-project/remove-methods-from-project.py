class Solution(object):
    def remainingMethods(self, n, k, invocations):
        # Build graph
        graph = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)

        # Find all methods suspicious because they are
        # reachable from method k
        suspicious = set()
        stack = [k]

        while stack:
            node = stack.pop()

            if node in suspicious:
                continue

            suspicious.add(node)

            for nxt in graph[node]:
                if nxt not in suspicious:
                    stack.append(nxt)

        # If any suspicious method is called by a non-suspicious
        # method, we cannot remove the suspicious methods.
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))

        # Otherwise, remove all suspicious methods
        return [i for i in range(n) if i not in suspicious]