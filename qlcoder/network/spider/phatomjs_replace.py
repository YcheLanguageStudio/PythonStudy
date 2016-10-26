import requests


def read_account_info():
    account_password_list = list()

    with open('account_passwd.txt') as fs:
        account_password_list = fs.readlines()

    account_password_list = map(lambda str: str.split('----'), account_password_list)
    for each_pair in account_password_list:
        each_pair[1] = each_pair[1].rstrip('\n')

    print account_password_list


if __name__ == '__main__':
    read_account_info()
