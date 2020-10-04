from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from models.user import User
from utlis.helpers import get_key_by_value
from consts import POSITIONS

with_settings_button = InlineKeyboardButton(
    "💫Сгенерировать картинку с настроек",
    callback_data="watermark_from_settings"
)
without_settings_button = InlineKeyboardButton(
    "🔍Сгенерировать без настроек",
    callback_data="watermark_default"
)


def inline_kbrd() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(row_width=1)


def generate_buttons() -> InlineKeyboardMarkup:
    return inline_kbrd().add(
        with_settings_button,
        without_settings_button
    )


def main_menu() -> InlineKeyboardMarkup:
    return inline_kbrd().add(
        InlineKeyboardButton("📖Настройки", callback_data="settings_menu"),
        with_settings_button,
        without_settings_button
    )


# TODO: InlineKeyboardButton(f"🧙Запустить мастер настройки", callback_data="master"),
def settings_menu(user: User) -> InlineKeyboardMarkup:
    return inline_kbrd().add(
        InlineKeyboardButton(f"👉Позиция: {get_key_by_value(POSITIONS, user.position)}", callback_data="position"),
        InlineKeyboardButton(f"🟥Цвет текста: {user.color}", callback_data="color"),
        InlineKeyboardButton(f"💫Прозрачность: {user.opacity}", callback_data="opacity"),
        InlineKeyboardButton(f"✏Шрифт: {user.font}", callback_data="font"),
        InlineKeyboardButton(f"📈Размер шрифта: {user.fontsize}", callback_data="fontsize"),
        InlineKeyboardButton(f"🗒Текст: {user.text}", callback_data="text"),
        InlineKeyboardButton(f"🌠В меню", callback_data="main_menu")
    )
