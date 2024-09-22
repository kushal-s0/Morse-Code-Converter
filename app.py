from flask import Flask, render_template, request

app = Flask(__name__)

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}

def to_morse_code(message):
    morse_code = ''
    for char in message.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
    return morse_code.strip()

def from_morse_code(morse_code):
    message = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for char, morse in morse_dict.items():
            if morse == code:
                message += char
    return message

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    if request.method == 'POST':
        choice = request.form.get('choice')
        input_text = request.form.get('inputText', '').strip()
        
        if choice == '1':
            output = to_morse_code(input_text)
        elif choice == '2':
            output = from_morse_code(input_text)
    
    return render_template('index.html', output=output)

if __name__ == "__main__":
    app.run(debug=True)
