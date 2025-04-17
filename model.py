import json
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import load_dict

class Model:
    def __init__(self):
        self.model_name = "tabularisai/multilingual-sentiment-analysis"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.texts = load_dict.load()

    def predict_sentiment(self , texts):
        inputs = self.tokenizer(texts, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        
        sentiment_map = {0: "Very Negative", 1: "Negative", 2: "Neutral", 3: "Positive", 4: "Very Positive"}
        return [sentiment_map[p] for p in torch.argmax(probabilities, dim=-1).tolist()]

    def run(self):
        if isinstance(self.texts, str):
            texts = [texts]
        results = {text: sentiment for text, sentiment in zip(self.texts, self.predict_sentiment(self.texts))}
        with open ("results.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(results, indent=4, ensure_ascii=False))

    def display_results(self):
        if isinstance(self.texts, str):
            texts = [texts]
        results = {text: sentiment for text, sentiment in zip(self.texts, self.predict_sentiment(self.texts))}
        return (json.dumps(results, indent=4, ensure_ascii=False))
