def on_on_chat():
    mobs.apply_effect(FIRE_RESISTANCE, mobs.target(LOCAL_PLAYER), 600, 255)
    blocks.fill(FIRE, pos(-5, 0, -5), pos(5, 0, 5), FillOperation.REPLACE)
player.on_chat("\"fireproof\"", on_on_chat)

def on_item_interacted_diamond_sword():
    mobs.apply_effect(REGENERATION, mobs.target(LOCAL_PLAYER), 600, 255)
player.on_item_interacted(DIAMOND_SWORD, on_item_interacted_diamond_sword)
