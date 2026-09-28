import pandas as pd

# Load Excel file
df = pd.read_excel('260929_aardvark_all_opinions.xlsx', engine='openpyxl')

# Sentiment word lists
positive_words = [
    'love','enjoy','admire','appreciate','grateful','charming','lovable',
    'fascinating','peaceful','unique','gentle','calm','alive','help',
    'support','balance','eventful','adorable','strength','surprises',
    'healthy','special','curious','thriving','beautiful'
]

negative_words = [
    'don’t','dont','not','dislike','annoy','frustrating','uncomfortable',
    'odd','strange','ignored','grumpy','slow','smell','quiet','serious',
    'discouraging','eerie','unexciting','too','hard','rarely','never',
    'avoid','disappointed','let down','intimidating','unpredictable',
    'hesitant'
]

# Sentiment classifier function
def classify_sentiment(text):
    text_lower = str(text).lower()
    pos = any(word in text_lower for word in positive_words)
    neg = any(word in text_lower for word in negative_words)
    
    if pos and not neg:
        return 'positive'
    elif neg and not pos:
        return 'negative'
    elif pos and neg:
        return 'mixed'
    else:
        return 'neutral'

# Apply sentiment classifier
df['sentiment'] = df['response'].apply(classify_sentiment)

# Save to CSV
df[['response','sentiment']].to_csv('aardvark_sentiment.csv', index=False)

print("CSV file successfully created: aardvark_sentiment.csv")
