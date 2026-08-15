class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        result = [""] * n

        # Store (score, original_index)
        athletes = [(score[i], i) for i in range(n)]

        # Sort by score in descending order
        athletes.sort(reverse=True)

        for rank in range(n):
            index = athletes[rank][1]

            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)

        return result
        