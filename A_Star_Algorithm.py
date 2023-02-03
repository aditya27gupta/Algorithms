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

    def fCost(self, node: str) -> int:
        return self.gCost[node] + self.hCost(node)

    def getPath(self, node):
        path = []
        while self.parents[node] != node:
            path.append(node)
            node = self.parents[node]
        path.append(node)
        path.reverse()
        return " -> ".join(path)

    def find_path(self) -> (List | None):
        self.gCost[self.startNode] = 0
        self.parents[self.startNode] = self.startNode

        while len(self.openNodes) > 0:
            currentNode = self.openNodes.__iter__().__next__()

            for node in self.openNodes:
                if self.fCost(node) < self.fCost(currentNode):
                    currentNode = node

            self.openNodes.remove(currentNode)

            if currentNode == self.endNode:
                return self.getPath(currentNode)

            elif self.getNeighbours(currentNode) is None:
                pass

            else:
                for node, cost in self.getNeighbours(currentNode):
                    successorCurrentCost = self.gCost[currentNode] + cost

                    if node in self.openNodes:
                        if self.gCost[node] <= successorCurrentCost:
                            continue
                    elif node in self.closedNodes:
                        if self.gCost[node] <= successorCurrentCost:
                            continue
                        self.closedNodes.remove(node)
                        self.openNodes.add(node)
                    else:
                        self.openNodes.add(node)

                    self.gCost[node] = successorCurrentCost
                    self.parents[node] = currentNode

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
