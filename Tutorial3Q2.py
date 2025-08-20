def limiter(message):
    return message[:160]

def limiter_words(message):
    return" ".join(message.split()[:20])