def send_telegram(chat_id, message):
    """Send telegram message synchronously"""
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result = loop.run_until_complete(send_telegram_message(chat_id, message))
            return result
        finally:
            loop.close()
    except Exception as e:
        print(f"Error sending telegram: {e}")
        return None
