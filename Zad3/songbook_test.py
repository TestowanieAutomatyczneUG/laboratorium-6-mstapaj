import unittest
from songbook import Songbook
from assertpy import *


class songbook_test(unittest.TestCase):

    def setUp(self):
        self.temp = Songbook()

    def test_song(self):
        assert_that(self.temp.song()).is_equal_to(
            "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\nOn the second day of "
            "Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\nOn the third day "
            "of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear "
            "Tree.\nOn the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, "
            "two Turtle Doves, and a Partridge in a Pear Tree.\nOn the fifth day of Christmas my true love gave to "
            "me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear "
            "Tree.\nOn the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, "
            "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the seventh "
            "day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
            "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the eighth "
            "day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, "
            "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
            "and a Partridge in a Pear Tree.\nOn the ninth day of Christmas my true love gave to me: nine Ladies "
            "Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
            "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the tenth "
            "day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, "
            "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
            "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the eleventh day of Christmas "
            "my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, "
            "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
            "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\nOn the twelfth day of Christmas my "
            "true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies "
            "Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
            "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n")

    def test_verse_1(self):
        assert_that(self.temp.verse(1)).is_equal_to(
            'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')

    def test_verse_7(self):
        assert_that(self.temp.verse(7)).is_equal_to(
            'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, '
            'five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear '
            'Tree.')

    def test_verse_12(self):
        assert_that(self.temp.verse(12)).is_equal_to(
            'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, '
            'ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, '
            'six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, '
            'and a Partridge in a Pear Tree.')

    def test_verse_none(self):
        assert_that(self.temp.verse).raises(TypeError).when_called_with(None)

    def test_verse_object(self):
        assert_that(self.temp.verse).raises(TypeError).when_called_with({})


    def test_verse_array(self):
        assert_that(self.temp.verse).raises(TypeError).when_called_with([])

    def test_verse_true(self):
        assert_that(self.temp.verse).raises(TypeError).when_called_with(True)

    def test_verse_false(self):
        assert_that(self.temp.verse).raises(TypeError).when_called_with(False)

    def test_verse_string(self):
        assert_that(self.temp.verse).raises(TypeError).when_called_with('abc')

    def test_verse_string_number(self):
        assert_that(self.temp.verse).raises(TypeError).when_called_with('4')

    def test_verse_float(self):
        assert_that(self.temp.verse).raises(TypeError).when_called_with(2.56)

    def test_verse_negative_int(self):
        assert_that(self.temp.verse).raises(ValueError).when_called_with(-4)

    def test_verse_negative_float(self):
        assert_that(self.temp.verse).raises(TypeError).when_called_with(-5.14)

    def test_verse_out_of_range(self):
        assert_that(self.temp.verse).raises(ValueError).when_called_with(-2)

    def test_verse_out_of_range_2(self):
        assert_that(self.temp.verse).raises(ValueError).when_called_with(13)

    def test_many_verse(self):
        assert_that(self.temp.many_verse(1,4)).is_equal_to('On the first day of Christmas my true love gave to me: a '
                                                           'Partridge in a Pear Tree.\nOn the second day of Christmas '
                                                           'my true love gave to me: two Turtle Doves, '
                                                           'and a Partridge in a Pear Tree.\nOn the third day of '
                                                           'Christmas my true love gave to me: three French Hens, '
                                                           'two Turtle Doves, and a Partridge in a Pear Tree.\nOn the '
                                                           'fourth day of Christmas my true love gave to me: four '
                                                           'Calling Birds, three French Hens, two Turtle Doves, '
                                                           'and a Partridge in a Pear Tree.\n')

    def test_many_verse_2(self):
        assert_that(self.temp.many_verse(6,11)).is_equal_to('On the sixth day of Christmas my true love gave to me: '
                                                            'six Geese-a-Laying, five Gold Rings, four Calling Birds, '
                                                            'three French Hens, two Turtle Doves, and a Partridge in '
                                                            'a Pear Tree.\nOn the seventh day of Christmas my true '
                                                            'love gave to me: seven Swans-a-Swimming, '
                                                            'six Geese-a-Laying, five Gold Rings, four Calling Birds, '
                                                            'three French Hens, two Turtle Doves, and a Partridge in '
                                                            'a Pear Tree.\nOn the eighth day of Christmas my true '
                                                            'love gave to me: eight Maids-a-Milking, '
                                                            'seven Swans-a-Swimming, six Geese-a-Laying, '
                                                            'five Gold Rings, four Calling Birds, three French Hens, '
                                                            'two Turtle Doves, and a Partridge in a Pear Tree.\nOn '
                                                            'the ninth day of Christmas my true love gave to me: nine '
                                                            'Ladies Dancing, eight Maids-a-Milking, '
                                                            'seven Swans-a-Swimming, six Geese-a-Laying, '
                                                            'five Gold Rings, four Calling Birds, three French Hens, '
                                                            'two Turtle Doves, and a Partridge in a Pear Tree.\nOn '
                                                            'the tenth day of Christmas my true love gave to me: ten '
                                                            'Lords-a-Leaping, nine Ladies Dancing, '
                                                            'eight Maids-a-Milking, seven Swans-a-Swimming, '
                                                            'six Geese-a-Laying, five Gold Rings, four Calling Birds, '
                                                            'three French Hens, two Turtle Doves, and a Partridge in '
                                                            'a Pear Tree.\nOn the eleventh day of Christmas my true '
                                                            'love gave to me: eleven Pipers Piping, '
                                                            'ten Lords-a-Leaping, nine Ladies Dancing, '
                                                            'eight Maids-a-Milking, seven Swans-a-Swimming, '
                                                            'six Geese-a-Laying, five Gold Rings, four Calling Birds, '
                                                            'three French Hens, two Turtle Doves, and a Partridge in '
                                                            'a Pear Tree.\n')

    def test_many_verse_single_verse(self):
        assert_that(self.temp.many_verse(2,2)).is_equal_to('On the second day of Christmas my true love gave to me: '
                                                           'two Turtle Doves, and a Partridge in a Pear Tree.\n')

    def test_many_verse_reverse(self):
        assert_that(self.temp.many_verse(3, 1)).is_equal_to('On the first day of Christmas my true love gave to me: a '
                                                            'Partridge in a Pear Tree.\nOn the second day of '
                                                            'Christmas my true love gave to me: two Turtle Doves, '
                                                            'and a Partridge in a Pear Tree.\nOn the third day of '
                                                            'Christmas my true love gave to me: three French Hens, '
                                                            'two Turtle Doves, and a Partridge in a Pear Tree.\n')

    def test_many_verse_out_of_range(self):
        assert_that(self.temp.many_verse).raises(ValueError).when_called_with(0, 4)

    def test_many_verse_out_of_range_2(self):
        assert_that(self.temp.many_verse).raises(ValueError).when_called_with(8, 14)

    def test_many_verse_out_of_range_3(self):
        assert_that(self.temp.many_verse).raises(ValueError).when_called_with(-3, 15)

    def test_many_verse_out_of_range_4(self):
        assert_that(self.temp.many_verse).raises(ValueError).when_called_with(0, 13)

    def test_many_verse_string_first(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with('abc', 4)

    def test_many_verse_string_second(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(1, 'abc')

    def test_many_verse_string(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with('cba', 'abc')

    def test_many_verse_string_number_first(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with('1', 4)

    def test_many_verse_string_number_second(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(1, '3')

    def test_many_verse_number_string(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with('3', '8')

    def test_many_verse_float_first(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(3.14, 4)

    def test_many_verse_float_second(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(1, 3.14)

    def test_many_verse_float(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(3.14, 2.56)

    def test_many_verse_negative_float_first(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(-3.14, 4)

    def test_many_verse_negative_float_second(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(1, -3.14)

    def test_many_verse_negative_float(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(-3.14, -2.56)

    def test_many_verse_negative_int_first(self):
        assert_that(self.temp.many_verse).raises(ValueError).when_called_with(-3, 4)

    def test_many_verse_negative_int_second(self):
        assert_that(self.temp.many_verse).raises(ValueError).when_called_with(1, -3)

    def test_many_verse_negative_int(self):
        assert_that(self.temp.many_verse).raises(ValueError).when_called_with(-3, -2)

    def test_many_verse_none_first(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(None, 4)

    def test_many_verse_none_second(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(1, None)

    def test_many_verse_none(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(None, None)

    def test_many_verse_object_first(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with({}, 4)

    def test_many_verse_object_second(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(1, {})

    def test_many_verse_object(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with({}, {})

    def test_many_verse_array_first(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with([], 4)

    def test_many_verse_array_second(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(1, [])

    def test_many_verse_array(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with([], [])

    def test_many_verse_true_first(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(True, 4)

    def test_many_verse_true_second(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(1, True)

    def test_many_verse_true(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(True, True)

    def test_many_verse_false_first(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(False, 4)

    def test_many_verse_false_second(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(1, False)

    def test_many_verse_false(self):
        assert_that(self.temp.many_verse).raises(TypeError).when_called_with(False, False)
        
    def tearDown(self):
        self.temp=None