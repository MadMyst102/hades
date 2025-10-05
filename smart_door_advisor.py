"""
smart_door_advisor.py - Contextual Room Choice Intelligence
"""

from typing import Dict, List
from enum import Enum

class RoomType(Enum):
    """All Hades room types."""
    GOD_BOON = "god"
    POM_OF_POWER = "pom"
    CENTAUR_HEART = "heart"
    CHARON_SHOP = "shop"
    GOLD = "gold"
    CHAOS = "chaos"
    EREBUS = "erebus"
    TRIAL = "trial"
    FOUNTAIN = "fountain"
    HAMMER = "hammer"
    HERMES = "hermes"

class SmartDoorAdvisor:
    """Intelligent contextual room recommendations."""
    
    def __init__(self):
        pass
    
    def analyze_door_choices(self, build_state: Dict, available_doors: List[str]) -> List[Dict]:
        """Analyze all door choices and rank them."""
        
        recommendations = []
        
        for door_type in available_doors:
            analysis = self.analyze_single_door(door_type, build_state)
            recommendations.append(analysis)
        
        recommendations.sort(key=lambda x: x['score'], reverse=True)
        return recommendations
    
    def analyze_single_door(self, door_type: str, build_state: Dict) -> Dict:
        """Analyze a single door choice."""
        
        boons = build_state.get('boons', set())
        hp_percent = build_state.get('hp_percent', 1.0)
        
        score = 50
        reasoning = []
        urgency = "NORMAL"
        
        if door_type == RoomType.GOD_BOON.value:
            score = 70
            if len(boons) < 3:
                score += 30
                reasoning.append("🎯 Early game - need core boons")
                urgency = "HIGH"
        
        elif door_type == RoomType.CENTAUR_HEART.value:
            score = 40
            if hp_percent < 0.4:
                score += 60
                reasoning.append("🚨 CRITICAL - Low HP!")
                urgency = "CRITICAL"
        
        elif door_type == RoomType.HAMMER.value:
            score = 75
            reasoning.append("🔨 DAEDALUS HAMMER - Game changer!")
            urgency = "CRITICAL"
        
        else:
            reasoning.append("Standard room")
        
        return {
            'type': door_type,
            'score': score,
            'reasoning': reasoning,
            'urgency': urgency,
            'recommendation': self.get_recommendation_text(score, urgency)
        }
    
    def get_recommendation_text(self, score: int, urgency: str) -> str:
        """Get recommendation text."""
        if urgency == "CRITICAL":
            return "🔥 TAKE THIS"
        elif urgency == "HIGH":
            return "⭐ RECOMMENDED"
        elif score >= 70:
            return "✅ GOOD CHOICE"
        else:
            return "💫 CONSIDER"
