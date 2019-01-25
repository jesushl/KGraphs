#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        df = pd.read_excel(documentPath )
        return df

    def getNPSColumnsColl(self, df):
        columnNames     = df.columns
        for questionColumnName in columnNames:
            questionColumnNameStr  = normalize('NFKC', questionColumnName).encode('utf-8', 'ignore')
            #print(type(questionColumnName))
            for question in self.NPSQuestions:
                #print(type(question))
                if question in questionColumnNameStr:
                    question =  '{0}{1}{2}'.format('¿', question, '?')
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
        #print(df)
        self.getNPSDat(df)
        finalColl   = []
        #Column names definition
        #print(self.NLPDS)
        for columnsKey in self.NLPDS:
            finalColl.append([self.NLPDS[columnsKey]['question'], self.NLPDS[columnsKey]['evaluacion']])
        #print(finalColl)
        finalColl =  self.getRandomMarketValues(finalColl)
        finalColl =  self.getRandomExpectedValues(finalColl)
        #print(finalColl)
        finalColl.insert(0,['Pretunta', 'Resultado', 'Mercado', 'Esperado'])
        return finalColl

    #finalColl column 2
    def getRandomMarketValues(self, finalColl):
        columnName      = 'Mercado'
        for questionRow in finalColl:
            questionRow.append(random.randrange(20, 50 ))
        return finalColl

    #finalColl column 2
    def getRandomExpectedValues(self, finalColl):
        for questionRow in finalColl:
            questionRow.append(random.randrange(75,100))
        return finalColl

    def getComments(self, df):
        columns =  df.columns
        commentsColl = ''
        commentsList        = []
        for columnName in columns:
            if 'que se requiere' in columnName:
                commentsColl = columnName
                break
        comments = set(df[commentsColl].dropna()  )
        for comment in comments:
            print(normalize('NFKC', comment).encode('utf-8', 'ignore'))
            comment = normalize('NFKC', comment).encode('iso-8859-1', 'ignore')
            commentsList.append(comment.lower().capitalize())
        return commentsList

if  __name__ == '__main__':
    npss    = NPSStractionData()

    #print(npss.NLPDS)
    npss.getNPSJSON4Graph('NPS Clientes.xlsx')
    print(npss.getComments(npss.getNPSDataFrame('NPS Clientes.xlsx')))
