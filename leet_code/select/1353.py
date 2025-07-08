class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort(key=lambda el: el[1])
        attended = 0
        current_day = 0

        for start, end in events:
            # выбираем день max(current_day+1, start)
            if start > current_day:
                current_day = start
            if current_day <= end:
                # «посетили» событие
                attended += 1
                current_day += 1
        
        return attended

    
events= [[26,27],[24,26],[1,4],[1,2],[3,6],[2,6],[9,13],[6,6],[25,27],[22,25],[20,24],[8,8],[27,27],[30,32]]
instance = Solution()
res = instance.maxEvents(events=events)
print(res)