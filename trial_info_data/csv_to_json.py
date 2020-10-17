import csv
import json
import os

csvFilePath = "YT6A/YT6A_trials_info.csv"
jsonFilePath = "YT6A/YT6A_trials_info.json"
# working_directory = os.getcwd()


# for folder in working_directory:
#     folder_name = os.path.join(working_directory, folder)
#     for filename in folder:
#         file_name = os.path.join(working_directory, folder, filename)
#         if filename.endswith(".csv"):
            # data = {}
            # with open(csvFilePath) as csvFile:
            #     csvReader = csv.DictReader(csvFile)
            #     header  = next(csvReader)
            #     for rows in csvReader:
            #         id =  rows['trial_number']
            #         data[id] = rows

            # with open(jsonFilePath,'w') as jsonFile:
            #     jsonFile.write(json.dumps(data,  indent=4))


data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    header  = next(csvReader)
    for rows in csvReader:
        id =  rows['trial_number']
        data[id] = rows

    with open(jsonFilePath,'w') as jsonFile:
        jsonFile.write(json.dumps(data,  indent=4))
