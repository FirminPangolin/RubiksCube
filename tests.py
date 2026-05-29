from visuals import *

"""TESTS ROTATION + ANTI = NEUTRE"""
#----
        
cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

cube.move_front()
cube.move_front_anti()

print(cube.cube == etat_initial)

#----

cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

cube.move_left()
cube.move_left_anti()

print(cube.cube == etat_initial)

#----

cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

cube.move_u()
cube.move_u_anti()

print(cube.cube == etat_initial)

#----

cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

cube.move_right()
cube.move_right_anti()

print(cube.cube == etat_initial)

#----

cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

cube.move_back()
cube.move_back_anti()

print(cube.cube == etat_initial)

#----

cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

cube.move_bottom()
cube.move_bottom_anti()

print(cube.cube == etat_initial)



"""TEST 4 ROTATIONS = NEUTRE"""
#----

cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

for _ in range(4):
    cube.move_right()

print(cube.cube == etat_initial)

#----

cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

for _ in range(4):
    cube.move_left()

print(cube.cube == etat_initial)

#----

cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

for _ in range(4):
    cube.move_u()

print(cube.cube == etat_initial)

#----

cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

for _ in range(4):
    cube.move_front()

print(cube.cube == etat_initial)

#----

cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

for _ in range(4):
    cube.move_back()

print(cube.cube == etat_initial)

#----

cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

for _ in range(4):
    cube.move_bottom()

print(cube.cube == etat_initial)


"""TEST OPERATIONS INVERSES"""

cube = Cube()

etat_initial = copy.deepcopy(cube.cube)

moves = cube.shuffle(200)

for move in range(len(moves) - 1, -1, -1):
    if len(moves[move]) == 2:
        cube.moves[moves[move][0]]()
    else:
        cube.moves[moves[move] + "'"]()

cube.showCube()

print(cube.cube == etat_initial)
