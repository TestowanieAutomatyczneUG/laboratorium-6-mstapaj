class Songbook:

    def __init__(self):
        file = open('lyrics.txt', 'r')
        self.lyrics = []
        for i in file:
            if i != '\n':
                self.lyrics.append(i[:-1])

    def song(self):
        result = ""
        for i in self.lyrics:
            result += i + '\n'
        return result

    def verse(self, number):
        if isinstance(number, int) and str(number) != 'True' and str(number) != 'False':
            if 0 < number < 13:
                return self.lyrics[number - 1]
            else:
                raise ValueError('Wers nie jest z przedziału 1-12')
        else:
            raise TypeError('Numer wersu nie jest typu int')

    def many_verse(self, first, second):
        if isinstance(first, int) and str(first) != 'True' and str(first) != 'False':
            if 0 < first < 13:
                if isinstance(second, int) and str(second) != 'True' and str(second) != 'False':
                    if 0 < second < 13:
                        if first <= second:
                            result = ''
                            for i in range(first, second + 1):
                                result += self.lyrics[i - 1] + '\n'
                            return result
                        else:
                            result = ''
                            for i in range(second, first + 1):
                                result += self.lyrics[i - 1] + '\n'
                            return result
                    else:
                        raise ValueError('Drugi numer wersu nie jest z przedziału 1-12')
                else:
                    raise TypeError('Drugi numer wersu nie jest typu int')
            else:
                raise ValueError('Pierwszy numer wersu nie jest z przedziału 1-12')
        else:
            raise TypeError('Pierwszy numer wersu nie jest typu int')
