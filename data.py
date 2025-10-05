"""
Hades Build Helper - Game Data Module
Contains all game constants, boon data, weapon information, and tier rankings.
"""

from typing import Dict, List, Any

# === GODS DATA ===
GODS_DATA: Dict[str, Dict[str, Any]] = {
    "Zeus": {
        "description": "God of Lightning. Grants boons focused on lightning damage, chain effects, and jolting foes.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"],
        "color": "#FFD700",
        "symbol": "⚡"
    },
    "Poseidon": {
        "description": "God of the Sea. Grants boons focused on knockback, rupture, and resource acquisition.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"],
        "color": "#00CED1",
        "symbol": "🌊"
    },
    "Athena": {
        "description": "Goddess of Wisdom. Grants boons focused on Deflect, invulnerability, and damage reduction.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"],
        "color": "#DAA520",
        "symbol": "🛡️"
    },
    "Aphrodite": {
        "description": "Goddess of Love. Grants boons focused on weakening foes and charm effects.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"],
        "color": "#FF69B4",
        "symbol": "💗"
    },
    "Ares": {
        "description": "God of War. Grants boons focused on Blade Rifts, Doom status, and high damage.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"],
        "color": "#DC143C",
        "symbol": "⚔️"
    },
    "Artemis": {
        "description": "Goddess of the Hunt. Grants boons focused on Critical hits and tracking shots.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"],
        "color": "#32CD32",
        "symbol": "🏹"
    },
    "Dionysus": {
        "description": "God of Wine. Grants boons focused on Hangover status, healing, and festive fog.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"],
        "color": "#9370DB",
        "symbol": "🍷"
    },
    "Hermes": {
        "description": "God of Speed. Grants boons focused on movement speed, dodge chance, and attack speed.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"],
        "color": "#F0E68C",
        "symbol": "🏃"
    },
    "Demeter": {
        "description": "Goddess of Seasons. Grants boons focused on Chill status, slowing foes, and crystal effects.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"],
        "color": "#87CEEB",
        "symbol": "❄️"
    },
    "Chaos": {
        "description": "Primordial entity. Grants boons that offer powerful buffs with temporary curses.",
        "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"],
        "color": "#8B008B",
        "symbol": "🌀"
    }
}

