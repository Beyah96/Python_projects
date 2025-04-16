def calculate_love_score(name1, name2):
    counter_true = 0
    counter_love = 0
    for letter in (name1 + name2).lower():
        if letter in "true":
            counter_true += 1
        if letter in "love":
            counter_love += 1
    result = 10 * counter_true + counter_love
    print(result)


calculate_love_score("Kanye West", "Kim Kardashian")