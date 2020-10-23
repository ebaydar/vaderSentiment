$ git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        vaderSentiment/.ipynb_checkpoints/
        vaderSentiment/Dictionainnary practice.ipynb
        vaderSentiment/Turkish Vader 2.ipynb
        vaderSentiment/Turkish Vader.ipynb
        vaderSentiment/english_turkish_cache.json
        vaderSentiment/english_turkish_lexicon.txt
        vaderSentiment/mixedlanguage_lexicon.csv
        vaderSentiment/turkish_vader_lexicon.txt
        vaderSentiment/turkish_words_cache.json
        vaderSentiment/turkishlanguagevader_lexicon.txt

nothing added to commit but untracked files present (use "git add" to track)

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   .gitignore

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        vaderSentiment/Dictionainnary practice.ipynb
        vaderSentiment/Turkish Vader 2.ipynb
        vaderSentiment/Turkish Vader.ipynb
        vaderSentiment/english_turkish_cache.json
        vaderSentiment/english_turkish_lexicon.txt
        vaderSentiment/mixedlanguage_lexicon.csv
        vaderSentiment/turkish_vader_lexicon.txt
        vaderSentiment/turkish_words_cache.json
        vaderSentiment/turkishlanguagevader_lexicon.txt

no changes added to commit (use "git add" and/or "git commit -a")

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git add .
warning: LF will be replaced by CRLF in vaderSentiment/Dictionainnary practice.ipynb.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in vaderSentiment/Turkish Vader 2.ipynb.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in vaderSentiment/Turkish Vader.ipynb.
The file will have its original line endings in your working directory

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git commit -am "edit notebooks data"

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'home@MyPC.(none)')

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git config --global user.email "ebaydar2012@gmail.com"

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git config --global user.name "Ert"

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git add .

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   .gitignore
        new file:   vaderSentiment/Dictionainnary practice.ipynb
        new file:   vaderSentiment/Turkish Vader 2.ipynb
        new file:   vaderSentiment/Turkish Vader.ipynb
        new file:   vaderSentiment/english_turkish_cache.json
        new file:   vaderSentiment/english_turkish_lexicon.txt
        new file:   vaderSentiment/mixedlanguage_lexicon.csv
        new file:   vaderSentiment/turkish_vader_lexicon.txt
        new file:   vaderSentiment/turkish_words_cache.json
        new file:   vaderSentiment/turkishlanguagevader_lexicon.txt


home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git commit -am "edit notebooks data"
[master 7f774c2] edit notebooks data
 10 files changed, 159748 insertions(+), 39 deletions(-)
 create mode 100644 vaderSentiment/Dictionainnary practice.ipynb
 create mode 100644 vaderSentiment/Turkish Vader 2.ipynb
 create mode 100644 vaderSentiment/Turkish Vader.ipynb
 create mode 100644 vaderSentiment/english_turkish_cache.json
 create mode 100644 vaderSentiment/english_turkish_lexicon.txt
 create mode 100644 vaderSentiment/mixedlanguage_lexicon.csv
 create mode 100644 vaderSentiment/turkish_vader_lexicon.txt
 create mode 100644 vaderSentiment/turkish_words_cache.json
 create mode 100644 vaderSentiment/turkishlanguagevader_lexicon.txt

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git push
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 8 threads
Compressing objects: 100% (13/13), done.
Writing objects: 100% (13/13), 627.42 KiB | 808.00 KiB/s, done.
Total 13 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
To github.com:ebaydar/vaderSentiment.git
   4a9ca0d..7f774c2  master -> master

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ history
    1  cd code
    2  ls
    3  cd code
    4  ls
    5  cd code
    6  ls
    7  pwd
    8  cd ..
    9  ls
   10  cd Users
   11  ls
   12  cd home
   13  ls
   14  cd code
   15  ls
   16  cd python_experiments/
   17  code
   18  ipython
   19  ls
   20  conda
   21  ls
   22  ls -al
   23  ls -al ~
   24  which deactivate
   25  cd ..
   26  cd ..
   27  ls
   28  cd Anaconda3/
   29  ls
   30  ls



home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   vaderSentiment/turkish_sentiment.py

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git add .

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   vaderSentiment/turkish_sentiment.py

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git commit -am "updated py file"
[master d5c058a] updated py file
 1 file changed, 56 insertions(+), 1 deletion(-)
____________________________________
-a
--all
Tell the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected.

-m <msg>
--message=<msg>
Use the given <msg> as the commit message. If multiple -m options are given, their values are concatenated as separate paragraphs.
____________________________________
home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

home@MyPC MINGW64 /c/Users/home/code/vaderSentiment (master)
$ git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.04 KiB | 267.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:ebaydar/vaderSentiment.git
   91ca499..d5c058a  master -> master
