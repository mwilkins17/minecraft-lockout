import random
import json

old_advancements = [
{"name": "Serious Dedication (hoe)"},
{"name": "Total Beelocation (3 bees)"},
{"name": "Best Friends Forever (tame)"},
{"name": "Sticky Situation (honey)"},
{"name": "Return to Sender (ghast)"},
{"name": "Bullseye (target)"},
{"name": "Sniper Duel (skeleton)"},
{"name": "Overpowered (notch)"},
{"name": "Arbalistic (crossbow 5 mobs)"},
{"name": "War Pigs (bastion chest)"},
{"name": "Who's the Pillager now (crossbow)"},
{"name": "Two Birds One Arrow (phantoms)"},
{"name": "Hired Help (iron golem)"},
{"name": "Postmortal (totem)"},
{"name": "A Throwaway Joke (trident)"},
{"name": "Hero of the Village (raid)"},
{"name": "Voluntary Exile (captain)"},
{"name": "The End (end)"},
{"name": "Free The End (dragon)"},
{"name": "Eye Spy (stronghold)"},
{"name": "Local Brewery (potion)"},
{"name": "Spooky Scary Skeleton (skull)"},
{"name": "Not Quite Nine Lives (anchor)"},
{"name": "Into Fire (blaze)"},
{"name": "Country Lode, Take Me Home (lodestone)"},
{"name": "This Boat Has Legs (strider)"},
{"name": "Oh Shiny (piglin)"},
{"name": "A Terrible Fortress (fortress)"},
{"name": "Subspace Bubble (travel)"},
{"name": "Hot Tourist Destinations (biomes)"},
{"name": "Hidden in the Depths (ancient debris)"},
{"name": "Zombie Doctor (cure)"},
{"name": "Enchanter (enchant)"},
{"name": "Cover Me With Diamonds (bling)"},
{"name": "Ice Bucket Challenge (obsidian)"},
]
new_advancements = [
{"name": "Caves & Cliffs (top to bottom fall)"},
{"name": "Star Trader (trade at build limit)"},
{"name": "Sound of Music (jukebox in meadow)"},
{"name": "Whatever Floats Your Goat! (goat boat)"},
{"name": "Wax on (Apply Honeycomb to a Copper block)"},
{"name": "Healing Power of Friendship! (Axolotl fight)"},
{"name": "Light as a Rabbit (Snow & Leather Boots)"},
{"name": "Is It a Bird? (Parrot through a Spyglass)"}
]

all_achievements_we_want = []
random.shuffle(old_advancements)
all_achievements_we_want.extend(old_advancements[:17])
all_achievements_we_want.extend(new_advancements)
random.shuffle(all_achievements_we_want)
print(json.dumps(all_achievements_we_want))
# print(all_achievements_we_want)
print(len(all_achievements_we_want))