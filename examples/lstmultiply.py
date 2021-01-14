# 1.
'python' * 5
[42] * 10
[None] * 10

# 2. prints a sentence in a centered "box" of correct width
# sentence = input('Input a Sentence:')
sentence = 'He is a very naughty boy.'

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print()
print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
print(' ' * left_margin + '|' + ' ' * text_width      + '    |')
print(' ' * left_margin + '|' +       sentence        + '    |')
print(' ' * left_margin + '|' + ' ' * text_width      + '    |')
print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
