from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/pronunciation_game', methods=['GET', 'POST'])
def pronunciation_game():
    if request.method == 'POST':
        level = request.form.get('level')
        if level in seviyeler:
            selected_words = random.sample(seviyeler[level], 3)  # 3 kelime seçiyoruz
            return jsonify({'words': selected_words})
        return jsonify({'error': 'Geçersiz seviye'})
    else:
        return render_template('pronunciation_game.html')

if __name__ == '__main__':
    app.run(debug=True)
