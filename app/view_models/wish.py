from app.view_models.book import BookViewModel


class MyWishes:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list

        self.gifts = self.parse()

    def parse(self):
        temp_gifts = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        return MyWish(gift.id, BookViewModel(gift.book), count)


class MyWish:
    def __init__(self, id, book, wishes_count):
        self.id = id
        self.book = book
        self.wishes_count = wishes_count
