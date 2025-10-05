"""
Mirror of Night talents data
"""

MIRROR_TALENTS = {
    "Death Defiance": {
        "category": "defense",
        "description": "Restore 50% HP when you die",
        "max_rank": 3,
        "icon": "💀",
        "alternative": None
    },
    "Stubborn Defiance": {
        "category": "defense",
        "description": "Restore to 30 HP when you die (once per chamber)",
        "max_rank": 1,
        "icon": "💀",
        "alternative": "Death Defiance"
    },
    "Greater Reflex": {
        "category": "mobility",
        "description": "Additional dash",
        "max_rank": 1,
        "icon": "🏃",
        "alternative": "Ruthless Reflex"
    },
    "Ruthless Reflex": {
        "category": "mobility",
        "description": "+50% damage after dash (1s)",
        "max_rank": 1,
        "icon": "🏃",
        "alternative": "Greater Reflex"
    },
    "Shadow Presence": {
        "category": "offense",
        "description": "+10/20% Strike damage from behind",
        "max_rank": 2,
        "icon": "⚔️",
        "alternative": "Fiery Presence"
    },
    "Fiery Presence": {
        "category": "offense",
        "description": "+10/20% damage at ≥80% HP",
        "max_rank": 2,
        "icon": "⚔️",
        "alternative": "Shadow Presence"
    },
    "Boiling Blood": {
        "category": "offense",
        "description": "+50% damage to bloodstone enemies",
        "max_rank": 1,
        "icon": "🩸",
        "alternative": "Abyssal Blood"
    },
    "Abyssal Blood": {
        "category": "offense",
        "description": "+50% cast damage",
        "max_rank": 1,
        "icon": "🩸",
        "alternative": "Boiling Blood"
    },
    "Thick Skin": {
        "category": "defense",
        "description": "+HP (5/10/15/20/25/30/40/50 per rank)",
        "max_rank": 8,
        "icon": "🛡️",
        "alternative": None
    }
}
