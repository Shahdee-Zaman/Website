from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)

app.secret_key = 'weirdo'


# Getting the word from a list(will swap to maybe using api once I am better at it)
def get_word():
    choices = ['Joule', 'Where', 'Give', 'Me']
    return random.choice(choices).upper()


# Initializing the  hangman game
def start():
    session['word'] = get_word()
    session['guess'] = []
    session['tries'] = 0
    session['blank'] = ['_'] * len(session['word'])
    session['attempts'] = 6


# Drawing for the hangman game
def drawing(index):
    draw = ["static/img/hangman_stage_0.png", "static/img/hangman_stage_1.png", "static/img/hangman_stage_2.png",
            "static/img/hangman_stage_3.png", "static/img/hangman_stage_4.png", "static/img/hangman_stage_5.png",
            "static/img/hangman_stage_6.png", "static/img/hangman_stage_7.png"]
    return draw[index]


# ------------------- End of Functions For The Hangman Game ---------------------------

@app.route('/')
def index():
    return render_template('templates.html', hangman=redirect(url_for('hangman')))


@app.route('/hangman', methods=['GET', 'POST'])
def hangman():
    # tart game and ensure new game is not started when site is refreshed
    if 'word' not in session:
        start()

    guessed_word = ''
    if request.method == 'POST':
        guessed_word = request.form.get("guess_user", "").upper()

        # Ensure the word user is guessing matches all requirements
        if len(guessed_word) == 1 and guessed_word.isalpha() and guessed_word not in session['guess']:
            session['guess'].append(guessed_word)

            #The blank is swapped with the guessed word if it was correct
            if guessed_word in session['word']:
                for i in range(len(session['word'])):
                    if session['word'][i] == guessed_word:
                        session['blank'][i] = guessed_word
                        print(session['blank'])
                    else:
                        session['blank'][i] = session['blank'][i]

            else:
                session['tries'] += 1
                session['attempts'] -= 1
            session.modified = True

    # No more _ blanks left as such all words were correctly guessed by the user
    if '_' not in session['blank']:
        return render_template('hangmanWin.html', word=session['word'], restart=redirect(url_for('restart')))
    # No more tries left so the user loses
    elif session['attempts'] <= 0:
        return render_template('hangmanLoss.html', word=session['word'], restart=redirect(url_for('restart')))

    return render_template('hangman.html', word=session['word'],
                           guess=session['guess'], attempts=session['attempts'], blank=session['blank'],
                           hangman=drawing(session['tries']), restart=redirect(url_for('restart')))


@app.route('/restart')
def restart():
    start()
    return redirect(url_for('hangman'))


if __name__ == '__main__':
    app.run(debug=True)
