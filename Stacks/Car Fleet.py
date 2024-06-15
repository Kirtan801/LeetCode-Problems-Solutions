class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position, speed), reverse=True)

        fleet=0
        time_to_destination=0

        for pos,spd in cars:
            time_to_reach_destination=(target-pos)/spd

            if time_to_reach_destination>time_to_destination:
                fleet+=1
                time_to_destination=time_to_reach_destination

        return fleet
        