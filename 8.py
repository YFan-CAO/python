f = open("sample.txt", "r", encoding='utf-8')
s = open("sample_copy.txt", "w", encoding='utf-8')
reads = f.read()
reads = reads.upper()
s.write(reads)
f.close()
s.close()
