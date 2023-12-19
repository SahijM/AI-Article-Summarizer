import tkinter as tk
from tkinter import scrolledtext
import nltk
from textblob import TextBlob
from newspaper import Article
from ttkthemes import ThemedStyle


def summarize():

    url = utext.get('1.0', "end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)
    
    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)
    
    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled') 



root = tk.Tk()
root.title("Summarizer")
root.geometry('800x600')
style = ThemedStyle(root)
style.set_theme("equilux")


tlabel = tk.Label(root, text="Title")
tlabel.pack()
title = scrolledtext.ScrolledText(root, height=1, width=100, state='disabled', wrap=tk.WORD)
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()
author = scrolledtext.ScrolledText(root, height=1, width=100, state='disabled', wrap=tk.WORD)
author.pack()

# Publication Date
plabel = tk.Label(root, text="Publication Date")
plabel.pack()
publication = scrolledtext.ScrolledText(root, height=1, width=100, state='disabled', wrap=tk.WORD)
publication.pack()


slabel = tk.Label(root, text="Summary")
slabel.pack()
summary = scrolledtext.ScrolledText(root, height=10, width=100, state='disabled', wrap=tk.WORD)
summary.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()
utext = tk.Text(root, height=1, width=100)
utext.pack()

button = tk.Button(root, text="Summarize", command=summarize)
button.pack()

root.mainloop()