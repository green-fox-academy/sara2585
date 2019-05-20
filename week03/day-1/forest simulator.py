class Tree:
    def __init__(self, height = 0):
        self.height = height

    def irrigate(self):
        pass

    def getHeight(self):
        return f"{self.height}"

class WhitebarkPine(Tree):
    
    def irrigate(self):
        self.height += 2

class FoxtailPine(Tree):

    def irrigate(self):
        self.height += 1

class Lumberjack:
    def canCut(self, tree):
        if tree.height > 4:
            return True
        else:
            return False

class Forest:
    def __init__(self, trees = []):
        self.trees = trees
    
    def addTrees(self, tree):
        self.trees.append(tree)

    def rain(self):
        for tree in self.trees:
            tree.irrigate()

    def cutTrees(self, lumberjack):
        cuttrees = []
        for tree in self.trees:
            if lumberjack.canCut(tree):
                cuttrees.append(tree)
        for i in cuttrees:
            for tree in self.trees:
                if i == tree:
                    self.trees.remove(tree)

    def isEmpty(self):
        if len(self.trees) == 0:
            return True
        else:
            return False

    def getStatus(self):
        for tree in self.trees:
            print(f"There is a {tree.height} tall {tree.__class__.__name__} in the forest ")

whitebarkpine1 = WhitebarkPine(1)
whitebarkpine1.irrigate()
foxtailpine1 = FoxtailPine(1)
foxtailpine1.irrigate()
whitebarkpine2 = WhitebarkPine(5)


forest = Forest()
forest.addTrees(whitebarkpine1)
forest.addTrees(whitebarkpine2)
forest.addTrees(foxtailpine1)

forest.rain()
# for tree in forest.trees:
#     print(f"{tree.height}")
lumberjack = Lumberjack()
forest.cutTrees(lumberjack)
for tree in forest.trees:
    print(f"{tree.height}")

#forest.getStatus()







    

        
        

