class MultiBarGraphsJSGenerator:
    multiBarFrameworw = ''

    def buildMultiBarGraph(self, multiBarFramework = 'multiBarFramework.txt', orientation = 'vetical' , lineSet = [2,3]):
        pass

    def loadMultiBarFramework(self, multiBarFrameworkFile):
        with open(multiBarFrameworkFile, 'r' ) as mbf:
            self.multiBarFramework =  mbf.read()
        return self.multiBarFramework

if __name__ == '__main__':
    mbgjsG = MultiBarGraphsJSGenerator()
    mbgjsG.loadMultiBarFramework('multiBarFramework.txt')
    print(mbgjsG.multiBarFramework)
