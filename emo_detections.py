#Новый алгоритм распознавания эмоций
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# нужные ресурсы NLTK загружены
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")
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
    ru_sentence = "Я люблю яблоки"
    example_sentence = pipe(f"{ru_sentence}")  # тут меняй переменную как хочешь, чтобы она могла быть встроеннна в бота
    print(example_sentence)
    print(example_sentence[("translation_text", 1)])
    result = analyze_emotion(example_sentence) # это лучше не менять, есть шанс что всё сломаеться :)
    # вывод результата
    print("\n--- Анализ эмоции ---")
    print(f"Предложение: {result['sentence']}")
    print(f"Оценки: {result['scores']}")
    print(f"Обнаруженные эмоции: {', '.join(result['detected_emotions'])}\n")
