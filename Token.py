import re
# هدف از این قطعه کد شناسایی و دسته بندی توکن ها است.
# تعریف عبارات باقاعده
token_specs = [
    ('FLOAT', r'[0-9]+\.[0-9]+'),   #عدد اعشاری
    ('INTEGER', r'0|[1-9][0-9]*'),  #عدد صحیح 
    ('IDENTIFIER', r'[a-zA-Z][a-zA-Z0-9]*'),    #شناسه
    ('WHITESPACE', r'\s+'), #فضای خالی
]

# ترکیب الگوها در یک عبارت بزرگ
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs)

def tokenize(text):
    tokens = []
    for match in re.finditer(token_regex, text):
        kind = match.lastgroup
        value = match.group()
        if kind != 'WHITESPACE':  # حذف فضاهای خالی
            tokens.append((kind, value))
    return tokens

# نمونه استفاده
input_text = "var1 = 123  \nprice = 123.5"
result = tokenize(input_text)

for token in result:
    print(token)
