"""
Door Choice Advisor - The Killer Feature
Analyzes current build and recommends which door to take
"""

from typing import Dict, List, Tuple, Set
from data import GODS_DATA, DUO_BOONS_DATA, LEGENDARY_BOONS_DATA, BOON_NAME_TO_DATA


class DoorAdvisor:
    """Intelligent door choice recommendation system."""
    
    # Room reward types
    REWARD_TYPES = [
        "Boon", "Pom of Power", "Centaur Heart", "Daedalus Hammer",
        "Gold", "Darkness", "Gemstone", "Nectar", "Ambrosia",
        "Chaos Gate", "Trial of Gods", "Shop", "Fountain"
    ]
    
    def __init__(self):
        self.current_region = "Tartarus"
        self.room_number = 1
        self.current_health = 100
        self.max_health = 100
        self.gold = 0
        self.acquired_boons = set()
        self.selected_gods = set()
        self.hammer_count = 0
        self.build_score = 0
        
    def set_run_state(self, region: str, room: int, health: int, max_hp: int, gold: int):
        """Update current run state."""
        self.current_region = region
        self.room_number = room
        self.current_health = health
        self.max_health = max_hp
        self.gold = gold
        
    def set_build_state(self, boons: Set[str], gods: Set[str], hammers: int, score: int):
        """Update current build state."""
        self.acquired_boons = boons
        self.selected_gods = gods
        self.hammer_count = hammers
        self.build_score = score
    
    def analyze_door(self, god: str, reward_type: str) -> Dict:
        """Analyze a single door choice and return priority score."""
        score = 50  # Base score
        reasons = []
        priority_level = "⭐⭐⭐"  # Default
        
        # === BOON DOOR ANALYSIS ===
        if reward_type == "Boon":
            # Check if this god helps toward duo/legendary
            duo_potential = self._check_duo_potential(god)
            if duo_potential > 0:
                score += duo_potential
                if duo_potential >= 40:
                    reasons.append(f"🌟 CAN GET DUO BOON!")
                else:
                    reasons.append(f"Progress toward duo (+{duo_potential})")
            
            legendary_potential = self._check_legendary_potential(god)
            if legendary_potential > 0:
                score += legendary_potential
                reasons.append(f"⚡ Progress toward legendary")
            
            # Check if we need this god for build diversity
            if god not in self.selected_gods:
                score += 15
                reasons.append("New god for build variety")
            
            # Early game priority (get core boons)
            if self.room_number <= 8 and len(self.acquired_boons) < 3:
                score += 20
                reasons.append("Early game - need core boons")
        
        # === POM ANALYSIS ===
        elif reward_type == "Pom of Power":
            if len(self.acquired_boons) >= 3:
                score += 20
                reasons.append("Good boon count for upgrade")
            else:
                score -= 20
                reasons.append("⚠️ Not enough boons yet")
        
        # === HEALTH ANALYSIS ===
        elif reward_type == "Centaur Heart":
            health_percent = (self.current_health / self.max_health) * 100
            
            if health_percent < 40:
                score += 50
                reasons.append("🚨 CRITICAL - Very low HP!")
            elif health_percent < 60:
                score += 30
                reasons.append("⚠️ Low HP - strongly consider")
            elif health_percent < 80:
                score += 15
                reasons.append("HP could be better")
            else:
                score -= 10
                reasons.append("HP is fine, skip for better rewards")
        
        # === HAMMER ANALYSIS ===
        elif reward_type == "Daedalus Hammer":
            if self.hammer_count == 0:
                score += 45
                reasons.append("🔨 FIRST HAMMER - High priority!")
            elif self.hammer_count == 1:
                score += 30
                reasons.append("🔨 Second hammer - good boost")
            else:
                score = 0
                reasons.append("❌ Already have 2 hammers")
        
        # === GOLD ANALYSIS ===
        elif reward_type == "Gold":
            if self.gold < 100:
                score += 15
                reasons.append("Low gold - could use some")
            elif self.gold > 300:
                score -= 20
                reasons.append("Already have plenty of gold")
        
        # === CHAOS GATE ANALYSIS ===
        elif reward_type == "Chaos Gate":
            health_percent = (self.current_health / self.max_health) * 100
            rooms_to_boss = self._rooms_until_boss()
            
            if health_percent < 50:
                score -= 40
                reasons.append("❌ RISKY - Low HP for curse")
            elif rooms_to_boss <= 2:
                score -= 30
                reasons.append("⚠️ RISKY - Boss approaching")
            else:
                score += 25
                reasons.append("Good risk/reward timing")
        
        # === SHOP ANALYSIS ===
        elif reward_type == "Shop":
            if self.gold > 200:
                score += 20
                reasons.append("Good gold for shopping")
            else:
                score -= 10
                reasons.append("Not much gold to spend")
        
        # === FOUNTAIN ANALYSIS ===
        elif reward_type == "Fountain":
            health_percent = (self.current_health / self.max_health) * 100
            if health_percent < 70:
                score += 35
                reasons.append("❤️ Good HP recovery opportunity")
        
        # Region-specific adjustments
        if self.current_region == "Tartarus" and reward_type == "Boon":
            score += 10
            reasons.append("Tartarus - prioritize boons")
        
        # Determine priority level
        if score >= 90:
            priority_level = "🔥 TAKE THIS!"
            color = "#FF4444"
        elif score >= 75:
            priority_level = "⭐⭐⭐⭐⭐"
            color = "#FFD700"
        elif score >= 60:
            priority_level = "⭐⭐⭐⭐"
            color = "#FFA500"
        elif score >= 40:
            priority_level = "⭐⭐⭐"
            color = "#90EE90"
        elif score >= 25:
            priority_level = "⭐⭐"
            color = "#ADD8E6"
        else:
            priority_level = "⭐ Skip"
            color = "#808080"
        
        return {
            'score': score,
            'priority': priority_level,
            'reasons': reasons,
            'color': color,
            'recommendation': self._get_recommendation(score)
        }
    
    def _check_duo_potential(self, god: str) -> int:
        """Check how much this god helps with duo boons."""
        score = 0
        
        for duo in DUO_BOONS_DATA:
            if god in duo['gods']:
                # Check if we have the other god
                other_gods = [g for g in duo['gods'] if g != god]
                if all(g in self.selected_gods for g in other_gods):
                    # Check prerequisite progress
                    prereqs_needed = [b for _, b in duo['prerequisites'] if b not in self.acquired_boons]
                    
                    if len(prereqs_needed) == 1:
                        score += 50  # One boon away!
                    elif len(prereqs_needed) == 2:
                        score += 25  # Two boons away
        
        return min(score, 60)  # Cap at 60
    
    def _check_legendary_potential(self, god: str) -> int:
        """Check legendary boon potential."""
        score = 0
        
        for leg in LEGENDARY_BOONS_DATA:
            if leg['god'] == god:
                prereqs_needed = [b for _, b in leg['prerequisites'] if b not in self.acquired_boons]
                
                if len(prereqs_needed) <= 1:
                    score += 30
        
        return score
    
    def _rooms_until_boss(self) -> int:
        """Calculate rooms until next boss."""
        region_boss_rooms = {
            "Tartarus": 14,
            "Asphodel": 24,
            "Elysium": 36,
            "Temple of Styx": 45
        }
        
        boss_room = region_boss_rooms.get(self.current_region, 14)
        return max(0, boss_room - self.room_number)
    
    def _get_recommendation(self, score: int) -> str:
        """Get text recommendation based on score."""
        if score >= 90:
            return "✅ TAKE THIS NOW"
        elif score >= 75:
            return "✅ Excellent choice"
        elif score >= 60:
            return "👍 Strong option"
        elif score >= 40:
            return "🤔 Consider it"
        elif score >= 25:
            return "😐 Meh, if nothing better"
        else:
            return "❌ Skip if possible"
    
    def compare_doors(self, doors: List[Tuple[str, str]]) -> List[Dict]:
        """Compare multiple doors and rank them.
        doors: [(god/type, reward_type), ...]
        """
        results = []
        
        for god_or_type, reward_type in doors:
            analysis = self.analyze_door(god_or_type, reward_type)
            analysis['god_or_type'] = god_or_type
            analysis['reward_type'] = reward_type
            results.append(analysis)
        
        # Sort by score (highest first)
        results.sort(key=lambda x: x['score'], reverse=True)
        
        return results
