```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        two same task have >= n unit of time
        least finish time
        count the freq of each task
        keep a heap
        for each time, do a task if have, during the n time, do other tasks
        keep the used tasks in a tmp so that they will not be used in the n time
        """
        count = Counter(tasks)
        pq = []
        for k, v in count.items():
            heapq.heappush(pq, (-v, k))
        cur_time = 0
        while pq: # 直到task用完
            i, tmp = 0, [] # 在接下来n的时间里，填充其他的task
            while i <= n:
                cur_time += 1
                if pq: # 如果有其它的task，填进去，因为不能重复出现， 所以先把他放在一个tmp里
                    x, y = heappop(pq)
                    if x != -1: # 如果这一次就用没了，就不用放了
                        tmp.append((x+1, y))
                if not pq and not tmp: break # 如果都没task了，就提前停止，要不时间一直走到最后
                i += 1 
            for item in tmp: # 把tmp里面的再放进去
                heappush(pq, item)
        return cur_time

                


            

```