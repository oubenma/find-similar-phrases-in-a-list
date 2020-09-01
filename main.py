import csv
import re
min_similar_words = 2


def getCsvData():
    file = open('data.csv')
    reader = csv.reader(file)
    data = list(reader)
    return data


def compare(title1, title2):
    #     print(re.split(';| |)|(|-|_', title2)) add other separators later
    list_title1 = re.split(';| ', title1.lower())
    list_title2 = re.split(';| ', title2.lower())
    count_words = 0
    for word in list_title1:
        if word in list_title2:
            count_words += 1
    if count_words >= min_similar_words:
        return count_words
    return 0


def saveCsvData(data):
    file = open('results.csv', mode='a', encoding='utf-8')
    writer = csv.writer(file, delimiter=',', quotechar='"')
    writer.writerows(data)


def main():
    products = getCsvData()
    length = len(products)
    current_id = 0
    for i in range(0, length):
        current_product = products[i][0]
        current_id += 1
        products[i].append("id_"+str(current_id)+"end")
        current_similarity_count = 0
        for j in range(i+1, length):
            if compare(current_product, products[j][0]) > 0:
                products[j].append("id_"+str(current_id)+"end")
    #      print(current_product + " ### vs ###" + products[j][0])
    saveCsvData(products)
    for i in range(0, length):
        print(products[i])


main()
