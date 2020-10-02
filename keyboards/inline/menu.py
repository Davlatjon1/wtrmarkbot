from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from models.user import User


def inline_kbrd() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(row_width=1)


def main_menu() -> InlineKeyboardMarkup:
    return inline_kbrd().add(
        InlineKeyboardButton("📖Настройки", callback_data="settings_menu"),
        InlineKeyboardButton("💫Сгенерировать картинку с настроек", callback_data="watermark_from_settings"),
        InlineKeyboardButton("🔍Сгенерировать без настроек", callback_data="watermark_default")
    )


def settings_menu(user: User) -> InlineKeyboardMarkup:
    return inline_kbrd().add(
        InlineKeyboardButton(f"👉Позиция: {user.position}", callback_data="position"),
        InlineKeyboardButton(f"🟥Цвет текста: {user.color}", callback_data="color"),
        InlineKeyboardButton(f"💫Прозрачность: {user.opacity}", callback_data="opacity"),
        InlineKeyboardButton(f"✏Шрифт: {user.font}", callback_data="font"),
        InlineKeyboardButton(f"📈Размер шрифта: {user.fontsize}", callback_data="fontsize"),
        InlineKeyboardButton(f"🗒Текст: {user.text}", callback_data="text"),
        InlineKeyboardButton(f"🧙Запустить мастер настройки", callback_data="master"),
        InlineKeyboardButton(f"🌠В меню", callback_data="main_menu")
    )
