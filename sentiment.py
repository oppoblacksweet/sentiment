import statistics

def detect_anomaly(coin, score, history, window_size=10, threshold=2.0):
    if coin not in history:
        history[coin] = []

    history[coin].append(score)
    if len(history[coin]) < window_size:
        return False

    recent = history[coin][-window_size:]
    mean = statistics.mean(recent)
    stdev = statistics.stdev(recent)

    # Заметное отклонение от среднего?
    if abs(score - mean) > threshold * stdev:
        return True
    return False
