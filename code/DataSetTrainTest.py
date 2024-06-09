import utils.Files as Files
import utils.GeoDataFrame as GeoData


datasetName = 'Atlanta_brightkite.tsv'
datasetName = 'Atlanta_gowalla.tsv'
datasetName = 'Beijing_brightkite.tsv'
datasetName = 'Beijing_gowalla.tsv'
datasetName = 'Berlin_brightkite.tsv'
datasetName = 'Berlin_gowalla.tsv'
datasetName = 'New York_brightkite.tsv'
datasetName = 'New York_gowalla.tsv'
datasetName = 'Rome_brightkite.tsv'
datasetName = 'Rome_gowalla.tsv'
datasetName = 'San Francisco_brightkite.tsv'
datasetName = 'San Francisco_gowalla.tsv'
trainPercentage = 0.8
minimumNeedleRecords = 100
rootDirectory = 'data/cities'

dataFrame = GeoData.getCleanedCSVFile(datasetName, rootDirectory)
numberOfUsers = len(dataFrame['AgentID'].unique())
numberOfNeedles = int(numberOfUsers*0.1)
if numberOfUsers < 50:
    exit('number of users is less than 50')
dataFrame = GeoData.getFilteredDataFrame(dataFrame, minimumNeedleRecords)
eligibleAgents = GeoData.getAgentsRecords(dataFrame)
totalAgents = len(eligibleAgents)
print('splitting dataFrame for train...')
trainDataFrame = GeoData.getTrainDataFrame(dataFrame, trainPercentage)

print('splitting dataFrame for test...')
testDataFrame = GeoData.getTestDataFrame(dataFrame, trainDataFrame)

print('selecting needles...')
selectedAgents = eligibleAgents.head(numberOfNeedles+1)
selectedAgents = selectedAgents.to_dict()

print('adding needles...')
replacedAgentIds = list(selectedAgents.keys())[0:numberOfNeedles]
needleIds = list(selectedAgents.keys())[1:numberOfNeedles+1]

swapAgents = (replacedAgentIds, needleIds)

testDataFrame = GeoData.addNeedle(testDataFrame, swapAgents)

trainFileName = f'train-{datasetName}-{numberOfNeedles}-needles-{totalAgents}-agents-{trainPercentage}-normal-portion.tsv'
testFileName = f'test-{datasetName}-{numberOfNeedles}-needles-{totalAgents}-agents-{trainPercentage}-normal-portion.tsv'
print('saving dataFrames...')
Files.saveDataFrame(trainDataFrame, trainFileName)

Files.saveDataFrame(testDataFrame, testFileName)
print('saving logs...')
Files.log(f'dataset name: {datasetName}')
Files.log(f'number of needles: {numberOfNeedles}')
Files.log(f'total agents: {totalAgents}')
Files.log(f'normal data for each needle: {trainPercentage*100}%')
Files.log(
    f'file name pattern: *-datasetName-numberOfNeedles-needles-totalAgents-agents-trainPercentage-normal-portion.tsv')
Files.log(
    f'file name pattern: *-{datasetName}{numberOfNeedles}-needles-{totalAgents}-agents-{trainPercentage}-normal-portion.tsv')
Files.log(f'Needles: {needleIds}')
