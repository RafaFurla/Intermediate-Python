word = str(input('')).lower()
word_list = [c for c in word if c not in ("aeiouãáàâäéèêëíìîïóòõöôúùûü ")]
print(word_list)
