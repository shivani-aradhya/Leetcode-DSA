class Solution:
    def completecircuit(self,gas, cost):
        tank=0
        shortage=0
        start =0
        for i in range(len(gas)):
            tank+= gas[i]
            if tank>= cost[i]:
                tank -= cost[i]
            else:
                shortage+= cost[i]- tank
                start = i+1
                tank=0

        if tank<shortage or start== len(gas):
            return -1
        return start