from wechat_api import Wechat


def main():
    wechat = Wechat()
    wechat.login(auto=True)
    friends = wechat.get_friends()
    print(friends)


if __name__ == '__main__':
    main()