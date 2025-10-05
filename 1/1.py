import sys
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from typing import Dict, List, Any, Optional, Set, Tuple
import random

# --- Game Data ---
# This data is hardcoded for simplicity. In a larger application, this might come from
# a JSON file, a database, or an external API.

GODS_DATA: Dict[str, Dict[str, Any]] = {
    "Zeus": {
        "description": "God of Lightning. Grants boons focused on lightning damage, chain effects, and jolting foes.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"]
    },
    "Poseidon": {
        "description": "God of the Sea. Grants boons focused on knockback, rupture, and resource acquisition.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"]
    },
    "Athena": {
        "description": "Goddess of Wisdom. Grants boons focused on Deflect, invulnerability, and damage reduction.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"]
    },
    "Aphrodite": {
        "description": "Goddess of Love. Grants boons focused on weakening foes and charm effects.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"]
    },
    "Ares": {
        "description": "God of War. Grants boons focused on Blade Rifts, Doom status, and high damage.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"]
    },
    "Artemis": {
        "description": "Goddess of the Hunt. Grants boons focused on Critical hits and tracking shots.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"]
    },
    "Dionysus": {
        "description": "God of Wine. Grants boons focused on Hangover status, healing, and festive fog.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"]
    },
    "Hermes": {
        "description": "God of Speed. Grants boons focused on movement speed, dodge chance, and attack speed.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"]
    },
    "Demeter": {
        "description": "Goddess of Seasons. Grants boons focused on Chill status, slowing foes, and crystal effects.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"]
    },
    "Chaos": {
        "description": "Primordial entity. Grants boons that offer powerful buffs with temporary curses.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"]
    }
}

