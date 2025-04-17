from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
import load_dict
import json
import os
import utills
class SpamDetector:
    def __init__(self):
        self.model_name = "AventIQ-AI/distilbert-spam-detection"
        self.tokenizer = DistilBertTokenizer.from_pretrained(self.model_name)
        self.model = DistilBertForSequenceClassification.from_pretrained(self.model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.text = None
    
    def predict_spam(self):
        self.model.eval()  # Set to evaluation mode
        text =self.text
        inputs = self.tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=128).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.softmax(outputs.logits, dim=-1)
            pred_class = torch.argmax(probs).item()
        return "Spam" if pred_class == 1 else "Not Spam"
    def fry(self):
        res = {}
        test_messages = load_dict.load()
        for msg in test_messages:  
            self.text = msg
            prediction = self.predict_spam()
            res[msg] = prediction     
        with open("fullresults.json", "w", encoding="utf-8") as f:
            json.dump(res, f, indent=4, ensure_ascii=False)    
        return res
    def frun(self):
        wrktext =self.fry()
        items =wrktext
        for i in wrktext:
            if wrktext[i] == "Spam":
                items = utills.remove_by_value(items, "Spam")
            else :
                continue
        with open("spam_results.json", "w", encoding="utf-8") as f:
            json.dump(items, f, indent=4, ensure_ascii=False)
        return items
    
    def run(self):
        self.frun()
        return load_dict.different_load()
        
        