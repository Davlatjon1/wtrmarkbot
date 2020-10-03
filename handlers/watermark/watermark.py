from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from states.watermark import SetWatermark
from utlis.image_converter import async_image_process
from .routes import TextRoute
from messages import routes_messages
from consts import POSITIONS, TEXT_COLORS, FONTS, MAX_FONT_SIZE
from utlis.helpers import validate_number, check_in

get_position = TextRoute(
    "position",
    POSITIONS.get,
    routes_messages.get("position"),
    routes_messages.get("color")
)
get_color = TextRoute(
    "color",
    TEXT_COLORS.get,
    routes_messages.get("color"),
    routes_messages.get("opacity")
)
get_opacity = TextRoute(
    "opacity",
    validate_number,
    routes_messages.get("opacity"),
    routes_messages.get("font")
)
get_font = TextRoute(
    "font",
    lambda text: check_in(text, FONTS),
    routes_messages.get("font"),
    routes_messages.get("fontsize")
)
get_fontsize = TextRoute(
    "fontsize",
    lambda text: validate_number(text, MAX_FONT_SIZE),
    routes_messages.get("fontsize"),
    routes_messages.get("text")
)


async def starting_from_command(msg: Message):
    await msg.answer(**routes_messages.get("starting"))
    await SetWatermark.get_pic.set()


async def starting_from_callback(callback_query: CallbackQuery):
    await callback_query.bot.send_message(
        chat_id=callback_query.from_user.id,
        **routes_messages.get("starting")
    )
    await SetWatermark.get_pic.set()


async def get_picture(msg: Message, state: FSMContext):
    last_photo = msg.photo[-1]
    await state.update_data(photo=last_photo)
    await SetWatermark.next()
    await msg.reply(**routes_messages.get("position"))


async def set_text(msg: Message, state: FSMContext):
    text = msg.text
    data = await state.get_data()
    data.get("color").append(data.get("opacity"))
    path_to_pic = f"pic/{data.get('photo').file_id}"

    await data.get('photo').download(path_to_pic)
    watermarked_photo = await async_image_process(
        msg.bot.loop,
        path_to_pic,
        data.get("position"),
        tuple(data.get("color")),
        f"fonts/{data.get('font')}.ttf",
        data.get("fontsize"),
        text
    )
    sended_pic = await msg.bot.send_photo(
        msg.chat.id,
        open(watermarked_photo, "rb")
    )
    await sended_pic.reply("Вот твоё фото с вотермаркой. "
                           "Клацай /start чтобы поставить вотермарку на ещё одно фото.")
    await state.finish()
