
def GenerateSentencesTimeStamp(AudioChunks):
    BeginTime = 0
    TimeStampChunks = []
    Index = list(range(len(AudioChunks)))
    for i in Index:
        CLen = len(AudioChunks[i])
        TimeStampChunks.append({"Begin":BeginTime,"End":BeginTime + CLen})
        BeginTime = BeginTime + CLen
    return TimeStampChunks

def GenerateSrtFormatFile(TimeStampList,Lesson_content):
    print(' *'*20,'生成srt开始',' *'*20)
    with open("subtitle.srt","w",encoding='utf-8') as handle:
        Index = list(range(len(TimeStampList)))
        for i in Index:
            handle.write(str(i + 1)+"\n")
            (Hour1, Minus1, Second1, MileSecond1) = GenerateHMSMSFromMileSecond(TimeStampList[i]["Begin"])
            (Hour2, Minus2, Second2, MileSecond2) = GenerateHMSMSFromMileSecond(TimeStampList[i]["End"])
            handle.write("%02d:%02d:%02d,%03d --> %02d:%02d:%02d,%03d\n" % (Hour1, Minus1, Second1, MileSecond1, Hour2, Minus2, Second2, MileSecond2))
            handle.write(str(Lesson_content[i]))
            handle.write("\n")
    print(' *'*20,'生成srt结束',' *'*20)

def GenerateHMSMSFromMileSecond(mileSecond):
    miles = mileSecond % 1000
    sec = mileSecond / 1000
    min = sec / 60
    sec = sec % 60
    hour = min / 60
    min = min % 60
    return (hour,min,sec,miles)