from pydub import AudioSegment

AudioSegment.from_wav("file_Instruments.wav").export("file_Instruments.mp3", format="mp3")
AudioSegment.from_wav("file_Vocals.wav").export("file_Vocals.mp3", format="mp3")
