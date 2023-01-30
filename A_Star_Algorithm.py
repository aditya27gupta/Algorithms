from typing import Dict, Tuple, List


class AStarSolver:
    def __init__(self, graph: Dict, startNode: str, endNode: str) -> None:
        self.graph = graph
        self.startNode = startNode
        self.endNode = endNode
        self.openNodes = set(startNode)
        self.closedNodes = set()
        self.gCost = {}
        self.parents = {}

    def getNeighbours(self, node) -> (Tuple[str, int] | None):
        if node in self.graph:
            return self.graph[node]
        else:
            return None

    def hCost(self, element: str) -> int:
        cost = {"A": 11, "B": 6, "C": 99, "D": 1, "E": 7, "G": 99}
        return cost[element]

    def find_path(self) -> (List | None):
        self.gCost[self.startNode] = 0
        self.parents[self.startNode] = self.startNode

        while len(self.openNodes) > 0:
            currentNode = None

            for node in self.openNodes:
                if currentNode is None:
                    currentNode = node
                elif self.gCost[node] + self.hCost(node) < self.gCost[
                    currentNode
                ] + self.hCost(currentNode):
                    currentNode = node

            if currentNode is None:
                print("Path Doesn't exist")
                return None

            if currentNode == self.endNode or self.getNeighbours(currentNode) is None:
                pass

            else:
                for node, cost in self.getNeighbours(currentNode):
                    if node not in self.openNodes and node not in self.closedNodes:
                        self.openNodes.add(node)
                        self.parents[node] = currentNode
                        self.gCost[node] = self.gCost[currentNode] + cost

                    else:
                        if self.gCost[node] > self.gCost[currentNode] + cost:
                            self.gCost[node] = self.gCost[currentNode] + cost
                            self.parents[node] = currentNode

                        if node in self.closedNodes:
                            self.closedNodes.remove(node)
                            self.openNodes.add(node)

            if currentNode == self.endNode:
                path = []
                while self.parents[currentNode] != currentNode:
                    path.append(currentNode)
                    currentNode = self.parents[currentNode]

                path.append(currentNode)
                path.reverse()
                return path

            self.openNodes.remove(currentNode)
            self.closedNodes.add(currentNode)

        print("Path doesn't exist")
        return None


def main():
    graph_nodes = {
        "A": [("B", 2), ("E", 2)],
        "B": [("C", 1), ("G", 9)],
        "C": None,
        "D": [("G", 1)],
        "E": [("D", 6)],
        "G": None,
    }

    start = "A"
    end = "G"

    aStarObject = AStarSolver(graph_nodes, start, end)
    path = aStarObject.find_path()
    print(path)


if __name__ == "__main__":
    main()
