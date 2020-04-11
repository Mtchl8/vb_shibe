from Settings import TOKEN, WEBHOOK
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
    name='EngShibe',
    avatar='https://previews.123rf.com/images/greenoptix/greenoptix1904/greenoptix190400022/123442578-illustration-shiba-inu-for-all-dog-owners-what-you-love-about-his-dog-puppy-dog-%C3%A2%E2%82%AC%E2%80%B9%C3%A2%E2%82%AC%E2%80%B9eyes-wagging-t.jpg',
    auth_token=TOKEN
)

viber = Api(bot_configuration)
print('setting webhook: '+WEBHOOK)
viber.set_webhook(WEBHOOK)
