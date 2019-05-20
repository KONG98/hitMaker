import sys

class SRT_pipeline:
    TimeStamps=[]
    Lesson_content=[]

    def __init__(self,TimeStamps,Lesson_content):
        self.TimeStamps = TimeStamps
        self.Lesson_content = Lesson_content

class log_pipeline:

    def openLog(self):
        self.f_handler=open('out.log', 'w',encoding='utf-8')
        sys.stdout=self.f_handler
    
    def closeLog(self):
        self.f_handler.close()


LOG = log_pipeline()