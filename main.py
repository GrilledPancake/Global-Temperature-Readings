with open("Global_Temperature_Data_File.txt", "r") as fileHandle:
    lines = fileHandle.readlines()

numReadings = len(lines)


totalOceanTemp = 0
totalLandTemp = 0
for line in lines:
    year, landTemp, oceanTemp = line.split("\t")
    totalOceanTemp += float(oceanTemp)
    totalLandTemp += float(landTemp)

avgLandTemp = totalLandTemp / numReadings
avgOceanTemp = totalOceanTemp / numReadings

print("Average land temperature anomaly: ", avgLandTemp)
print("Average ocean temperature anomaly: ", avgOceanTemp)

landVariance = 0
oceanVariance = 0

with open("Global_Temperature_Data_File.txt", "r") as fileHandle:
    lines = fileHandle.readlines()

numReadings = len(lines)

sumofLandTemp = 0
sumofOceanTemp = 0
for line in lines:
    year, landTemp, oceanTemp = line.split("\t")
    sumofLandTemp += float(landTemp)
    sumofOceanTemp += float(oceanTemp)

meanLandTemp = sumofLandTemp / numReadings
meanOceanTemp = sumofOceanTemp / numReadings

sumSquaredDiffLand = sum((float(landTemp) - meanLandTemp) ** 2 for _, landTemp, _ in map(str.split, lines))
sumSquaredDiffOcean = sum((float(oceanTemp) - meanOceanTemp) ** 2 for _, _, oceanTemp in map(str.split, lines))

sampleVarianceLand = sumSquaredDiffLand / (numReadings - 1)
sampleVarianceOcean = sumSquaredDiffOcean / (numReadings - 1)

print("Land temperature anomaly variance:",sampleVarianceLand)
print("Ocean temperature anomaly variance:",sampleVarianceOcean)


