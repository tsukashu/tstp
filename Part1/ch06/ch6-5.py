words = [
    'The',
    'fox',
    'jumped',
    'over',
    'the',
    'fence',
    '.'
]

# add space after each word in the list.
add_space = []
add_space = ' '.join(words)
print(add_space)

# remove the space before the period.
remove_space = add_space.replace(' .','.')
print(remove_space)


"""
If each word has a 'space' after itself,
just do below.

join_words = []
join_words = ' '.join(words)
print(join_words)

It may be better the list word has period with it.
Or make function that replace ALL kind of symbols



"""
