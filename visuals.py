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

    """Affiche le cube"""
    def showCube(self):
            for face in self.cube:
                #UI
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


    """Permet de tourner une face sur elle même clockwise"""
    def rotate_face_clockwise(self, face): 
        upMiddle = self.cube[face][0][1] #Futur milieu droit
        downMiddle = self.cube[face][2][1] #Futur milieu gauche

        Left = [self.cube[face][2][0], self.cube[face][1][0], self.cube[face][0][0]]
        Right = [self.cube[face][2][2], self.cube[face][1][2], self.cube[face][0][2]]

        self.cube[face][0] = Left
        self.cube[face][2] = Right

        self.cube[face][1][0] = downMiddle
        self.cube[face][1][2] = upMiddle

    """Rotation clockwise de la face haute"""
    def move_u(self):
        #Gestion de la ligne haute des faces latérales
        front = self.cube["F"][0].copy()
        left = self.cube["L"][0].copy()
        right = self.cube["R"][0].copy()
        back = self.cube["BA"][0].copy()

        self.cube["R"][0] = back
        self.cube["BA"][0] = left
        self.cube["L"][0] = front
        self.cube["F"][0] = right

        #Gestion de la face haute elle-même
        self.rotate_face_clockwise("U")
    
    """Rotation anti clockwise de la face haute"""
    def move_u_anti(self):
        for i in range(3):
            self.move_u() #3 rotation clockwise = 1 rotation anti clockwise

    """Rotation clockwise de la face avant"""
    def move_front(self):
        #Gestion de l'interchangement des faces affectées
        up = self.cube["U"][2].copy()
        bottom = self.cube["BO"][0].copy()
        right = [self.cube["R"][i][0] for i in range(3)]
        left = [self.cube["L"][i][2] for i in range(3)]

        left.reverse() #Car pendant rotation ordre changé
        right.reverse()

        self.cube["U"][2] = left
        self.cube["BO"][0] = right

        for i in range(3):
            self.cube["R"][i][0] = up[i]
            self.cube["L"][i][2] = bottom[i]
            
        #Gestion de la face avant elle-même
        self.rotate_face_clockwise("F")
        
    def move_front_anti(self):
        for i in range(3):
            self.move_front()

        
cube = Cube()

cube.move_front()
cube.move_front_anti()

cube.showCube()
        


#TODO  :
"""
UP - Done
FRONT
BACK 
LEFT
RIGHT
BOTTOM

CHECK SOLVED
"""