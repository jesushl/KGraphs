import pandas as pd
import numpy
import json

class DataAnalizator:

    jsonResult = {}

    def getDataFrameFromExcel(self, excelFile):
        return pd.read_excel(excelFile, encoding='utf-8')


    def getAverage(self, df, columnName):
        return df[columnName].mean()

    def getDicFromColumn(self, dataFrame, columName  ):
        return dataFrame.to_dict(orient='dict')

    def getQuestionColumns(self, dataFrame):
        questionMark        =  '¿'
        questionColumns = []
        columns = dataFrame.columns
        for column in columns:
            if  '¿' in   column:
                questionColumns.append(column)
        return questionColumns

    def getColumnDataType(self, dataFrame, columnName):
        return dataFrame[columnName].dtype

    def getClassificationValues(self,df ,classificationColumn):
        return sorted(list( set( df[classificationColumn]) ))

    def getBarGraphValues(self, df, columnXAxis):
        barCollections  = {}
        numberQuestionColumns = []
        questionColumns = self.getQuestionColumns(df)
        for questionColumn in questionColumns:
            columnDataType      = self.getColumnDataType(df, questionColumn)
            if  columnDataType.type is  numpy.float64:
                numberQuestionColumns.append(questionColumn)
        xAxisValues = self.getClassificationValues(df, columnXAxis )
        #print(xAxisValues)
        if numberQuestionColumns:
            for questionNumColumn in numberQuestionColumns:
                if xAxisValues:
                    for xAxisValue in xAxisValues:
                        subDF       = df[questionNumColumn][df[columnXAxis] == xAxisValue]
                        average    = subDF.mean()
                        if not  isinstance(questionNumColumn, str):
                            print(questionNumColumn.type)
                            fixedColumnName = questionNumColumn.decode('utf-8')
                        else:
                            fixedColumnName = questionNumColumn
                        fixedColumnName = fixedColumnName.replace('[','').replace(']','').replace('-','')
                        #print(fixedColumnName)
                        if fixedColumnName in barCollections:
                            barCollections[fixedColumnName ][xAxisValue] = average
                            #barCollections[xAxisValue ][questionNumColumn] = average
                        else:
                            barCollections[fixedColumnName] = {xAxisValue : average }
                            #barCollections[xAxisValue] = {questionNumColumn : average }
        #print(barCollections)
        return self.orderinternalItems(barCollections)
        #return  barCollections

    def orderinternalItems(self, collection):
        orderedCollection = {}
        for innerCollection in collection:
            #print("Collection")
            print(innerCollection)
            innerKeys = collection[innerCollection]
            #print("Inner keys")
            #print(innerKeys.keys())
            innerOrderedKeys = sorted(list(innerKeys.keys()))
            #print(innerOrderedKeys)
            for orderedKey in innerOrderedKeys:
                if innerCollection in orderedCollection:
                    orderedCollection[innerCollection].append({orderedKey : collection[innerCollection][orderedKey]})
                else:
                    orderedCollection[innerCollection] = [{orderedKey : collection[innerCollection][orderedKey]}]
        print(orderedCollection)
        return orderedCollection

    def getClimaOrganizacional(self, df, columnXAxis):
        numberQuestionColumns = []
        dataCollection                       = {}
        xAxisValues                = self.getClassificationValues(df, columnXAxis )
        questionColumns     =  self.getQuestionColumns(df)

        for questionColumn in questionColumns:
            columnDataType      = self.getColumnDataType(df, questionColumn)
            if  columnDataType.type is  numpy.float64:
                numberQuestionColumns.append(questionColumn)
        for questionNumColumn in     numberQuestionColumns:
            dataList = []
            dataList.append(['Label', 'Value'])
            for xAxisValue in xAxisValues:
                #SubDF es una extraccion de una columna a los valores de un grupo
                subDF       = df[questionNumColumn][df[columnXAxis] == xAxisValue]
                print("*" * 30)
                print("Grupo: {0}  Pregunta {1}".format(xAxisValue, questionNumColumn[:20]))
                print(subDF)
                #print(subDF.between(9, 10))
                #print(subDF[subDF.between(9, 10)].mean())
                maxCalification = subDF[~subDF.isnull()].size * 10
                print("Maxima Calificacion : {}".format(maxCalification))
                promedioDePromotores = subDF[subDF.between(9, 10)].sum()
                promedioDeDetractores =  subDF[subDF.between(1, 6)].sum()
                print("pPromotores = {0} pDetractores ={1}".format(promedioDePromotores, promedioDeDetractores))
                promotoresMenosDetractores = promedioDePromotores - promedioDeDetractores
                calificacion = (promotoresMenosDetractores * 100) /  maxCalification
                print("Calificacion : {}".format(calificacion))
                dataList.append([xAxisValue, calificacion ])
            fixedColumnName = questionNumColumn.replace('[','').replace(']','').replace('-','').strip()
            fixedColumnName = "{0}{1}".format(fixedColumnName, '?')
            dataCollection[fixedColumnName] = dataList
        print(dataCollection)
        return dataCollection

    def buildDataJSONFile(self, excelFile, mainColumn, classColumn, jsonFileName):
        global jsonResult
        df = self.getDataFrameFromExcel(excelFile)
        jsonBarData     = self.getBarGraphValues(df, classColumn )
        with open(jsonFileName, 'w', encoding = 'utf-8') as jsonFile:
            json.dump(jsonBarData, jsonFile)

    def createJSONFile(self, collection, jsonFile):
        with open(jsonFile, 'w', encoding = 'utf-8') as jsonFile:
            json.dump(collection, jsonFile)
    

if __name__ == "__main__":
    da = DataAnalizator()
    excelFile = 'NPS_2018_PRIMARIA_PHI-ToProcess.xls'
    df = da.getDataFrameFromExcel(excelFile)
    #print(df.columns)

    #print(da.getAverage(df,'Tiempo total'))
    #print(da.getDicFromColumn(df, 'ID de respuesta ').keys)
    #print(da.getDicFromColumn(df, 'ID de respuesta ')['¿Que considera que se requiere para que su calificación sea 10-'])
    #print(da.getCuestionColumns(df))
    #print(da.getColumnDataType(df,'¿Cómo califica la atención y educación que recibió su hij@ en las materias de: [Español]' ))
    #print(df'¿Por favor, indíquenos alguna acción de mejora en los conceptos anteriores-' ))
    #print( df['Temporización del grupo: Nivel de Satisfacción' ][df['Grado'] == '1A'])
    #print(da.getBarGraphValues(df, 'Grado'))
    #da.buildDataJSONFile(excelFile, '', 'Grado', "barData.json")
    da.createJSONFile(da.getClimaOrganizacional(df, 'Grado'), "prototype2.json")
