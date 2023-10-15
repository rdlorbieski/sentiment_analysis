import tkinter as tk
from textblob import TextBlob

def analyze_sentiment():
    sentence = input_text.get()
    analysis = TextBlob(sentence)

    if analysis.sentiment.polarity > 0:
        result_label.config(text="Sentiment: Positive :)")
    elif analysis.sentiment.polarity < 0:
        result_label.config(text="Sentiment: Negative :(")
    else:
        result_label.config(text="Sentiment: Neutral :|")

# Window configuration
window = tk.Tk()
window.title("Sentiment Analysis")
window.geometry("400x400")

# Instruction label for users
instruction_label = tk.Label(window, text="Enter an English sentence in the field below.")
instruction_label.pack(pady=5)

instruction_label = tk.Label(window, text="We will automatically analyze the tone of your message.")
instruction_label.pack(pady=5)


# Text entry for sentence input
input_text = tk.Entry(window, width=40)
input_text.pack(pady=10)

# Button to trigger sentiment analysis
analyze_button = tk.Button(window, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack()

# Label to display the result of sentiment analysis
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the graphical interface
window.mainloop()
