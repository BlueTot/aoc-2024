data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".splitlines()

data = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################""".splitlines()

data = """#############################################################################################################################################
#...#.............#...................#.....#.#...............#.....#...#.......#.................#...#.........#.......#..................E#
#.###.#######.###.#.###.###.#########.#.###.#.#.#########.###.#.#.###.#.#.#.###.#####.#.#####.#.###.#.#.#######.#.#.###.###.#####.#.#.#######
#.....#.....#...#.....#...#...#.....#...#.....#.#...#.......#.#.#...#...............#...#.....#.....#.#.....#...#.#...#...#.#.#...#.#.......#
#.#####.#.#####.###.#.###.###.#.###.###.#######.###.#.###.#.#.#.###.#.#######.#.#.#.###.#.###.###.###.#####.#.###.###.###.#.#.#.#.#.#.#####.#
#.....#.#.....#.#.#...#.....#.#...#.#...#.......#...#.....#.#.#...#.....#.....#...#...#.#.#.#...#...#.......#.....#...#.....#.#...#...#...#.#
#####.#####.###.#.#.#########.#.###.#.###.#######.#.#####.#.#.###.#######.#####.#.###.#.#.#.#.#.#########.#########.#.#######.#.#.###.#.#.#.#
#...#.#.....#...#.#.#.........#.#...#...#.....#...#...#...#.....#.#.............#...#.#...#...#.........#.#...#.....#.#...#.........#.#.....#
###.#.#.#####.###.#.#.#########.#.#.#.#.#####.###.#.#.#.#.#######.#.#######.#######.#.#.###.#.###.#####.#.#.#.#.###.###.#.#####.#.#.#.#.#.#.#
#...#...#.....#...#.#...#.......#.....#.......#...#...#.............................#.............#...#.#.#.#...#...#...#.#.....#...#.#.#.#.#
#.#####.#.#####.###.#.#.#.#########.#.#.#.#####.###.#####.#########.#.###.#.#####.###.#.#.###.#####.#.#.#.#.#########.###.#.###.#.#.#.#.#.#.#
#.......#.....#.....#.#.......#...#...#.........#.....#.......#...#.#...#.#.....#.#.....#.#...#.....#.#.#.#...#.........#.#.#.....#.....#.#.#
#############.###.#.###########.#.#.#.###.#.#######.#.###.#.#.###.#.#####.#####.#.###.#####.#.#.#####.#.#.###.#.#########.#.#.#.#.###.###.#.#
#.....#.....#...#...............#...................#.....#.#...#.#...#.......#.#...#.#.....#...#.....#.#...#...#.#.....#.#.#...#.#.....#.#.#
#.#.#.#.###.###.###################.#.#.#.#.#.#####.#####.#.###.#.###.#.#####.#.###.###.#.#.#####.#####.#######.#.#.###.#.#.#.#.#.###.#.#.#.#
#.#.#...#...#...#.....#.......#.....#.#.....#.#.#...#...#.#...#...#...#.....#.....#.#...#.......#.#...#.......#...#.#.#.#.....#.#...#...#.#.#
#.#.#####.###.###.#####.###.#.#####.#.###.###.#.#.###.###.###.#####.###.###.#####.#.#.###########.#.#.#######.#####.#.#.#.#####.#.#.#.#.#.#.#
#.#.....#...#...#...#.....#.#.#...#.#.........#.#...#.....#...#...#.#.#.#...#.......#.#.#...#.....#.#.......#.#.....#.#.#.#.....#.#.#.#.#.#.#
#.#.#.#####.###.#.#.#.#####.#.#.#.#.###########.###.#.#####.#.#.#.#.#.#.#.###.#######.#.#.#.#.#####.#####.#.#.#.#####.#.#.#.###.###.#.#.#.#.#
#.#.#.#...#.#...#.#...#.....#...#...#.#.............#...#...#.#.#...#...#.....#.......#...#.#...#.#.....#.#.#.#.#...#.#.#.#...#.....#...#.#.#
#.#.###.#.#.#.###.#####.#.#######.#.#.#.###############.#.###.#.#######.#######.#######.###.###.#.###.#.#.###.#.#.#.#.#.#.###.#.#######.#.#.#
#.#.....#.#...#...#.....#.#...#...#.#.#...#...#.......#...#...#.......#.......#...#...#.#...#...#...#.#.#.....#...#.#...#.#...#...#.....#...#
#.#.###.#.#.#######.###.###.#.###.#.#.###.###.#.#####.#####.#########.#.#####.###.#.#.#.#.#.#.#####.#.#.###########.#.###.#.#.#.#.#.###.#.#.#
#.....#.................#...#...#...#...#...#.#...#.#.........#.....#...#.......#.#.#...#.#.#.....#.#.#...............#.#.#.....#.#.........#
#.#.#.#.###.#############.#####.#.#####.###.#.###.#.###########.###.###.#.#######.#.#####.#.#####.#.#.#.#############.#.#.#####.#.#.###.#.###
#.................#...#...#...#.#...........#...#.#.#...........#.#...#.#...#.....#.#...#.......#.#...#...#...#.......#.#.#.................#
###.#.#.#.#.#####.#.#.#.###.#.#.#######.###.#.#.#.#.#.###########.###.#.#####.#######.#.#.#.###.#.###.###.###.#.###.#.#.#.#.#.#.###.#.###.#.#
#.#.#.#.#.......#.#.#.......#.#.#.......#...#.#.....#...#.........#.#.#.....#.#.#.....#.#.#...#.#...#...#...#.#...#.#.#...#.#.#.#.....#.....#
#.#.#.#.###.#.#.#.#.#######.#.#.###.#####.###.###.#####.#.#####.#.#.#.#.###.#.#.#.#.###.#.###.#####.###.###.#.###.#.#.#.#.###.#.#.#######.###
#...#.#.#.....#.#.#.....#...#.#...#.#.....#.......#.....#.#.#...#.#.#.#...#...#.#.....#.#.#...#.....#.#.#...#.....#.#.#.#.....#.....#.......#
#.###.#.#.#.#####.###.###.#.###.#.###.#########.###.#####.#.#.###.#.#.#######.#.#.###.#.###.###.#####.#.#.#########.#.#.#####.###.#.#.#####.#
#.#...#...#.......#...#...#...#.#...#.#.........#...#...#.....#.#.#.#.#.....#.#.....#.#.....#...#.........#...........#.....#.....#.......#.#
###.#.#.###.#####.#.###.#####.#####.#.###.#.###.#.###.#.#####.#.#.#.#.#.###.#.#.#####.#####.#.###.###########.###.###.#.###.#####.#########.#
#.......#...#.....#...#...#.#.....#...#...#...#.#.#...#.#.....#.#.#.#...#...#.#.#.....#.#...#...#...#.......#...#.#...#.#...#.....#...#...#.#
#.###.#.#.#####.#####.###.#.#.###.#.###.#####.#.#.###.#.#.#####.#.#.#####.#.#.###.#####.#.#####.#####.#####.#.#.###.###.#####.###.#.#.#.#.#.#
#.#...#.#.....#.#.......#.#.....#.#.#...#...#.#...#...#...#.........#.....#.#.....#...#.#.#...#...........#.#.#.....#...#.....#...#.#...#...#
#.#.#.#.#####.###.#######.###.#.#.#.###.#.###.#.#.#.###########.###.#.###.#.#.#####.#.#.#.#.#.###########.#.#.#######.###.#####.#.#.#######.#
#.#.....#...#.........#...#...#.#.#.....#.....#.#.#.#...#.....#.....#.#...#.#.#.....#.#.#.#.......#.#.......#.#.....#...........#.#.#.....#.#
#.###.#.#.#.###.#######.###.###.#.#######.#######.#.#.#.#.###.#####.###.#.#.###.#.###.#.#.###.###.#.#.#####.#.#.###.#############.#.#.#####.#
#.#...#...#.#...#.......#...#...#.....#...........#.#.#...#.#.....#.....#.#.....#.#...#.#.....#.....#.........#.#.....#.....#.......#.#...#.#
#.#.#.#####.###.#.#####.#.###########.###.#########.#.#####.#####.#.#############.#.###.#.#####.#####.#####.###.#####.#.###.#.###.###.#.#.#.#
#...#...#.#...#.#.......#.....#.....#...#.#...#.#.............#.#.#.#.....#.....#.#...#...#...#...#...#...#.#.....#.#.#...#...#.............#
#####.#.#.###.#.#######.#####.#.#.#.###.###.#.#.#.###########.#.#.###.###.#.#.#.#.###.###.#.#.###.#.###.#.#.#####.#.#.###.#######.###.#######
#.#.....#...#.#...#.....#...#.#.#.#...#.....#.#...#.........#...#...#.#.#.#.#.#.#...#...#.#.#...#.#.#...#.#.....#.#.#...#.......#...#...#...#
#.#.#.###.#.#.#.###.#####.#.#.#.#.###########.#.###.#######.###.###.#.#.#.#.#.#.###.###.#.#.#.#.#.#.#.###.#####.#.#.###.#.#####.#.#.#.#.#.#.#
#.#.#.....#.....#...#.....#...#.#.........#...#...#.......#...#.#.....#.#.#.#.#.....#.#.#.#.#...#.#...#...#...#.#.#...#.#.....#...#.#.#.#.#.#
#.#.#.###.#######.###.#####.###.#####.###.#.#############.###.#.#.###.#.#.#.#.#####.#.#.###.#.#####.###.###.#.#.#.###.#.#########.#.#.#.###.#
#.#...#.#.........#...#.....#.......#.#.#.#.............#.#...#.......#.#...#.#.#...#.......#.....#...#.#...#.#.#...#...........#.#.#.#.....#
#.#####.#.#####.###.#####.###.#######.#.#.#########.#####.#.#####.#.###.#####.#.#.###.###########.#####.#.###.#.#.#.###########.#.#.#.#####.#
#...............#.......#...#.#.....#.#...#.....#.#.#.....#.....#...#.........#.......#.........#.....#.....#.#.#.#...#.....#...............#
#######.#.#####.#.#####.#####.#.###.#.#.###.###.#.#.#.#########.#.#####.###.#.#.#######.###.#########.#.#####.#.###.#.#.###.###.#.#.#.#.#.#.#
#...............#.#...#.......#...#...#...........#...#.......#.#.#.....#...#.#.#.......#.#...........#...#...#...#.......#...#.#.#...#.....#
#.###.###.#.#.###.#.#############.#######.#############.#.###.#.#.#.#.###.###.###.#######.#################.#####.#######.###.#.#.###.#####.#
#.#.............#.#.............#...#.....#...........#...#...#.#.#.#.#...#...#...#.....#.......#...........#.....#...#...#.....#...#...#...#
#.#.#####.###.#.#.###.#######.#####.#.#####.#########.#.#.#.###.#.###.#.###.#.#.###.###.#######.#.#.#########.#####.#.#.###.###.###.#.#.#.#.#
#...........#...#.....#.......#.....#.#.....#.......#...#.#.#.#.#.....#...#.#.#.....#.#.......#...#.#.......#.#.....#.#...#...#...#...#.#...#
#.###.#.#.###.#.#######.#.#.###.#.#####.#####.#####.#####.#.#.#.###.#####.#.#.#####.#.#######.#.###.#.#####.#.###.###.#.#####.###.###.#.#.#.#
#...#.#.......#.#.......#.#.#...#.#.....#.....#.....#.....#.#.#.......#.#.#.........#.....#...#...#...#.....#.....#.#.#.#.................#.#
###.#.###.###.#.#.#######.#.#.#####.#####.#####.#####.#.###.#.#######.#.#.#####.#####.###.#.###.#######.###########.#.###.#.#.#.###.#.###.#.#
#...#.....#.#...#.#.......#.#.....#.#...#...#.#...#.......#.........#.#.#.#...#...#.....#.#.......#.....#...........#...#.#.#.#.#...#.#...#.#
#.#######.#.#####.#.###.###.#####.#.###.###.#.###.###.###.#####.#####.#.#.#.#.###.#.###.#.#######.#.###########.#######.#.#.#.#.#.###.#.#.#.#
#.....#.#.#.......#.....#...#...#...#...#...#...#...#...#...#...#.....#.#...#.#.#...#.....#...#.#...#.........#...#...#...#.#.#...#...#.#...#
#.###.#.#.#######.#######.###.#.#####.###.###.#####.#######.#.#.#.#####.#####.#.#####.###.#.#.#.#####.###.###.###.#.#.#####.#.#.###.###.#.#.#
#.#.#.#.........#.#.....#...#.#.......#...#.......#.........#...#.#.........#...#.....#...........#...#...#.....#.#.#...#...#.#.#...#...#...#
#.#.#.#########.#.#.###.###.###.#####.#.###.###.###############.#.#####.#.#####.#.#############.#.#.#.#.#######.#.#.###.#.###.#.###.#######.#
#...#.......#...#.#.#.#.............#.....#.#.#.........#...#...#.....#.#.......#...#...#.........#.#...#...#.....#...#.#...#.#...#.......#.#
###.#######.#.###.#.#.###########.#.#####.#.#.###.#.#####.#.#.#####.#.#.#######.###.#.#.#####.#####.#.###.#.#####.###.#.###.#.###.#.#####.#.#
#.................#.......#.......#.......#.#...#.#.#.....#.#.#.....#.#.#...........#.#.....#.....#.#.....#.....#...#.#.#...#.#.#.#.....#.#.#
#.###.#.#.#.#####.#####.###.###############.#.###.###.#####.#.###.#.#.###.#######.###.#####.#######.###########.#####.#.#.###.#.#.#####.#.#.#
#.#...#.#.#.#...#.#.....#...#.....#.....#...#.#...#...#...#...#...#.#...#...#.....#...#.....#...#...#.........#.......#.#...#.#.........#...#
#.###.#.#.#.#.#.#.#.#####.###.#.#.#.#.#.#.###.#.###.#.#.#.#####.#.#.###.#.#.#####.#.###.#####.#.#.###.#######.#######.#.###.#.#########.#.###
#...#...#.#...#.#...#.....#.#.#.#.#.#.#.#.#...#.#...#.#.#.#.....#...#.#.#.#.#...#.#.#.#.....#.#...#.......#.#.......#.....#.#...#...#...#...#
###.#####.#####.###.#.#####.#.#.###.#.###.###.#.#.###.#.#.#.###.###.#.###.#.#.#.#.#.#.#####.#.#####.###.#.#.#.#####.#.###.#.###.#.#.#.#.###.#
#...#.....#...#.....#.#.......#.....#.....#...#...#...#.#...#.#...#.#...#.#...#.#.#.#.#.....#...#...#...#.#.#.#...#.#...#.#...#...#.#.......#
#.#.#.###.#.#####.###.###.#################.#.#######.#.#####.#.#.#.#.#.#.#####.###.#.#.###.###.#####.#.#.#.#.###.#.###.#.###.#####.###.###.#
#...#.#...#.#.......#...#.............#.....#.#.....#.#.#.......#.#...#.#.....#.......#.#...#.#.#...#.#.#...#...#...#...#.#.#.#.....#.#.....#
#.###.#.###.#.#####.###.#############.#.###.#.###.#.#.#.###.#####.#####.#####.#########.#.#.#.#.#.#.#.#.#######.#.###.###.#.#.#.#####.#.#####
#.....#...#...#...#...#.......#.....#.#.#...#.....#.#.....#.#...#...#.#...#.....#.....#.#.....#...#.#.#.#.......#...#...#...#.#.#.........#.#
#######.#.#.#.#.#####.#######.###.#.#.###.#########.#.###.#.#.#.###.#.###.#######.###.#.#####.#####.#.#.#.#####.#######.#####.#.#######.#.#.#
#...#...#.#.#...#.......#...#...#...#...#.....#...#.#...#.#...#...#.#...#.......#.#...#.....#.....#...#.#.#.....#.....#.....#.#.....#...#.#.#
#.#.#.#.#.#.#.###.###.###.#.#.#.#.#####.#.###.#.###.#.#.#.#######.#.###.#######.#.#.#####.#.###.#######.#.#.#####.###.#####.#.#####.#.#.#.#.#
#.#.#.#.#.#...#...#...#...#.#.#.#.#...#.#...#.#.#...#.#...#.......#...#...#.......#.....#.#...#...........#.#.....#.#.....#.#.#...#...#.#...#
###.#.#.#.#####.###.###.###.###.#.#.#.#.#####.#.#.#####.###.###.#####.#.#.#.###########.###.#.###.###########.#####.#####.#.#.#.#.#.###.###.#
#...#.................#.#...#...#...#...#.....#.#.#...#.#...#...#.....#.#...#.....#.......#.#...#.#...#.......#.........#...#...#.#.#...#...#
#.###.#.#####.#.#######.#.#.#.###.#.#####.#####.#.#.#.#.#.###.###.#######.###.###.#######.###.#.#.#.###.#######.###.#######.#####.###.#.#.###
#.....#...#...#...#...#.#...#...#.#...#...#.........#.#.#.#.#...#.......#.#.....#.......#.....#.....#...#.......#.#.#.....#.#...#.#...#.....#
#.#######.#.###.#.#.#.#.###.###.#.###.#.###.#########.#.#.#.###.###.#.#.###.#########.#.#####.#####.#.#.#.###.###.#.#.###.#.#.#.#.#.###.#.#.#
#.......#.#...#.#.#.#...#.#...#.#.......#...#...#.....#.#.#.......#...#.....#.#.....#.#.#...#.....#.#.#.#...#.....#...#...#.#.#.#...#.....#.#
#######.#.###.###.#.#####.###.#.#########.#.#.#.#.#.###.#.#.#####.###########.#.###.###.#.#.#####.###.#.#.#.#########.#.###.###.#####.#.###.#
#...........#.....#.....#.......#...#.....#.#.#...#.#.....#.#...#.#.......#...#.#.......#.#.#.#.......#.#.#...........#.........#...#.#.....#
#.###.#.###.#####.#####.#.#.#####.#.#.#####.#.#####.#.#######.#.#.#.#####.#.#.#.#######.#.#.#.#.#####.###.###########.#######.#.#.#.#.#.###.#
#...#.#...#.....#...#...#.#...#...#.#.#.....#.#...#.........#.#.#...........#.#.....#...#.#.#.#...#.......#.........#...#.....#...#.#.#...#.#
#.#.#.###.#####.###.#.###.#.###.###.#.#.#####.#.#.#####.###.#.#.#.#####.#########.#.#####.#.#.###.#.#######.#######.###.#.###.#####.#.#.#.#.#
#.#.#.#...#.#.....#.#.#...#...#.#.#.#.#.........#.....#.#.#...#.#.#...#.#.......#.#.......#.#.....#.....#.#.....#.....#...#...#...#.#...#.#.#
#.#.###.###.#.###.#.#.###.###.#.#.#.#################.#.#.#####.###.#.#.#.#####.#####.#####.#.#########.#.#.###.#.###.#####.###.#.#.#####.#.#
#.#...#.....#...#.#.#.........#.#.#...........#.#...#.#.#.....#...#.#.#.#...#.......#...#...#.#.......#.#.....#...#...#.....#.#.#...#...#...#
#.###.#####.###.#.#.###.#######.#.#####.#####.#.#.#.#.#.#.#.#.###.#.#.#####.#######.#####.###.#.#######.#.#####.#.#.#.#.#####.#.#####.#.###.#
#...#.......#.#.#.#...#...#...#...#...#...#...#...#.....#.#.#...#...#.....#...#...#.#...................#.#.....#.#.#...#...#...#.....#...#.#
###.#####.###.#.#.###.###.#.#.#.###.#.#.###.###.#.#.#####.#.#.###########.###.#.###.#.#########.#.#######.#.###.###.#####.#.#.###.#####.###.#
#.#...#.#.....#.#...#.#.#...#...#...#...#...#...#.....#.....#.#.......#.#.....#.....#.....#.....#.#...#...#.#.#.#...#.....#.#...#.#...#.#...#
#.###.#.#.###.#.#####.#.#########.###.###.#######.###.#.#####.#.#.###.#.#######.#####.###.#.#.#.#.###.#.###.#.#.#.#####.#.#####.###.#.#.#.###
#.#...#...#...#.......#.......#.#...#...#.#.....#...#.#...#...#.#...#.........#.#...#...#.#.#.#.#...#.....#.#...#.....#.#.....#...#.#.#.#...#
#.#.###.#.#.#.###.#####.#####.#.###.###.#.###.#.###.#.###.#.###.###.###########.#.#####.#.#.#.#####.#######.#.#######.#####.#.###.#.#.#.###.#
#...........#.#.........#...#.....#.#.#.#...#.#.....#...#.#.#...#.#.........#...#.....#.#...#.....#...#.....#...#...#.....#.#.....#.#.#...#.#
#.###.###.#.#.#########.###.#####.#.#.#.#.#.#.#########.#.###.###.#########.#.#######.#.#####.###.###.#.#######.#.#######.#.#######.#.#.#.#.#
#...#.....#.#.#.....#...#.....#...#.#...#.#.#.#...#...#.#.#...#.....#.......#.......#...#...#.#.....#...#.#.....#.........#...#.....#...#.#.#
#.#.#####.#.#.#.###.#.###.#.###.###.#.#####.#.###.#.#.#.#.#.#####.#.#.#####.#######.#####.#.###.#########.#.#####.#.#########.#####.#.#####.#
#.#.....#...#...#...#.#...#.....#...#.......#...#...#.#.#.#...#...#...#.......#...#.#.....#...#...#.......#.......#.#.......#.......#.......#
#.#####.#########.###.#.###.#.###.#############.#####.#.#.###.#.#.#.#####.###.#.#.#.#.#######.###.#.###.#.#####.###.#.#####.#######.#.#######
#.....#...#.....#.....#...#.#...#...#...........#.....#.....#.#.#.#.......#.....#.#...#...#.#.....#...#.#.#.....#...#...#.#.#.....#.#...#...#
#####.#.#.#.#####.#.###.#.#.###.###.#.#.#########.#########.#.#.#.#######.#####.#.###.#.#.#.###.###.###.#.#.#####.#.###.#.#.#.###.#.#.#.###.#
#...#.#.#...#.....#...#.#.#.#...#...#.#.........#...........#.#.#.....#...#...#.#.....#.#.......#...#...#.#.#.....#.#.....#.#...#.....#.#...#
###.#.#.#.###.#####.#.###.#.#.###.#.###.#.#####.#####.#####.#.#.#####.#.#.#.#.###.#####.#.#######.#.#.#####.#.#####.#.#.#.#.#########.#.#.###
#...#.#.#.#...#.....#.#...#.#.#.#.....#.#.#...#.#...#.......#.#...#.....#.#.#.#.....#...#.....#...#.#.......#.#.#...#.#...#.....#.......#...#
#.#.#.#.###.###.#####.#.#####.#.#####.#.#.#.#.#.#.#.#.#######.#.#.#.#####.#.#.#.#####.#######.#.###.#########.#.#.###.#.#######.#.###.###.#.#
#.#.#.#...#.#...#...#.#...#...#...#.#.....#.#.#...#.#.#.....#.#.#.#.#.....#.....#.#...#.#...#...#.....#.....#.#.......#.#.....#.#...#.....#.#
#.#.#.###.#.#####.#.#.#.#.#.###.#.#.#.###.#.#.#####.#.#.#.###.###.###.###.#.#####.#.###.#.#.#######.#.#.###.#.#########.#.###.#.###.#######.#
#.#.#...#.#.#...#.#...#.#.#.........#...#.#.#...#...#.#.#...#...#.#...#...#.#.....#...#...#...#.....#...#...#.#.........#.#...#...#.........#
#.#####.#.#.#.#.#.#######.###.#####.###.###.###.#.###.#####.###.#.#.#######.#.#######.#.###.#.###.###.#######.#.###########.#.#.#.#########.#
#.........#.#.#.#.#.....#.#...#...#.#...#...#...#.#.......#...#...#.#.......#...#...#.#...#.#.....#...#.....#.#.#.#.........#.......#.....#.#
#.#.#.#.#.#.#.#.#.#.###.#.#.###.#.###.###.###.###.#######.#.#####.#.#.#########.#.#.#.#####.#######.###.###.#.#.#.#.#.#.#.#####.#.#.#.#.#.#.#
#.#.#...#.#.#.#...#.#...#.#...#.#...#...#...#.....#...#.....#.....#.#.....#.....#.#.#.#...#.#.....#.#.#.#.....#.#.#...#.......#.#...#.#.#.#.#
#.#.#####.#.#.#.###.#.###.#.###.###.#.#.#.#.#.#####.#.#.#####.#####.#####.#.#.###.#.#.#.#.#.###.#.#.#.#.#####.#.#.#.#.#####.#.#.###.#.#.###.#
#.#.....#.#.#.#.#...#.....#.#...#.#.#.#.#.#.#.......#.#...#...#.....#.....#.#.....#.#...#.#...#.#.#.#.#.#...#.#.#...#.......#.#...#.#.#.....#
#.#####.#.#.#.###.#####.#.#.#.###.#.#.#.###.#.#######.#####.###.###.#.#####.#######.#####.###.#.#.#.#.#.#.#.#.#.#######.#.###.###.#.#.#####.#
#...#...#.#.#.........#.#...#.#...#.#.#.#...#.#...#...#.....#...#.#.#.#.....#.#.........#.....#.#.#...#...#.#.#...#...#...#.....#.#.#.#.....#
###.#.###.#.#.###.#####.#####.###.#.#.#.#.###.#.#.#.###.#####.#.#.#.#.#####.#.#.#######.#######.###.#.#####.#.###.#.#.###.#.###.#.#.#.#.#.#.#
#...#.#...#.#.....#...#.....#.#...#.#.#.#.#...#.#.#.....#...#.#.....#.....#.#.#.....#.#.....#...#.....#.#...#...#.#.#.......#...#.#.#.#...#.#
#.###.#.#.#.#####.#.#.#####.#.#.###.###.#.#.#####.#######.#.#.###.#######.#.#.#####.#.#####.#.#.#.#.###.#.###.#.#.#.#####.###.###.#.#.#.###.#
#.....#.#.#.#...#.#.#.#.....#.#...#.....#...#.....#...#...#.#...#.#.....#.#.#.....#.#.........#.#.#.....#.......#.#.#...#...#...#.#.#.#...#.#
#.#####.#.#.#.###.#.#.#.#####.###.#######.###.#####.#.#.###.#.#.#.###.#.#.#.#.###.#.#.#########.#.#.#.#.#####.#.#.#.#.#.#.#.#.###.#.#.#.#.#.#
#.#.....#.#.#.....#.#...#.....#.........#.#...#.....#...#...#.#...........#...#...#.#.#.................#.......#...#.#.....#.#...#.#...#...#
#.#.#####.#.#####.#.###.#.#####.#########.###.#.#########.###.#.#######.#######.#.#.#.###.#.#.#####.#.#.#.###.#######.###.###.#.###.###.###.#
#.#...#...#.#...#.#.#.#.#.....#.............#...#.....#.#.#...#.......#.#.......#.#.#.....#.#...#...#...#.....................#.#.....#...#.#
#.###.#.###.#.#.#.#.#.#.#####.#.###########.#.#.###.#.#.#.###########.#.#.#####.###.###.###.#.#.#.#.#.#.#####.###########.#.#.#.#######.#.#.#
#.#.#.#...#...#.....#.......#.#.#...#.....#...#.....#...#.....#.....#.....#.........#...#...#.#.#...#.#.....#.........#...#.#.#.........#...#
#.#.#.#####.#####.###.#.#####.#.#.###.###.#############.#####.#.###.#####.#####.#########.#.#.#.###.###.#.#.#######.#.#.#.#.#.#########.#####
#.#.#.........#.....#.#.......#...#...#.#.........#...#...#...#.#.#.#...#.#...........#...#...#...#...#.#.#.#.....#.#.#.#...#.#.............#
#.#.#######.###.#.###.#.###########.###.#######.###.#.###.#.###.#.#.#.#.###.#.#.#####.#.###.#.###.#.#.#.#.#.#.###.#.#.#.#####.#####.#######.#
#S........#.....#.....#.......................#.....#.......................#.......#.......#...#.......#.....#.............................#
#############################################################################################################################################""".splitlines()

