#Новый алгоритм распознавания эмоций
import nltk
import re
from nltk.sentiment import SentimentIntensityAnalyzer

# нужные ресурсы NLTK загружены
nltk.download('vader_lexicon')

# Инициализация анализатора тональности
sia = SentimentIntensityAnalyzer()

# список эмоций
EMOTIONS = {
    "радость": ["happy", "joy", "pleased"],
    "печаль": ["sad", "sorrow", "unhappy"],
    "гнев": ["angry", "mad", "furious"],
    "страх": ["fear", "scared", "afraid"],
    "удивление": ["surprised", "shocked", "amazed"],
    "отвращение": ["disgust", "repulsion", "distaste"],
    "восторг": ["delight", "ecstatic", "thrilled"],
    "гордость": ["proud", "pride", "accomplished"],
    "вина": ["guilt", "guilty", "remorse"],
    "стыд": ["shame", "ashamed", "embarrassed"],
    "вдохновение": ["inspired", "inspiring", "motivated"],
    "зависть": ["envy", "jealous", "covet"],
    "умиротворение": ["calm", "peaceful", "relaxed"],
    "скука": ["bored", "boredom", "uninterested"],
    "неуверенность": ["uncertain", "doubt", "hesitant"],
    "обида": ["offended", "hurt", "resentful"],
    "любопытство": ["curious", "inquisitive", "interested"],
    "уверенность": ["confident", "certain", "assured"],
    "разочарование": ["disappointed", "frustrated", "let down"],
    "надежда": ["hope", "hopeful", "optimistic"]
}


def analyze_emotion(sentence):

    scores = sia.polarity_scores(sentence)

    detected_emotions = []
    for emotion, keywords in EMOTIONS.items():
        if any(keyword in sentence.lower() for keyword in keywords):
            detected_emotions.append(emotion)

    # Если эмоции не найдены, оставляем нейтральное значение
    if not detected_emotions:
        detected_emotions = ["Нейтрально"]

    return {
        'sentence': sentence,
        'scores': scores,
        'detected_emotions': detected_emotions
    }

# запуск
if __name__ == "__main__":
    example_sentence = "I feel so proud and accomplished today!" #тут меняй переменную как хочешь, чтобы она могла быть встроеннна в бота
    result = analyze_emotion(example_sentence) # это лучше не менять, есть шанс что всё сломаеться :)
    # вывод результата
    print("\n--- Анализ эмоции ---")
    print(f"Предложение: {result['sentence']}")
    print(f"Оценки: {result['scores']}")
    print(f"Обнаруженные эмоции: {', '.join(result['detected_emotions'])}\n")
