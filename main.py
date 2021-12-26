import json

"""Loading And Dumping JSON Data
    """


class JsonData:
    @staticmethod
    def load_data(json_file):
        """
        this method is used to load the json data
        :param json_file: sample4 file
        :return: json file in dictionary format
        """
        data = open(json_file)
        json_file = json.load(data)
        return json_file

    @staticmethod
    def dump_data():
        """
        this method is used to dump the json data
        :return: dictionary in the json format
        """
        data_dict = {
            "people": [
                {
                    "firstName": "Joe",
                    "lastName": "Jackson",
                    "gender": "male",
                    "age": 28,
                    "number": "7349282382"
                },
                {
                    "firstName": "James",
                    "lastName": "Smith",
                    "gender": "male",
                    "age": 32,
                    "number": "5678568567"
                },
                {
                    "firstName": "Emily",
                    "lastName": "Jones",
                    "gender": "female",
                    "age": 24,
                    "number": "456754675"
                }
            ]
        }
        out_json = open("dumpfile.json", "w")
        json_dump = json.dump(data_dict, out_json, indent=6)
        out_json.close()
        return json_dump


value = JsonData()
data1 = value.load_data('D:/BrizePython/JsonData/sample4.json')
data2 = value.dump_data()
print(data1)
print(data2)

