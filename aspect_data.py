"""
Weapon aspects and their optimal strategies
"""

WEAPON_ASPECTS = {
    "Stygian Blade": {
        "Zagreus": {
            "ability": "+5% damage per rank",
            "strategy": "Balanced - works with any build",
            "best_boons": ["Aphrodite Attack", "Artemis Special", "Athena Dash"],
            "playstyle": "aggressive"
        },
        "Nemesis": {
            "ability": "+20% crit chance when above 80% HP",
            "strategy": "High-risk high-reward crit build",
            "best_boons": ["Artemis Attack", "Deadly Strike", "Pressure Points"],
            "playstyle": "careful"
        },
        "Poseidon": {
            "ability": "Special becomes AoE dislodging cast",
            "strategy": "Cast-focused build",
            "best_boons": ["Any cast", "Poseidon Special", "Mirage Shot"],
            "playstyle": "cast"
        },
        "Arthur": {
            "ability": "50 HP, new moveset, slower",
            "strategy": "Tank build with AoE",
            "best_boons": ["Dionysus Attack", "Divine Dash", "Aphrodite Special"],
            "playstyle": "tank"
        }
    },
    "Heart-Seeking Bow": {
        "Zagreus": {
            "ability": "+10% damage per rank",
            "strategy": "Standard bow play",
            "best_boons": ["Aphrodite Attack", "Artemis Special", "Any dash"],
            "playstyle": "ranged"
        },
        "Chiron": {
            "ability": "Special shots home on enemies hit by attack",
            "strategy": "Attack + Special synergy",
            "best_boons": ["Aphrodite Attack", "Artemis Special", "Relentless Volley"],
            "playstyle": "combo"
        },
        "Hera": {
            "ability": "Load casts into bow for massive damage",
            "strategy": "Cast-focused build",
            "best_boons": ["Aphrodite/Demeter cast", "Exit Wounds", "Quick Reload"],
            "playstyle": "cast"
        },
        "Rama": {
            "ability": "Shared damage buff with perfect shots",
            "strategy": "Precision timing build",
            "best_boons": ["Aphrodite Attack", "Any damage boons", "Concentrated Volley"],
            "playstyle": "skilled"
        }
    },
    "Shield of Chaos": {
        "Zagreus": {
            "ability": "+2% block damage per rank",
            "strategy": "Bull rush focused",
            "best_boons": ["Ares/Aphrodite Special", "Artemis Attack", "Zeus Dash"],
            "playstyle": "aggressive"
        },
        "Chaos": {
            "ability": "+5 shield bounces",
            "strategy": "Special spam build (STRONGEST)",
            "best_boons": ["Aphrodite Special", "Artemis Crit", "Mirage Shot"],
            "playstyle": "special"
        },
        "Zeus": {
            "ability": "Blocks charge Zeus Aid",
            "strategy": "Block-focused defensive",
            "best_boons": ["Zeus Aid", "Zeus Dash", "High Voltage"],
            "playstyle": "defensive"
        },
        "Beowulf": {
            "ability": "Cast-loading for big bull rush",
            "strategy": "Cast + bull rush combo",
            "best_boons": ["Aphrodite/Artemis cast", "Charged Shot", "Quick Recovery"],
            "playstyle": "cast"
        }
    },
    "Eternal Spear": {
        "Zagreus": {
            "ability": "+15% damage per rank after special",
            "strategy": "Special then attack combo",
            "best_boons": ["Artemis Attack", "Any Special", "Deadly Flourish"],
            "playstyle": "combo"
        },
        "Achilles": {
            "ability": "+150% damage on rush, +50% after",
            "strategy": "Rush in, combo attack",
            "best_boons": ["Artemis/Aphrodite Attack", "Deadly Strike", "Quick Favor"],
            "playstyle": "aggressive"
        },
        "Hades": {
            "ability": "Spin attack applies Boiling Blood",
            "strategy": "Cast-focused build",
            "best_boons": ["Any cast", "Boiling Blood mirror", "Exit Wounds"],
            "playstyle": "cast"
        },
        "Guan Yu": {
            "ability": "-70 HP, heal on kills, heavy spin",
            "strategy": "High-risk lifesteal build",
            "best_boons": ["Ares Attack", "Doom effects", "Curse of Longing"],
            "playstyle": "berserker"
        }
    },
    "Twin Fists": {
        "Zagreus": {
            "ability": "+5% speed per rank",
            "strategy": "Fast aggressive play",
            "best_boons": ["Aphrodite Attack", "Artemis Dash-Strike", "Merciful End"],
            "playstyle": "aggressive"
        },
        "Talos": {
            "ability": "Magnetic uppercut",
            "strategy": "Special-focused vacuum build",
            "best_boons": ["Dionysus Special", "Merciful End", "Strong Drink"],
            "playstyle": "special"
        },
        "Demeter": {
            "ability": "+12 dash-strikes",
            "strategy": "Dash-strike spam",
            "best_boons": ["Aphrodite/Artemis Attack", "Divine Dash", "Hunter Dash"],
            "playstyle": "mobile"
        },
        "Gilgamesh": {
            "ability": "New moves, Maim debuff",
            "strategy": "Heavy combo build",
            "best_boons": ["Aphrodite Attack", "Zeus Special", "Merciful End"],
            "playstyle": "technical"
        }
    },
    "Adamant Rail": {
        "Zagreus": {
            "ability": "+10% speed per rank",
            "strategy": "Standard gun play",
            "best_boons": ["Zeus Attack", "Artemis Special", "Any dash"],
            "playstyle": "ranged"
        },
        "Eris": {
            "ability": "+75% damage after special",
            "strategy": "Special debuff then attack",
            "best_boons": ["Zeus Attack", "Any Special", "Thunder Flourish"],
            "playstyle": "combo"
        },
        "Hestia": {
            "ability": "Manual reload for big damage",
            "strategy": "Slow precise shots",
            "best_boons": ["Aphrodite Attack", "Artemis Crit", "Flurry Fire"],
            "playstyle": "precise"
        },
        "Lucifer": {
            "ability": "Beam mode with omega moves",
            "best_boons": ["Demeter Attack", "Artemis Special", "Rare Crop"],
            "strategy": "Beam build",
            "playstyle": "sustained"
        }
    }
}
