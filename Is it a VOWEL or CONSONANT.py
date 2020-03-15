c=input().upper()
print("Vowel"*bool(c in "AEIOU")+"Consonant"*bool(c not in "AEIOU"))