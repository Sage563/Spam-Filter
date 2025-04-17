import json

class LoadDict_score:
    def __init__(self):
        self.score =self.get_values()
        self.actual_vlaue = int(self.run())
    def get_values(self):
        """Load the JSON file and extract values
        Load the JSON data
        Assuming the JSON file is named 'results.json"""
        with open('results.json', 'r', encoding='utf-8') as file:
            data_json = file.read()
        data = json.loads(data_json)
        values_list = data.values()
        valuess =list(values_list)
        return valuess
    
    def rating(self):
        """Get the rating based on the actual value"""
        if self.actual_vlaue >= 100:
            return "Very Positive"
        elif self.actual_vlaue >= 80:
            return "Positive"
        elif self.actual_vlaue >= 50:
            return "Neutral"
        elif self.actual_vlaue >= 30:
            return "Negative"
        else:
            return "Very Negative"
        
    def run(self):
        """Run the function to get the values"""
        value =10
        score =["Very Negative" , "Negative", "Neutral", "Positive","Very Positive"]

        for i in self.score:

            if not value >= 100:
                if i =="Neutral":
                    value +=5
                elif i =="Positive":
                    value +=7
                elif i =="Very Positive":
                    value +=8

            
            if  value >= 100:
                if i =="Very Negative":
                    value -=7
                elif i =="Negative":
                    value -=7
        return str(value)
        