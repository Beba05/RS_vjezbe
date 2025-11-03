# Kraća verzija (pomoću dictionary comprehensiona i sum())

def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return {
        'samoglasnici': sum(1 for z in tekst if z in vowels),
        'suglasnici': sum(1 for z in tekst if z in consonants)
    }

tekst = "Python je zabavan programski jezik!"
print(count_vowels_consonants(tekst))