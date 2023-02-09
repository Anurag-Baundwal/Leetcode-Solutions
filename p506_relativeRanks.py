class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        # dictioanry for storing rank
        score_to_rank = {score: "" for score in scores}

        # sorting the list to find the rank of each of player
        sorted_scores = sorted(scores, reverse=True)
        
        # update dictionary values
        for i, score in enumerate(sorted_scores):
            if i == 0:
                score_to_rank[score] = "Gold Medal"
            elif i == 1:
                score_to_rank[score] = "Silver Medal"
            elif i == 2:
                score_to_rank[score] = "Bronze Medal"
            else:
                score_to_rank[score] = str(i + 1)
        
        # fetching values from the dictionary
        # in the order we need using list comprehension
        # and then return the result
        return [score_to_rank[score] for score in scores]