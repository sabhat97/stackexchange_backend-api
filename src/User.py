import sys
from stackauth import StackAuth
from stackexchange import Site, StackOverflow


class User:

    def getComments(self):
        user_id = 41983 if len(sys.argv) < 2 else int(sys.argv[1])
        print('StackOverflow user %d\'s accounts:' % user_id)

        stack_auth = StackAuth()
        so = Site(StackOverflow)
        accounts = stack_auth.associated(so, user_id)
        reputation = {}

        for q in so.questions(tagged=['java', 'javascript', 'python', 'html'], pagesize=50):
            print(q.tags)

        print(so.all_tag_badges().items)




if __name__ == '__main__':
    user = User()
    user.getComments()
