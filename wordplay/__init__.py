from requests import post

def pos_tagging(language, text):
    result = []
    data = {
        "text": text,
        "language": language
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    r = post("https://parts-of-speech.info/tagger/tagger", data = data, headers = headers)
    for word in r.json()["taggedText"].split():
        if "_" in word:
            result.append({
                "word": word.split("_")[0],
                "pos": word.split("_")[1]
            })
    return result
