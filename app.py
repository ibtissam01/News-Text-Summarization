from flask import Flask, render_template, request as req
from transformers import BartTokenizer, BartForConditionalGeneration
import processing
app = Flask(__name__)


# Charger le modèle BART et le tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)


# Fonction de summarization
def summarize_text(text, maxL):
    # Tokenization : pretraitement et nettoyage de données
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)

    # Générer le résumé
    summary_ids = model.generate(inputs["input_ids"], max_length=maxL, min_length=20, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if req.method == "POST":

        data = req.form["data"]
        maxL = int(req.form["maxL"])

        summary = summarize_text(data,maxL)
        print(maxL,summary)
        word_count=len(summary.split(' '))

        sentiment, chaine = processing.preprocess_with_features(data)
        return render_template("index.html", result=summary, word_count=str(word_count),sentiment=sentiment,pertinence=chaine)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