# BOONS_DATA: Each boon includes its god, type, description, and tags for synergy.
# 'status_curse_applied' indicates if this boon applies a specific status curse.
# 'status_curse_name' is used for the actual status curse boons (e.g., "Jolted" itself).
BOONS_DATA: List[Dict[str, Any]] = [
    # Zeus Boons
    {"name": "Lightning Strike", "god": "Zeus", "type": "Attack", "description": "Your Attack deals bonus lightning damage.", "tags": ["attack", "lightning", "damage"], "status_curse_applied": "Jolted"},
    {"name": "Thunder Flourish", "god": "Zeus", "type": "Special", "description": "Your Special creates a lightning bolt that strikes nearby foes.", "tags": ["special", "lightning", "damage"], "status_curse_applied": "Jolted"},
    {"name": "Thunder Dash", "god": "Zeus", "type": "Dash", "description": "Your Dash creates a lightning bolt that strikes nearby foes.", "tags": ["dash", "lightning", "damage"], "status_curse_applied": "Jolted"},
    {"name": "Storm Lightning", "god": "Zeus", "type": "Cast", "description": "Your Cast creates a storm cloud that strikes foes.", "tags": ["cast", "lightning", "damage"], "status_curse_applied": "Jolted"},
    {"name": "Billowing Strength", "god": "Zeus", "type": "Call", "description": "Your Call deals lightning damage and makes you invulnerable.", "tags": ["call", "lightning", "invulnerability"], "status_curse_applied": "Jolted"},
    {"name": "Static Discharge", "god": "Zeus", "type": "Utility", "description": "Your lightning effects also make foes Jolted.", "tags": ["jolted_applier", "status_curse_applier", "lightning_synergy"], "status_curse_applied": "Jolted"},
    {"name": "Double Strike", "god": "Zeus", "type": "Utility", "description": "Your lightning effects have a chance to strike twice.", "tags": ["lightning_enhancer", "damage_enhancer"]},
    {"name": "High Voltage", "god": "Zeus", "type": "Utility", "description": "Your lightning effects deal damage in a larger area.", "tags": ["lightning_enhancer", "aoe_enhancer"]},
    {"name": "Clouded Judgment", "god": "Zeus", "type": "Utility", "description": "Your Jolted effects deal more damage.", "tags": ["jolted_enhancer", "status_curse_damage"]},
    {"name": "Splitting Bolt", "god": "Zeus", "type": "Utility", "description": "Your lightning effects have a chance to strike an additional foe.", "tags": ["lightning_enhancer", "chain_effect"]},
    {"name": "Jolted", "god": "Zeus", "type": "Status Curse", "description": "Foes struck by your lightning effects become Jolted. Jolted foes take damage if they attack.", "tags": ["status_curse", "jolted"], "status_curse_name": "Jolted"},

    # Poseidon Boons
    {"name": "Tidal Dash", "god": "Poseidon", "type": "Dash", "description": "Your Dash creates a splash that damages foes and knocks them away.", "tags": ["dash", "knockback", "damage"]},
    {"name": "Tempest Strike", "god": "Poseidon", "type": "Attack", "description": "Your Attack deals bonus damage and knocks foes away.", "tags": ["attack", "knockback", "damage"]},
    {"name": "Flood Shot", "god": "Poseidon", "type": "Cast", "description": "Your Cast fires a projectile that bursts, damaging and knocking foes away.", "tags": ["cast", "knockback", "damage"]},
    {"name": "Poseidon's Aid", "god": "Poseidon", "type": "Call", "description": "Your Call deals damage and knocks foes away.", "tags": ["call", "knockback", "damage"]},
    {"name": "Typhoon's Fury", "god": "Poseidon", "type": "Utility", "description": "Your knock-away effects deal more damage.", "tags": ["knockback_enhancer", "damage_enhancer"]},
    {"name": "Razor Shoals", "god": "Poseidon", "type": "Utility", "description": "Your knock-away effects also inflict Rupture.", "tags": ["rupture_applier", "status_curse_applier"], "status_curse_applied": "Rupture"},
    {"name": "Wave Pounce", "god": "Poseidon", "type": "Dash", "description": "Your Dash deals more damage and knocks foes away.", "tags": ["dash", "knockback", "damage"]},
    {"name": "Hydraulic Might", "god": "Poseidon", "type": "Utility", "description": "After using your Call, your Attack and Special deal more damage for a short time.", "tags": ["damage_enhancer", "call_synergy"]},
    {"name": "Breaking Wave", "god": "Poseidon", "type": "Utility", "description": "Your knock-away effects deal damage in a larger area.", "tags": ["knockback_enhancer", "aoe_enhancer"]},
    {"name": "Rip Current", "god": "Poseidon", "type": "Utility", "description": "Your Casts travel farther and deal more damage.", "tags": ["cast_enhancer", "damage_enhancer"]},
    {"name": "Sweet Nectar", "god": "Poseidon", "type": "Utility", "description": "Find Poms of Power more often.", "tags": ["resource_gain"]},
    {"name": "Rupture", "god": "Poseidon", "type": "Status Curse", "description": "Foes afflicted with Rupture take damage over time while moving.", "tags": ["status_curse", "rupture"], "status_curse_name": "Rupture"},
    {"name": "Ocean's Bounty", "god": "Poseidon", "type": "Legendary", "description": "You find more Darkness, Gemstones, and Keys.", "tags": ["resource_gain", "legendary"]},

    # Athena Boons
    {"name": "Divine Dash", "god": "Athena", "type": "Dash", "description": "Your Dash makes you Deflect.", "tags": ["dash", "deflect", "utility"]},
    {"name": "Divine Strike", "god": "Athena", "type": "Attack", "description": "Your Attack makes you Deflect.", "tags": ["attack", "deflect", "utility"]},
    {"name": "Divine Flourish", "god": "Athena", "type": "Special", "description": "Your Special makes you Deflect.", "tags": ["special", "deflect", "utility"]},
    {"name": "Phalanx Shot", "god": "Athena", "type": "Cast", "description": "Your Cast fires a projectile that Deflects.", "tags": ["cast", "deflect", "utility"]},
    {"name": "Athena's Aid", "god": "Athena", "type": "Call", "description": "Your Call makes you Deflect and invulnerable.", "tags": ["call", "deflect", "invulnerability"]},
    {"name": "Holy Shield", "god": "Athena", "type": "Utility", "description": "You take less damage from foes in front of you.", "tags": ["damage_reduction", "utility"]},
    {"name": "Blinding Flash", "god": "Athena", "type": "Utility", "description": "Your Deflect effects also make foes Weak.", "tags": ["weak_applier", "status_curse_applier", "deflect_synergy"], "status_curse_applied": "Weak"},
    {"name": "Sure Footing", "god": "Athena", "type": "Utility", "description": "You are immune to damage from traps.", "tags": ["utility", "trap_immunity"]},
    {"name": "Deathless Stand", "god": "Athena", "type": "Utility", "description": "When your HP is depleted, restore some HP once per encounter.", "tags": ["survivability", "death_defiance"]},
    {"name": "Brilliant Riposte", "god": "Athena", "type": "Utility", "description": "After you Deflect, your next Attack or Special deals more damage.", "tags": ["deflect_synergy", "damage_enhancer"]},
    {"name": "Unraveling", "god": "Athena", "type": "Utility", "description": "Your Deflect effects also remove enemy buffs.", "tags": ["deflect_synergy", "utility"]},
    {"name": "Divine Protection", "god": "Athena", "type": "Utility", "description": "You take no damage from a single hit once per encounter.", "tags": ["survivability", "death_defiance"]},
    {"name": "Proud Bearing", "god": "Athena", "type": "Legendary", "description": "Start each encounter with some Call gauge.", "tags": ["call_synergy", "resource_gain", "legendary"]},

    # Aphrodite Boons
    {"name": "Heartbreak Strike", "god": "Aphrodite", "type": "Attack", "description": "Your Attack deals bonus damage and inflicts Weak.", "tags": ["attack", "damage", "weak_applier"], "status_curse_applied": "Weak"},
    {"name": "Crush Shot", "god": "Aphrodite", "type": "Cast", "description": "Your Cast fires a slow projectile that deals damage and inflicts Weak.", "tags": ["cast", "damage", "weak_applier"], "status_curse_applied": "Weak"},
    {"name": "Passion Dash", "god": "Aphrodite", "type": "Dash", "description": "Your Dash deals damage and inflicts Weak.", "tags": ["dash", "damage", "weak_applier"], "status_curse_applied": "Weak"},
    {"name": "Aphrodite's Aid", "god": "Aphrodite", "type": "Call", "description": "Your Call deals damage and inflicts Charm.", "tags": ["call", "damage", "charm_applier"], "status_curse_applied": "Charm"},
    {"name": "Empty Inside", "god": "Aphrodite", "type": "Utility", "description": "Your Weak effects last longer.", "tags": ["weak_enhancer", "status_curse_duration"]},
    {"name": "Low Tolerance", "god": "Aphrodite", "type": "Utility", "description": "Your Weak effects deal more damage.", "tags": ["weak_enhancer", "status_curse_damage"]},
    {"name": "Sweet Surrender", "god": "Aphrodite", "type": "Utility", "description": "Foes afflicted with Weak take more damage from all sources.", "tags": ["weak_enhancer", "damage_enhancer"]},
    {"name": "Unhealthy Fixation", "god": "Aphrodite", "type": "Utility", "description": "Your Charm effects last longer and affect more foes.", "tags": ["charm_enhancer", "status_curse_duration"]},
    {"name": "Dying Lament", "god": "Aphrodite", "type": "Utility", "description": "When foes afflicted with Weak are defeated, they deal damage to nearby foes.", "tags": ["weak_synergy", "aoe_damage"]},
    {"name": "Weak", "god": "Aphrodite", "type": "Status Curse", "description": "Foes afflicted with Weak deal less damage.", "tags": ["status_curse", "weak"], "status_curse_name": "Weak"},
    {"name": "Charm", "god": "Aphrodite", "type": "Status Curse", "description": "Foes afflicted with Charm attack other foes.", "tags": ["status_curse", "charm"], "status_curse_name": "Charm"},
    {"name": "Life Affirmation", "god": "Aphrodite", "type": "Legendary", "description": "Any health you restore is worth more.", "tags": ["healing_enhancer", "survivability", "legendary"]},

    # Ares Boons
    {"name": "Curse of Agony", "god": "Ares", "type": "Attack", "description": "Your Attack inflicts Doom.", "tags": ["attack", "doom_applier"], "status_curse_applied": "Doom"},
    {"name": "Curse of Pain", "god": "Ares", "type": "Special", "description": "Your Special inflicts Doom.", "tags": ["special", "doom_applier"], "status_curse_applied": "Doom"},
    {"name": "Blade Dash", "god": "Ares", "type": "Dash", "description": "Your Dash creates a Blade Rift.", "tags": ["dash", "blade_rift", "damage"]},
    {"name": "Slicing Shot", "god": "Ares", "type": "Cast", "description": "Your Cast creates a Blade Rift.", "tags": ["cast", "blade_rift", "damage"]},
    {"name": "Ares' Aid", "god": "Ares", "type": "Call", "description": "Your Call creates a large Blade Rift.", "tags": ["call", "blade_rift", "damage"]},
    {"name": "Bloody Stand", "god": "Ares", "type": "Utility", "description": "You take less damage while standing in your Blade Rifts.", "tags": ["blade_rift_synergy", "damage_reduction"]},
    {"name": "Engulfing Vortex", "god": "Ares", "type": "Utility", "description": "Your Blade Rifts are larger and last longer.", "tags": ["blade_rift_enhancer", "aoe_enhancer"]},
    {"name": "Impending Doom", "god": "Ares", "type": "Utility", "description": "Your Doom effects deal more damage, but take longer to activate.", "tags": ["doom_enhancer", "status_curse_damage"]},
    {"name": "Dire Misfortune", "god": "Ares", "type": "Utility", "description": "Your Doom effects deal more damage each time they activate in quick succession.", "tags": ["doom_enhancer", "status_curse_damage"]},
    {"name": "Doom", "god": "Ares", "type": "Status Curse", "description": "Foes afflicted with Doom take a burst of damage after a short delay.", "tags": ["status_curse", "doom"], "status_curse_name": "Doom"},
    {"name": "Battle Rage", "god": "Ares", "type": "Legendary", "description": "After defeating a foe, deal more damage for a short time.", "tags": ["damage_enhancer", "kill_synergy", "legendary"]},

    # Artemis Boons
    {"name": "Deadly Strike", "god": "Artemis", "type": "Attack", "description": "Your Attack has a chance to deal Critical damage.", "tags": ["attack", "crit_chance"]},
    {"name": "Deadly Flourish", "god": "Artemis", "type": "Special", "description": "Your Special has a chance to deal Critical damage.", "tags": ["special", "crit_chance"]},
    {"name": "True Shot", "god": "Artemis", "type": "Cast", "description": "Your Cast fires a seeking arrow that deals Critical damage.", "tags": ["cast", "crit_damage", "seeking"]},
    {"name": "Hunter Dash", "god": "Artemis", "type": "Dash", "description": "Your Dash deals damage and has a chance to deal Critical damage.", "tags": ["dash", "crit_chance", "damage"]},
    {"name": "Artemis' Aid", "god": "Artemis", "type": "Call", "description": "Your Call fires a seeking arrow that deals massive Critical damage.", "tags": ["call", "crit_damage", "seeking"]},
    {"name": "Clean Kill", "god": "Artemis", "type": "Utility", "description": "Your Critical effects deal more damage.", "tags": ["crit_damage_enhancer"]},
    {"name": "Hunter's Mark", "god": "Artemis", "type": "Utility", "description": "After you deal Critical damage, a foe is Marked. Attacks against Marked foes have a higher Critical chance.", "tags": ["crit_synergy", "crit_chance"]},
    {"name": "Pressure Points", "god": "Artemis", "type": "Utility", "description": "Any damage you deal has a chance to be Critical.", "tags": ["crit_chance", "damage_enhancer"]},
    {"name": "Support Fire", "god": "Artemis", "type": "Utility", "description": "After you use your Attack, Special, or Cast, fire a seeking arrow.", "tags": ["damage_enhancer", "seeking"]},
    {"name": "Exit Wounds", "god": "Artemis", "type": "Utility", "description": "Your Casts deal damage when removed from foes.", "tags": ["cast_synergy", "damage"]},
    {"name": "Fully Loaded", "god": "Artemis", "type": "Legendary", "description": "Gain +2 Cast ammo.", "tags": ["cast_enhancer", "resource_gain", "legendary"]},

    # Dionysus Boons
    {"name": "Trippy Shot", "god": "Dionysus", "type": "Cast", "description": "Your Cast lobs a projectile that creates a Festive Fog, inflicting Hangover.", "tags": ["cast", "hangover_applier", "aoe"], "status_curse_applied": "Hangover"},
    {"name": "Drunken Strike", "god": "Dionysus", "type": "Attack", "description": "Your Attack inflicts Hangover.", "tags": ["attack", "hangover_applier"], "status_curse_applied": "Hangover"},
    {"name": "Drunken Flourish", "god": "Dionysus", "type": "Special", "description": "Your Special inflicts Hangover.", "tags": ["special", "hangover_applier"], "status_curse_applied": "Hangover"},
    {"name": "Drunken Dash", "god": "Dionysus", "type": "Dash", "description": "Your Dash creates a Festive Fog, inflicting Hangover.", "tags": ["dash", "hangover_applier", "aoe"], "status_curse_applied": "Hangover"},
    {"name": "Dionysus' Aid", "god": "Dionysus", "type": "Call", "description": "Your Call creates a Festive Fog that inflicts Hangover and makes you invulnerable.", "tags": ["call", "hangover_applier", "invulnerability", "aoe"], "status_curse_applied": "Hangover"},
    {"name": "Numbing Sensation", "god": "Dionysus", "type": "Utility", "description": "Your Hangover effects also slow foes.", "tags": ["hangover_enhancer", "slow_effect"]},
    {"name": "After Party", "god": "Dionysus", "type": "Utility", "description": "If your HP is low after an encounter, restore some HP.", "tags": ["healing", "survivability"]},
    {"name": "Nourished Soul", "god": "Dionysus", "type": "Utility", "description": "Any health you restore is worth more, and you gain +50 max HP.", "tags": ["healing_enhancer", "survivability", "max_hp"]},
    {"name": "Premium Vintage", "god": "Dionysus", "type": "Utility", "description": "Start each run with 1 Nectar. The first Nectar you find also restores HP.", "tags": ["resource_gain", "healing"]},
    {"name": "Strong Drink", "god": "Dionysus", "type": "Utility", "description": "After using a Fountain of Health, restore more HP and gain bonus damage for a short time.", "tags": ["healing_enhancer", "damage_enhancer"]},
    {"name": "Hangover", "god": "Dionysus", "type": "Status Curse", "description": "Foes afflicted with Hangover take damage over time.", "tags": ["status_curse", "hangover"], "status_curse_name": "Hangover"},
    {"name": "High Confidence", "god": "Dionysus", "type": "Legendary", "description": "You deal more damage while your HP is above 80%.", "tags": ["damage_enhancer", "hp_synergy", "legendary"]},

    # Hermes Boons
    {"name": "Quick Strike", "god": "Hermes", "type": "Attack", "description": "Your Attack is faster.", "tags": ["attack_speed", "attack_enhancer"]},
    {"name": "Swift Flourish", "god": "Hermes", "type": "Special", "description": "Your Special is faster.", "tags": ["special_speed", "special_enhancer"]},
    {"name": "Greater Reflex", "god": "Hermes", "type": "Dash", "description": "Gain +1 Dash.", "tags": ["dash_enhancer", "utility"]},
    {"name": "Hyper Sprint", "god": "Hermes", "type": "Dash", "description": "After Dashing, gain bonus move speed for a short time.", "tags": ["dash_synergy", "move_speed"]},
    {"name": "Flurry Cast", "god": "Hermes", "type": "Cast", "description": "Your Cast is faster.", "tags": ["cast_speed", "cast_enhancer"]},
    {"name": "Hermes' Aid", "god": "Hermes", "type": "Call", "description": "Your Call makes you move extremely fast and Deflect.", "tags": ["call", "move_speed", "deflect"]},
    {"name": "Rush Delivery", "god": "Hermes", "type": "Utility", "description": "You deal bonus damage based on your bonus move speed.", "tags": ["move_speed_synergy", "damage_enhancer"]},
    {"name": "Side Hustle", "god": "Hermes", "type": "Utility", "description": "Gain 10 Obols each time you enter a new chamber.", "tags": ["resource_gain"]},
    {"name": "Greatest Reflex", "god": "Hermes", "type": "Legendary", "description": "Gain +2 Dashes.", "tags": ["dash_enhancer", "utility", "legendary"]},
    {"name": "Bad News", "god": "Hermes", "type": "Legendary", "description": "Your Attack and Special deal more damage to foes not targeting you.", "tags": ["damage_enhancer", "utility", "legendary"]},
    {"name": "Second Wind", "god": "Hermes", "type": "Legendary", "description": "After using your Dash, restore some Call gauge.", "tags": ["dash_synergy", "call_synergy", "legendary"]},

    # Demeter Boons
    {"name": "Frost Strike", "god": "Demeter", "type": "Attack", "description": "Your Attack deals bonus damage and inflicts Chill.", "tags": ["attack", "damage", "chill_applier"], "status_curse_applied": "Chill"},
    {"name": "Frost Flourish", "god": "Demeter", "type": "Special", "description": "Your Special deals bonus damage and inflicts Chill.", "tags": ["special", "damage", "chill_applier"], "status_curse_applied": "Chill"},
    {"name": "Crystal Beam", "god": "Demeter", "type": "Cast", "description": "Your Cast creates a crystal that fires a beam, inflicting Chill.", "tags": ["cast", "chill_applier", "summon"], "status_curse_applied": "Chill"},
    {"name": "Demeter's Aid", "god": "Demeter", "type": "Call", "description": "Your Call creates a large crystal that fires a beam, inflicting Chill.", "tags": ["call", "chill_applier", "summon"], "status_curse_applied": "Chill"},
    {"name": "Killing Freeze", "god": "Demeter", "type": "Utility", "description": "Your Chill effects deal damage when foes are defeated.", "tags": ["chill_synergy", "aoe_damage"]},
    {"name": "Arctic Blast", "god": "Demeter", "type": "Utility", "description": "Your Chill effects deal damage when they expire.", "tags": ["chill_enhancer", "status_curse_damage"]},
    {"name": "Ravenous Will", "god": "Demeter", "type": "Utility", "description": "You deal more damage while you have no Cast ammo.", "tags": ["cast_synergy", "damage_enhancer"]},
    {"name": "Rare Crop", "god": "Demeter", "type": "Utility", "description": "Upgrade the rarity of a random boon.", "tags": ["utility", "rarity_upgrade"]},
    {"name": "Chill", "god": "Demeter", "type": "Status Curse", "description": "Foes afflicted with Chill are slowed. Stacks up to 10 times.", "tags": ["status_curse", "chill"], "status_curse_name": "Chill"},
    {"name": "Winter Harvest", "god": "Demeter", "type": "Legendary", "description": "Foes afflicted with Chill are more susceptible to damage and take damage when they are defeated.", "tags": ["chill_enhancer", "damage_enhancer", "aoe_damage", "legendary"]},

    # Chaos Boons (simplified, as they are unique)
    {"name": "Chaos' Shot", "god": "Chaos", "type": "Cast", "description": "Your Cast deals more damage.", "tags": ["cast", "damage_enhancer"]},
    {"name": "Chaos' Strike", "god": "Chaos", "type": "Attack", "description": "Your Attack deals more damage.", "tags": ["attack", "damage_enhancer"]},
    {"name": "Chaos' Flourish", "god": "Chaos", "type": "Special", "description": "Your Special deals more damage.", "tags": ["special", "damage_enhancer"]},
    {"name": "Chaos' Dash", "god": "Chaos", "type": "Dash", "description": "Your Dash deals more damage.", "tags": ["dash", "damage_enhancer"]},
    {"name": "Chaos' Soul", "god": "Chaos", "type": "Utility", "description": "Gain +1 Cast ammo.", "tags": ["cast_enhancer", "resource_gain"]},
    {"name": "Chaos' Favor", "god": "Chaos", "type": "Utility", "description": "You deal more damage to foes with full health.", "tags": ["damage_enhancer"]},
    {"name": "Chaos' Shield", "god": "Chaos", "type": "Utility", "description": "Gain +1 Death Defiance.", "tags": ["survivability", "death_defiance"]},
    {"name": "Chaos' Life", "god": "Chaos", "type": "Utility", "description": "Gain +25 max HP.", "tags": ["max_hp"]},
]

