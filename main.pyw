from keyboard import is_pressed, write, press_and_release as press, write
from random import randint
from quotes import quotes
import asyncio

async def paste(quote):
    press("shift+enter")
    await asyncio.sleep(.1)
    write(quote)
    await asyncio.sleep(.1)
    press("enter")
    await asyncio.sleep(.8)

class PasteQuotes:
    def __init__(self, paste_func = paste, quote_delay = 60, delta = 30, startup = 20, interrupt_key = 'j'):
        self.QUOTE_DELAY = quote_delay
        self.DELTA = delta
        self.STARTUP = startup
        self.INERRUPT_KEY = interrupt_key
        self.quotes = quotes
        self.no_more_quotes = False
        self.interrupted = False
        self.paste = paste_func

    def run(self):
        asyncio.run(self._run())

    async def _run(self):
        await asyncio.sleep(self.STARTUP)
        main = asyncio.create_task(self.main_loop())
        check_interrupt = asyncio.create_task(self.check_interrupt())
        await check_interrupt

    async def check_interrupt(self):
        while True:
            await asyncio.sleep(0.05)
            if is_pressed(self.INERRUPT_KEY):
                self.interrupted = True
                break

    async def main_loop(self):
        await asyncio.sleep(1)
        while not self.interrupted and not self.no_more_quotes:
            segments = self.split_quote(self.select_quote())
            for segment in segments:
                await self.paste(segment)
            await asyncio.sleep(self.QUOTE_DELAY + randint(-self.DELTA, self.DELTA))
        print("OUT OF QUOTES!")

    def split_quote(self, quote):
        segments = []
        while len(quote) > 240:
            last_space = quote[:240].rindex(" ")
            segments.append(quote[:last_space])
            quote = quote[last_space + 1:]
        return segments + [quote]

    def select_quote(self):
        selected = self.quotes.pop(randint(0, len(self.quotes) - 1))
        if len(self.quotes) == 0: self.no_more_quotes = True
        return selected


if __name__ == "__main__":
    paste = PasteQuotes()
    paste.run()
