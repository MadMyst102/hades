"""
heat_management.py - Advanced Heat Strategy System
"""

from typing import Dict

class HeatManagementSystem:
    """32+ heat optimization and strategy."""
    
    def __init__(self):
        pass
    
    def generate_heat_strategy(self, target_heat: int, weapon: str, 
                               aspect: str, playstyle: str) -> Dict:
        """Generate optimal heat configuration."""
        
        if target_heat <= 8:
            return self.generate_low_heat_strategy(target_heat)
        elif target_heat <= 16:
            return self.generate_medium_heat_strategy(target_heat)
        else:
            return self.generate_high_heat_strategy(target_heat)
    
    def generate_low_heat_strategy(self, target_heat: int) -> Dict:
        """0-8 heat strategy."""
        return {
            'config': {
                'Hard Labor': min(5, target_heat),
                'Lasting Consequences': max(0, target_heat - 5)
            },
            'total_heat': target_heat,
            'reasoning': [],
            'difficulty': 'EASY',
            'tips': [
                "Perfect for learning",
                "Focus on core mechanics"
            ]
        }
    
    def generate_medium_heat_strategy(self, target_heat: int) -> Dict:
        """9-16 heat strategy."""
        return {
            'config': {
                'Hard Labor': 5,
                'Lasting Consequences': 3,
                'Convenience Fee': 2,
                'Jury Summons': min(3, target_heat - 10),
                'Middle Management': 1 if target_heat >= 12 else 0
            },
            'total_heat': target_heat,
            'reasoning': [],
            'difficulty': 'MEDIUM',
            'tips': [
                "⚔️ Play aggressively",
                "🛡️ Get defensive boons"
            ]
        }
    
    def generate_high_heat_strategy(self, target_heat: int) -> Dict:
        """17-32 heat strategy."""
        return {
            'config': {
                'Hard Labor': 5,
                'Lasting Consequences': 4,
                'Convenience Fee': 2,
                'Jury Summons': 3,
                'Middle Management': 1,
                'Extreme Measures': min(4, target_heat - 20)
            },
            'total_heat': target_heat,
            'reasoning': [],
            'difficulty': 'HARD',
            'tips': [
                "💀 Expert only",
                "🌟 Duo boons mandatory",
                "🛡️ Must have defensive dash"
            ]
        }