# Duo Boons
DUO_BOONS_DATA: List[Dict[str, Any]] = [
    {
        "name": "Smoldering Air",
        "gods": ["Zeus", "Aphrodite"],
        "description": "Your Call charges automatically and is always at max strength, but its gauge is reduced.",
        "prerequisites": [("Zeus", "Lightning Strike"), ("Aphrodite", "Heartbreak Strike")]
    },
    {
        "name": "Exclusive Access",
        "gods": ["Poseidon", "Dionysus"],
        "description": "Boons from other Gods are always Rare or better.",
        "prerequisites": [("Poseidon", "Tidal Dash"), ("Dionysus", "Trippy Shot")]
    },
    {
        "name": "Curse of Vengeance",
        "gods": ["Ares", "Aphrodite"],
        "description": "When you take damage, a foe near you is afflicted with Doom.",
        "prerequisites": [("Ares", "Curse of Agony"), ("Aphrodite", "Heartbreak Strike")]
    },
    {
        "name": "Vengeful Mood",
        "gods": ["Ares", "Athena"],
        "description": "Your Call gauge fills automatically.",
        "prerequisites": [("Ares", "Curse of Agony"), ("Athena", "Divine Dash")]
    },
    {
        "name": "Splitting Headache",
        "gods": ["Artemis", "Dionysus"],
        "description": "Your Hangover effects have a chance to deal Critical damage.",
        "prerequisites": [("Artemis", "Deadly Strike"), ("Dionysus", "Trippy Shot")]
    },
    {
        "name": "Cold Fusion",
        "gods": ["Zeus", "Demeter"],
        "description": "Your Jolted effects also inflict Chill.",
        "prerequisites": [("Zeus", "Lightning Strike"), ("Demeter", "Frost Strike")]
    },
    {
        "name": "Ice Wine",
        "gods": ["Dionysus", "Demeter"],
        "description": "Your Cast creates a Festive Fog that also inflicts Chill.",
        "prerequisites": [("Dionysus", "Trippy Shot"), ("Demeter", "Crystal Beam")]
    },
    {
        "name": "Mirage Shot",
        "gods": ["Artemis", "Poseidon"],
        "description": "Your Cast fires an additional projectile, but deals less damage.",
        "prerequisites": [("Artemis", "True Shot"), ("Poseidon", "Flood Shot")]
    },
    {
        "name": "Heart Rend",
        "gods": ["Artemis", "Aphrodite"],
        "description": "Your Critical effects deal even more damage to Weak foes.",
        "prerequisites": [("Artemis", "Deadly Strike"), ("Aphrodite", "Heartbreak Strike")]
    },
    {
        "name": "Curse of Longing",
        "gods": ["Ares", "Aphrodite"],
        "description": "Your Doom effects deal more damage to Weak foes.",
        "prerequisites": [("Ares", "Curse of Agony"), ("Aphrodite", "Heartbreak Strike")]
    },
    {
        "name": "Lightning Rod",
        "gods": ["Zeus", "Artemis"],
        "description": "Your Casts stick in foes and periodically strike them with lightning.",
        "prerequisites": [("Zeus", "Storm Lightning"), ("Artemis", "True Shot")]
    },
    {
        "name": "Freezing Vortex",
        "gods": ["Ares", "Demeter"],
        "description": "Your Blade Rifts also inflict Chill.",
        "prerequisites": [("Ares", "Blade Dash"), ("Demeter", "Frost Strike")]
    },
    {
        "name": "Scintillating Feast",
        "gods": ["Zeus", "Dionysus"],
        "description": "Your Festive Fog also strikes foes with lightning.",
        "prerequisites": [("Zeus", "Lightning Strike"), ("Dionysus", "Trippy Shot")]
    },
    {
        "name": "Deadly Reversal",
        "gods": ["Artemis", "Athena"],
        "description": "After you Deflect, your next Attack or Special is Critical.",
        "prerequisites": [("Artemis", "Deadly Strike"), ("Athena", "Divine Dash")]
    },
    {
        "name": "Calculated Risk",
        "gods": ["Athena", "Dionysus"],
        "description": "Your Festive Fog also makes you Deflect.",
        "prerequisites": [("Athena", "Divine Dash"), ("Dionysus", "Trippy Shot")]
    },
]

