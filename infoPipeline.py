import sys


class SRT_pipeline:
    TimeStampList = []
    Lesson_content = []

    def __init__(self, TimeStampList, Lesson_content):
        self.TimeStampList = TimeStampList
        self.Lesson_content = Lesson_content


class log_pipeline:

    def openLog(self):
        self.f_handler = open('out.log', 'w', encoding='utf-8')
        sys.stdout = self.f_handler

    def closeLog(self):
        self.f_handler.close()


LOG = log_pipeline()
