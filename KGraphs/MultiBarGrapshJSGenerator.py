from NPSStractionData import NPSStractionData

class MultiBarGraphsJSGenerator:
    multiBarFramework = ''

    def buildMultiBarGraph(self, xmlFile, elementID = 'multiGraph' , multiBarFramework = 'multiBarFramework.txt', orientation = 'vetical' , lineSet = [2,3]):
        self.loadMultiBarFramework(multiBarFramework)
        nps         = NPSStractionData()
        dataSet     = nps.getNPSJSON4Graph(xmlFile)
        self.multiBarFramework = self.multiBarFramework.replace('{DATATABLE}', str(dataSet))
        self.multiBarFramework = self.multiBarFramework.replace('{SERIES}', str(self.getLineSeriesConf(lineSet)) )
        self.multiBarFramework = self.multiBarFramework.replace('{ORIENTATION}', orientation)
        self.multiBarFramework = self.multiBarFramework.replace('{ELEMENTID}', '\'{}\''.format(elementID))
        print(self.multiBarFramework)

    def getLineSeriesConf(self, lineSet):
        series = {'series':{}}
        for line in lineSet:
            series['series'].update({line : '{type : \'line\''})
        return series

    def loadMultiBarFramework(self, multiBarFrameworkFile):
        with open(multiBarFrameworkFile, 'r' ) as mbf:
            self.multiBarFramework =  mbf.read()
        return self.multiBarFramework

if __name__ == '__main__':
    mbgjsG = MultiBarGraphsJSGenerator()
    mbgjsG.buildMultiBarGraph(xmlFile = 'NPS Clientes.xlsx')
    print(mbgjsG.multiBarFramework)
