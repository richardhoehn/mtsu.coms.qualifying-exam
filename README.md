# MTSU COMS - Qualifying Exam

## Title

Improving Emotion Detection through Translation of Text to ML Models Trained in Different Languages

## Abstract

This Qualifying Exam research paper investigates enhancing Emotion Detection (ED) by translating extended text data into various Machine Learning (ML) models trained in distinct languages. We focused on English and German text data to enhance prediction accuracy, aiming to overcome challenges arising from limited labeled datasets and language fragmentation in ED research.

Expanding an original English dataset with translated German data increases the training data's volume, potentially improving prediction rates in ED applications. Additionally, translating English to German to extend the German dataset and accessing in real-time ML models trained in both could further improve prediction rates.

For presentation purposes, datasets in both English and German were collected, parsed, cleaned, and translated. Multiple ML models trained in English and German where built, and made accessible via an API for predictions in either language including real-time translation using a GET method.

The research findings suggest that the extension of datasets through translation has not yielded improvements in predictive accuracy for both English and German languages. Modest enhancements could potentially be achieved by concurrently accessing English and German models through real-time translation via the RESTful API; however, the benefits may not fully justify the efforts.

We posit that the prevalence of numerous classes in this multi-class classification model has contributed to instances of overfitting across several labels/classes. This occurrence, in turn, has led to a memorization effect rather than facilitating genuine learning within the models.

In conclusion, it becomes evident that a more substantial accumulation of data is required, or an innovative approach involving the utilization of AI to generate analogous data must be employed to comprehensively address this research question.

## Translater Information

Using Python libs to translate. I used the `deep-translator` by installing using `pip` with the following command: `pip install deep-translator`.
I used the following link: `https://medium.com/analytics-vidhya/how-to-translate-text-with-python-9d203139dcf5`

I installed `pip3 install googletrans==4.0.0-rc1` for PySpark translation.

## Dataframe Work

I installed the following: `pip install -q transformers` and `pip install torch` and `pip install matplotlib`
