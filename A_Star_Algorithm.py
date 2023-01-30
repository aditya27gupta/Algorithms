from typing import Dict, Tuple


class AStarSolver:
    def __init__(self, graph: Dict, startNode: str, endNode: str):
        self.graph = graph
        self.startNode = startNode
        self.endNode = endNode

    def getNeighbours(self, node) -> (Tuple[str, int] | None):
        if node in self.graph:
            return self.graph[node]
        else:
            return None

    def hCost(self, element: str):
        cost = {"A": 11, "B": 6, "C": 99, "D": 1, "E": 7, "G": 99}
        return cost[element]

    def find_path(self):
        openNodes = set(self.startNode)
        closedNodes = set()
        gCost = {}
        parents = {}

        gCost[self.startNode] = 0
        parents[self.startNode] = self.startNode

        while len(openNodes) > 0:
            currentNode = None

            for node in openNodes:
                if currentNode is None:
                    currentNode = node
                elif gCost[node] + self.hCost(node) < gCost[currentNode] + self.hCost(
                    currentNode
                ):
                    currentNode = node

            if currentNode is None:
                print("Path Doesn't exist")
                return None

            if currentNode == self.endNode or self.getNeighbours(currentNode) is None:
                pass

            else:
                for node, cost in self.getNeighbours(currentNode):
                    if node not in openNodes and node not in closedNodes:
                        openNodes.add(node)
                        parents[node] = currentNode
                        gCost[node] = gCost[currentNode] + cost

                    else:
                        if gCost[node] > gCost[currentNode] + cost:
                            gCost[node] = gCost[currentNode] + cost
                            parents[node] = currentNode

                        if node in closedNodes:
                            closedNodes.remove(node)
                            openNodes.add(node)

            if currentNode == self.endNode:
                path = []
                while parents[currentNode] != currentNode:
                    path.append(currentNode)
                    currentNode = parents[currentNode]

                path.append(currentNode)
                path.reverse()
                return path

            openNodes.remove(currentNode)
            closedNodes.add(currentNode)

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
