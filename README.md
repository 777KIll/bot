# Telegram Checker Bot 🤖

Professional Telegram bot for checking combos with multiple features:
- Multi-user support with user levels
- Complete admin dashboard
- Config management (.svb files)
- Proxy testing & management
- Live checking results
- Statistics & reporting

## Features 🌟

- **Admin Dashboard:**
  - User management
  - Statistics & reports
  - Broadcast messages
  - Config management

- **User Features:**
  - Multiple config support
  - Proxy testing
  - Live check results
  - Profile management  
  
- **Checker Engine:**
  - Support all config types
  - Multi-proxy support
  - Auto proxy testing
  - Live results

## Installation 🚀

1. Clone the repository
```bash
git clone https://github.com/777KIll/bot.git
```

2. Install requirements
```bash
pip install -r requirements.txt
```

3. Configure `config/bot_config.py`
```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
ADMIN_IDS = [YOUR_TELEGRAM_ID]
```

4. Run the bot
```bash
python main.py
```

## Structure 📁

```
telegram_checker_bot/
├── config/           # Bot configuration
├── database/         # Database models
├── handlers/         # Message handlers
├── utils/           # Utility functions
├── keyboards/       # Telegram keyboards
└── main.py         # Main bot file
```

## License 📝

MIT License - Copyright (c) 2025 777KIll