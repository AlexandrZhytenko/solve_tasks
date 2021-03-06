# Ever tried to send a secret message to someone without using the postal service?
# You could use newspapers to tell your secret.
# Even if someone finds your message, its easy to brush them off and that its
# paranoia and a bogus conspiracy theory. One of the simplest ways to hide a secret
# message is to use capital letters. Let's find some of these secret messages.
# You are given a chunk of text. Gather all capital letters in one word in the order
# that they appear in the text.
# For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.",
# if we collect all of the capital letters, we get the message "HELLO".
# print "l"

import re
def find_message(text):
    return "".join(re.findall(r"[A-Z]+", text))
# or
# find_message = lambda text: ''.join(filter(str.isupper, text))

# or
# def find_message(text):
#     return ''.join(c for c in text if c.isupper())

if __name__ == '__main__':
    print find_message("How are you? Eh, ok. Low or Lower? Ohhh.")