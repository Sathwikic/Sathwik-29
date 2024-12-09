def findMinPlatforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    n = len(arrivals)
    platforms_needed = 0
    max_platforms_needed = 0
    i = 0 
    j = 0 
    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        max_platforms_needed = max(max_platforms_needed, platforms_needed)
    return max_platforms_needed
arrivals = [900,940,950, 1100, 1500,1800]
departures = [910,1200, 1120, 1130, 1900,2000]
print("Minimum platforms needed:", findMinPlatforms(arrivals, departures))

