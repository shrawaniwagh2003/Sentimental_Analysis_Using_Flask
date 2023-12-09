from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], 'Positive')
        
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'Negative')
        
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], 'Neutral')

if __name__ == '__main__':
    unittest.main()
















# from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
# import unittest

# class TestSentimentAnalyzer(unittest.TestCase):
#     def test_sentiment_analyzer(self):
#         result_1 = sentiment_analyzer('I love working with Python')
#         self.assertEqual(result_1['label'], 'Positive sentiment')  # Update to match your actual labels
#         result_2 = sentiment_analyzer('I hate working with Python')
#         self.assertEqual(result_2['label'], 'Negative sentiment')  # Update to match your actual labels
#         result_3 = sentiment_analyzer('I am neutral on Python')
#         self.assertEqual(result_3['label'], 'Neutral sentiment')  # Update to match your actual labels

# if __name__ == '__main__':
#     unittest.main()