# === WEAPONS DATA ===
WEAPONS_DATA: Dict[str, Dict[str, Any]] = {
    "Stygian Blade": {
        "description": "Fast, balanced melee weapon. Good all-around choice.",
        "attack_speed": "Fast",
        "damage_type": "Balanced",
        "preferred_gods": ["Ares", "Aphrodite", "Zeus"],
        "focus": "Attack",
        "symbol": "🗡️",
        "aspects": {
            "Zagreus": {"desc": "Versatile - works with any boon", "preferred": ["Any"]},
            "Nemesis": {"desc": "Crit-focused - pairs with Artemis", "preferred": ["Artemis", "Aphrodite"]},
            "Poseidon": {"desc": "Dash-strike focused", "preferred": ["Poseidon", "Zeus"]},
            "Arthur": {"desc": "Slow heavy hits", "preferred": ["Aphrodite", "Ares"]}
        }
    },
    "Heart-Seeking Bow": {
        "description": "Ranged weapon with charge shots. Rewards precise timing.",
        "attack_speed": "Medium",
        "damage_type": "High Single Hit",
        "preferred_gods": ["Artemis", "Aphrodite", "Ares"],
        "focus": "Special",
        "symbol": "🏹",
        "aspects": {
            "Zagreus": {"desc": "Attack-focused", "preferred": ["Artemis", "Aphrodite"]},
            "Chiron": {"desc": "Special-focused", "preferred": ["Zeus", "Dionysus"]},
            "Hera": {"desc": "Cast-focused", "preferred": ["Demeter", "Artemis"]},
            "Rama": {"desc": "Special spam", "preferred": ["Zeus", "Dionysus"]}
        }
    },
    "Shield of Chaos": {
        "description": "Defensive weapon with blocking and ranged special.",
        "attack_speed": "Medium",
        "damage_type": "Balanced",
        "preferred_gods": ["Zeus", "Dionysus", "Ares"],
        "focus": "Special",
        "symbol": "🛡️",
        "aspects": {
            "Zagreus": {"desc": "Balanced", "preferred": ["Zeus"]},
            "Chaos": {"desc": "Special spam", "preferred": ["Zeus", "Dionysus"]},
            "Zeus": {"desc": "Shield throw", "preferred": ["Zeus", "Artemis"]},
            "Beowulf": {"desc": "Cast-focused", "preferred": ["Ares", "Aphrodite"]}
        }
    },
    "Eternal Spear": {
        "description": "Mid-range weapon with spin attack and throw.",
        "attack_speed": "Fast",
        "damage_type": "Multi-Hit",
        "preferred_gods": ["Zeus", "Dionysus", "Artemis"],
        "focus": "Special",
        "symbol": "🔱",
        "aspects": {
            "Zagreus": {"desc": "Spin attack", "preferred": ["Zeus", "Dionysus"]},
            "Achilles": {"desc": "Dash-strike", "preferred": ["Artemis", "Aphrodite"]},
            "Hades": {"desc": "Spin + special", "preferred": ["Zeus", "Dionysus"]},
            "Guan Yu": {"desc": "Slow heavy", "preferred": ["Aphrodite", "Artemis"]}
        }
    },
    "Twin Fists": {
        "description": "Extremely fast melee weapon with rapid strikes.",
        "attack_speed": "Very Fast",
        "damage_type": "Multi-Hit",
        "preferred_gods": ["Zeus", "Dionysus", "Demeter"],
        "focus": "Attack",
        "symbol": "👊",
        "aspects": {
            "Zagreus": {"desc": "Fast hits", "preferred": ["Zeus", "Dionysus"]},
            "Talos": {"desc": "Magnetic special", "preferred": ["Artemis"]},
            "Demeter": {"desc": "Auto-attack", "preferred": ["Zeus", "Dionysus"]},
            "Gilgamesh": {"desc": "Dash-strike", "preferred": ["Artemis", "Zeus"]}
        }
    },
    "Adamant Rail": {
        "description": "Ranged weapon with rapid fire and special bomb.",
        "attack_speed": "Very Fast",
        "damage_type": "Multi-Hit",
        "preferred_gods": ["Zeus", "Dionysus", "Artemis"],
        "focus": "Attack",
        "symbol": "🔫",
        "aspects": {
            "Zagreus": {"desc": "Attack-focused", "preferred": ["Zeus", "Dionysus"]},
            "Eris": {"desc": "High damage", "preferred": ["Artemis", "Aphrodite"]},
            "Hestia": {"desc": "Manual reload", "preferred": ["Aphrodite", "Artemis"]},
            "Lucifer": {"desc": "Beam focus", "preferred": ["Demeter", "Zeus"]}
        }
    }
}

