import math
import matplotlib.pyplot as plt
def word_count(book):
    paragraphs = book.split('\n\n')

    word_count_list = []

    for paragraph in paragraphs:
        words = paragraph.split()
        
        word_count_list.append(math.ceil(len(words) / 10.0) * 10)

    return sorted(word_count_list)

def graph(sorted_list):
    plt.hist(sorted_list, bins=range(min(sorted_list), max(sorted_list) + 10, 10), edgecolor='black')
    plt.title('Distribution of Number of Words per Paragraph')
    plt.xlabel('Number of Words (rounded to nearest ten)')
    plt.ylabel('Frequency')
    plt.savefig('./img/word_count_plot.png')
    plt.show()
    