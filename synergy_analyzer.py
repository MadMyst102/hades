"""
Boon synergy analysis system
"""

from typing import List, Dict, Set
from data import DUO_BOONS_DATA, BOON_NAME_TO_DATA

class SynergyAnalyzer:
    """Analyzes boon synergies and anti-synergies."""
    
    def __init__(self):
        # Define synergy rules
        self.synergies = {
            # Ares synergies
            "Curse of Agony": {
                "strong": ["Zeus boons (Vengeful Mood)", "Athena boons (Merciful End)", "Aphrodite boons (Curse of Longing)"],
                "weak": ["Poseidon knockback (interrupts Doom)"]
            },
            "Slicing Shot": {
                "strong": ["Artemis boons (Hunting Blades)", "Ares boons (Blade Dash)"],
                "weak": []
            },
            
            # Zeus synergies
            "Lightning Strike": {
                "strong": ["Poseidon boons (Sea Storm)", "Dionysus boons (Scintillating Feast)", "Artemis boons (Lightning Rod)"],
                "weak": []
            },
            "Thunder Flourish": {
                "strong": ["Aphrodite boons (Smoldering Air)", "Demeter boons (Cold Fusion)"],
                "weak": []
            },
            
            # Aphrodite synergies
            "Heartbreak Strike": {
                "strong": ["Artemis boons (Heart Rend)", "Zeus boons (Smoldering Air)", "Weak effects"],
                "weak": []
            },
            "Heartbreak Flourish": {
                "strong": ["Artemis boons (Heart Rend)", "Weak synergies"],
                "weak": []
            },
            
            # Artemis synergies
            "Deadly Strike": {
                "strong": ["Aphrodite boons (Heart Rend)", "Pressure Points", "Support Fire"],
                "weak": []
            },
            "Deadly Flourish": {
                "strong": ["Aphrodite boons (Heart Rend)", "Hunter's Mark"],
                "weak": []
            },
            
            # Poseidon synergies
            "Tempest Strike": {
                "strong": ["Zeus boons (Sea Storm)", "Rupture synergy", "Typhoon's Fury"],
                "weak": ["Doom effects (knockback interrupts)"]
            },
            "Tidal Dash": {
                "strong": ["Zeus boons (Sea Storm)", "Rupture synergy"],
                "weak": ["Doom effects (knockback interrupts)"]
            },
            
            # Dionysus synergies
            "Drunken Strike": {
                "strong": ["Hangover stacking", "Zeus boons (Scintillating Feast)", "Demeter boons (Ice Wine)"],
                "weak": []
            },
            
            # Demeter synergies
            "Frost Strike": {
                "strong": ["Zeus boons (Cold Fusion)", "Chill stacking", "Arctic Blast"],
                "weak": []
            },
            
            # Athena synergies
            "Divine Strike": {
                "strong": ["Ares boons (Merciful End)", "Deflect builds", "Holy Shield"],
                "weak": []
            },
            "Divine Dash": {
                "strong": ["Most builds (best dash)", "Merciful End", "Deathless Stand"],
                "weak": []
            }
        }
    
    def analyze_boon(self, boon_name: str, acquired_boons: Set[str], selected_gods: Set[str]) -> Dict:
        """Analyze synergies for a specific boon."""
        result = {
            'synergies': [],
            'potential_duos': [],
            'anti_synergies': [],
            'synergy_score': 0
        }
        
        # Get synergy data
        if boon_name in self.synergies:
            syn_data = self.synergies[boon_name]
            result['synergies'] = syn_data.get('strong', [])
            result['anti_synergies'] = syn_data.get('weak', [])
        
        # Check duo potential
        boon_data = BOON_NAME_TO_DATA.get(boon_name)
        if boon_data:
            boon_god = boon_data['god']
            
            for duo in DUO_BOONS_DATA:
                if boon_god in duo['gods']:
                    # Check if this boon is part of the duo prerequisites
                    for prereq_god, prereq_boon in duo['prerequisites']:
                        if prereq_boon == boon_name:
                            # Check if we have the other god
                            other_gods = [g for g in duo['gods'] if g != boon_god]
                            if any(g in selected_gods for g in other_gods):
                                result['potential_duos'].append({
                                    'name': duo['name'],
                                    'other_god': other_gods[0] if other_gods else None,
                                    'still_needed': [b for _, b in duo['prerequisites'] if b not in acquired_boons]
                                })
        
        # Calculate synergy score
        score = 0
        score += len(result['synergies']) * 10
        score += len(result['potential_duos']) * 25
        score -= len(result['anti_synergies']) * 15
        
        result['synergy_score'] = max(0, score)
        
        return result
    
    def get_duo_progress(self, acquired_boons: Set[str], selected_gods: Set[str]) -> List[Dict]:
        """Get progress toward all possible duo boons."""
        duos = []
        
        for duo in DUO_BOONS_DATA:
            # Check if we have both required gods
            if all(g in selected_gods for g in duo['gods']):
                prereq_list = [b for _, b in duo['prerequisites']]
                acquired_prereqs = [b for b in prereq_list if b in acquired_boons]
                needed = [b for b in prereq_list if b not in acquired_boons]
                
                progress = (len(acquired_prereqs) / len(prereq_list)) * 100
                
                duos.append({
                    'name': duo['name'],
                    'gods': duo['gods'],
                    'description': duo.get('description', ''),
                    'progress': progress,
                    'acquired': acquired_prereqs,
                    'needed': needed,
                    'ready': len(needed) == 0
                })
        
        # Sort by progress
        duos.sort(key=lambda x: x['progress'], reverse=True)
        return duos
