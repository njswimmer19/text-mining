from mediawiki import MediaWiki
wikipedia = MediaWiki()
pokemon = wikipedia.page("Pokémon")
print(pokemon.title)
print(pokemon.content)
print("------------------------------------")
def word_freq(text, s):
    """
    This function counts the interested word within the wikipedia page. 
    """
    dic = text.split()
    count = 0
    for word in dic:
        if (word == s) or (word == s.lower()):
            count = count + 1
    return count

def decode(text):
    """
    This function organizes the inputted string variables by removing special characters.
    """
    null = ""
    special_characters = '''=!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for word in text:
        if word not in special_characters:
            null = null + word
    lowercase = null.lower() 
    # determine frequency of each words
    storage = dict()
    prompt = lowercase.split()
    for word in prompt:
        if word in storage:
            storage[word] += 1
        else:
            storage[word] = 1
    dic = storage
    dictionary = dict()
    for key, appearance in dic.items():
        if key.isnumeric() == False:
            dictionary[key] = appearance
    return dictionary

def top_10(dic):
    """
    This function searches for the top 10 most common words in the inputted dictionary.
    """
    rank = sorted(dic.keys(), key=lambda k: dic[k], reverse=True)
    doc = dict()
    for i in rank:
        doc[i] = dic[i]
    doc_items = doc.items()
    top_10 = tuple(doc_items)[:10]
    print("The top 10 most common words are")
    count = 0
    for key, appearance in top_10:
        count = count + 1
        print(f'{count}. {key}: {appearance}')

def main():
    dictionary = decode(pokemon.content)
    top_10(dictionary)
    print("-------------------------------------")
    print(f'The word "Pikachu" appears {word_freq(pokemon.content,"Pikachu")} times.')
    print("-------------------------------------")


if __name__ == "__main__":
    main()



