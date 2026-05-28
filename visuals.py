class Cube:
    def __init__(self):
        self.cube = {
            "U" : [["W" for _ in range(3)] for _ in range(3)],
            "L" : [["O" for _ in range(3)] for _ in range(3)],
            "F" : [["G" for _ in range(3)] for _ in range(3)],
            "R" : [["R" for _ in range(3)] for _ in range(3)],
            "BA" : [["B" for _ in range(3)] for _ in range(3)],
            "BO" : [["Y" for _ in range(3)] for _ in range(3)]
        }

    def showCube(self):
            for face in self.cube:
                """ UI """
                print()
                if face == "U":
                    print("TOP")
                elif face == "L":
                    print("LEFT")
                elif face == "F":
                    print("FRONT")
                elif face == "R":
                    print("RIGHT")
                elif face == "BA":
                    print("BACK")
                elif face == "BO":
                    print("BOTTOM")
                print()

                for ligne in range(3):
                    for colonne in range(3):
                        print(self.cube[face][ligne][colonne], end=" ")
                    
                    print()
                
    def move_u(self):
        front = self.cube["F"][0].copy()
        left = self.cube["L"][0].copy()
        right = self.cube["R"][0].copy()
        back = self.cube["BA"][0].copy()

        self.cube["R"][0] = back
        self.cube["BA"][0] = left
        self.cube["L"][0] = front
        self.cube["F"][0] = right

        upMiddle = self.cube["U"][0][1] #Futur milieu droit
        downMiddle = self.cube["U"][2][1] #Futur milieu gauche

        upLeft = [self.cube["U"][2][0], self.cube["U"][1][0], self.cube["U"][0][0]]
        upRight = [self.cube["U"][2][2], self.cube["U"][1][2], self.cube["U"][0][2]]

        self.cube["U"][0] = upLeft
        self.cube["U"][2] = upRight

        self.cube["U"][1][0] = downMiddle
        self.cube["U"][1][2] = upMiddle


cube = Cube()

cube.move_u()

cube.showCube()
        