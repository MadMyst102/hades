"""
Real-time Damage Calculator for Hades builds
"""

from typing import Dict, List
from data import BOON_NAME_TO_DATA

class DamageCalculator:
    """Calculate actual DPS based on build."""
    
    # Base weapon damage values
    BASE_DAMAGE = {
        "Stygian Blade": {"attack": 20, "special": 30, "speed": 1.2},
        "Heart-Seeking Bow": {"attack": 50, "special": 10, "speed": 0.8},
        "Shield of Chaos": {"attack": 20, "special": 35, "speed": 1.0},
        "Eternal Spear": {"attack": 25, "special": 40, "speed": 1.1},
        "Twin Fists": {"attack": 12, "special": 20, "speed": 2.0},
        "Adamant Rail": {"attack": 10, "special": 50, "speed": 3.0}
    }
    
    # Damage bonus per boon type
    DAMAGE_MULTIPLIERS = {
        "Strike": 0.4,      # 40% damage increase
        "Flourish": 0.6,    # 60% damage increase
        "Deadly": 0.2,      # 20% + crit
        "Heartbreak": 0.5,  # 50% + weak
        "Thunder": 0.1,     # 10% + chain lightning
        "Lightning": 0.1,   # 10% + chain
        "Curse": 0.6,       # Doom damage
        "Frost": 0.3,       # 30% + chill
        "Tidal": 0.3,       # 30% knockback
    }
    
    def __init__(self):
        self.weapon = None
        self.boons = []
        self.pom_levels = {}
        self.hammer_count = 0
        
    def set_weapon(self, weapon: str):
        self.weapon = weapon
        
    def set_boons(self, boons: List[str], pom_levels: Dict[str, int]):
        self.boons = boons
        self.pom_levels = pom_levels
        
    def set_hammers(self, count: int):
        self.hammer_count = count
        
    def calculate_dps(self) -> Dict:
        """Calculate complete DPS breakdown."""
        if not self.weapon:
            return {
                "total_dps": 0,
                "base_damage": 0,
                "modified_damage": 0,
                "crit_damage": 0,
                "multiplier": 1.0,
                "crit_chance": 0,
                "attack_speed": 0,
                "rating": "📊 No Weapon"
            }
        
        weapon_data = self.BASE_DAMAGE.get(self.weapon, {"attack": 20, "speed": 1.0})
        base_attack = weapon_data["attack"]
        attack_speed = weapon_data["speed"]
        
        # Calculate damage multiplier from boons
        total_multiplier = 1.0
        crit_chance = 0.0
        
        for boon_name in self.boons:
            boon_data = BOON_NAME_TO_DATA.get(boon_name)
            if not boon_data:
                continue
            
            # Check boon type and add multiplier
            for damage_type, multiplier in self.DAMAGE_MULTIPLIERS.items():
                if damage_type in boon_name:
                    level = self.pom_levels.get(boon_name, 1)
                    # Each pom level adds 2% more effectiveness
                    adjusted_multiplier = multiplier * (1 + (level - 1) * 0.02)
                    total_multiplier += adjusted_multiplier
                    break
            
            # Check for crit boons
            if "Deadly" in boon_name or "Artemis" in boon_data.get('god', ''):
                crit_chance += 0.15  # 15% base crit chance
        
        # Hammer bonus (each hammer adds ~20% damage)
        total_multiplier += self.hammer_count * 0.2
        
        # Calculate final damage
        modified_damage = base_attack * total_multiplier
        
        # Apply critical hits (crits do 3x damage)
        avg_damage_with_crit = modified_damage * (1 + crit_chance * 2)
        
        # Calculate DPS
        dps = avg_damage_with_crit * attack_speed
        
        return {
            "total_dps": round(dps, 1),
            "base_damage": base_attack,
            "modified_damage": round(modified_damage, 1),
            "crit_damage": round(avg_damage_with_crit, 1),
            "multiplier": round(total_multiplier, 2),
            "crit_chance": round(crit_chance * 100, 1),
            "attack_speed": attack_speed,
            "rating": self._rate_dps(dps)
        }
    
    def _rate_dps(self, dps: float) -> str:
        """Rate DPS output."""
        if dps >= 150:
            return "🔥 God-Tier"
        elif dps >= 100:
            return "⭐ Excellent"
        elif dps >= 70:
            return "✨ Strong"
        elif dps >= 40:
            return "💫 Decent"
        elif dps > 0:
            return "📊 Developing"
        else:
            return "📊 No Build"
    
    def get_recommendations(self) -> List[str]:
        """Get recommendations to improve DPS."""
        recommendations = []
        
        if not self.weapon:
            return ["⚔️ Select a weapon to get started"]
        
        if not self.boons:
            return ["✨ Add boons to begin building"]
        
        # Check for attack/special boons
        has_attack = any("Strike" in b for b in self.boons)
        has_special = any("Flourish" in b for b in self.boons)
        
        if not has_attack:
            recommendations.append("⚡ Add an Attack boon for consistent damage")
        
        if not has_special:
            recommendations.append("💥 Add a Special boon for burst damage")
        
        # Check for crit
        has_crit = any("Deadly" in b or "Artemis" in BOON_NAME_TO_DATA.get(b, {}).get('god', '') for b in self.boons)
        if not has_crit:
            recommendations.append("🎯 Add Artemis boons for critical hits")
        
        # Check for hammers
        if self.hammer_count == 0:
            recommendations.append("🔨 Get Daedalus Hammers for +20% damage each")
        elif self.hammer_count == 1:
            recommendations.append("🔨 Second Daedalus Hammer available for more power")
        
        # Check pom levels
        low_level_boons = [b for b in self.boons if self.pom_levels.get(b, 1) == 1]
        if len(low_level_boons) > 3:
            recommendations.append("📈 Use Poms to upgrade your core damage boons")
        
        # Check for duo potential
        gods_used = set()
        for boon in self.boons:
            boon_data = BOON_NAME_TO_DATA.get(boon)
            if boon_data:
                gods_used.add(boon_data['god'])
        
        if len(gods_used) >= 2:
            recommendations.append("🌟 You have multiple gods - look for duo boon opportunities!")
        
        if not recommendations:
            recommendations.append("✅ Build looks solid! Keep optimizing with Poms and Hammers!")
        
        return recommendations[:5]  # Limit to top 5
