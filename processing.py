import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from textblob import TextBlob
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Fonction de prétraitement du texte avec analyse de sentiment et POS
def preprocess_with_features(text):
    # Analyse de sentiment
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    # Le sentiment du text (score compris entre [-1,1]
    if sentiment_score <-0.1 :
        sentiment = "Negatif"
    elif sentiment_score < 0.1 :
        sentiment = "Neutral"
    else :
        sentiment = "Positif"

    stop_words = set(stopwords.words('english'))

    text_sans_mot_vide=""
    word =""
    for caractere in text :
      if caractere !=" ":
        word+=caractere.lower()
      else:
        if word not in stop_words:
          text_sans_mot_vide+=word+" "
        word=""

    # Création d'une liste de textes (dans notre cas, un seul texte)
    corpus = [text_sans_mot_vide]
    # Initialisation du vectoriseur TF-IDF
    vectorizer = TfidfVectorizer()

    # Calcul des scores TF-IDF
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Obtention des noms des mots (features)
    feature_names = vectorizer.get_feature_names_out()

    # Création d'un DataFrame pour afficher les scores TF-IDF
    df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

    # Tri par ordre décroissant des scores TF-IDF pour obtenir les mots les plus pertinents
    top_words = df.transpose().sort_values(0, ascending=False).head(3)
    # Convertir les pertinences en pourcentage
    top_words_percentage = (top_words[0] * 100).round(2)

    # Convertir top_words_percentage en un dictionnaire
    top_words_dict = top_words_percentage.to_dict()

    # Convertir le dictionnaire en une liste de tuples (mot, pertinence en pourcentage)
    top_words_list = list(top_words_dict.items())
    chaine =""
    for item in top_words_list :
       chaine = chaine + " | " + item[0] + " -> " + str(item[1]) + "%"
    return sentiment, chaine
if __name__ == "__main__":
    # Exemple d'utilisation
    sentiment, top_words = preprocess_with_features("Mohamed is a bad man")
    print("Sentiment Score:", sentiment)
    print("Top Words:\n", top_words)
