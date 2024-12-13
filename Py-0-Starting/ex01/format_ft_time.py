import datetime as dt

now = dt.datetime.now()

seconds = 'Seconds since January 1, 1970: {0} or \
{0:.2e} in scientific notation'.format(now.timestamp())

date = '{0:%b %d %Y}'.format(now)

print(seconds + '\n' + date)
