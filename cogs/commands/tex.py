import io
import re
import urllib.parse

from discord.ext import commands
from discord.ext.commands import Bot, Context, clean_content
from discord.file import File
from PIL import Image

import utils

LONG_HELP_TEXT = """
Render a LaTeX maths expression to an image and show it in-line.
"""

SHORT_HELP_TEXT = """Display LaTeX formatted maths."""

API_URL = r"https://latex.codecogs.com/png.image?\dpi{300}\bg{black}"


class Tex(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.hybrid_command(help=LONG_HELP_TEXT, brief=SHORT_HELP_TEXT)
    async def tex(self, ctx: Context, *, tex: str):
        tex_raw = await clean_content().convert(ctx, tex)

        # Input filtering
        if not tex_raw:
            await ctx.send("Your message contained nothing to render")

        if tex_raw[0] == "```tex":
            tex_raw = ("```", *tex_raw[1:])

        tex_code = tex_raw.strip("`")
        # If $ are included, wrap in \text to format normal text
        if tex_code.count("$") >= 2:
            tex_code = f"\\text{{{tex_code}}}"
        # Code with no colour commands
        tex_white = re.sub(r"\\color{.*?\}", "", tex_code)

        # Make request
        url = API_URL + urllib.parse.quote(tex_code)
        r = await utils.get_from_url(url)
        if r is None:
            return await ctx.reply("Invalid equation :nerd:")
        c = io.BytesIO(r)

        # Make second request
        url2 = API_URL + urllib.parse.quote(tex_white)
        r2 = await utils.get_from_url(url2)
        c2 = io.BytesIO(r2)

        # Mask in colours (API only does a few colours)
        text = Image.open(c).convert("RGB")
        mask = Image.open(c2).convert("L")
        bg = Image.new("RGB", (text.width, text.height), (54, 57, 63))
        result = Image.composite(text, bg, mask)

        # Save masked image
        img = io.BytesIO()
        result.save(img, format="png")
        img.seek(0)

        # Load the image as a file to be attached to an image
        img_file = File(img, filename="tex.png")
        await ctx.reply(f"Here you go! :abacus:", file=img_file)


async def setup(bot: Bot):
    await bot.add_cog(Tex(bot))
