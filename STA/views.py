from django.shortcuts import render
from rest_framework.views import APIView
from STA.serializers import SignUpSerializer, LoginSerializer
from STA.permissions import *
from STA.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from langdetect import detect
import h5py
import tensorflow as tf
import numpy as mp
from keras.preprocessing.text import Tokenizer
import tensorflow as tf
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.datasets import imdb
from hazm import Normalizer, word_tokenize, stopwords_list
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer
import joblib
import os
import numpy as np
import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier


def detect_spam(input_string):
    
    df = pd.read_csv("C:\code\smart-text-analysis-dj\STA\sms_dataset.tsv", delimiter='\t')

    X = df.message   # X_feature
    y = df.label   # y_label
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    count_vectorizer = CountVectorizer()
    tfidf_transformer = TfidfTransformer()

    count_vectorizer.fit(X_train)
    X_train_cv = count_vectorizer.transform(X_train)
    tfidf_transformer.fit(X_train_cv)
    X_train_tfidf = tfidf_transformer.transform(X_train_cv)

    X_test_cv = count_vectorizer.transform(X_test)
    X_test_tfidf = tfidf_transformer.transform(X_test_cv)

    # Initialize the classifiers
    naive_bayes = MultinomialNB()
    linear_svc = LinearSVC()
    decision_tree = DecisionTreeClassifier()

    # Create the voting classifier
    voting_classifier = VotingClassifier(
        estimators=[('nb', naive_bayes), ('svc', linear_svc), ('dt', decision_tree)],
        voting='hard'  # Use 'hard' voting for majority voting
    )


    voting_classifier.fit(X_train_tfidf, y_train)


    prediction = voting_classifier.predict(X_test_tfidf)




    print(classification_report(y_test, prediction))
    print("Accuracy: ", accuracy_score(y_test, prediction))




    def predict_spam(input_string):
        # Load the saved model
        loaded_model = joblib.load("C:\code\smart-text-analysis-dj\STA\spam_detection_ensemble.joblib")


        input_tfidf = tfidf_transformer.transform(count_vectorizer.transform([input_string]))


        prediction = loaded_model.predict(input_tfidf)

        return "Spam" if prediction[0] == 1 else "Not Spam"
    result = predict_spam(input_string)
    print(f" - Prediction: {result}")
    return "Accuracy: " + str(accuracy_score(y_test, prediction).round()) + '\nPrediction:' + result


# views here.

def preprocess_input(sentence, tokenizer, max_len):
    normalizer = Normalizer()
    normalized_text = normalizer.normalize(sentence)
    words = word_tokenize(normalized_text)
    words = [w for w in words if w not in stopwords_list()]
    encoded_text = tokenizer.texts_to_sequences([' '.join(words)])
    padded_sequence = pad_sequences(encoded_text, maxlen=max_len, padding='post')
    return padded_sequence

class UserSignUpAPI(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = ()
    authentication_classes = ()
    
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class LoginApiView(APIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            serializer = LoginSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                user = serializer.validated_data['user']
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class STAApiView(APIView):
    permission_classes = ()
    authentication_classes = ()
    def post(self, request):
        data = request.data



        #sentiment of text
        if data['output-type'] == 'sen' :
            lang = detect(data['input'])
            print(lang)
            if lang == 'fa':
                df= pd.read_csv("C:\code\smart-text-analysis-dj\STA\data.csv")
                texts = df.Text.values
                FA_tokenizer = Tokenizer(num_words=5000, oov_token='<UNK>')
                FA_tokenizer.fit_on_texts(texts)
                padded_input = preprocess_input(data['input'], FA_tokenizer, 100)
                FA_loaded_model = tf.keras.models.load_model("C:\code\smart-text-analysis-dj\STA\Per_Sen_Analysis_Model.hdf5")
                FA_prediction  = FA_loaded_model.predict(padded_input)
                FA_sentiment = "Positive" if FA_prediction[0][0] >= 0.5 else "Negative"
                print("FA ---->"  , " : " , FA_prediction  , " : " , FA_sentiment  )
                return Response({
                'message' :'result: ' + str(FA_prediction)  + " sentiment: " + str(FA_sentiment),
                },status=status.HTTP_200_OK)
        # Convert the predicted score to a binary sentiment label

        
            elif lang == 'en':
                word_to_index = imdb.get_word_index()
                VOCAB_SIZE = 30000  # Ensure VOCAB_SIZE is the same as used during training
                tokenizer = Tokenizer(num_words=VOCAB_SIZE)
                tokenizer.word_index = word_to_index
                input_sequence = tokenizer.texts_to_sequences([data['input']])
                input_sequence = pad_sequences(input_sequence, maxlen=2494)
                new_model = tf.keras.models.load_model("C:\code\smart-text-analysis-dj\STA\EN_Sen_Analysis_Model.h5")
                prediction = new_model.predict(input_sequence)[0][0]
                sentiment = "Positive" if prediction >= 0.5 else "Negative"
                print( " : " , prediction  , " : " , sentiment  )
                return Response({
                'message' : 'result: ' + str(prediction)  + " sentiment: " + str(sentiment),
                },status=status.HTTP_200_OK)
            else:
                return Response({
                'error' : 'invalid input',
            },status=status.HTTP_400_BAD_REQUEST)




        elif data['output-type'] == 'sum':
            pass




        #spam detect
        elif data['output-type'] == 'spa':
            res = detect_spam(data['input'])
            return Response({
                'message' : res,
                },status=status.HTTP_200_OK)
        else:
            return Response({
                'error' : 'invalid input',
            },status=status.HTTP_400_BAD_REQUEST)
        