# Legendary Boons
LEGENDARY_BOONS_DATA: List[Dict[str, Any]] = [
    {
        "name": "Zeus's Aid (Greater)",
        "god": "Zeus",
        "description": "Your Call deals massive lightning damage and makes you invulnerable.",
        "prerequisites": [("Zeus", "Billowing Strength")]
    },
    {
        "name": "Fully Loaded",
        "god": "Artemis",
        "description": "Gain +2 Cast ammo.",
        "prerequisites": [("Artemis", "True Shot")]
    },
    {
        "name": "Greatest Reflex",
        "god": "Hermes",
        "description": "Gain +2 Dashes.",
        "prerequisites": [("Hermes", "Greater Reflex")]
    },
    {
        "name": "Winter Harvest",
        "god": "Demeter",
        "description": "Foes afflicted with Chill are more susceptible to damage and take damage when they are defeated.",
        "prerequisites": [("Demeter", "Frost Strike")]
    },
    {
        "name": "Bad News",
        "god": "Hermes",
        "description": "Your Attack and Special deal more damage to foes not targeting you.",
        "prerequisites": [("Hermes", "Quick Strike")]
    },
    {
        "name": "Second Wind",
        "god": "Hermes",
        "description": "After using your Dash, restore some Call gauge.",
        "prerequisites": [("Hermes", "Hyper Sprint")]
    },
    {
        "name": "Proud Bearing",
        "god": "Athena",
        "description": "Start each encounter with some Call gauge.",
        "prerequisites": [("Athena", "Athena's Aid")]
    },
    {
        "name": "Battle Rage",
        "god": "Ares",
        "description": "After defeating a foe, deal more damage for a short time.",
        "prerequisites": [("Ares", "Curse of Agony")]
    },
    {
        "name": "High Confidence",
        "god": "Dionysus",
        "description": "You deal more damage while your HP is above 80%.",
        "prerequisites": [("Dionysus", "Drunken Strike")]
    },
    {
        "name": "Life Affirmation",
        "god": "Aphrodite",
        "description": "Any health you restore is worth more.",
        "prerequisites": [("Aphrodite", "Heartbreak Strike")]
    },
    {
        "name": "Ocean's Bounty",
        "god": "Poseidon",
        "description": "You find more Darkness, Gemstones, and Keys.",
        "prerequisites": [("Poseidon", "Tidal Dash")]
    },
]

