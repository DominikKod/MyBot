import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

energy_tips = [
    "💡 Turn off the lights when you leave a room.",
    "🔌 Unplug devices when you're not using them.",
    "🌡️ Keep your heating at a low but comfy temperature.",
    "🕶️ Let sunlight in instead of turning on lights during the day.",
    "📴 Turn off your game console completely – don't leave it on standby!"
]

quiz_questions = [
    {
        "question": "What uses more energy?",
        "options": ["Leaving the TV on for 8 hours", "Using the microwave for 5 minutes"],
        "answer": 1
    },
    {
        "question": "Which saves more power?",
        "options": ["Turning your PC off overnight", "Putting it to sleep mode"],
        "answer": 0
    }
]

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hey {ctx.author.name}, I'm here to help you save energy! ⚡")

@bot.command()
async def tip(ctx):
    tip = random.choice(energy_tips)
    embed = discord.Embed(title="🌱 Simple Energy-Saving Tip", description=tip, color=0x00ff00)
    await ctx.send(embed=embed)

@bot.command()
async def quiz(ctx):
    q = random.choice(quiz_questions)
    options_text = "\n".join([f"{i + 1}. {opt}" for i, opt in enumerate(q["options"])])
    embed = discord.Embed(title="🧠 Energy Quiz", description=f"{q['question']}\n\n{options_text}", color=0x3498db)
    await ctx.send(embed=embed)

    def check(m):
        return m.author == ctx.author and m.content.isdigit()

    try:
        response = await bot.wait_for("message", check=check, timeout=15.0)
        user_answer = int(response.content) - 1
        if user_answer == q["answer"]:
            await ctx.send("✅ That's right! You're an energy hero!")
        else:
            await ctx.send("❌ Oops! Not quite. But now you know!")
    except:
        await ctx.send("⌛ Time's up! Try the quiz again later.")

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTM4MzExNzEwNDQ3NTAxNzM2Ng.GHxEwJ.PR0Ns-1vSEbCk70CS0HsBa9_IO69Vokbap4E6c")
