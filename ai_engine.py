# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("question-answering", model="google/bigbird-base-trivia-itc")
