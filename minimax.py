from predict import predict

def stability_check(text, keywords):
    base_label, base_conf = predict(text)

    scores = []

    for word in keywords:
        modified = text.replace(word, "")
        _, conf = predict(modified)
        scores.append(conf)

    stability = abs(base_conf - min(scores)) / 100
    return round(stability, 3)