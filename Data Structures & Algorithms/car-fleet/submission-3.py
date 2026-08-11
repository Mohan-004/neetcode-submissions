class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        n = len(position)

        if n == 1 :
            return 1
        distance = [target-i for i in position]
        time = [distance[i]/speed[i] for i in range(n)]
        
        cars = sorted([(distance[i], time[i]) for i in range(n)], key = lambda item : item[0])

        fleet_time = 0
        fleets = 0

        for distance, time in cars:
            if time > fleet_time:
                fleets += 1
                fleet_time = time
        
        return fleets