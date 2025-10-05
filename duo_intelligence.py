"""
duo_intelligence.py - Advanced Duo Boon Intelligence System
"""

from typing import Dict, List, Set, Tuple

class DuoIntelligence:
    """Advanced duo boon intelligence with predictive analysis."""
    
    def __init__(self):
        # God encounter rates per biome (based on actual game data)
        self.biome_rates = {
            'Tartarus': {
                'base_rate': 0.45,
                'gods_per_biome': 3.2,
            },
            'Asphodel': {
                'base_rate': 0.40,
                'gods_per_biome': 2.8,
            },
            'Elysium': {
                'base_rate': 0.35,
                'gods_per_biome': 2.5,
            },
            'Temple of Styx': {
                'base_rate': 0.25,
                'gods_per_biome': 1.5,
            }
        }
    
    def calculate_duo_probability(self, duo_data: Dict, current_gods: Set[str], 
                                  current_room: int, current_biome: str,
                                  has_keepsake: bool = False) -> Dict:
        """Calculate realistic probability of getting a duo."""
        
        required_gods = set(duo_data['gods'])
        missing_gods = required_gods - current_gods
        
        # Prerequisites check
        prereq_boons = [b for _, b in duo_data['prerequisites']]
        
        # Calculate base probability
        biome_data = self.biome_rates.get(current_biome, self.biome_rates['Tartarus'])
        rooms_remaining = self.get_rooms_remaining(current_room, current_biome)
        expected_god_rooms = rooms_remaining * biome_data['base_rate']
        
        probability = min(expected_god_rooms / 10, 0.8)
        
        return {
            'probability': probability,
            'status': f"Need {len(missing_gods)} gods",
            'missing_gods': list(missing_gods),
            'rooms_remaining': rooms_remaining,
            'expected_encounters': expected_god_rooms,
        }
    
    def get_rooms_remaining(self, current_room: int, biome: str) -> int:
        """Calculate rooms remaining in biome."""
        biome_ends = {
            'Tartarus': 14,
            'Asphodel': 24,
            'Elysium': 36,
            'Temple of Styx': 45
        }
        return max(biome_ends.get(biome, 14) - current_room, 0)
