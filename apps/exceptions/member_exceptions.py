class MemberLoginFailError(Exception):
    """ 로그인에 실패함 """

    def __init__(self):
        super(MemberLoginFailError, self).__init__()
