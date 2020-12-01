def cakes(recipe, available):
    min_q = float("inf")
    for i in recipe:
        if i in available:
            min_q = available[i]//recipe[i] if available[i]//recipe[i] < min_q else min_q
        else:
            return 0
    return min_q

