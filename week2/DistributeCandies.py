class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        # compile set of candy kinds
        kinds = set()
        for c in candies:
            kinds.add(c)

        # collect values
        numKinds = len(kinds)
        numCandies = len(candies)

        # solution is numKinds, but caps at half of the possible candies
        optimal = min((numCandies/2), numKinds)

        return optimal