# === BOONS DATA ===
BOONS_DATA: List[Dict[str, Any]] = [
    # Zeus Boons
    {"name": "Lightning Strike", "god": "Zeus", "type": "Attack", "description": "Your Attack deals bonus lightning damage.", "tags": ["attack", "lightning", "damage"], "status_curse_applied": "Jolted", "tier": "S", "weapon_synergy": ["Twin Fists", "Adamant Rail", "Eternal Spear"]},
    {"name": "Thunder Flourish", "god": "Zeus", "type": "Special", "description": "Your Special creates lightning bolts.", "tags": ["special", "lightning", "damage"], "status_curse_applied": "Jolted", "tier": "S", "weapon_synergy": ["Shield of Chaos", "Eternal Spear"]},
    {"name": "Thunder Dash", "god": "Zeus", "type": "Dash", "description": "Your Dash creates lightning.", "tags": ["dash", "lightning", "damage"], "status_curse_applied": "Jolted", "tier": "A", "weapon_synergy": ["Stygian Blade"]},
    {"name": "Storm Lightning", "god": "Zeus", "type": "Cast", "description": "Your Cast creates a storm cloud.", "tags": ["cast", "lightning", "damage"], "status_curse_applied": "Jolted", "tier": "B", "weapon_synergy": []},
    {"name": "Double Strike", "god": "Zeus", "type": "Utility", "description": "Lightning strikes twice.", "tags": ["lightning_enhancer", "damage_enhancer"], "tier": "A", "weapon_synergy": []},
    {"name": "High Voltage", "god": "Zeus", "type": "Utility", "description": "Lightning deals damage in larger area.", "tags": ["lightning_enhancer", "aoe_enhancer"], "tier": "A", "weapon_synergy": []},
    {"name": "Clouded Judgment", "god": "Zeus", "type": "Utility", "description": "Jolted effects deal more damage.", "tags": ["jolted_enhancer", "status_curse_damage"], "tier": "S", "weapon_synergy": []},
    
    # Poseidon Boons
    {"name": "Tidal Dash", "god": "Poseidon", "type": "Dash", "description": "Dash damages and knocks away foes.", "tags": ["dash", "knockback", "damage"], "tier": "S", "weapon_synergy": ["Stygian Blade"]},
    {"name": "Tempest Strike", "god": "Poseidon", "type": "Attack", "description": "Attack knocks foes away.", "tags": ["attack", "knockback", "damage"], "tier": "B", "weapon_synergy": []},
    {"name": "Typhoon's Fury", "god": "Poseidon", "type": "Utility", "description": "Knock-away deals more damage.", "tags": ["knockback_enhancer", "damage_enhancer"], "tier": "A", "weapon_synergy": []},
    {"name": "Razor Shoals", "god": "Poseidon", "type": "Utility", "description": "Knock-away inflicts Rupture.", "tags": ["rupture_applier", "status_curse_applier"], "status_curse_applied": "Rupture", "tier": "A", "weapon_synergy": []},
    
    # Athena Boons
    {"name": "Divine Dash", "god": "Athena", "type": "Dash", "description": "Your Dash Deflects.", "tags": ["dash", "deflect", "utility"], "tier": "S", "weapon_synergy": []},
    {"name": "Divine Strike", "god": "Athena", "type": "Attack", "description": "Your Attack Deflects.", "tags": ["attack", "deflect", "utility"], "tier": "B", "weapon_synergy": []},
    {"name": "Divine Flourish", "god": "Athena", "type": "Special", "description": "Your Special Deflects.", "tags": ["special", "deflect", "utility"], "tier": "B", "weapon_synergy": []},
    {"name": "Blinding Flash", "god": "Athena", "type": "Utility", "description": "Deflect makes foes Weak.", "tags": ["weak_applier", "status_curse_applier", "deflect_synergy"], "status_curse_applied": "Weak", "tier": "A", "weapon_synergy": []},
    {"name": "Deathless Stand", "god": "Athena", "type": "Utility", "description": "Death Defiance effect.", "tags": ["survivability", "death_defiance"], "tier": "A", "weapon_synergy": []},
    
    # Aphrodite Boons
    {"name": "Heartbreak Strike", "god": "Aphrodite", "type": "Attack", "description": "Attack deals bonus damage and Weak.", "tags": ["attack", "damage", "weak_applier"], "status_curse_applied": "Weak", "tier": "S", "weapon_synergy": ["Stygian Blade", "Heart-Seeking Bow"]},
    {"name": "Heartbreak Flourish", "god": "Aphrodite", "type": "Special", "description": "Special deals damage and Weak.", "tags": ["special", "damage", "weak_applier"], "status_curse_applied": "Weak", "tier": "A", "weapon_synergy": []},
    {"name": "Crush Shot", "god": "Aphrodite", "type": "Cast", "description": "Cast inflicts Weak.", "tags": ["cast", "damage", "weak_applier"], "status_curse_applied": "Weak", "tier": "B", "weapon_synergy": []},
    {"name": "Sweet Surrender", "god": "Aphrodite", "type": "Utility", "description": "Weak foes take more damage.", "tags": ["weak_enhancer", "damage_enhancer"], "tier": "S", "weapon_synergy": []},
    {"name": "Dying Lament", "god": "Aphrodite", "type": "Utility", "description": "Weak foes explode when killed.", "tags": ["weak_synergy", "aoe_damage"], "tier": "B", "weapon_synergy": []},
    
    # Ares Boons
    {"name": "Curse of Agony", "god": "Ares", "type": "Attack", "description": "Attack inflicts Doom.", "tags": ["attack", "doom_applier"], "status_curse_applied": "Doom", "tier": "S", "weapon_synergy": ["Stygian Blade", "Heart-Seeking Bow"]},
    {"name": "Curse of Pain", "god": "Ares", "type": "Special", "description": "Special inflicts Doom.", "tags": ["special", "doom_applier"], "status_curse_applied": "Doom", "tier": "S", "weapon_synergy": ["Shield of Chaos"]},
    {"name": "Blade Dash", "god": "Ares", "type": "Dash", "description": "Dash creates Blade Rift.", "tags": ["dash", "blade_rift", "damage"], "tier": "A", "weapon_synergy": []},
    {"name": "Slicing Shot", "god": "Ares", "type": "Cast", "description": "Cast creates Blade Rift.", "tags": ["cast", "blade_rift", "damage"], "tier": "B", "weapon_synergy": []},
    {"name": "Impending Doom", "god": "Ares", "type": "Utility", "description": "Doom deals more damage but slower.", "tags": ["doom_enhancer", "status_curse_damage"], "tier": "S", "weapon_synergy": []},
    {"name": "Dire Misfortune", "god": "Ares", "type": "Utility", "description": "Doom damage stacks.", "tags": ["doom_enhancer", "status_curse_damage"], "tier": "A", "weapon_synergy": []},
    
    # Artemis Boons
    {"name": "Deadly Strike", "god": "Artemis", "type": "Attack", "description": "Attack has Critical chance.", "tags": ["attack", "crit_chance"], "tier": "A", "weapon_synergy": ["Heart-Seeking Bow", "Stygian Blade"]},
    {"name": "Deadly Flourish", "god": "Artemis", "type": "Special", "description": "Special has Critical chance.", "tags": ["special", "crit_chance"], "tier": "A", "weapon_synergy": ["Heart-Seeking Bow"]},
    {"name": "True Shot", "god": "Artemis", "type": "Cast", "description": "Cast fires seeking Critical arrow.", "tags": ["cast", "crit_damage", "seeking"], "tier": "S", "weapon_synergy": []},
    {"name": "Hunter Dash", "god": "Artemis", "type": "Dash", "description": "Dash deals Critical damage.", "tags": ["dash", "crit_chance", "damage"], "tier": "B", "weapon_synergy": []},
    {"name": "Clean Kill", "god": "Artemis", "type": "Utility", "description": "Critical effects deal more damage.", "tags": ["crit_damage_enhancer"], "tier": "S", "weapon_synergy": []},
    {"name": "Hunter's Mark", "god": "Artemis", "type": "Utility", "description": "Mark foes for higher Crit chance.", "tags": ["crit_synergy", "crit_chance"], "tier": "A", "weapon_synergy": []},
    {"name": "Pressure Points", "god": "Artemis", "type": "Utility", "description": "Any damage can be Critical.", "tags": ["crit_chance", "damage_enhancer"], "tier": "S", "weapon_synergy": []},
    {"name": "Support Fire", "god": "Artemis", "type": "Utility", "description": "Fire seeking arrows automatically.", "tags": ["damage_enhancer", "seeking"], "tier": "A", "weapon_synergy": []},
    
    # Dionysus Boons
    {"name": "Drunken Strike", "god": "Dionysus", "type": "Attack", "description": "Attack inflicts Hangover.", "tags": ["attack", "hangover_applier"], "status_curse_applied": "Hangover", "tier": "S", "weapon_synergy": ["Twin Fists", "Adamant Rail"]},
    {"name": "Drunken Flourish", "god": "Dionysus", "type": "Special", "description": "Special inflicts Hangover.", "tags": ["special", "hangover_applier"], "status_curse_applied": "Hangover", "tier": "S", "weapon_synergy": ["Shield of Chaos", "Eternal Spear"]},
    {"name": "Trippy Shot", "god": "Dionysus", "type": "Cast", "description": "Cast creates Festive Fog with Hangover.", "tags": ["cast", "hangover_applier", "aoe"], "status_curse_applied": "Hangover", "tier": "B", "weapon_synergy": []},
    {"name": "Drunken Dash", "god": "Dionysus", "type": "Dash", "description": "Dash creates Festive Fog.", "tags": ["dash", "hangover_applier", "aoe"], "status_curse_applied": "Hangover", "tier": "B", "weapon_synergy": []},
    {"name": "Numbing Sensation", "god": "Dionysus", "type": "Utility", "description": "Hangover slows foes.", "tags": ["hangover_enhancer", "slow_effect"], "tier": "A", "weapon_synergy": []},
    {"name": "Positive Outlook", "god": "Dionysus", "type": "Utility", "description": "Take less damage at low health.", "tags": ["survivability"], "tier": "B", "weapon_synergy": []},
    
    # Hermes Boons
    {"name": "Quick Strike", "god": "Hermes", "type": "Attack", "description": "Attack speed increased.", "tags": ["attack_speed", "attack_enhancer"], "tier": "B", "weapon_synergy": ["Stygian Blade", "Twin Fists"]},
    {"name": "Swift Flourish", "god": "Hermes", "type": "Special", "description": "Special speed increased.", "tags": ["special_speed", "special_enhancer"], "tier": "B", "weapon_synergy": []},
    {"name": "Greater Reflex", "god": "Hermes", "type": "Dash", "description": "Gain +1 Dash.", "tags": ["dash_enhancer", "utility"], "tier": "S", "weapon_synergy": []},
    {"name": "Hyper Sprint", "god": "Hermes", "type": "Dash", "description": "After Dash gain move speed.", "tags": ["dash_synergy", "move_speed"], "tier": "A", "weapon_synergy": []},
    {"name": "Rush Delivery", "god": "Hermes", "type": "Utility", "description": "Deal damage based on move speed.", "tags": ["move_speed_synergy", "damage_enhancer"], "tier": "A", "weapon_synergy": []},
    
    # Demeter Boons
    {"name": "Frost Strike", "god": "Demeter", "type": "Attack", "description": "Attack inflicts Chill.", "tags": ["attack", "damage", "chill_applier"], "status_curse_applied": "Chill", "tier": "A", "weapon_synergy": ["Twin Fists", "Adamant Rail"]},
    {"name": "Frost Flourish", "god": "Demeter", "type": "Special", "description": "Special inflicts Chill.", "tags": ["special", "damage", "chill_applier"], "status_curse_applied": "Chill", "tier": "A", "weapon_synergy": []},
    {"name": "Crystal Beam", "god": "Demeter", "type": "Cast", "description": "Cast creates crystal beam with Chill.", "tags": ["cast", "chill_applier", "summon"], "status_curse_applied": "Chill", "tier": "A", "weapon_synergy": []},
    {"name": "Killing Freeze", "god": "Demeter", "type": "Utility", "description": "Chill explodes when foes die.", "tags": ["chill_synergy", "aoe_damage"], "tier": "B", "weapon_synergy": []},
    {"name": "Arctic Blast", "god": "Demeter", "type": "Utility", "description": "Chill deals damage when it expires.", "tags": ["chill_enhancer", "status_curse_damage"], "tier": "A", "weapon_synergy": []},
    {"name": "Rare Crop", "god": "Demeter", "type": "Utility", "description": "Upgrade random boon rarity.", "tags": ["utility", "rarity_upgrade"], "tier": "S", "weapon_synergy": []},
]

