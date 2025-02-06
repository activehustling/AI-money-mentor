const { Telegraf } = require('telegraf');

// Replace '7888972897:AAHbPkOx7awTSLv_oIiLfht7kYccjJcEHuI' with your actual token
const bot = new Telegraf('7888972897:AAHbPkOx7awTSLv_oIiLfht7kYccjJcEHuI');

bot.start((ctx) => ctx.reply('Hello, I am your bot!'));
bot.launch();
