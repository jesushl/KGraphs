#!/usr/bin/env python

import pandas as pd
import random
from unicodedata import normalize
#Esta clase trabaja el DataFrame de un documento relacionado con NPS
class NPSStractionData:

    NPSQuestions = ['Cómo calificas la atención recibida','Qué tanto ha profundizado en tus necesidades',
                    'Hasta el momento ¿Qué tanto hemos cumplido con la promesa de venta',
                    'Siempre haz encontrado a personas que te atiendan y se ocupen de ti cuando tú lo necesitas',
                    'Cómo calificas nuestra oferta de valor']
    NLPDS         = {}

    def getNPSDataFrame(self, documentPath):
        df = pd.read_excel(documentPath)
        return df

    def getNPSColumnsColl(self, df):
        columnNames     = df.columns
        for questionColumnName in columnNames:
            questionColumnName  = normalize('NFC', questionColumnName)
            for question in self.NPSQuestions:
                if question in questionColumnName:
                    if questionColumnName in self.NLPDS:
                        self.NLPDS[questionColumnName].update({'question' : question} )
                    else:
                        self.NLPDS[questionColumnName]  = {'question' : question}

    def getNPSDat(self, df):
        for column in self.NLPDS:
            nps  = self.getColumnNPSResults(df,column)
            self.NLPDS[column].update(nps)

    def getColumnNPSResults(self, df, column):
        promotores      = len(df[df[column] > 8 ])
        detractores     = len(df[df[column] < 6 ])
        total = promotores + detractores
        promotores_detractores = promotores - detractores
        evaluacion      = (100 * promotores_detractores) / total
        return {'promotores' : promotores, 'detractores' : detractores, 'evaluacion' : evaluacion}

    def getNPSJSON4Graph(self, excelFile):
        df          = self.getNPSDataFrame(excelFile)
        self.getNPSColumnsColl(df)
        print(df)
        self.getNPSDat(df)
        finalColl   = []
        #Column names definition
        print(self.NLPDS)
        for columnsKey in self.NLPDS:
            finalColl.append([self.NLPDS[columnsKey]['question'], self.NLPDS[columnsKey]['evaluacion']])
        print(finalColl)
        finalCollT  = []
        for row in zip(*finalColl):
            finalCollT.append(list(row))

        finalCollT =  self.getRandomMarketValues(finalCollT)
        finalCollT =  self.getExpectedValues(finalCollT)
        print(finalCollT)

    def getRandomMarketValues(self, finalColl):
        columnName      = 'Mercado'
        finalColl[0].append(columnName)
        marketValues = len(finalColl[0])
        value = random.randrange(65, 80 )
        finalColl[1].append(value)
        return finalColl

    def getExpectedValues(self, finalColl):
        columnName      = 'Resultado Esperado'
        finalColl[0].append(columnName)
        marketValues    = len(finalColl[0])
        value = random.randrange(85,100)
        finalColl[1].append(value)
        return finalColl

if  __name__ == '__main__':
    npss    = NPSStractionData()

    #print(npss.NLPDS)
    npss.getNPSJSON4Graph('NPS Clientes.xlsx')
