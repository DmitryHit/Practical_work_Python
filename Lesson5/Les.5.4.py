num_text = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыри"}
num_trans = []
carry = []
with open("text_5_4.txt", "r", encoding="utf-8") as trans:
    for line in trans:
        carry = line.split(" - ")
        if carry[0] in num_text:
            word = num_text[carry[0]]
            num_trans.append(word + '-' + carry[1])

with open("text_trans_5_4.txt", "w", encoding="utf-8") as file_input:
    file_input.writelines(num_trans)
