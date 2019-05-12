from tikTokMaker import *

breakPoints = [0.12,0.22,1.02,1.22,2.02,2.15,3.02,3.15,4.15,4.20,5.13,6.20,
                    7.07,8.05,9.17,10.00,11.0,12.10,12.30,15.10,16.00]

a  = tkHit_Speed(Name = 'higher',M = 1, speedRate = 5,breakPoints = breakPoints,clipName='video.mp4')
a.run('BGM.mp3')