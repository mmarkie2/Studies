import datetime

from bs4 import BeautifulSoup
import os
from urllib import request

class Subject:
    def __init__(self, name=None, lecturer=None, class_=None, time_start=None, time_end=None):
        self.name = name
        self.lecturer = lecturer
        self.class_ = class_
        self.time_start = time_start
        self.time_end = time_end

def main():
    url = 'http://we1.pollub.pl/ats4/plan.php?type=0&id=6200&winW=943&winH=852&loadBG=000000'
    req = request.urlopen(url).read().decode('UTF-8')
    soup = BeautifulSoup(req, 'html.parser')
    result = soup.find_all('div', class_='coursediv')
    r2 = BeautifulSoup(str(result), 'html.parser')

    tab = []
    subjects = []
    for r in r2.contents:
        soup = BeautifulSoup(str(r), 'html.parser')
        if soup.text != ', ':
            tab.append(soup.contents)
            for i in soup.contents:
                strings = BeautifulSoup(str(i), 'html.parser').strings
                my_strings = []
                for s in strings:
                    if s != '\n' and s != '[' and s != ']':
                        my_strings.append(str(s))
                if len(my_strings) > 3:
                    subject = Subject()
                    subject.name = str(my_strings[0])
                    if subject.name.find(', lekt') != -1:
                        subject.lecturer = 'Not defined'
                        subject.class_ = 'Not defined'
                    else:
                        subject.lecturer = str(my_strings[1])
                        subject.class_ = str(my_strings[2])
                        
                    time = my_strings[len(my_strings)-1]
                    subject.time_start = str(time[:5])
                    subject.time_end = str(time[8:13])
                    
                    print(subject.name, type(subject.name))
                    print(subject.lecturer, type(subject.lecturer))
                    print(subject.class_, type(subject.class_))
                    print(datetime.datetime.strptime(subject.time_start, '%H:%M').time(), type(subject.time_start))
                    print(subject.time_end, type(subject.time_end))
                    print('\n')

                    subjects.append(subject)
                elif len(my_strings) > 2:
                    subject = Subject()
                    subject.name = str(my_strings[0])

                    subject.lecturer = 'Not defined'
                    subject.class_ = str(my_strings[1])

                    time = str(my_strings[2])
                    subject.time_start = str(time[:5])
                    subject.time_end = str(time[8:13])

                    print(subject.name, type(subject.name))
                    print(subject.lecturer, type(subject.lecturer))
                    print(subject.class_, type(subject.class_))
                    print(datetime.datetime.strptime(subject.time_start, '%H:%M').time(), type(subject.time_start))
                    print(subject.time_end, type(subject.time_end))
                    print('\n')

                    subjects.append(subject)



    data = ''
    file_path = os.path.join('.', 'data.txt')
    try:
        with open(file_path, 'w') as f:
            f.write(data)
    except FileNotFoundError:
        print('File not found!')


if __name__ == '__main__':
    main()
