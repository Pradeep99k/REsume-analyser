def score(found, required):

    total=len(required)
    matched=0
    for i in required:
        if i in found:
            matched+=1
            return (matched/total)*100