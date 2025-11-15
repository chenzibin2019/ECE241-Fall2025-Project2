from graph import Graph, Vertex
from sys import maxsize

class ISPNetwork:
    def __init__(self):
        self.network = Graph()
        self.MST = Graph()

    def buildServiceMesh(self, filename):
        pass

    def canCommunicate(self, svc1, svc2, hops):
        pass

    def buildCoreMonitoringTree(self, source):
        pass

    def findMonitoringPath(self, router1, router2):
        pass

    def findLowestLatencyPath(self, router1, router2):
        pass

    def findBottleneckPath(self, router1, router2):
        pass

    def checkRoutingLoop(self, route):
        pass


