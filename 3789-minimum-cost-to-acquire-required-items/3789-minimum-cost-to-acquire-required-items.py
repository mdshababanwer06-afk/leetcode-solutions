class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Strategy 1: Buy all items individually
        option_a = need1 * cost1 + need2 * cost2
        
        # Strategy 2: Buy only Type 3 bundles to satisfy both
        option_b = max(need1, need2) * costBoth
        
        # Strategy 3: Buy Type 3 bundles for the overlap, then individual items for the rest
        overlap = min(need1, need2)
        option_c = (overlap * costBoth 
                    + (need1 - overlap) * cost1 
                    + (need2 - overlap) * cost2)
        
        return min(option_a, option_b, option_c)