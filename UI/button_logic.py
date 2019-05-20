from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys

from recognizer import getSRT_PRE
from recognizer import getSRT_AFTER


def click_getSRT_1th(self):
    filepath = ''
    pipe = getSRT_PRE(filepath).Lesson
    Lesson_content = pipe.Lesson_content

    for sentence in Lesson_content:
        self.textEdit.append(sentence)

    return pipe


def click_getSRT_2th(self):
    pipe = click_getSRT_1th()
    content = self.textEdit

    Lesson_content = getSRT_AFTER()
