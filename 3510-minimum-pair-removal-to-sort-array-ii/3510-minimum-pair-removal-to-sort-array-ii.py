class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        arr = list(map(int, nums))
        removed = [False] * n

        pq = []
        sorted_pairs = 0

        for i in range(1, n):
            heapq.heappush(pq, (arr[i-1] + arr[i], i-1))
            if arr[i] >= arr[i-1]:
                sorted_pairs += 1

        if sorted_pairs == n - 1:
            return 0

        rem = n
        prev = [i-1 for i in range(n)]
        nxt = [i+1 for i in range(n)]

        while rem > 1:
            if not pq:
                break

            s, left = heapq.heappop(pq)
            right = nxt[left]

          
            if right >= n or removed[left] or removed[right]:
                continue
            if arr[left] + arr[right] != s:
                continue

            pre = prev[left]
            nx = nxt[right]

            if arr[left] <= arr[right]:
                sorted_pairs -= 1
            if pre != -1 and arr[pre] <= arr[left]:
                sorted_pairs -= 1
            if nx != n and arr[right] <= arr[nx]:
                sorted_pairs -= 1

            arr[left] += arr[right]
            removed[right] = True
            rem -= 1

            if pre == -1:
                prev[left] = -1
            else:
                heapq.heappush(pq, (arr[pre] + arr[left], pre))
                if arr[pre] <= arr[left]:
                    sorted_pairs += 1

            if nx == n:
                nxt[left] = n
            else:
                prev[nx] = left
                nxt[left] = nx
                heapq.heappush(pq, (arr[left] + arr[nx], left))
                if arr[left] <= arr[nx]:
                    sorted_pairs += 1

            if sorted_pairs == rem - 1:
                return n - rem

        return n
