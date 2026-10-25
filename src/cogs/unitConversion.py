import discord
from discord.ext import commands
from discord import app_commands

#Create a group and cog for unit conversion commands
class unitConversion(commands.GroupCog, group_name="convert", group_description="Commands for unit conversion(heh, Americans)"):
    def __init__(self, bot):
        self.bot = bot

    #AI generated, helper function for number significance
    @classmethod
    def format_result(self, value: float, significance: int | None) -> str:
        if significance is None:
            return str(int(value)) if value.is_integer() else str(value)
        return f"{value:.{significance}g}"
    #helper function for embeds
    @classmethod
    def format_embed(self, title: str, value: float, result_value: float, from_unit: str, to_unit: str, significance: int|None):
        embed = discord.Embed(colour=discord.Colour.dark_blue(), title=f"{title} conversion")
        if significance == None:
            embed.set_footer(text=f"No significance set")
        else:
            embed.set_footer(text=f"Significance of {significance}")
        embed.add_field(name="Input", value=f"{value} {from_unit}", inline=True)
        embed.add_field(name="Result", value=f"{result_value} {to_unit}", inline=True)
        return embed
    
    #distance conversion, takes millimeters, centimeters, meters, kilometers, miles, feet, inches & yards as units
    @app_commands.command(name="distance", description="Convert distance units")
    @app_commands.describe(value="USE . AS SEPARATOR. The value to convert", from_unit="The unit to convert from", to_unit="The unit to convert to", significance="The amount of significant numbers (default 2)")
    @app_commands.choices(
        from_unit=[app_commands.Choice(name="Millimeters", value="millimeters"), app_commands.Choice(name="Centimeters", value="centimeters"), app_commands.Choice(name="Meters", value="meters"), app_commands.Choice(name="Kilometers", value="kilometers"), app_commands.Choice(name="Miles", value="miles"), app_commands.Choice(name="Feet", value="feet"), app_commands.Choice(name="Inches", value="inches"), app_commands.Choice(name="Yards", value="yards")],
        to_unit=[app_commands.Choice(name="Millimeters", value="millimeters"), app_commands.Choice(name="Centimeters", value="centimeters"), app_commands.Choice(name="Meters", value="meters"), app_commands.Choice(name="Kilometers", value="kilometers"), app_commands.Choice(name="Miles", value="miles"), app_commands.Choice(name="Feet", value="feet"), app_commands.Choice(name="Inches", value="inches"), app_commands.Choice(name="Yards", value="yards")]
    )
    async def distance(self, interaction: discord.Interaction, value: float, from_unit: str, to_unit: str, significance: int|None=None):
        #unit conversion rates
        RATES = {
            "millimeters": 0.001,
            "centimeters": 0.01,
            "meters": 1.0,
            "kilometers": 1000.0,
            "miles": 1609.34,
            "feet": 0.3048,
            "inches": 0.0254,
            "yards": 0.9144
        }
        #calculate the converted value
        converted_value = value * RATES.get(from_unit, 1.0) / RATES.get(to_unit, 1.0)
        result_value = self.format_result(converted_value, significance)
        #send back the values with the according units and significant numbers
        await interaction.response.send_message(embed=self.format_embed(title="Distance", value=value, result_value=result_value, from_unit=from_unit, to_unit=to_unit, significance=significance))
        print(f"converted {value} {from_unit} to {converted_value} {to_unit} with a significance of {significance}")
    #speed conversion, takes meters per second, kilometers per hour, miles per hour & feet per second as units
    @app_commands.command(name="speed", description="Convert speed units")
    @app_commands.describe(value="USE . AS SEPARATOR. The value to convert", from_unit="The unit to convert from", to_unit="The unit to convert to", significance="The amount of significant numbers (default 0)")
    @app_commands.choices(
        from_unit=[app_commands.Choice(name="Meters per second", value="m/s"), app_commands.Choice(name="Kilometers per hour", value="km/h"), app_commands.Choice(name="Miles per hour", value="mph"), app_commands.Choice(name="Feet per second", value="ft/s")],
        to_unit=[app_commands.Choice(name="Meters per second", value="m/s"), app_commands.Choice(name="Kilometers per hour", value="km/h"), app_commands.Choice(name="Miles per hour", value="mph"), app_commands.Choice(name="Feet per second", value="ft/s")]
    )
    async def speed(self, interaction: discord.Interaction, value: float, from_unit: str, to_unit: str, significance: int|None=None):
        #unit conversion rates
        RATES = {
            "m/s": 1.0,
            "km/h": 1 / 3.6,
            "mph": 0.44704,
            "ft/s": 0.3048
        }
        #calculate the converted value
        converted_value = value * RATES.get(from_unit, 1.0) / RATES.get(to_unit, 1.0)
        result_value = self.format_result(converted_value, significance)
        #send back the values with the according units and significant numbers
        await interaction.response.send_message(embed=self.format_embed(title="Speed", value=value, result_value=result_value, from_unit=from_unit, to_unit=to_unit, significance=significance))
        print(f"converted {value} {from_unit} to {converted_value} {to_unit} with a significance of {significance}")
    #weight conversion, takes milligrams grams kilograms ounces pounds tonne & ton as units
    @app_commands.command(name="weight", description="Convert weight units")
    @app_commands.describe(value="USE . AS SEPARATOR. The value to convert", from_unit="The unit to convert from", to_unit="The unit to convert to", significance="The amount of significant numbers (default 2)")
    @app_commands.choices()
    async def weight(self, interaction: discord.Interaction, value: float, from_unit: str, to_unit: str, significance: int|None=None):
        #unit conversion rates
        RATES = {
            "milligrams": 0.001,
            "grams": 1.0,
            "kilograms": 1000.0,
            "ounces": 28.349523125,
            "pounds": 453.59237,
            "tonne": 1000000.0,
            "ton": 907184.74
        }
        #calculate the converted value
        converted_value = value * RATES.get(from_unit, 1.0) / RATES.get(to_unit, 1.0)
        result_value = self.format_result(converted_value, significance)
        #send back the values with the according units and significant numbers
        await interaction.response.send_message(embed=self.format_embed(title="Weight", value=value, result_value=result_value, from_unit=from_unit, to_unit=to_unit, significance=significance))
        print(f"converted {value} {from_unit} to {converted_value} {to_unit} with a significance of {significance}")
    #temperature conversion, takes celsius, fahrenheit & kelvin as units
    @app_commands.command(name="temperature", description="Convert temperature units")
    @app_commands.describe(value="USE . AS SEPARATOR. The value to convert", from_unit="The unit to convert from", to_unit="The unit to convert to", significance="The amount of significant numbers (default 0)")
    @app_commands.choices(
        from_unit=[app_commands.Choice(name="Celsius", value="celsius"), app_commands.Choice(name="Fahrenheit", value="fahrenheit"), app_commands.Choice(name="Kelvin", value="kelvin")],
        to_unit=[app_commands.Choice(name="Celsius", value="celsius"), app_commands.Choice(name="Fahrenheit", value="fahrenheit"), app_commands.Choice(name="Kelvin", value="kelvin")]
    )
    async def temperature(self, interaction: discord.Interaction, value: float, from_unit: str, to_unit: str, significance: int|None=None):
        converted_value = value
        if from_unit == "celsius":
            if to_unit == "fahrenheit":
                converted_value = value * 9 / 5 + 32
            elif to_unit == "kelvin":
                converted_value = value + 273.15
        elif from_unit == "fahrenheit":
            if to_unit == "celsius":
                converted_value = (value - 32) * 5 / 9
            elif to_unit == "kelvin":
                converted_value = (value - 32) * 5 / 9 + 273.15
        elif from_unit == "kelvin":
            if to_unit == "celsius":
                converted_value = value - 273.15
            elif to_unit == "fahrenheit":
                converted_value = (value - 273.15) * 9 / 5 + 32
        result_value = self.format_result(converted_value, significance)
        #send back the values with the according units and significant numbers
        await interaction.response.send_message(embed=self.format_embed(title="Distance", value=value, result_value=result_value, from_unit=from_unit, to_unit=to_unit, significance=significance))
        print(f"converted {value} {from_unit} to {converted_value} {to_unit} with a significance of {significance}")

async def setup(bot):
    await bot.add_cog(unitConversion(bot))