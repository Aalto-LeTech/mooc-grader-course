
try:
    with open('number') as orig_file:
        start = int(orig_file.read().strip())
    with open('solution') as submitted_file:
        solution = int(submitted_file.read().strip())
    
    orignumber = None
    try:
        with open('orignumber') as f:
            orignumber = int(f.read().strip())
    except IOError:
        pass

    max_points = 10
    points = 0
    if solution == (start + 1):
        points = max_points

    print("TotalPoints: {}".format(points))
    print("MaxPoints: {}".format(max_points))
    
    print("Original number was: {}".format(start))
    print("Your solution was: {}".format(solution))
    
    print("Previous number was: {}".format(orignumber)) # just to test store_user_files action

except Exception:
    print("ERROR")
    raise
