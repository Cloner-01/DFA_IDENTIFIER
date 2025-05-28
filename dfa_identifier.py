def is_letter(ch):
    return ch.isalpha()

def is_letter_or_digit(ch):
    return ch.isalnum()

def run_dfa(filename):
    with open(filename, 'r') as fp:
        content = fp.read()

    state = 1
    i = 0
    length = len(content)

    while i < length:
        ch = content[i]

        if state == 1:
            if is_letter(ch):
                start_index = i
                state = 2
                i += 1
            else:
                i += 1  # حرکت به جلو در حالت نامعتبر
        elif state == 2:
            if is_letter_or_digit(ch):
                i += 1
            else:
                identifier = content[start_index:i]
                print(f"ID: {identifier}")
                state = 1
                # بررسی دوباره کاراکتر فعلی در حالت 1 (بدون تغییر i)

    # بررسی شناسه آخر در انتهای فایل
    if state == 2:
        identifier = content[start_index:i]
        print(f"ID: {identifier}")

# اجرا
run_dfa("source.txt")
