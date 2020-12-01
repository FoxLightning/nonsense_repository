states_needed = {"mt", "wa", "or", "id","nv", "ut", "ca", "az"}
stations = {}
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}



choise = set()
while states_needed:
    states_covered = set()
    best_station = None
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    choise.add( best_station )
    states_needed -= states_covered

print(choise)

