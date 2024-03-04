# VOCAL-REMOVER
## 1. Introduction
This repo is folked from [tsurumeso/vocal-remover](https://github.com/tsurumeso/vocal-remover)  
I modified that repo for people who need remove vocal from a .mp4 file.  
## 2. Requirements
+ `Python` is installed, version >= 3.11 (I have not tried with older version)  
+ `Python Virtual Environment` is installed  
+ `ffmpeg` is installed and added to computer's environment  
+ Operating System: `Windows`  
+ `git bash` is installed  
## 3. Installation
+ Step 1: clone this repo  
+ Step 2: create python venv and install required packages:
```bash
cd handle
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
## 4. Usage
- Step 1: copy .mp4 file to this folder and rename it to `file.mp4`  
- Step 2: using `git bash` to run `run.sh` file, or double click to `run.sh` file if your computer run any .sh file using `git bash` by default  
- Step 3: wait until the black window turn off itself (about 1-2 minutes). You will receive 3 new files:  
    - `file.mp3`: audio-only part of original file.mp4  
    - `file_Instruments.mp3`: vocal-removed audio file  
    - `file_Vocals.mp3`: vocal audio file  
## 5. Conclusion
This repo is own of Bonachan  
