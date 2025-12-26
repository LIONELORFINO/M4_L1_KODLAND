@bot.command()
async def get_my_score(ctx):
    user_id = ctx.author.id

    # hadiah yang sudah didapat user
    info = manager.get_winners_img(user_id)
    won_images = [x[0] for x in info]

    all_images = os.listdir('img')

    image_paths = [
        f'img/{img}' if img in won_images else f'hidden_img/{img}'
        for img in all_images
    ]

    collage = create_collage(image_paths)

    if collage is None:
        await ctx.send("Kamu belum memiliki pencapaian 😅")
        return

    output = f'collage_{user_id}.png'
    cv2.imwrite(output, collage)

    with open(output, 'rb') as img:
        await ctx.send(
            content="🏆 **Pencapaian Kamu** 🏆",
            file=discord.File(img)
        )

    os.remove(output)
