#!/usr/bin/env python3

"""
Benimaru Telegram Bot
Control your anime blog automation from Telegram
"""

import os
import json
import logging
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('BenimaruBot')

load_dotenv()

# Bot configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_OWNER = "binnyverse-alt"
REPO_NAME = "Benimaru-Agent"

# Available topics
TOPICS = {
    'ranking_power': '🏆 Ranking/Power Levels',
    'character_comparison': '⚔️ Character Comparison',
    'theory': '🧠 Theory/Analysis',
    'news': '📰 News'
}

TIME_SLOTS = {
    'morning': '☀️ Morning (8:00 AM)',
    'afternoon': '🌤️ Afternoon (2:00 PM)',
    'evening': '🌙 Evening (8:00 PM)'
}

class BenimaruTelegramBot:
    """Telegram bot for managing Benimaru content"""
    
    def __init__(self):
        self.calendar_file = 'content_calendar.json'
        self.calendar_data = self.load_calendar()
    
    def load_calendar(self):
        """Load content calendar from file"""
        try:
            with open(self.calendar_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {'posts': [], 'categories': []}
    
    def save_calendar(self):
        """Save content calendar to file"""
        with open(self.calendar_file, 'w') as f:
            json.dump(self.calendar_data, f, indent=2)
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Start command"""
        welcome_text = """
🎌 **Welcome to Benimaru Telegram Bot!**

I help you manage your anime blog automation directly from Telegram.

**Available Commands:**
/add - Add new blog post
/view - View scheduled posts
/today - Today's posts
/tomorrow - Tomorrow's posts
/categories - View categories
/help - Show help menu

**Topics:**
🏆 ranking_power - Top 10, Rankings
⚔️ character_comparison - VS battles, Comparisons
🧠 theory - Theories, Analysis
📰 news - Breaking news, Announcements

Start by typing /add to create your first post!
        """
        await update.message.reply_text(welcome_text, parse_mode='Markdown')
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Help command"""
        help_text = """
📚 **Benimaru Bot Help**

**🎯 Main Commands:**
/add - Create a new post
/view - List all scheduled posts
/today - Show today's posts
/tomorrow - Show tomorrow's posts
/edit - Edit an existing post
/delete - Delete a post
/categories - Show all categories

**📅 Date Format:** DD/MM/YYYY (e.g., 29/05/2026)

**⏰ Time Slots:**
morning - 8:00 AM UTC
afternoon - 2:00 PM UTC
evening - 8:00 PM UTC

**📝 Topics:**
ranking_power - Ranking/Power Levels
character_comparison - Character Comparison
theory - Theory/Analysis
news - News

**Example:**
Date: 30/05/2026
Time: morning
Title: Top 10 Best Anime
Topic: ranking_power
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    async def add_post(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Start adding a new post"""
        context.user_data['add_step'] = 'date'
        keyboard = []
        await update.message.reply_text(
            "📅 **Enter the date** (DD/MM/YYYY)\nExample: 29/05/2026",
            parse_mode='Markdown'
        )
    
    async def view_posts(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """View all scheduled posts"""
        posts = self.calendar_data.get('posts', [])
        
        if not posts:
            await update.message.reply_text("❌ No posts scheduled yet!")
            return
        
        # Group by date
        posts_by_date = {}
        for post in posts:
            date = post['date']
            if date not in posts_by_date:
                posts_by_date[date] = []
            posts_by_date[date].append(post)
        
        message = "📋 **All Scheduled Posts:**\n\n"
        for date in sorted(posts_by_date.keys()):
            message += f"📅 **{date}**\n"
            for post in posts_by_date[date]:
                emoji = {
                    'morning': '☀️',
                    'afternoon': '🌤️',
                    'evening': '🌙'
                }.get(post['time_slot'], '⏰')
                message += f"{emoji} {post['time_slot']}: {post['title']}\n"
                message += f"   Topic: {post['topic']}\n\n"
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def today_posts(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show today's posts"""
        today = datetime.now().strftime('%Y-%m-%d')
        posts = [p for p in self.calendar_data.get('posts', []) if p['date'] == today]
        
        if not posts:
            await update.message.reply_text(f"❌ No posts for today ({today})")
            return
        
        message = f"📅 **Today's Posts ({today})**\n\n"
        for post in posts:
            emoji = {
                'morning': '☀️',
                'afternoon': '🌤️',
                'evening': '🌙'
            }.get(post['time_slot'], '⏰')
            message += f"{emoji} **{post['time_slot'].upper()}**\n"
            message += f"Title: {post['title']}\n"
            message += f"Topic: {post['topic']}\n"
            message += f"Keywords: {', '.join(post['keywords'])}\n\n"
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def tomorrow_posts(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show tomorrow's posts"""
        tomorrow = datetime.now().strftime('%Y-%m-%d')
        # Calculate next day
        from datetime import timedelta
        next_day = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        
        posts = [p for p in self.calendar_data.get('posts', []) if p['date'] == next_day]
        
        if not posts:
            await update.message.reply_text(f"❌ No posts for tomorrow ({next_day})")
            return
        
        message = f"📅 **Tomorrow's Posts ({next_day})**\n\n"
        for post in posts:
            emoji = {
                'morning': '☀️',
                'afternoon': '🌤️',
                'evening': '🌙'
            }.get(post['time_slot'], '⏰')
            message += f"{emoji} **{post['time_slot'].upper()}**\n"
            message += f"Title: {post['title']}\n"
            message += f"Topic: {post['topic']}\n"
            message += f"Keywords: {', '.join(post['keywords'])}\n\n"
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def show_categories(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show available categories"""
        categories = self.calendar_data.get('categories', [])
        
        message = "📚 **Available Categories:**\n\n"
        for i, cat in enumerate(categories, 1):
            message += f"{i}. {cat}\n"
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle user messages during post creation"""
        if 'add_step' not in context.user_data:
            return
        
        step = context.user_data['add_step']
        message_text = update.message.text
        
        if step == 'date':
            context.user_data['post_date'] = message_text
            context.user_data['add_step'] = 'time'
            
            # Show time slot buttons
            keyboard = [
                [InlineKeyboardButton("☀️ Morning", callback_data='time_morning')],
                [InlineKeyboardButton("🌤️ Afternoon", callback_data='time_afternoon')],
                [InlineKeyboardButton("🌙 Evening", callback_data='time_evening')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(
                "⏰ **Select time slot:**",
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
        
        elif step == 'time':
            context.user_data['add_step'] = 'title'
            await update.message.reply_text("📝 **Enter post title:**")
        
        elif step == 'title':
            context.user_data['post_title'] = message_text
            context.user_data['add_step'] = 'topic'
            
            # Show topic buttons
            keyboard = [
                [InlineKeyboardButton("🏆 Ranking/Power", callback_data='topic_ranking_power')],
                [InlineKeyboardButton("⚔️ Comparison", callback_data='topic_character_comparison')],
                [InlineKeyboardButton("🧠 Theory", callback_data='topic_theory')],
                [InlineKeyboardButton("📰 News", callback_data='topic_news')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(
                "🎯 **Select topic:**",
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
        
        elif step == 'keywords':
            keywords = [k.strip() for k in message_text.split(',')]
            context.user_data['post_keywords'] = keywords
            
            # Create the post
            post = {
                'id': len(self.calendar_data['posts']) + 1,
                'date': context.user_data['post_date'],
                'time_slot': context.user_data['post_time'],
                'title': context.user_data['post_title'],
                'topic': context.user_data['post_topic'],
                'category': context.user_data.get('post_category', 'Anime'),
                'keywords': keywords,
                'status': 'draft',
                'author': 'Binny'
            }
            
            self.calendar_data['posts'].append(post)
            self.save_calendar()
            
            # Clear context
            context.user_data.clear()
            
            message = f"""
✅ **Post Added Successfully!**

📅 Date: {post['date']}
⏰ Time: {post['time_slot']}
📝 Title: {post['title']}
🎯 Topic: {post['topic']}
🏷️ Keywords: {', '.join(keywords)}
            """
            await update.message.reply_text(message, parse_mode='Markdown')
    
    async def button_click(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle button clicks"""
        query = update.callback_query
        data = query.data
        
        await query.answer()
        
        if data.startswith('time_'):
            time_slot = data.replace('time_', '')
            context.user_data['post_time'] = time_slot
            context.user_data['add_step'] = 'title'
            await query.edit_message_text("📝 **Enter post title:**")
        
        elif data.startswith('topic_'):
            topic = data.replace('topic_', '')
            context.user_data['post_topic'] = topic
            context.user_data['add_step'] = 'keywords'
            await query.edit_message_text(
                "🏷️ **Enter keywords (separated by comma):**\nExample: anime, power, ranking"
            )

async def main():
    """Start the bot"""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("❌ TELEGRAM_BOT_TOKEN not set in .env")
        return
    
    logger.info("🤖 Starting Benimaru Telegram Bot...")
    
    bot = BenimaruTelegramBot()
    
    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", bot.start))
    application.add_handler(CommandHandler("help", bot.help_command))
    application.add_handler(CommandHandler("add", bot.add_post))
    application.add_handler(CommandHandler("view", bot.view_posts))
    application.add_handler(CommandHandler("today", bot.today_posts))
    application.add_handler(CommandHandler("tomorrow", bot.tomorrow_posts))
    application.add_handler(CommandHandler("categories", bot.show_categories))
    
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_message))
    application.add_handler(CallbackQueryHandler(bot.button_click))
    
    logger.info("✅ Bot started successfully!")
    
    # Start polling
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
