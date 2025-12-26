@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type != discord.InteractionType.component:
        return

    prize_id = interaction.data['custom_id']
    user_id = interaction.user.id
    username = interaction.user.name

    # cek apakah hadiah masih tersedia (maks 3)
    if manager.count_winners(prize_id) >= 3:
        await interaction.response.send_message(
            content="😢 Maaf, hadiah sudah habis.",
            ephemeral=True
        )
        return

    # coba tambahkan pemenang
    success = manager.add_winner(user_id, username, prize_id)

    if not success:
        await interaction.response.send_message(
            content="❌ Kamu sudah mengambil hadiah ini!",
            ephemeral=True
        )
        return

    # kirim gambar hadiah
    img = manager.get_prize_img(prize_id)
    with open(f'img/{img}', 'rb') as photo:
        file = discord.File(photo)
        await interaction.response.send_message(
            content="🎉 Selamat, kamu mendapatkan gambar!",
            file=file
        )
