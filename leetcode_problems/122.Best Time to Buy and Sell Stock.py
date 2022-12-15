class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        k=i+1
        curr_prof=0
        prof=0
        for j in range(len(prices)):
            while k<=j:
                curr_prof=prices[k]-prices[i]
                # print("curr_prof",curr_prof)
                if curr_prof <0:
                    i+=1
                    # print("curr_i",i)
                elif i==k :
                    k+=1
                    # print("curr_k_if_eq",k)
                else:
                    k+=1    
                    # print("curr_k",k)
                prof=max(prof, curr_prof)
                # print("curr_Maxprof",prof)
        if prof<0:
            return 0
        else:
            return prof   