from aiogram import types

from data.config import channels
from data.dict_pack import dict_of_topics
from keyboards.default.main_buttons import generate_button
from loader import dp, _, bot
from utils.misc import subscription


@dp.message_handler(text=_('🧠 Заниматься'))
async def navigation(msg: types.Message):
    result = str()
    for channel in channels:
        status = await subscription.check(user_id=msg.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            await msg.answer(_('Выбери тему и начни попрактиковаться'),
                             reply_markup=generate_button(dict_of_topics, False))
        else:
            invite_link = await channel.export_invite_link()
            result += _("Чтобы попрактиковаться <a href='{}'>Нужно подписаться на канал.</a>\n\n").format(invite_link)

    await msg.answer(result, disable_web_page_preview=True)



