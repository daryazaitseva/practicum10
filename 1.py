with open('/Users/dasha/Desktop/1_task.txt', 'r') as f:
    text = f.read()
new_text = text.upper()
with open('output.txt', 'w') as f:
    f.write(new_text)
    print(new_text)
