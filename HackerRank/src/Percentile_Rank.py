# Case study to find percentile rank based on scores of students for assignment
# https://en.wikipedia.org/wiki/Percentile_rank

n = int(input("Enter the number of students: "))
dataset = []
for index in range(1, n+1):
    dataset.append(int(input(f"Student {index}'s score: ")))


def find_percentile_rank(score):
    # cumulative frequency is the count of all scores less than or equal to score of interest
    cFreq = cumulative_frequency(score)
    print(f"cFreq: {cFreq}")
    # frequency for the score of interest
    freq = dataset.count(score)
    print(f"freq: {freq}")
    percentile_rank = (cFreq - (0.5 * freq)) / n * 100

    return percentile_rank


def cumulative_frequency(score):
    cfreq = 0
    sData = list(set(dataset))
    for i in range(len(sData)):
        if sData[i] <= score:
            cfreq += dataset.count(sData[i])
    return cfreq


for data in dataset:
    print(f"Score: {data}, Percentile: {find_percentile_rank(data)}")
