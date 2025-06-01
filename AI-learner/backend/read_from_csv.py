import csv

def read_from_csv(csvFileName, debug=0):
    if debug >= 1:
        print("AI_001:read_from_csv - Function started")
        print(f"AI_002:read_from_csv - Input csvFileName = {csvFileName}")

    dataList = []

    try:
        with open(csvFileName, mode='r') as file:
            csvReader = csv.DictReader(file)
            headers = csvReader.fieldnames

            if debug >= 2:
                print(f"AI_003:read_from_csv - CSV Headers: {headers}")

            for row in csvReader:
                dataList.append(row)
                if debug >= 2:
                    print(f"AI_004:read_from_csv - Read row: {row}")

        if debug >= 1:
            print("AI_005:read_from_csv - File read successfully")

    except Exception as error:
        if debug >= 1:
            print(f"AI_006:read_from_csv - Error occurred: {error}")

    return dataList