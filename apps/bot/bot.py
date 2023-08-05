import os

import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from utils.media import get_text_from_file, read_all_files


class StatefulChatbot:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "bert-large-uncased-whole-word-masking-finetuned-squad")
        self.model = AutoModelForQuestionAnswering.from_pretrained(
            "bert-large-uncased-whole-word-masking-finetuned-squad")
        self.knowledge_base = read_all_files()

    def update_knowledge_base(self, file):
        self.knowledge_base += " " + get_text_from_file(f'media/{file}')

    def answer_question(self, question):
        inputs = self.tokenizer.encode_plus(
            question, self.knowledge_base, return_tensors="pt")
        outputs = self.model(**inputs)
        answer_start = torch.argmax(outputs.start_logits)
        answer_end = torch.argmax(outputs.end_logits) + 1
        answer = self.tokenizer.convert_tokens_to_string(
            self.tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end]))

        if len(answer.split()) < 3:
            return "I'm sorry, but I don't have information on that topic."

        return answer
