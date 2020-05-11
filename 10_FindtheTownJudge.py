class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N==1:
            if not trust:
                return 1
        from collections import defaultdict
        new_dict = defaultdict(set)
        non_trustable = set()
        trustable=set()

        for rec in trust:
            new_dict[rec[1]].add(rec[0])
            non_trustable.add(rec[0])
            trustable.add(rec[1])

        # for item in non_trustable:
        #     if item in trustable:
        #         trustable.remove(item)

        for item in trustable:
            if item not in non_trustable:
                if len(new_dict[item])==N-1:
                    return item
                    print("Found", item)
        return -1
        # print("Not found")

        
