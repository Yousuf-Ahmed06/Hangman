import sqlite3 as sql
import random

print("Welcome to hangman game")
conn = sql.connect('words.sqlite')
cur = conn.cursor()

diff = input("Welcome to hangman \n Select Difficulty(easy, med, hard): ").lower()
if diff == "easy": diflow = 0; difmax = 7; max_attmp = 12
elif diff == "med": diflow = 7; difmax = 9; max_attmp = 10
elif diff == "hard": diflow = 9; difmax = 14; max_attmp = 8
cur.execute("SELECT word FROM Words WHERE LENGTH(word) > (?) AND LENGTH(word) < (?)", (diflow, difmax))
avl_words = cur.fetchall()
length = len(avl_words)
ran_num = random.randint(0, length)
selc_word = str(avl_words[ran_num]).strip("(',)")
attempt_count = 0
attempted_words = str()
word_guessed = False
sec_word = "_" * len(selc_word)
while attempt_count != max_attmp or word_guessed == False:
    print(f'Guess the word {sec_word}')
    attempt = input("Please enter a letter: ").lower().strip()
    if attempt in attempted_words: print("Word already given, please try a different letter"); continue
    attempted_words = attempted_words + attempt
    
    if attempt in selc_word:
        print("attempt in secret word \n remaining attempts: {(max_attmp - attempt_count)}")
        try:
            index = [w for w, i in enumerate(selc_word) if i == attempt]
            lst = list(sec_word)
            for n in index:
                lst[n] = attempt
            sec_word = "".join(lst)
        except:
            print(f"letter not in the secret word, please try again \n remaining attempts: {(max_attmp - attempt_count)}")
    attempt_count += 1
print(len(avl_words))
print(ran_num)

# ---------------------------
#             |
#             |
#             @
#            /|\
#             |
#            / \

# ___________________________