#!/usr/bin/env python3

"""
Benimaru Telegram Bot - Simple Version
Control your anime blog automation from Telegram
"""

import os
import json
import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, 
    CallbackQueryHandler, ContextTypes, filters
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('telegram_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('BenimaruBot')

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

class BenimaruBot:
    def __init__(self):
        self.calendar_file = 'content_calendar.json'
        logger.info("✅ Benimaru Bot initialized")
    
    def load_calendar(self):
        try:
            with open(self.calendar_file, 'r') as f:
                return json.load(f)
        except:
            return {'posts': [], 'categories': []}
    
    def save_calendar(self, data):
        with open(self.calendar_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Start command"""
        msg = """🎌 **Benimaru Anime Bot Ready!**

I help manage your anime blog automation.

**📋 Commands:**
/add - Add new post
/view - View all posts
/today - Today's posts
/help - Show help
"""
        await update.message.reply_text(msg, parse_mode='Markdown')
    
    async def help_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Help command"""
        msg = """📚 **Help Menu**

/start - Welcome
/add - Create post
/view - See posts
/today - Today posts
/tomorrow - Tomorrow posts
/help - This menu
"""
        await update.message.reply_text(msg, parse_mode='Markdown')
    
    async def add(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Add post command"""
        context.user_data['step'] = 'date'
        await update.message.reply_text("📅 Enter date (DD/MM/YYYY):\nExample: 31/05/2026")
    
    async def view(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """View all posts"""
        data = self.load_calendar()
        posts = data.get('posts', [])
        
        if not posts:
            await update.message.reply_text("❌ No posts")
            return
        
        msg = "📋 **All Posts:**\n\n"
        for post in posts:
            msg += f"📅 {post['date']} {post['time_slot']}\n"
            msg += f"📝 {post['title']}\n"
            msg += f"🎯 {post['topic']}\n\n"
        
        await update.message.reply_text(msg, parse_mode='Markdown')
    
    async def today(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Today's posts"""
        today = datetime.now().strftime('%Y-%m-%d')
        data = self.load_calendar()
        posts = [p for p in data.get('posts', []) if p['date'] == today]
        
        if not posts:
            await update.message.reply_text(f"❌ No posts today ({today})")
            return
        
        msg = f"📅 **Today ({today}):**\n\n"
        for post in posts:
            msg += f"{post['time_slot']}: {post['title']}\n"
        
        await update.message.reply_text(msg, parse_mode='Markdown')
    
    async def tomorrow(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Tomorrow's posts"""
        tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        data = self.load_calendar()
        posts = [p for p in data.get('posts', []) if p['date'] == tomorrow]
        
        if not posts:
            await update.message.reply_text(f"❌ No posts tomorrow ({tomorrow})")
            return
        
        msg = f"📅 **Tomorrow ({tomorrow}):**\n\n"
        for post in posts:
            msg += f"{post['time_slot']}: {post['title']}\n"
        
        await update.message.reply_text(msg, parse_mode='Markdown')
    
    async def message_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle messages"""
        if 'step' not in context.user_data:
            return
        
        step = context.user_data['step']
        text = update.message.text
        
        if step == 'date':
            context.user_data['date'] = text
            context.user_data['step'] = 'time'
            
            keyboard = [
                [InlineKeyboardButton("☀️ Morning", callback_data='time_morning')],
                [InlineKeyboardButton("🌤️ Afternoon", callback_data='time_afternoon')],
                [InlineKeyboardButton("🌙 Evening", callback_data='time_evening')]
            ]
            await update.message.reply_text(
                "⏰ Select time:",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        
        elif step == 'title':
            context.user_data['title'] = text
            context.user_data['step'] = 'topic'
            
            keyboard = [
                [InlineKeyboardButton("🏆 Ranking", callback_data='topic_ranking_power')],
                [InlineKeyboardButton("⚔️ Comparison", callback_data='topic_character_comparison')],
                [InlineKeyboardButton("🧠 Theory", callback_data='topic_theory')],
                [InlineKeyboardButton("📰 News", callback_data='topic_news')]
            ]
            await update.message.reply_text(
                "🎯 Select topic:",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        
        elif step == 'keywords':
            keywords = [k.strip() for k in text.split(',')]
            
            # Create post
            data = self.load_calendar()
            post = {
                'id': len(data['posts']) + 1,
                'date': context.user_data['date'],
                'time_slot': context.user_data['time'],
                'title': context.user_data['title'],
                'topic': context.user_data['topic'],
                'category': 'Anime',
                'keywords': keywords,
                'status': 'draft',
                'author': 'Binny'
            }
            
            data['posts'].append(post)
            self.save_calendar(data)
            context.user_data.clear()
            
            await update.message.reply_text(
                f"✅ **Post Added!**\n📝 {post['title']}\n🎯 {post['topic']}"
            )
    
    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle button clicks"""
        query = update.callback_query
        await query.answer()
        
        if query.data.startswith('time_'):
            time = query.data.replace('time_', '')
            context.user_data['time'] = time
            context.user_data['step'] = 'title'
            await query.edit_message_text("📝 Enter post title:")
        
        elif query.data.startswith('topic_'):
            topic = query.data.replace('topic_', '')
            context.user_data['topic'] = topic
            context.user_data['step'] = 'keywords'
            await query.edit_message_text("🏷️ Enter keywords (comma separated):")

async def main():
    if not TELEGRAM_BOT_TOKEN:
        logger.error("❌ TELEGRAM_BOT_TOKEN not found!")
        return
    
    logger.info("🚀 Starting Benimaru Bot...")
    
    bot = BenimaruBot()
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", bot.start))
    app.add_handler(CommandHandler("help", bot.help_cmd))
    app.add_handler(CommandHandler("add", bot.add))
    app.add_handler(CommandHandler("view", bot.view))
    app.add_handler(CommandHandler("today", bot.today))
    app.add_handler(CommandHandler("tomorrow", bot.tomorrow))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot.message_handler))
    app.add_handler(CallbackQueryHandler(bot.button_handler))
    
    logger.info("✅ Bot handlers registered")
    logger.info("🎌 Benimaru Bot is running...")
    
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
