#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:16:15 2019

@author: elizabethalarcon
"""

class Graph():
    
    
    def __init__(self):
        self.numberNodes = 0
        self.adjacentList = {}
        
        
    def addVertex(self,node):
        
        if not node in self.adjacentList.keys():
            self.adjacentList.update({node:[]})
            self.numberNodes += 1
        
        return self
    
    
    def addEdge(self,node1, node2):
        
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
    
    
    def showConnections(self):
                
        for node in self.adjacentList.keys():
            
            nodeConnections = self.adjacentList[node]
            connections = ''
            for vertex in nodeConnections:
                connections += vertex + ' '
            print (node + '-->' + connections)


            
myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1') 
myGraph.addEdge('3', '4') 
myGraph.addEdge('4', '2') 
myGraph.addEdge('4', '5') 
myGraph.addEdge('1', '2') 
myGraph.addEdge('1', '0') 
myGraph.addEdge('0', '2') 
myGraph.addEdge('6', '5')

myGraph.showConnections();