from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Initiate the Flask app
app = Flask("Sentiment Analyzer")

# Threshold for considering sentiment valid
VALID_SENTIMENT_THRESHOLD = 0.05

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid input! Please provide a non-empty text."

    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']

    # Check if sentiment is valid based on the threshold
    if abs(score) < VALID_SENTIMENT_THRESHOLD:
        return "Invalid input! Please provide a more meaningful text."

    return "The given text has been identified as {} with a score of {}.".format(label, score)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)





# from flask import Flask, request
# from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# app = Flask(__name__)

# @app.route("/sentimentAnalyzer")
# def sent_analyzer():
#     text_to_analyze = request.args.get('textToAnalyze')
#     response = sentiment_analyzer(text_to_analyze)
#     label = response['label']
#     score = response['score']

#     if label is None:
#         return "Invalid input! Try again."
#     else:
#         return "The given text has been identified as {} with a score of {}.".format(label, score)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)


# from flask import Flask, render_template, request
# from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# app = Flask("Sentiment Analyzer")

# @app.route("/sentimentAnalyzer")
# def sent_analyzer():
#     text_to_analyze = request.args.get('textToAnalyze')
#     response = sentiment_analyzer(text_to_analyze)
#     label = response['label']
#     score = response['score']

#     if label is None:
#         return "Invalid input! Try again."
#     else:
#         label_parts = label.split('_')
#         if len(label_parts) >= 2:
#             return "The given text has been identified as {} with a score of {}.".format(label_parts[1], score)
#         else:
#             return "The given text has been identified as {} with a score of {}.".format(label, score)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)











# ''' Executing this function initiates the application of sentiment
#     analysis to be executed over the Flask channel and deployed on
#     localhost:5000.
# '''
# from flask import Flask, render_template, request
# from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# #Initiate the flask app : TODO
# app = Flask("Sentiment Analyzer")

# @app.route("/sentimentAnalyzer")
# def sent_analyzer():
#     text_to_analyze = request.args.get('textToAnalyze')
#     response = sentiment_analyzer(text_to_analyze)
#     label = response['label']
#     score = response['score']

#     if label is None:
#         return "Invalid input! Try again."
#     else:
#         return "The given text has been identified as {} with a score of {}.".format(label, score)

# @app.route("/")
# def render_index_page():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)
