class flames:

    # def __init__(self):
    #     self.relation = ""
    #     self.relation = ""

    @staticmethod
    def r_pred(male,female):
        if male == female:
            relation = "both names are similiar..  I think you are in love with yourself ;)"
            return relation
        else:
            word_count = len(male)+len(female)
            for i in range(len(male)):
                for j in range(len(female)):
                    if male[i] == female[j]:
                        word_count -= 1
            if word_count % 6 == 1:
                relation = "the best relationship that can work WELL between these two names is FRIENDSHIP"
            elif word_count % 6 == 2:
                relation = "the best relationship that can work WELL between these two names is LOVE"
            elif word_count % 6 == 3:
                relation = "the best relationship that can work WELL between these two names is AFFECTION"
            elif word_count % 6 == 4:
                relation = "the best relationship that can work WELL between these two names is SPOUSE"
            elif word_count % 6 == 5:
                relation = "the best relationship that can work WELL between these two names is ENEMY"
            elif word_count % 6 == 0:
                relation = "the best relationship that can work WELL between these two names is SIBLINGS"
            else:
                relation = "Opps.......Not a valid input"
        return relation