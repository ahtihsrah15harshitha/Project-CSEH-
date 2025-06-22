from zxcvbn import zxcvbn
#password checker
def password_check(password):
    result= zxcvbn(password)
    print("score [0-4]:",result['score'])
    print("feedback:",result['feedback'])