from heapq import heappop, heappush

for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == "S":
            start = (r, c)
        if char == "E":
            end = (r, c)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pq = [(0, start, (0, 1))]
visited = set()
distances = {}
distances[(start, (0, 1))] = 0

while pq:
    weight, curr, dir = heappop(pq)
    if (curr, dir) not in visited:
        visited.add((curr, dir))
        if data[nr := curr[0]+dir[0]][nc := curr[1]+dir[1]] != "#": # not a wall
            if ((nr, nc), dir) not in visited and weight + 1 < distances.get(((nr, nc), dir), float("inf")):
                heappush(pq, (weight+1, (nr, nc), dir)) # move forward
                distances[((nr, nc), dir)] = weight + 1
        if (curr, ndir := dirs[(dirs.index(dir)+1)%4]) not in visited and weight + 1000 < distances.get((curr, ndir), float("inf")):
            heappush(pq, (weight+1000, curr, ndir)) # turn right
            distances[(curr, ndir)] = weight + 1000
        if (curr, ndir := dirs[(dirs.index(dir)-1)%4]) not in visited and weight + 1000 < distances.get((curr, ndir), float("inf")):
            heappush(pq, (weight+1000, curr, ndir)) # turn left
            distances[(curr, ndir)] = weight + 1000

mindist = float("inf")
for node, weight in distances.items():
    if node[0] == end:
        mindist = min(mindist, weight)
print(mindist)