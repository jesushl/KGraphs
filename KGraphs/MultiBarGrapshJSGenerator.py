from NPSStractionData import NPSStractionData

class MultiBarGraphsJSGenerator:
    multiBarFramework = ''

    def buildMultiBarGraph(self, xmlFile, elementID = 'multiGraph', multiBarFramework = 'multiBarFramework.txt', orientation = '\'horizontal\'' , lineSet = [1,2]):
        self.loadMultiBarFramework(multiBarFramework)
        nps         = NPSStractionData()
        dataSet     = nps.getNPSJSON4Graph(xmlFile)
        self.multiBarFramework = self.multiBarFramework.replace('{DATATABLE}', str(dataSet))
        self.multiBarFramework = self.multiBarFramework.replace('{SERIES}', str(self.getLineSeriesConf(lineSet)) )
        self.multiBarFramework = self.multiBarFramework.replace('{ORIENTATION}', '{}'.format(orientation))
        self.multiBarFramework = self.multiBarFramework.replace('{ELEMENTID}', '\'{}\''.format(elementID))
        print(self.multiBarFramework)

    def getLineSeriesConf(self, lineSet):
        serieString  = 'series  : {1}{0}{2},'
        seriesBuild  = '{0} : {1} type : \'line\'{2}'
        series       = ''
        for line in lineSet:
            series = ',{0}, {1}'.format(series, seriesBuild.format(line, '{', '}'))
            series =  series[1:]
        series =  serieString.format(series, '{', '}')
        return series.replace(': {,', ':{ ')

    def loadMultiBarFramework(self, multiBarFrameworkFile):
        with open(multiBarFrameworkFile, 'r' ) as mbf:
            self.multiBarFramework =  mbf.read()
        return self.multiBarFramework

    def saveFile(self, fileName, fileContent):
        with open(fileName, 'w') as nFile:
            nFile.write(fileContent)



if __name__ == '__main__':
    mbgjsG = MultiBarGraphsJSGenerator()
    mbgjsG.buildMultiBarGraph(xmlFile = 'NPS Clientes.xlsx')
    print(mbgjsG.multiBarFramework)
    mbgjsG.saveFile('multiLineGraph.js', mbgjsG.multiBarFramework)
    print(mbgjsG.getLineSeriesConf([1,2,3]))
