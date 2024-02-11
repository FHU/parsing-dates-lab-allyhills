def parse_month(month):
    dict = {'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05', 'June':'06', 'July':'07',
            'August':'08', 'September':'09', 'October':'10', 'November':'11', 'December':'12'}
    
    return dict.get(month)

def parse_date(user_string):
    user_string = user_string.split()
    user_string[1] = user_string[1].replace(',','')
    user_string[0] = parse_month(user_string[0])
    if len(user_string[1]) == 1:
        user_string[1] = '0' + user_string[1]
    
    return('/').join(user_string)

if __name__ == '__main__':
    user_string = input('Enter a date:')
    print(parse_date(user_string))

