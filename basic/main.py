from difflib import SequenceMatcher

with open('basic/file1.txt') as f1, open('basic/file2.txt') as f2:
    file1Data = f1.read()
    file2Data = f2.read()

    similarity = SequenceMatcher(None, file1Data, file2Data).ratio()
    print(similarity*100)
