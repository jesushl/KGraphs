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

    def buildCarousel(self, xmlFile, data-target):
        nps                 = NPSStractionData()
        comments   = nps.getComments() 
        commentsList
    def getCommentSitations(self, commentsList):
        quotesWrapper               = '<div class = "item{0}">{1}</div>'
        commentsBlockQuote = '<blockquote> {} </blockquote>'
        commentItems = ''
        activeSet = False
        for comment in commentsList:
            currentBock =    commentsBlockQuote.format(comment)
            if not activeSet:
                active = ' active'
                active = True
            else:
                active = ''
            currentQuoteWrapper = quotesWrapper.format(active, currentBock)
            commentItems = '{0}{1}'.format(commentItems, currentQuoteWrapper)

        def getCarouserIndicators(self, comments, data-target):
            indicators = ''
            indicatorFormat = '<li data-target={0} data-slide-to="{1}" {3}>'
            classStr                = 'class="active"'
            activeClass         = False
            for itemNumber in range(len(comments)):
                currentIndicator = ''
                if not activeClass:
                    currentIndicator = indicatorFormat.format(data-target, itemNumber, classStr)
                    activeClass = True
                else:
                    currentIndicator = indicatorFormat.format(data-target, itemNumber, '')
                indicators = '{0} {1}'.format(indicators, currentIndicator)
            return indicators

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
