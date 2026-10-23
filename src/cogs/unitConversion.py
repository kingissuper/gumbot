import discord
from discord.ext import commands
from discord import app_commands

#Create a group and cog for unit conversion commands
class unitConversion(commands.GroupCog, group_name="convert", group_description="Commands for unit conversion(heh, Americans)"):
    def __init__(self, bot):
        self.bot = bot

    #distance conversion, takes millimeters, centimeters, meters, kilometers, miles, feet, inches & yards as units
    @app_commands.command(name="distance", description="Convert distance units")
    @app_commands.describe(value="USE . AS SEPARATOR. The value to convert", from_unit="The unit to convert from", to_unit="The unit to convert to")
    @app_commands.choices(
        from_unit=[app_commands.Choice(name="Millimeters", value="millimeters"), app_commands.Choice(name="Centimeters", value="centimeters"), app_commands.Choice(name="Meters", value="meters"), app_commands.Choice(name="Kilometers", value="kilometers"), app_commands.Choice(name="Miles", value="miles"), app_commands.Choice(name="Feet", value="feet"), app_commands.Choice(name="Inches", value="inches"), app_commands.Choice(name="Yards", value="yards")],
        to_unit=[app_commands.Choice(name="Millimeters", value="millimeters"), app_commands.Choice(name="Centimeters", value="centimeters"), app_commands.Choice(name="Meters", value="meters"), app_commands.Choice(name="Kilometers", value="kilometers"), app_commands.Choice(name="Miles", value="miles"), app_commands.Choice(name="Feet", value="feet"), app_commands.Choice(name="Inches", value="inches"), app_commands.Choice(name="Yards", value="yards")]
    )
    async def distance(self, interaction: discord.Interaction, value: float, from_unit: str, to_unit: str):
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
        #calculate the converted value and round to 2 decimal places
        converted_value = round(value * RATES.get(from_unit, 1.0) / RATES.get(to_unit, 1.0), 2)
        #send back the values with the according units
        await interaction.response.send_message(f"{value} {from_unit}={converted_value} {to_unit}")
        print(f"converted {from_unit} to {to_unit} with {value}")

async def setup(bot):
    await bot.add_cog(unitConversion(bot))