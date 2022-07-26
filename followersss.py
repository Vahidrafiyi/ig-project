import datetime
start = datetime.datetime.now()
import instaloader
import pandas

L = instaloader.Instaloader()

# Login or load session
username = "muslim344421"
password = "@#Mu1234"
L.login(username, password)  # (login)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, 'web_burger.ir')

# Print list of followees
follower_list = []
following_list = []
not_followed = []

for followee in profile.get_followers():
    follower_list.append(followee.username)

for followee in profile.get_followees():
    following_list.append(followee.username)

for user in following_list:
    if user not in follower_list:
        not_followed.append(user)

output = {}
output[f'web_burger.ir followers'] = follower_list
output[f'web_burger.ir followings'] = following_list
output[f' فالووینگ هایی که web_burger.ir را دنبال نکرده اند '] = not_followed
data = pandas.DataFrame.from_dict(output, orient='index')
data = data.transpose()
writer = pandas.ExcelWriter(f'webburger.xlsx')
data.to_excel(writer)
writer.save()
end = datetime.datetime.now()
print(end-start)
