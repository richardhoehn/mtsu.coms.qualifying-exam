# MTSU COMS - Qualifying Exam

## Title

Improving Emotion Detection through Translation of Text to ML Models Trained in Different Languages

## Abstract

This Qualifying Exam research paper investigates the potential of improving Emotion Detection (ED) through translation of extended text data to multiple Machine Learning (ML) models trained in different languages. Our research focused on  English and German (voting articles) datasets to improve prediction accuracy. By this our research aims to address the challenges posed by the lack of comprehensive labeled datasets and language fragmentation in ED research and projects.

By extending an original English language dataset with a translated dataset from German to English the training data (extended dataset) becomes larger and the hope is that better prediction rates can be achieved in ED analysis applications due to ML training having more data for learning. Furthermore, translating English to German to extend the German dataset and training another ML model using PySpark and accessing both models in real-time by a simple RESTful API may improve the prediction rates even more by dual processing a sentence at the same time.

In order to present the results presented both orally to the MTSU's Computational Data & Science Committee and within this paper labeled datasets both in English and German were collected, parsed, cleaned, translated, and two ML models built that can be accessed via an API to get a prediction by inputting sentences both in German or English via GET method using a simple query-string.

Sadly the research and results point to the realization that extending the datasets by translation did not improve prediction rates of English or German. Some minor gains can be achieved by accessing both English and German models at the same time via the RESTful API but unfortunately the benefits may not really support the efforts. In conclusion it that much more data needs to be collected in order to be able to definitely answer this research question.

## Translater Information

Using Python libs to translate. I used the `deep-translator` by installing using `pip` with the following command: `pip install deep-translator`.
I used the following link: `https://medium.com/analytics-vidhya/how-to-translate-text-with-python-9d203139dcf5`

I installed `pip3 install googletrans==4.0.0-rc1` for PySpark translation.

## Dataframe Work

I installed the following: `pip install -q transformers` and `pip install torch` and `pip install matplotlib`



 "boredom",
    "love",
    "relief",
    "fun",
    "hate",
    "neutral",
    "anger",
    "happiness",
    "surprise",
    "sadness",
    "worry",
    "enthusiasm",
    "empty",
    "---",