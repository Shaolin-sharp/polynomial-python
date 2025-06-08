class MessageFilter:

    def __init__(self, text):
        self.tokenized = text.split()
        self.flagged = 0

        for token in self.tokenized:
            upper_letters = sum(1 for ch in token if 'A' <= ch <= 'Z')
            if upper_letters >= 2:
                self.flagged += 1
                continue

            if any(not ch.isalpha() for ch in token):
                self.flagged += 1
                continue

            lowered = token.lower()
            repeated_chars = {}
            suspicious = False
            vowel_found = False

            for ch in lowered:
                if ch in repeated_chars:
                    repeated_chars[ch] += 1
                    if repeated_chars[ch] >= 3:
                        suspicious = True
                        break
                else:
                    repeated_chars[ch] = 1

                if ch in 'aeiou':
                    vowel_found = True

            if suspicious or not vowel_found:
                self.flagged += 1

    def __str__(self):
        return str(self.flagged)


print(MessageFilter("Takhfif VIZHEEEEE Porteghal dr Link zir:"))
print(MessageFilter("AGAR Mmmmmmmatn Zir ro baraye 3 nfr nafresti gooooshit hack mishe"))