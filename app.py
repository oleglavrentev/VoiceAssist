import torch
from transformers import AutoTokenizer, AutoModel

from sklearn.metrics.pairwise import cosine_similarity
import sounddevice as sd
import vosk
import numpy as np
import json
import queue

import words
from skills import *
import voice

q = queue.Queue()

model = vosk.Model('model_small')
tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny")
model_bert = AutoModel.from_pretrained("cointegrated/rubert-tiny")

device = sd.default.device  # <--- по умолчанию
# или -> sd.default.device = 1, 3, python -m sounddevice просмотр
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])  # получаем частоту микрофона

def embed_bert_cls(text, model_bert, tokenizer):
    t = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model_bert(**{k: v.to(model_bert.device) for k, v in t.items()})
    embeddings = model_output.last_hidden_state[:, 0, :]
    embeddings = torch.nn.functional.normalize(embeddings)
    return embeddings[0].cpu().numpy()

def callback(indata, frames, time, status):
    '''
    Добавляет в очередь семплы из потока.
    вызывается каждый раз при наполнении blocksize
    в sd.RawInputStream'''

    q.put(bytes(indata))

def classify_cosine_similarity(user_input, vectorized_data_set,
                               tokenizer):
    cl_dist = 0
    cl_phrase = None
    user_input_vectorized = embed_bert_cls(user_input, model_bert, tokenizer)
    for key in vectorized_data_set:
      dist = cosine_similarity(user_input_vectorized, vectorized_data_set[key])
      if dist > cl_dist:
        cl_dist = dist
        cl_phrase = key
    return cl_phrase

def recognize(data, model_bert, tokenizer, vectorized_data_set):
    '''
    Анализ распознанной речи
    '''

    # проверяем есть ли имя бота в data, если нет, то return
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return

    # удаляем имя бота из текста
    data.replace(list(trg)[0], '')

    # получаем вектор полученного текста
    # сравниваем с вариантами, получая наиболее подходящий ответ
    text_vector = embed_bert_cls(data, model_bert, tokenizer)
    answer = classify_cosine_similarity(text_vector, vectorized_data_set,
                                        tokenizer)

    # получение имени функции из ответа из data_set
    func_name = answer.split()[0]

    # озвучка ответа из модели data_set
    voice.speaker(answer.replace(func_name, ''))

    # запуск функции из skills
    exec(func_name + '()')


def main():
    '''
    Обучаем матрицу ИИ
    и постоянно слушаем микрофон
    '''

    # Векторизуем дата сет
    vectorized_data_set = {}
    for data in words.data_set:
        emb = embed_bert_cls(data, model_bert, tokenizer)
        vectorized_data_set[words.data_set[data]] = emb

    del words.data_set

    # постоянная прослушка микрофона
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                           channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, model_bert, tokenizer, vectorized_data_set)
            # else:
            #     print(rec.PartialResult())


if __name__ == '__main__':
    main()