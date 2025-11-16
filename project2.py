from graph import Graph, Vertex
from sys import maxsize

class ServiceMesh:
    def __init__(self):
        self.serviceMesh = Graph()
        self.coreMonitoringTree = Graph()

    def buildServiceMesh(self, filename):
        pass

    def canCommunicate(self, svc1, svc2, hops):
        pass

    def buildCoreMonitoringTree(self, source):
        pass

    def findMonitoringPath(self, svc1, svc2):
        pass

    def findLowestLatencyPath(self, svc1, svc2):
        pass

    def findBottleneckPath(self, svc1, svc2):
        pass

    def checkRoutingLoop(self, route):
        pass


