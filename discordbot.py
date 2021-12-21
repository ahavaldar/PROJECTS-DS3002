import discord
import requests
import time
import random

TOKEN = "$$$$OTE5MzM2OTgzNjE5MzMwMDY4.$$$$$$$YbUVSQ.0hyiAevZnuib4RZItQfOg33A3VI$$$$$$"

client = discord.Client()

help_choices = ["Valid Stock Tickers", "Where Can I Find Stock Info", "How to Retrieve Stock Info"]
hello_options = ["wassup", "How's it going?", "Welcome!", "Hello!", "Hola", "Howdy", "Good day", "hi", "Hi", "hello",
                 "Hello"]


@client.event
async def on_message(message):
    if message.author == client.user:
        return
### Hello Command
    if message.content.startswith("Hi"):
        await message.channel.send(random.choice(hello_options))
### Help Commands
    if message.content.startswith("help"):
        await message.channel.send("What do you need help with? (please select the option number): " + " (1) " +
                                   help_choices[0] + " (2) " + help_choices[1] + " (3) " + help_choices[2])
    if message.content.startswith("1"):
        await message.channel.send("Valid stock tickers are 1-4 letter symbols that can be either "
                                       "uppercase or lowercase.")
    if message.content.startswith("2"):
        await message.channel.send("All stock info is pulled from the Yahoo Finance API, which can be found at"
                                       " https://yahoofinanceapi.com.")
    if message.content.startswith("3"):
        await message.channel.send("Enter 'stock: ' followed by the 1-4 letter stock ticker.")
### Using stock API
    if message.content.startswith("stock:"):
        phrase = message.content.split()
        stock = ""
        for word in phrase[1:]:             # Splits the stock phrase so the bot only stores the following stock ticker
            stock += word
            stock += " "

        # Defining the key and URL
        apikey = "AToTpREVIw55N3JNY5otS66TdWPPfqNMKAeWP0e7"
        url = "https://yfapi.net/v6/finance/quote"

        # Getting the stock info from the API
        querystring = {"symbols": stock}
        headers = {
            'x-api-key': apikey
        }
        response = requests.request("GET", url, headers=headers, params=querystring)

        stock_json = response.json()

        # Converting the time into readable format
        timestamp = stock_json['quoteResponse']['result'][0]["regularMarketTime"]
        real_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timestamp))

        # Printing the resulting stock data
        result = ("Company Name: " + str(stock_json['quoteResponse']['result'][0]["shortName"]) +
                  " Price: $" + str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]) +
                  " Market Time: " + real_time)
        await message.channel.send("Finding stock information for: " + stock)
        await message.channel.send(result)

### Welcoming someone to server
@client.event
async def on_member_join(member):
    await member.channel.send(f'Hello {member.name}, welcome to the Server!')


@client.event
async def on_ready():
    print("running")

client.run(TOKEN)
print(client.user.name)
