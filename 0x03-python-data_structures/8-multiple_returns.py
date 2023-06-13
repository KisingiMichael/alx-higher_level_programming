#!/usr/bin/python3
def multiple_returns(sentence):
    sent_len = len(sentence)
    if (sent_len == 0):
        new_tuple = (sent_len, None)
    else:
        new_tuple = (sent_len, sentence[0])
    return new_tuple
