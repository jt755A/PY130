'''
P
Rules:
    - Word delimted by spaces OR sentence ending characters
        - '.', '!', '?', ' '
    - Calculate longest sentence by words
    - Print that sentence, INCLUDING ending punctuation
    - Return a message with length of longest sentence
E
D
Input: single string: parenthesis

Output: string, message with integer length

Intermediate:
    - A list of all sentences in string?
        - Can you use split() method using a tuple?
    -   - Or iterate until you reach a sentence ending character,
            - appending chars up to that point to sentence_lst


    - Create helper function: returns index of sentence ending character.
        - This must be "attached" to word, i.e. not wholly made up of
        sentence ending. '--' is a word

    - Sentence ends are ending char + whitespace ' '

    - Iterate through combinations of '. ', '! ', '? ' to get sentences?



A

GET SENTENCES

- given sentence
- init `sentences` to blank list
- init `sentence_ending_chars`

- start iterating over a copy of `sentence`, through `setnence_ending_chars`
    - return list of indexes of `sentence_ending` - `end_idxes`
    - extract string
    - set `start_idxes`:
        - (end_idx + 1), unless end_idx[0], start_idx = 0

    Or, iterate over copy of sentence
    - when find sentence_end, extract form start up to that idx
        - assign to `sentences`
    - reassign sentence copy from NEXT_IDX to end
    - continue to iterate until sentence empty

GET LONGEST SENTENCE
- Iterate thorugh `sentences`,
    - make Copy
    - split by whitespace
    - get length of words, add to dictionary with original sentence

C
# '''
def longest_sentence(text):
    sentences = get_sentences(text)

    sentence_length = {}
    for sentence in sentences:
        words = sentence.split()
        sentence_length[sentence] = len(words)

    longest = max(sentence_length, key=sentence_length.get)

    length_message = (f'The longest sentence has '
                      f'{sentence_length[longest]} words.')
    final = f'{longest}\n\n{length_message}\n'
    print(final)

def find_sentence_end(text):
    sentence_ending_chars = ('.', '?', '!')
    found = {ending_char: text.find(ending_char)
             for ending_char in sentence_ending_chars
             if text.find(ending_char) != -1}
    if found:
        return min(found.values())
    return len(text)

def get_sentences(text):
    sentences = []
    text_copy = text[:]

    while text_copy:
        sentence_end_idx = find_sentence_end(text_copy)
        new_sentence = text_copy[:sentence_end_idx + 1]
        sentences.append(new_sentence.strip())
        text_copy = text_copy[sentence_end_idx + 1:]

    return sentences


# needs to return the smallest found idx, for all chars


long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)

longest_sentence(long_text)
# Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.
#
# The longest sentence has 30 words.

longest_sentence(longer_text)
# It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
#
# The longest sentence has 86 words.

longest_sentence("Where do you think you're going? What's up, Doc?")

# print("Where do you think you're going? What's up, Doc?"[31])
# Where do you think you're going?
#
# The longest sentence has 6 words.

longest_sentence("To be or not to be! Is that the question?")
longest_sentence("To be or not to be! Is that the question or not really")

# print(find_sentence_end("To be or not to be! Is that the question?"))

# To be or not to be!
#
# The longest sentence has 6 words.