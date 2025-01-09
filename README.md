# Fake Version History
## Introduction
Python script for appending text to a word document in order to fake the version history. The purpose of this was to find a way to take pre-written text and paste it into a document such that you could fake the version history to where it could stand up to mild scrutiny. The idea behind this is that if you use an AI LLM to write an essay for you, if someone were to challenge you on the authenticity you would be able to show them the version history in the cloud version to "prove" you wrote the document.

As of right now, the entire script was written by ChatGPT with minor tweaks by me (paths, times, etc.). The purpose of this was to prove that someone could complete this task using ChatGPT alone and starting with a mild understanding of software coding, namely being able to set up an environment to run Python. Obviously, you can use ChatGPT to explain everything and teach you the process if you have no knowledge, but I already had the knowledge so I didn't need to do that. 

## What this does
This takes input text and breaks it down into random chunks that it appends and saves to a document in random intervals, to create the iillusion of a person writing this themselves. This results in a document which has version history that looks at least mildly believeable under mild scutiny. 

## Where the project currently stands
- Only supports .docx file type
- Only tested with Microsoft Word / OneDrive
- Requirements:
  - (Optional) Windows Subsystem for Linux 2 https://learn.microsoft.com/en-us/windows/wsl/
    - This just makes it easier to setup and work with Python in my opinon.
  - (Optional) Git https://docs.github.com/en/get-started/getting-started-with-git/set-up-git
    - This is just for downloading the repo. You can also choose to just download in your browser and unzip the file.
  - Python3 setup on your computer. https://www.python.org/downloads/
    - python-docx package
  - Office/Microsoft 365
    - OneDrive
      - Need to have a folder on your computer that is synced to OneDrive and make sure sync is on.
    - Word
      - Just the online version, you don't need the installed version. 
  - Your essay that has already been written by AI or someone else.

## How to use
1. Clone this repo to where you have Python3 setup. 
    - If you are using WSL you can use git to clone the repo by using `git clone git@github.com:fitz250/FakeVersionHistory.git`
    - If you don't want to use git, click on Code above and then choose 'Download ZIP'. Then unpack the file.
2. Open OneDrive in your browser and go to the folder that is synced. 
3. Create a new word document and give it a name. This will be your final file that has the version history. 
4. Open the file and enter a title then a new line, just like you'd do if you were writing the essay. Save and close the file. 
5. Download the file and place it in the folder on your actual computer. Make sure you see the OneDrive status show it is synced.
6. Rename `variables_example.py` to `variables.py`
7. In `variables.py` change the value of `document_path` to the path where you just saved the file on your computer. So like `C:\Users\{your_username}\OneDrive\Documents\myfile.docx`
    - If using WSL, use forward slashes `/` and make sure you include the necessary `/mnt/` before the path so WSL knows to go to the Windows part of the computer. 
8. In `variables.py` the variable `input_text` will be where you input the text of the essay you want it to write.
    - Copy each paragraph of the source essay on to a new line, surrounded by double-quotes, with a comma at the end of each line except the last line. Look at the example to get an idea. 
9. Open `fakeversionhistory.py`
10. On line 24, `word_count` determines how many words will be appended each time it tries, randomly secting a number between the 2 supplied options in `random.randint`. There's 2 numbers at the end, change those to the minimum and maximum number of words you want it to append each time. Make sure they are not the same. 
11. On line 47, `wait_time` determines how long it waits, in seconds, before trying to append the next chunk of words and then saving. Again, this will randomly select a number between the 2 values in `random.randint`, which is set to 120 (2 minutes) and 300 (5 minutes) by default.  This will also be the amount of time between saves shown in version history, so choose a number that would make sense for how long it would take to write each chunk based on the chunk size you set earlier.
12. Save any changes.
13. Open the terminal on your computer and go to where you have the files for this project saved.
14. In the terminal, run `python3 fakeversionhistory.py`
15. You should now see it start working. It will tell you how many words it is appending from each line as it goes. 
16. This will run in the background, so feel free to watch Youtube or something while you wait, just **do not close the terminal or open the output file until you see it finish in the terminal**. It will say `Text appending completed.` when finished. 
    - If you need to stop the script for whatever reason, you should be able to use `Ctrl + C` in the terminal to interrupt it.

## Future plans
- Add support for Google Docs
- Add a way to also make revisions and edits that look natural
- Streamline setup process so it's easier for people with no coding knowledge. 


