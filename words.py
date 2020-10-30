from urllib.request import urlopen

def fetch():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_words(story_words):
    for word in story_words:
        print(word)

# print(__name__)

if __name__ == '__main__':
    fetch()