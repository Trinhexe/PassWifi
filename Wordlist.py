import itertools

def generate_wordpass_list(length):
    digits = '0123456789'
    wordpass_list = [''.join(p) for p in itertools.product(digits, repeat=length)]
    return wordpass_list

def save_to_file(wordpass_list, filename):
    with open(filename, 'w') as f:
        for wordpass in wordpass_list:
            f.write(wordpass + '\n')

length = 8
filename = '100milion_password_wifi.txt'
wordpass_list = generate_wordpass_list(length)
save_to_file(wordpass_list, filename)