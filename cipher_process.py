class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = []

        if is_encrypt == True:
            for letter in text.lower():
                    if letter in self.alphabet:
                        letter_index = (self.alphabet.find(letter) + shift) % 33
                        letter = self.alphabet[letter_index]
                        result.append(letter)
            else:
                result.append(letter)
            return ''.join(result)
        else:
            for letter in text.lower():
                if letter in self.alphabet:
                    letter_index = (self.alphabet.find(letter) - shift) % 33
                    letter = self.alphabet[letter_index]
                    result.append(letter)
                else:
                    result.append(letter)  # здесь ваш код
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