# === DUO BOONS DATA ===
DUO_BOONS_DATA: List[Dict[str, Any]] = [
    {"name": "Smoldering Air", "gods": ["Zeus", "Aphrodite"], "description": "Call charges automatically.", "prerequisites": [("Zeus", "Lightning Strike"), ("Aphrodite", "Heartbreak Strike")], "tier": "A"},
    {"name": "Curse of Vengeance", "gods": ["Ares", "Zeus"], "description": "After revenge, foes get struck by lightning.", "prerequisites": [("Ares", "Curse of Agony"), ("Zeus", "Lightning Strike")], "tier": "B"},
    {"name": "Vengeful Mood", "gods": ["Ares", "Zeus"], "description": "Revenge attacks occur more often.", "prerequisites": [("Ares", "Curse of Agony"), ("Zeus", "Thunder Flourish")], "tier": "A"},
    {"name": "Splitting Headache", "gods": ["Artemis", "Dionysus"], "description": "Hangover can deal Critical damage.", "prerequisites": [("Artemis", "Deadly Strike"), ("Dionysus", "Drunken Strike")], "tier": "S"},
    {"name": "Cold Fusion", "gods": ["Zeus", "Demeter"], "description": "Jolted effects also Chill.", "prerequisites": [("Zeus", "Lightning Strike"), ("Demeter", "Frost Strike")], "tier": "A"},
    {"name": "Ice Wine", "gods": ["Dionysus", "Demeter"], "description": "Festive Fog also Chills.", "prerequisites": [("Dionysus", "Trippy Shot"), ("Demeter", "Crystal Beam")], "tier": "B"},
    {"name": "Heart Rend", "gods": ["Artemis", "Aphrodite"], "description": "Crits deal more damage to Weak foes.", "prerequisites": [("Artemis", "Deadly Strike"), ("Aphrodite", "Heartbreak Strike")], "tier": "S"},
    {"name": "Curse of Longing", "gods": ["Ares", "Aphrodite"], "description": "Doom deals more to Weak foes.", "prerequisites": [("Ares", "Curse of Agony"), ("Aphrodite", "Heartbreak Strike")], "tier": "S"},
    {"name": "Lightning Rod", "gods": ["Zeus", "Artemis"], "description": "Casts stick and strike with lightning.", "prerequisites": [("Zeus", "Storm Lightning"), ("Artemis", "True Shot")], "tier": "A"},
    {"name": "Sea Storm", "gods": ["Zeus", "Poseidon"], "description": "Knockback triggers lightning.", "prerequisites": [("Zeus", "Lightning Strike"), ("Poseidon", "Tidal Dash")], "tier": "S"},
    {"name": "Freezing Vortex", "gods": ["Ares", "Demeter"], "description": "Blade Rifts inflict Chill.", "prerequisites": [("Ares", "Blade Dash"), ("Demeter", "Frost Strike")], "tier": "B"},
    {"name": "Scintillating Feast", "gods": ["Zeus", "Dionysus"], "description": "Festive Fog strikes with lightning.", "prerequisites": [("Zeus", "Lightning Strike"), ("Dionysus", "Trippy Shot")], "tier": "B"},
    {"name": "Deadly Reversal", "gods": ["Artemis", "Athena"], "description": "After Deflect, next attack is Critical.", "prerequisites": [("Artemis", "Deadly Strike"), ("Athena", "Divine Dash")], "tier": "A"},
    {"name": "Calculated Risk", "gods": ["Athena", "Dionysus"], "description": "Festive Fog makes you Deflect.", "prerequisites": [("Athena", "Divine Dash"), ("Dionysus", "Trippy Shot")], "tier": "B"},
    {"name": "Merciful End", "gods": ["Ares", "Athena"], "description": "Deflect triggers Doom immediately.", "prerequisites": [("Ares", "Curse of Agony"), ("Athena", "Divine Dash")], "tier": "S"},
]

