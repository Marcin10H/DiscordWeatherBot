import discord


class GlobalLayout(discord.ui.LayoutView):
    def __init__(
        self,
        description: str = "",
    ):
        super().__init__()
        self.description = description

        container = discord.ui.Container(accent_colour=discord.Color(0xFCF5AB))
        container.add_item(
            discord.ui.TextDisplay(self.description)
        )
        container.add_item(discord.ui.Separator(spacing=discord.SeparatorSpacing.large))

        self.add_item(container)
