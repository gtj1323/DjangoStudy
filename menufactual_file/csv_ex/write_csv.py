lunch = {
    '고갯마루':'02-123-4567',
    '세븐브릭스':'02-234-5678',
    '아랑졸돈까스':'02-345-6789'
}
# 1. string formatting을 사용하는 방법
with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write(f'{item[0]}, {item[1]}\n')

# 2. join을 사용하는 방법
with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write(','.join(item)+'\n')

# 3. csv.writer
import csv
with open('lunch3.csv', 'w', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)