# Helper for quick boon data lookup by name
BOON_NAME_TO_DATA: Dict[str, Dict[str, Any]] = {boon['name']: boon for boon in BOONS_DATA}

# Define possible room items
ROOM_ITEMS: List[str] = ["Pom of Power", "Gold (50)", "Centaur Heart", "Nectar"]

# Constants for run simulation
MAX_ROOMS = 15
INITIAL_GOD_CHOICES = 3 # How many gods to initially select from
NUM_ROOM_OFFERINGS = 3 # How many options (boons, new gods, items) to offer in a standard room


class HadesBuildHelperApp:
    """
    A Tkinter GUI application for the Hades Build Helper.
    Simulates a simplified run, allowing users to make choices in rooms
    and get dynamic recommendations.
    """

    def __init__(self, master: tk.Tk) -> None:
        """
        Initializes the HadesBuildHelperApp.

        Args:
            master: The root Tkinter window.
        """
        self.master = master
        master.title("Hades Build Helper (Run Simulator)")
        master.geometry("1200x800") # Wider for 3 panels
        master.resizable(True, True)

        # Configure style for ttk widgets
        self.style = ttk.Style()
        self.style.theme_use('clam') # 'clam', 'alt', 'default', 'classic'
        self.style.configure('TFrame', background='#333333')
        self.style.configure('TLabel', background='#333333', foreground='#EEEEEE', font=('Helvetica', 10))
        self.style.configure('TButton', font=('Helvetica', 10, 'bold'))
        self.style.configure('TCheckbutton', background='#333333', foreground='#EEEEEE', font=('Helvetica', 9))
        self.style.map('TCheckbutton',
                       background=[('active', '#555555')],
                       foreground=[('active', '#FFFFFF')])
        self.style.configure('TRadiobutton', background='#333333', foreground='#EEEEEE', font=('Helvetica', 9))
        self.style.map('TRadiobutton',
                       background=[('active', '#555555')],
                       foreground=[('active', '#FFFFFF')])
        self.style.configure('TLabelframe', background='#333333', foreground='#FFD700', font=('Helvetica', 11, 'bold'))
        self.style.configure('TLabelframe.Label', background='#333333', foreground='#FFD700', font=('Helvetica', 11, 'bold'))

        # Main frame for padding
        self.main_frame = ttk.Frame(master, padding="10 10 10 10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # State variables for the run
        self.current_room_num: int = 0
        self.active_gods_in_run: Set[str] = set() # Gods whose boons can appear
        self.acquired_boons_in_run: List[str] = [] # List of boon names acquired
        self.all_available_gods: List[str] = sorted([g for g in GODS_DATA.keys() if g != "Chaos"]) # All gods except Chaos for initial selection

        # Widgets for room choices
        self.room_choice_var = tk.StringVar(value="")
        self.room_choice_widgets: List[Any] = [] # To store radio buttons/buttons for choices

        self._create_widgets()
        self._start_new_run() # Start a new run immediately on app launch

    def _create_widgets(self) -> None:
        """
        Creates and lays out all the GUI widgets for the run simulation.
        """
        # Configure grid for 3 main columns
        self.main_frame.grid_columnconfigure(0, weight=1) # Run Info
        self.main_frame.grid_columnconfigure(1, weight=2) # Room Offerings (wider)
        self.main_frame.grid_columnconfigure(2, weight=2) # Recommendations (wider)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # --- Left Panel: Run Information ---
        self.run_info_frame = ttk.LabelFrame(self.main_frame, text="Current Run Info", padding="10 10 10 10")
        self.run_info_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.room_label = ttk.Label(self.run_info_frame, text="Room: 0 / 0")
        self.room_label.pack(anchor=tk.W, pady=(0, 10))

        ttk.Label(self.run_info_frame, text="Active Gods:").pack(anchor=tk.W)
        self.active_gods_text = scrolledtext.ScrolledText(
            self.run_info_frame, wrap=tk.WORD, height=5, width=25,
            bg='#222222', fg='#EEEEEE', font=('Consolas', 9),
            insertbackground='#EEEEEE', relief=tk.FLAT, padx=3, pady=3
        )
        self.active_gods_text.pack(fill=tk.X, pady=(0, 10))
        self.active_gods_text.config(state=tk.DISABLED)

        ttk.Label(self.run_info_frame, text="Acquired Boons:").pack(anchor=tk.W)
        self.acquired_boons_text = scrolledtext.ScrolledText(
            self.run_info_frame, wrap=tk.WORD, height=20, width=25,
            bg='#222222', fg='#EEEEEE', font=('Consolas', 9),
            insertbackground='#EEEEEE', relief=tk.FLAT, padx=3, pady=3
        )
        self.acquired_boons_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.acquired_boons_text.config(state=tk.DISABLED)

        # --- Middle Panel: Room Offerings / Initial God Selection ---
        self.room_offerings_frame = ttk.LabelFrame(self.main_frame, text="Room Offerings", padding="10 10 10 10")
        self.room_offerings_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.room_title_label = ttk.Label(self.room_offerings_frame, text="Select Initial Gods to Start Your Run", font=('Helvetica', 11, 'bold'))
        self.room_title_label.pack(anchor=tk.W, pady=(0, 10))

        self.room_choices_frame = ttk.Frame(self.room_offerings_frame, style='TFrame')
        self.room_choices_frame.pack(fill=tk.BOTH, expand=True)

        self.confirm_choice_button = ttk.Button(self.room_offerings_frame, text="Confirm Choice", command=self._confirm_room_choice, state=tk.DISABLED)
        self.confirm_choice_button.pack(pady=(10, 0))

        # --- Right Panel: Recommendations ---
        self.recommendation_frame = ttk.LabelFrame(self.main_frame, text="Recommendations", padding="10 10 10 10")
        self.recommendation_frame.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        self.recommendation_text = scrolledtext.ScrolledText(
            self.recommendation_frame, wrap=tk.WORD, width=60, height=25,
            bg='#222222', fg='#EEEEEE', font=('Consolas', 10),
            insertbackground='#EEEEEE', relief=tk.FLAT, padx=5, pady=5
        )
        self.recommendation_text.pack(fill=tk.BOTH, expand=True)
        self.recommendation_text.tag_configure('Header', foreground='#FFD700', font=('Consolas', 11, 'bold'))
        self.recommendation_text.config(state=tk.DISABLED) # Make it read-only

        # --- Bottom Control Buttons ---
        self.control_frame = ttk.Frame(self.main_frame, style='TFrame')
        self.control_frame.grid(row=1, column=0, columnspan=3, pady=10)

        self.start_new_run_button = ttk.Button(self.control_frame, text="Start New Run", command=self._start_new_run)
        self.start_new_run_button.pack(side=tk.LEFT, padx=5)

    def _clear_room_choices(self) -> None:
        """Clears all widgets from the room_choices_frame."""
        for widget in self.room_choices_frame.winfo_children():
            widget.destroy()
        self.room_choice_widgets = []
        self.room_choice_var.set("") # Reset the radio button variable

    def _update_run_display(self) -> None:
        """Updates the run info panel with current state."""
        self.room_label.config(text=f"Room: {self.current_room_num} / {MAX_ROOMS}")

        self.active_gods_text.config(state=tk.NORMAL)
        self.active_gods_text.delete(1.0, tk.END)
        if self.active_gods_in_run:
            self.active_gods_text.insert(tk.END, ", ".join(sorted(list(self.active_gods_in_run))))
        else:
            self.active_gods_text.insert(tk.END, "None")
        self.active_gods_text.config(state=tk.DISABLED)

        self.acquired_boons_text.config(state=tk.NORMAL)
        self.acquired_boons_text.delete(1.0, tk.END)
        if self.acquired_boons_in_run:
            for boon_name in sorted(self.acquired_boons_in_run):
                boon_data = BOON_NAME_TO_DATA.get(boon_name)
                if boon_data:
                    self.acquired_boons_text.insert(tk.END, f"- {boon_name} ({boon_data['god']})\n")
                else:
                    self.acquired_boons_text.insert(tk.END, f"- {boon_name} (Unknown God)\n")
        else:
            self.acquired_boons_text.insert(tk.END, "No boons acquired yet.")
        self.acquired_boons_text.config(state=tk.DISABLED)

    def _start_new_run(self) -> None:
        """Resets the run state and starts the initial god selection phase."""
        self.current_room_num = 0
        self.active_gods_in_run = set()
        self.acquired_boons_in_run = []
        self.room_choice_var.set("")
        self.confirm_choice_button.config(state=tk.DISABLED)
        self.room_offerings_frame.config(text="Initial Setup")
        self.room_title_label.config(text="Select 1-3 Initial Gods (like a Keepsake)")

        self._clear_room_choices()
        self._update_run_display()
        self._update_recommendations() # Clear recommendations

        self._show_initial_god_selection()

    def _show_initial_god_selection(self) -> None:
        """Presents checkboxes for the user to select initial gods."""
        self._clear_room_choices()

        selectable_gods = self.all_available_gods # Excludes Chaos

        self.initial_god_vars: Dict[str, tk.IntVar] = {}
        for god_name in selectable_gods:
            var = tk.IntVar(value=0)
            cb = ttk.Checkbutton(self.room_choices_frame, text=god_name, variable=var,
                                 command=self._check_initial_god_selection_limit)
            cb.pack(anchor=tk.W, pady=2)
            self.initial_god_vars[god_name] = var
            self.room_choice_widgets.append(cb)

        self.confirm_choice_button.config(text="Confirm Initial Gods", command=self._confirm_initial_gods, state=tk.DISABLED)

    def _check_initial_god_selection_limit(self) -> None:
        """Ensures that no more than INITIAL_GOD_CHOICES are selected."""
        selected_count = sum(var.get() for var in self.initial_god_vars.values())
        if selected_count > INITIAL_GOD_CHOICES:
            messagebox.showwarning("Too Many Gods", f"Please select a maximum of {INITIAL_GOD_CHOICES} Gods.")
            # A more robust solution would track the last clicked and uncheck it.
            # For now, we just disable the confirm button until they correct it.
            self.confirm_choice_button.config(state=tk.DISABLED)
        elif selected_count > 0:
            self.confirm_choice_button.config(state=tk.NORMAL)
        else:
            self.confirm_choice_button.config(state=tk.DISABLED)

    def _confirm_initial_gods(self) -> None:
        """Processes the initial god selection and starts the first room."""
        selected_initial_gods = [god for god, var in self.initial_god_vars.items() if var.get() == 1]

        if not selected_initial_gods:
            messagebox.showwarning("No Gods Selected", "Please select at least one God to start your run.")
            return

        self.active_gods_in_run.update(selected_initial_gods)
        self.current_room_num = 1
        self.confirm_choice_button.config(text="Confirm Choice", command=self._confirm_room_choice, state=tk.DISABLED)
        self._update_run_display()
        self._generate_room_offerings()

    def _generate_room_offerings(self) -> None:
        """Generates and displays choices for the current room, mixing boons, new gods, and items."""
        if self.current_room_num > MAX_ROOMS:
            self._end_run()
            return

        self._clear_room_choices()
        self.room_offerings_frame.config(text=f"Room {self.current_room_num} Offerings")
        self.room_title_label.config(text=f"Choose your reward for Room {self.current_room_num}:")
        self.confirm_choice_button.config(state=tk.DISABLED)

        available_options: List[Tuple[str, str]] = [] # Stores (type, name) tuples

        # Add boons from active gods to the pool
        for god_name in self.active_gods_in_run:
            available_boons_from_god = [
                b for b in BOONS_DATA
                if b['god'] == god_name and
                   b['name'] not in self.acquired_boons_in_run and
                   b['type'] not in ["Status Curse", "Legendary"] # Don't offer these directly as choices
            ]
            
            # Prioritize missing core boons for this god
            core_boon_types_acquired = {
                b['type'] for b in BOONS_DATA
                if b['god'] == god_name and b['name'] in self.acquired_boons_in_run and b['type'] in GODS_DATA[god_name]['core_boon_types']
            }
            missing_core_boon_types = [
                t for t in GODS_DATA[god_name]['core_boon_types']
                if t not in core_boon_types_acquired
            ]
            
            temp_boon_pool_for_god: List[Dict[str, Any]] = []
            # Add one of each missing core boon type if available
            for core_type in missing_core_boon_types:
                potential_boons = [b for b in available_boons_from_god if b['type'] == core_type and b not in temp_boon_pool_for_god]
                if potential_boons:
                    temp_boon_pool_for_god.append(random.choice(potential_boons))
            
            # Add remaining boons to fill up potential offerings for this god (up to a reasonable limit)
            remaining_boons = [b for b in available_boons_from_god if b not in temp_boon_pool_for_god]
            temp_boon_pool_for_god.extend(random.sample(remaining_boons, min(len(remaining_boons), 3 - len(temp_boon_pool_for_god))))

            for boon_data in temp_boon_pool_for_god:
                available_options.append(("boon", boon_data['name']))

        # Add new gods to the pool
        potential_new_gods = [g for g in self.all_available_gods if g not in self.active_gods_in_run]
        for god_name in potential_new_gods:
            available_options.append(("new_god", god_name))

        # Add items to the pool
        for item_name in ROOM_ITEMS:
            available_options.append(("item", item_name))

        # Ensure unique options in the pool (in case a boon name is identical to an item name, etc.)
        unique_options_set = set(available_options)
        available_options = list(unique_options_set)

        # If no options are available (e.g., all boons acquired, all gods active), end run or show message
        if not available_options:
            self.room_title_label.config(text="No more choices available for this run!")
            self.confirm_choice_button.config(state=tk.DISABLED)
            messagebox.showinfo("Run Stalled", "No more unique boons, gods, or items could be offered. Ending run.")
            self._end_run()
            return

        # Randomly select NUM_ROOM_OFFERINGS options from the available pool
        num_to_offer = min(NUM_ROOM_OFFERINGS, len(available_options))
        offered_choices = random.sample(available_options, num_to_offer)

        for choice_type, choice_name in offered_choices:
            display_text = ""
            value = ""
            if choice_type == "boon":
                boon_data = BOON_NAME_TO_DATA.get(choice_name)
                if boon_data:
                    display_text = f"Boon from {boon_data['god']}: {boon_data['name']} - {boon_data['description']}"
                    value = choice_name
            elif choice_type == "new_god":
                god_data = GODS_DATA.get(choice_name)
                if god_data:
                    display_text = f"Encounter {choice_name}: {god_data['description']}"
                    value = f"GOD_CHOICE:{choice_name}"
            elif choice_type == "item":
                display_text = f"Acquire {choice_name}"
                value = f"ITEM_CHOICE:{choice_name}"
            
            if display_text and value:
                rb = ttk.Radiobutton(self.room_choices_frame, text=display_text, variable=self.room_choice_var,
                                     value=value, command=lambda: self.confirm_choice_button.config(state=tk.NORMAL))
                rb.pack(anchor=tk.W, pady=2)
                self.room_choice_widgets.append(rb)

        self._update_recommendations()

    def _confirm_room_choice(self) -> None:
        """Processes the user's choice for the current room."""
        chosen_value = self.room_choice_var.get()
        if not chosen_value:
            messagebox.showwarning("No Choice Made", "Please select an option before confirming.")
            return

        if chosen_value.startswith("GOD_CHOICE:"):
            god_name = chosen_value.split(":")[1]
            self.active_gods_in_run.add(god_name)
            messagebox.showinfo("Choice Made", f"You chose to encounter {god_name}. {god_name} is now active.")
        elif chosen_value.startswith("ITEM_CHOICE:"):
            item_name = chosen_value.split(":")[1]
            # In a real game, this would update resources. Here, just acknowledge.
            messagebox.showinfo("Choice Made", f"You acquired {item_name}.")
        else: # It's a boon
            boon_name = chosen_value
            self.acquired_boons_in_run.append(boon_name)
            messagebox.showinfo("Choice Made", f"You acquired {boon_name}.")

        self.current_room_num += 1
        self._update_run_display()
        self._update_recommendations()

        if self.current_room_num <= MAX_ROOMS:
            self._generate_room_offerings()
        else:
            self._end_run()

    def _end_run(self) -> None:
        """Displays a summary when the run ends."""
        self._clear_room_choices()
        self.room_offerings_frame.config(text="Run Complete!")
        self.room_title_label.config(text="Congratulations! Your run has ended.")
        self.confirm_choice_button.config(state=tk.DISABLED)

        self.recommendation_text.config(state=tk.NORMAL)
        self.recommendation_text.insert(tk.END, "\n--- FINAL BUILD SUMMARY ---\n", 'Header')
        if self.acquired_boons_in_run:
            for boon_name in sorted(self.acquired_boons_in_run):
                boon_data = BOON_NAME_TO_DATA.get(boon_name)
                if boon_data:
                    self.recommendation_text.insert(tk.END, f"- {boon_name} ({boon_data['god']}): {boon_data['description']}\n")
        else:
            self.recommendation_text.insert(tk.END, "No boons acquired in this run.\n")
        self.recommendation_text.config(state=tk.DISABLED)
        messagebox.showinfo("Run Complete", "Your simulated run has ended. Check the recommendations panel for a summary.")


    def _update_recommendations(self) -> None:
        """
        Generates and displays boon recommendations based on the current run state.
        """
        self.recommendation_text.config(state=tk.NORMAL)
        self.recommendation_text.delete(1.0, tk.END)

        if not self.active_gods_in_run:
            self.recommendation_text.insert(tk.END, "Select initial Gods to see recommendations.")
            self.recommendation_text.config(state=tk.DISABLED)
            return

        recommendations = self._generate_boon_recommendations_logic(
            list(self.active_gods_in_run), self.acquired_boons_in_run
        )

        self.recommendation_frame.config(text="Current Build Analysis")

        has_recommendations = False
        for category, boons in recommendations.items():
            if boons:
                has_recommendations = True
                self.recommendation_text.insert(tk.END, f"\n{category}:\n", 'Header')
                for boon_rec in boons:
                    self.recommendation_text.insert(tk.END, f"- {boon_rec}\n")
        
        if not has_recommendations:
            self.recommendation_text.insert(tk.END, "No specific recommendations at this time based on your current build.")
        
        self.recommendation_text.config(state=tk.DISABLED)

    def _generate_boon_recommendations_logic(self, active_gods: List[str], acquired_boons: List[str]) -> Dict[str, List[str]]:
        """
        Generates boon recommendations based on active gods and acquired boons.
        This is the core logic from the original `recommend_boons` function, adapted.

        Args:
            active_gods: A list of god names currently active in the run.
            acquired_boons: A list of boon names the user has already acquired.

        Returns:
            A dictionary containing categorized lists of recommended boons.
        """
        recommendations: Dict[str, List[str]] = {
            "Potential Duo Boons": [],
            "Potential Legendary Boons": [],
            "Synergistic Boons (Enhancers)": [],
            "Synergistic Boons (Core Coverage)": [],
            "Other Boons from Active Gods": []
        }

        acquired_boon_names_set = set(acquired_boons)
        active_gods_set = set(active_gods)
        already_recommended_boons: Set[str] = set() # To prevent duplicate recommendations

        # 1. Duo Boon Recommendations
        for duo_boon in DUO_BOONS_DATA:
            god1, god2 = duo_boon['gods']
            if god1 in active_gods_set and god2 in active_gods_set:
                if duo_boon['name'] in acquired_boon_names_set:
                    continue # Already acquired

                all_prereqs_met = True
                missing_prereqs = []
                for prereq_god, prereq_boon_name in duo_boon['prerequisites']:
                    if prereq_boon_name not in acquired_boon_names_set:
                        all_prereqs_met = False
                        missing_prereqs.append(f"{prereq_boon_name} ({prereq_god})")

                if all_prereqs_met:
                    recommendations["Potential Duo Boons"].append(
                        f"{duo_boon['name']} ({god1}/{god2}): {duo_boon['description']} (All prerequisites met!)"
                    )
                    already_recommended_boons.add(duo_boon['name'])
                elif missing_prereqs:
                    recommendations["Potential Duo Boons"].append(
                        f"{duo_boon['name']} ({god1}/{god2}): {duo_boon['description']} (Missing: {', '.join(missing_prereqs)})"
                    )
                    already_recommended_boons.add(duo_boon['name'])

        # 2. Legendary Boon Recommendations
        for legendary_boon in LEGENDARY_BOONS_DATA:
            god = legendary_boon['god']
            if god in active_gods_set:
                if legendary_boon['name'] in acquired_boon_names_set:
                    continue # Already acquired

                all_prereqs_met = True
                missing_prereqs = []
                for prereq_god, prereq_boon_name in legendary_boon['prerequisites']:
                    if prereq_boon_name not in acquired_boon_names_set:
                        all_prereqs_met = False
                        missing_prereqs.append(f"{prereq_boon_name} ({prereq_god})")

                if all_prereqs_met:
                    recommendations["Potential Legendary Boons"].append(
                        f"{legendary_boon['name']} ({god}): {legendary_boon['description']} (All prerequisites met!)"
                    )
                    already_recommended_boons.add(legendary_boon['name'])
                elif missing_prereqs:
                    recommendations["Potential Legendary Boons"].append(
                        f"{legendary_boon['name']} ({god}): {legendary_boon['description']} (Missing: {', '.join(missing_prereqs)})"
                    )
                    already_recommended_boons.add(legendary_boon['name'])

        # 3. Synergistic Boons (Enhancers)
        # Identify status curses applied by acquired boons
        applied_status_curses: Set[str] = set()
        for boon_name in acquired_boon_names_set:
            boon_data = BOON_NAME_TO_DATA.get(boon_name)
            if boon_data and 'status_curse_applied' in boon_data and boon_data['status_curse_applied']:
                applied_status_curses.add(boon_data['status_curse_applied'])

        for curse in applied_status_curses:
            for boon in BOONS_DATA:
                if boon['god'] in active_gods_set and \
                   boon['name'] not in acquired_boon_names_set and \
                   boon['name'] not in already_recommended_boons:
                    if f"{curse.lower()}_enhancer" in boon['tags'] or f"{curse.lower()}_synergy" in boon['tags']:
                        recommendations["Synergistic Boons (Enhancers)"].append(
                            f"{boon['name']} ({boon['god']}): {boon['description']} (Enhances your {curse} effects)"
                        )
                        already_recommended_boons.add(boon['name'])

        # 4. Core Boon Coverage (Attack, Special, Dash, Cast, Call)
        for god in active_gods_set:
            acquired_types_for_god: Set[str] = set()
            for boon_name in acquired_boon_names_set:
                boon_data = BOON_NAME_TO_DATA.get(boon_name)
                if boon_data and boon_data['god'] == god and boon_data['type'] in GODS_DATA[god]['core_boon_types']:
                    acquired_types_for_god.add(boon_data['type'])
            
            for core_type in GODS_DATA[god]['core_boon_types']:
                if core_type not in acquired_types_for_god:
                    # Suggest one unacquired boon of that type from this god
                    for boon in BOONS_DATA:
                        if boon['god'] == god and boon['type'] == core_type and \
                           boon['name'] not in acquired_boon_names_set and \
                           boon['name'] not in already_recommended_boons:
                            recommendations["Synergistic Boons (Core Coverage)"].append(
                                f"{boon['name']} ({boon['god']}): {boon['description']} (Fills a core {core_type} slot for {god})"
                            )
                            already_recommended_boons.add(boon['name'])
                            break # Only suggest one per type for brevity

        # 5. General Utility/Damage (other unacquired boons from active gods)
        # Prioritize boons with general utility/damage tags if not already covered
        for boon in BOONS_DATA:
            if boon['god'] in active_gods_set and \
               boon['name'] not in acquired_boon_names_set and \
               boon['name'] not in already_recommended_boons and \
               boon['type'] not in ["Status Curse", "Legendary"]: # Don't recommend status curse boons directly or legendaries again
                # Only recommend boons that are not already covered by other categories
                recommendations["Other Boons from Active Gods"].append(
                    f"{boon['name']} ({boon['god']}): {boon['description']} (General boon from {boon['god']})"
                )
                already_recommended_boons.add(boon['name'])

        return recommendations


def main() -> None:
    """
    Main function to run the Hades build helper GUI application.
    """
    root = tk.Tk()
    app = HadesBuildHelperApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()