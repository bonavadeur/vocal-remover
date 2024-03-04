handle/venv/Scripts/python handle/convert_mp4_mp3.py
rm file.mp4

mv file.mp3 handle/
cd handle
venv/Scripts/python inference.py --input 'file.mp3'
cd ..
mv handle/file.mp3 .
mv handle/*.wav .

handle/venv/Scripts/python handle/convert_wav_mp3.py
rm file_Instruments.wav
rm file_Vocals.wav
