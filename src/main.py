import os
import asyncio
import logging
from telegram import Update
from telegram.ext import (
    filters,
    Application,
    ContextTypes,
    MessageHandler,
    PicklePersistence,
)

from storage import Storage, STORAGES

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

MAIN_LOCK = asyncio.Lock()


async def check(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Check user's answer"""
    async with MAIN_LOCK:
        await _check(update, context)


async def _check(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    topic = update.message.message_thread_id
    topics: dict[int, Storage | None] = context.bot_data.setdefault("topics", {})
    topics.setdefault(topic, None)

    if topic not in STORAGES:
        return

    if topics[topic] is None:
        topics[topic] = STORAGES[update.message.message_thread_id].defaults()

        for msg in topics[topic].initial_messages():
            await context.bot.send_message(
                update.message.chat_id,
                msg,
                message_thread_id=topic,
                parse_mode="Markdown",
            )

    correct = topics[topic].update(update.message.text)

    await context.bot.delete_message(
        chat_id=update.message.chat_id,
        message_id=update.message.message_id,
    )

    if correct:
        await context.bot.send_message(
            update.message.chat_id,
            topics[topic].to_message(),
            message_thread_id=topic,
            parse_mode="Markdown",
        )
        return


def main() -> None:
    """Start the bot."""
    persistence = PicklePersistence(filepath="ngp.data", update_interval=1)
    application = (
        Application.builder().token(os.getenv("TOKEN")).persistence(persistence).build()
    )
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
