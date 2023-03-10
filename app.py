from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import sounddevice as sd
import vosk
import json
import queue

import words
from skills import *
import voice
from PyQt5 import QtWidgets
import sys
import newinterface
import threading



q = queue.Queue()
model = vosk.Model('model_small')
device = sd.default.device  # <--- по умолчанию
# или -> sd.default.device = 1, 3, python -m sounddevice просмотр
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])  # получаем частоту микрофона


class Assist(QtWidgets.QMainWindow, newinterface.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле newinterface.py
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.start_thread_assist)
        self.pushButton_2.pressed.connect(self.off)

    def callback(self ,indata, frames, time, status):
        '''
        Добавляет в очередь семплы из потока.
        вызывается каждый раз при наполнении blocksize
        в sd.RawInputStream'''

        q.put(bytes(indata))


    def recognize(self, data, vectorizer, clf):
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
        text_vector = vectorizer.transform([data]).toarray()[0]
        answer = clf.predict([text_vector])[0]

        # получение имени функции из ответа из data_set
        func_name = answer.split()[0]

        # озвучка ответа из модели data_set
        voice.speaker(answer.replace(func_name, ''))
        #добавления ответа в qt disegner
        item = QtWidgets.QListWidgetItem()
        item.setText(answer.replace(func_name, ''))
        self.listWidget.addItem(item)



        # запуск функции из skills
        exec(func_name + '()')

    def off(self):
        '''Отключает бота'''
        sys.exit()

    def start_thread_assist(self):
        thread = threading.Thread(target=self.main, args=())
        thread.start()

    def main(self):
        '''
        Обучаем матрицу ИИ
        и постоянно слушаем микрофон
        '''

        #Обучение матрицы на data_set модели
        vectorizer = CountVectorizer()
        vectors = vectorizer.fit_transform(list(words.data_set.keys()))

        clf = LogisticRegression()
        clf.fit(vectors, list(words.data_set.values()))

        del words.data_set

        # постоянная прослушка микрофона
        with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                               channels=1, callback=self.callback):

            rec = vosk.KaldiRecognizer(model, samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    data = json.loads(rec.Result())['text']
                    self.recognize(data, vectorizer, clf)
                # else:
                #     print(rec.PartialResult())


    #if __name__ == '__main__':
        #main()
app = QtWidgets.QApplication([])
window = Assist()
window.show()
app.exec_()