```python
# req: 1500
# 1200  1300   1200  1300   1200  2000
# 12000 24000  14000 22000  13000 30000 
def findValuation(reqArea, areas, prices) -> int:
0: avg 13500, dev: sqrt ((13000 - avg)^2 + (14000 - avg)^2 ) // n. abs(price[0]-avg) > 3 * dev
    
    n = len(prices)
    outlier = [False for _  in range(n)]
    comparisonList = defaultdict(list)
    for price, area in zip(prices, areas):
        comparisonList[area].append(price)
    for i in range(n):
        price, area = prices[i], areas[i]
        complist = comparisonList[area]
        complist.remove(price)
        if len(complist) == 0:
            continue
        avg = sum(complist) // len(complist)
        dev = 0
        for comp in complist:
            dev += (com-avg)^2
        dev = sqrt(dev) // len(complist)
        if abs(price[i]-avg) > 3 * dev:
            outlier[i] True
    prices = [prices[i] for i in range(len(prices)) if not outlier[i]]
    areas = [areas[i] for i in range(len(areas)) if not outlier[i]]
    if len(prices) == 0: return 1000
    if len(prices) == 1: return prices[0]
    map = defaultdict(list)
    for price, area in data:
        map[area].append(price)
    if reqArea in map:
        return round(sum(map[reqArea]) / len(map[reqArea]))
    areas = sorted(areas)
    x1, x2 = 0, 0
    if reqArea > areas[-1]:
        x1, x2 = areas[-1], areas[-2]
    elif reqArea < areas[0]:
        x1, x2 = areas[1], areas[0]
    else:
        for i in range(1, len(data)):
            if areas[i-1] < reqArea < areas[i]:
                x1, x2= areas[i], areas[i-1]
    y1, y2 = sum(map[x1]) // len(map[x1]), sum(map[x2]) // len(map[x2])

    return round(y1 + (x-x2)*(y1-y2)/(x1-x2))
            
    
```