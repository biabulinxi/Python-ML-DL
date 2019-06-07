from wxpy import *
# 实例化，并登录微信
bot = Bot(cache_path=True)
# 调用图灵机器人API
my_friend = bot.friends().search('可达!')[0]
tuling = Tuling(api_key='4a0488cdce684468b95591a641f0971d')
# tuling = Tuling(api_key='a9fe6601fe3045e5be1f7eb767ae8a90')
@bot.register(my_friend)
def auto_reply(msg):
    tuling.do_reply(msg)
embed()