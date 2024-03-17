# Time:  O(n)
# Space: O(n)

# prefix sum, greedy
class Solution(object):
    def minimumMoves(self, nums, k, maxChanges):
        """
        :type nums: List[int]
        :type k: int
        :type maxChanges: int
        :rtype: int
        """
        idxs = [i for i, x in enumerate(nums) if x]
        prefix = [0]*(len(idxs)+1)
        for i in xrange(len(idxs)):
            prefix[i+1] = prefix[i]+idxs[i]
        result = float("inf")
        for l in xrange(max(k-maxChanges, 0), min(max(k-maxChanges, 0)+3, k, len(idxs))+1):
            for i in xrange(len(idxs)-l+1):
                cnt2 = (prefix[(i+l-1)+1]-prefix[(i+l-1)-(l//2-1)])-(prefix[(i+(l//2-1))+1]-prefix[i])
                cnt1 = (k-l)*2
                result = min(result, cnt2+cnt1)
        return result
