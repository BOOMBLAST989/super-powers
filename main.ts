player.onChat("\"fireproof\"", function () {
    mobs.applyEffect(FIRE_RESISTANCE, mobs.target(LOCAL_PLAYER), 600, 255)
    blocks.fill(
    FIRE,
    pos(-5, 0, -5),
    pos(5, 0, 5),
    FillOperation.Replace
    )
})
player.onItemInteracted(DIAMOND_SWORD, function () {
    mobs.applyEffect(REGENERATION, mobs.target(LOCAL_PLAYER), 600, 255)
})