# === LEGENDARY BOONS DATA ===
LEGENDARY_BOONS_DATA: List[Dict[str, Any]] = [
    {"name": "Fully Loaded", "god": "Artemis", "description": "Gain +2 Cast ammo.", "prerequisites": [("Artemis", "True Shot")], "tier": "A"},
    {"name": "Greatest Reflex", "god": "Hermes", "description": "Gain +2 Dashes.", "prerequisites": [("Hermes", "Greater Reflex")], "tier": "S"},
    {"name": "Winter Harvest", "god": "Demeter", "description": "Chill makes foes vulnerable and explode.", "prerequisites": [("Demeter", "Frost Strike")], "tier": "A"},
    {"name": "Proud Bearing", "god": "Athena", "description": "Start encounters with Call gauge.", "prerequisites": [("Athena", "Divine Strike")], "tier": "B"},
    {"name": "Battle Rage", "god": "Ares", "description": "After killing, deal more damage.", "prerequisites": [("Ares", "Curse of Agony")], "tier": "A"},
    {"name": "High Confidence", "god": "Dionysus", "description": "Deal more damage above 80% HP.", "prerequisites": [("Dionysus", "Drunken Strike")], "tier": "B"},
    {"name": "Life Affirmation", "god": "Aphrodite", "description": "Healing is more effective.", "prerequisites": [("Aphrodite", "Heartbreak Strike")], "tier": "B"},
]

# === HELPER LOOKUPS ===
BOON_NAME_TO_DATA: Dict[str, Dict[str, Any]] = {boon['name']: boon for boon in BOONS_DATA}

TIER_COLORS = {
    "S": "#FF4444",
    "A": "#FFD700",
    "B": "#87CEEB",
    "C": "#90EE90",
    "D": "#A0A0A0"
}

TIER_ICONS = {
    "S": "🔥",
    "A": "⭐",
    "B": "✨",
    "C": "💫",
    "D": "·"
}

# === BOSS DATA ===
BOSSES = ["Tartarus", "Asphodel", "Elysium", "Temple of Styx", "Hades"]
