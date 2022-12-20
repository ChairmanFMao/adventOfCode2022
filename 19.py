from math import ceil

f = open("19Input.txt","r")

lines = f.read().split("\n")
lines.pop()
f.close()

# for part 1 I am going to do a dfs and simulate all the possible
# ways things could happen
# I might have to do dynamic programming here actually
# I think you can only make one robot at a time
# Time complexity is quite bad
# I think even in dynamic programming the dimensions would be too
# big to hold, like 8 dimensions
# potentially do it as a two stage problem
# splitting it into: ore and clay, obsidian and geode
# like a meet in the middle problem
# unsure what I would want from them
# or maybe even 4 stages for each of the robot types
# We can just iterate over the number of each robot we want
# then we can just make them greedily
# I think that this should be a viable time complexity
# need to also try all permutations of the if statements
# We just need to jump from robot creation points
# I think that the time complexity is roughly 4^24 ish in worst
# need to somehow do further pruning
# part 1 took like 10-15 mins to run
# I think I might need to change my approach for part 2
# For part 2 dp would still come with the same problems
# I think we can get the dp such that it works out
# Just need to store ore from 0 to biggest ore * 32
# but this would lead to 100**4 * 20**4
# I will have a go at part 2 tomorrow I think
# 206540 is too high
# 10230 is too low
# the first two values are 10 and 32
# the third one takes especially long to run
# I had to tweak the pruning for the third one but I get it as 44
# 14080 is not right
# I think the problem might be with the third case
# Potentially it could be with the earlier ones tho
# With further searching I got 47 for the third
# 15040 is laso not right
# the first one is 10
# the second one is 33
# the third one is 47
# I finally got it!
# I tweaked around with the pruning for so long but I got it to
# work properly in the end
# This took so long but its so nice to have it done!

# Set to 0 for part 1
out = 1

# Each of these will be a list that stores all the data
# 3 long lists
# First element stores the number of that element
# Second element stores the number of robots
# Third element stores what is required to make one
# this is a dfs that I abandoned

# This is just a helper method to make the code more clean
def update(ore,clay,obsidian,geode,req):
    ore[0] += req*ore[1]
    clay[0] += req*clay[1]
    obsidian[0] += req*obsidian[1]
    geode[0] += req*geode[1]

# I use these to keep track of the recursion
ops = []
itr = 0
END = 32
occurs = [0 for i in range(END+1)]
seen = dict()
def dfs(ore, clay, obsidian, geode, time,best):
    global itr, occurs
    itr += 1
    if time > END:
        return 0
    occurs[time] += 1
    best = max(best,geode[0]+(END-time)*geode[1])
    if not itr % int(1e6):
        print("check in:",occurs,best)
    
    # We go over all of the possible robots we could create

    if obsidian[1]:
        # geode robot
        req = 0
        if ore[0] >= geode[2][0]:
            req = 0
        else:
            req = max(0,ceil((geode[2][0]-ore[0])/ore[1]))

        if obsidian[0] >= geode[2][1]:
            req = max(req,0)
        else:
            req = max(req,ceil((geode[2][1]-obsidian[0])/obsidian[1]))
        req += 1
        update(ore,clay,obsidian,geode,req)
        geode[1] += 1
        ore[0] -= geode[2][0]
        obsidian[0] -= geode[2][1]
        ops.append([3,time+req])
        best = max(best,dfs(ore,clay,obsidian,geode,time+req,best))
        ops.pop()
        ore[0] += geode[2][0]
        obsidian[0] += geode[2][1]
        geode[1] -= 1
        update(ore,clay,obsidian,geode,-req)

    if time > 27:
        return best

    if clay[1] and geode[2][1] > obsidian[1]:
        # obsidian robot
        req = 0
        if ore[0] >= obsidian[2][0]:
            req = 0
        else:
            req = max(0,ceil((obsidian[2][0]-ore[0])/ore[1]))

        if clay[0] >= obsidian[2][1]:
            req = max(req,0)
        else:
            req = max(req,ceil((obsidian[2][1]-clay[0])/clay[1]))
        req += 1
        update(ore,clay,obsidian,geode,req)
        obsidian[1] += 1
        ore[0] -= obsidian[2][0]
        clay[0] -= obsidian[2][1]
        ops.append([2,time+req])
        best = max(best,dfs(ore,clay,obsidian,geode,time+req,best))
        ops.pop()
        ore[0] += obsidian[2][0]
        clay[0] += obsidian[2][1]
        obsidian[1] -= 1
        update(ore,clay,obsidian,geode,-req)

    if time > 25:
        return best

    if obsidian[2][1] > clay[1]:
        # clay robot
        req = 0
        if ore[0] >= clay[2]:
            req = max(req,0)
        else:
            req = max(req,ceil((clay[2]-ore[0])/ore[1]))
        req += 1
        update(ore,clay,obsidian,geode,req)
        clay[1] += 1
        ore[0] -= clay[2]
        ops.append([1,time+req])
        best = max(best,dfs(ore,clay,obsidian,geode,time+req,best))
        ops.pop()
        ore[0] += clay[2]
        clay[1] -= 1
        update(ore,clay,obsidian,geode,-req)

    if max(clay[2],obsidian[2][0],geode[2][1]) > ore[1]:
        # ore robot
        req = 0
        if ore[0] >= ore[2]:
            req = max(req,0)
        else:
            req = max(req,ceil((ore[2]-ore[0])/ore[1]))
        req += 1
        update(ore,clay,obsidian,geode,req)
        ore[1] += 1
        ore[0] -= ore[2]
        ops.append([0,time+req])
        best = max(best,dfs(ore,clay,obsidian,geode,time+req,best))
        ops.pop()
        ore[0] += ore[2]
        ore[1] -= 1
        update(ore,clay,obsidian,geode,-req)
    
    return best


# Iterates over the blueprints
for bluePrint in lines:
    seen = dict()
    # This gets the blueprint number
    val = int(bluePrint.split("Blueprint ")[1].split(": ")[0])
    if val != 2:
        continue
    # Gets the ore required to make an ore robot
    ore = int(bluePrint.split("ore robot costs ")[1].split(" ore. Each clay")[0])
    # Gets the materials required to make a clay robot
    clay = int(bluePrint.split("clay robot costs ")[1].split(" ore. Each obsidian")[0])
    # This gets the materials to make an obsidian robot
    obsidian = list(map(int,bluePrint.split("Each obsidian robot costs ")[1].split(" clay. Each geode robot")[0].split(" ore and ")))
    # This gets the materials to make a geode robot
    geode = list(map(int,bluePrint.split("Each geode robot costs ")[1].split(" obsidian.")[0].split(" ore and ")))
    # Start with 1 ore collecting robot
    #code that calls the dfs
    best = dfs([0,1,ore],[0,0,clay],[0,0,obsidian],[0,0,geode],0,0)
    print("done!",val,best)
    # Part 1
    #out += best*val
    # Part 2
    out *= best

print(out)

