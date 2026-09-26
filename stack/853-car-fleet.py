class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # fleets stack
        fleets = []

        # sort positions
        position_sorted = [(i, start) for i, start in enumerate(position)]
        position_sorted.sort(key=lambda x: x[1], reverse=True)

        for i, start in position_sorted:
            # calculate time to target
            independent_arrival_time = (target - start) / speed[i]

            # does it catch up to fleet ahead?
            # (bottleneck is always fleet ahead)
            # if yes: merge into fleet ahead, no actions needed
            # if no: new fleet, push onto stack
            if (not fleets) or independent_arrival_time > fleets[-1]:
                fleets.append(independent_arrival_time)

        return len(fleets)
