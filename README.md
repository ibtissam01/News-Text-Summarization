# News-Text-Summarization
![image](https://github.com/ibtissam01/News-Text-Summarization/assets/89752387/7e3b32be-e105-4c5d-b8b8-ca713c6f457a)

# Plateforme de Résumé Automatique d'Articles d'Al Jazeera

Ce projet vise à développer une plateforme de résumé automatique de textes à partir des articles d'Al Jazeera. Le résumé automatique de texte consiste à générer une version condensée et précise d'un document textuel en utilisant des techniques informatiques. Notre objectif est de fournir aux utilisateurs un résumé clair et concis du contenu des articles d'Al Jazeera.

![image](https://github.com/ibtissam01/News-Text-Summarization/assets/89752387/3e29c142-0e8f-47c6-8280-a37394fb2249)

## Réalisé par :
- Ibtissam LABYADY
- Sokhna Mai WANE
- Mohamed CISSE
## Encadré par:
- Najima DAOUDI
- Ghizlane BOURAHOUAT
## Technologies utilisées
![image](https://github.com/ibtissam01/News-Text-Summarization/assets/89752387/a2c94d2f-35c8-4e5f-bd49-a2f0a24552a9)

Nous avons utilisé les technologies suivantes pour la réalisation de ce projet :

- Web Scraping : Nous avons extrait les articles d'Al Jazeera à partir des sites web suivants :
  - [Al Jazeera English](https://www.aljazeera.com/)
  - [Al Jazeera Arabic](https://www.aljazeera.net/)

- Modèles de résumé automatique :
  - T5: Text-To-Text Transfer Transformer
  - Modèle BART
  - PEGASUS

## Approche adoptée
Nous avons exploré deux approches différentes pour générer des résumés dans la langue cible :

1. Utilisation de la traduction avec un modèle pré-entraîné : Nous avons utilisé des modèles pré-entraînés T5, BART et PEGASUS pour traduire les articles en langue cible, puis nous avons généré des résumés à partir des traductions.

2. Fine-tuning sur des données dans la langue cible : Nous avons effectué un fine-tuning des modèles de T5  en utilisant des données dans la langue cible. Cela nous a permis d'adapter les modèles aux spécificités de la tâche de résumé et d'améliorer leur capacité à produire des résumés pertinents et de qualité.

## Évaluations des modèles fine-tunés
Nous avons évalué les performances des modèles fine-tunés sur notre tâche de résumé en utilisant les métriques appropriées. Voici les modèles fine-tunés que nous avons évalués :
![image](https://github.com/ibtissam01/News-Text-Summarization/assets/89752387/0ed674e4-b13d-4274-8443-c343b66b3ec4)

- Modèle T5 fine-tuné pour la génération de résumés de news : [ibtissam369/t5-base-finetuned-summarize-news-finetuned-xsum](https://github.com/ibtissam369/t5-base-finetuned-summarize-news-finetuned-xsum)

![image](https://github.com/ibtissam01/News-Text-Summarization/assets/89752387/c3841c64-419e-4de0-af2b-4245b2f8ab4e)

- Modèle AraT5v2 fine-tuné pour la génération de résumés d'articles d'Al Jazeera : [ibtissam369/AraT5v2-base-1024-finetuned-ALjazeera](https://github.com/ibtissam369/AraT5v2-base-1024-finetuned-ALjazeera)

## Conclusion
En conclusion, les modèles RNN (Réseaux de Neurones Récurrents) et LLMs (Langage Models) offrent des avantages significatifs pour les tâches de résumé grâce à leur capacité à capturer les dépendances contextuelles à long terme et à être adaptés à travers le fine-tuning. Cependant, il reste des défis à relever, tels que la génération de résumés cohérents et la gestion des ressources computationnelles. De plus, l'extension de ces modèles à des langues spécifiques comme le darija nécessite des efforts supplémentaires de collecte de données et de formation.
