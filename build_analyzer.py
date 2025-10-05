"""
Build Analyzer - Boss prep, Pom priority, Chaos calculator, Build strength
"""

from typing import Dict, List, Set
from data import BOON_NAME_TO_DATA, DUO_BOONS_DATA, LEGENDARY_BOONS_DATA


class BuildAnalyzer:
    """Analyzes build strength and provides strategic recommendations."""
    
    def __init__(self):
        self.acquired_boons = set()
        self.selected_gods = set()
        self.pom_levels = {}
        self.hammer_count = 0
        self.weapon = None
        self.current_health = 100
        self.max_health = 100
        self.room_number = 1
        self.region = "Tartarus"
        
    def set_state(self, boons: Set[str], gods: Set[str], poms: Dict, hammers: int, 
                  weapon: str, hp: int, max_hp: int, room: int, region: str):
        """Update analyzer state."""
        self.acquired_boons = boons
        self.selected_gods = gods
        self.pom_levels = poms
        self.hammer_count = hammers
        self.weapon = weapon
        self.current_health = hp
        self.max_health = max_hp
        self.room_number = room
        self.region = region
    
    def calculate_build_strength(self) -> Dict:
        """Calculate overall build strength (0-100)."""
        strength = {
            'total': 0,
            'offense': 0,
            'defense': 0,
            'utility': 0,
            'consistency': 0,
            'rating': '',
            'breakdown': []
        }
        
        # === OFFENSE (40 points) ===
        offense = 0
        
        has_attack = any('Strike' in b for b in self.acquired_boons)
        has_special = any('Flourish' in b for b in self.acquired_boons)
        has_cast = any('Shot' in b or 'Cast' in b for b in self.acquired_boons)
        
        if has_attack:
            offense += 12
            strength['breakdown'].append("✅ Attack boon")
        else:
            strength['breakdown'].append("❌ Missing attack boon")
        
        if has_special:
            offense += 10
            strength['breakdown'].append("✅ Special boon")
        
        if has_cast:
            offense += 8
        
        if self.hammer_count >= 1:
            offense += 5
            strength['breakdown'].append(f"✅ {self.hammer_count} Hammer(s)")
        else:
            strength['breakdown'].append("❌ No Daedalus Hammer")
        
        duo_count = self._count_duo_boons()
        legendary_count = self._count_legendary_boons()
        
        offense += duo_count * 3
        offense += legendary_count * 2
        
        if duo_count > 0:
            strength['breakdown'].append(f"✅ {duo_count} Duo boon(s)")
        
        strength['offense'] = min(offense, 40)
        
        # === DEFENSE (25 points) ===
        defense = 0
        
        has_dash = any('Dash' in b for b in self.acquired_boons)
        has_call = any('Aid' in b or 'Call' in b for b in self.acquired_boons)
        
        if has_dash:
            defense += 8
            strength['breakdown'].append("✅ Dash boon")
        else:
            strength['breakdown'].append("❌ No dash boon")
        
        if has_call:
            defense += 7
            strength['breakdown'].append("✅ Call boon")
        
        hp_percent = (self.current_health / self.max_health) * 100 if self.max_health > 0 else 0
        if hp_percent >= 80:
            defense += 10
        elif hp_percent >= 60:
            defense += 7
        elif hp_percent >= 40:
            defense += 4
        else:
            defense += 2
            strength['breakdown'].append("⚠️ Low health!")
        
        strength['defense'] = min(defense, 25)
        
        # === UTILITY (20 points) ===
        utility = 0
        
        god_count = len(self.selected_gods)
        utility += min(god_count * 3, 12)
        
        boon_count = len(self.acquired_boons)
        utility += min(boon_count, 8)
        
        strength['utility'] = min(utility, 20)
        
        # === CONSISTENCY (15 points) ===
        consistency = 0
        
        avg_pom_level = sum(self.pom_levels.values()) / len(self.pom_levels) if self.pom_levels else 1
        consistency += min(int((avg_pom_level - 1) * 3), 10)
        
        if self._has_good_synergy():
            consistency += 5
            strength['breakdown'].append("✅ Good boon synergy")
        
        strength['consistency'] = min(consistency, 15)
        
        # === TOTAL ===
        strength['total'] = strength['offense'] + strength['defense'] + strength['utility'] + strength['consistency']
        
        if strength['total'] >= 85:
            strength['rating'] = "🔥 Godlike"
            strength['color'] = "#FFD700"
        elif strength['total'] >= 70:
            strength['rating'] = "⭐ Excellent"
            strength['color'] = "#00FF00"
        elif strength['total'] >= 55:
            strength['rating'] = "✨ Strong"
            strength['color'] = "#90EE90"
        elif strength['total'] >= 40:
            strength['rating'] = "💫 Decent"
            strength['color'] = "#FFA500"
        else:
            strength['rating'] = "📊 Developing"
            strength['color'] = "#808080"
        
        return strength
    
    def boss_preparation_check(self) -> Dict:
        """Check if ready for upcoming boss."""
        boss_info = {
            'boss_name': '',
            'rooms_until': 0,
            'ready': False,
            'readiness': 0,
            'warnings': [],
            'recommendations': []
        }
        
        boss_rooms = {
            'Tartarus': (14, 'Megaera'),
            'Asphodel': (24, 'Bone Hydra'),
            'Elysium': (36, 'Theseus & Asterius'),
            'Temple of Styx': (45, 'Hades')
        }
        
        if self.region not in boss_rooms:
            return boss_info
        
        boss_room, boss_name = boss_rooms[self.region]
        rooms_until = max(0, boss_room - self.room_number)
        
        boss_info['boss_name'] = boss_name
        boss_info['rooms_until'] = rooms_until
        
        if rooms_until > 3:
            return boss_info
        
        readiness = 0
        
        hp_percent = (self.current_health / self.max_health) * 100 if self.max_health > 0 else 0
        if hp_percent >= 80:
            readiness += 30
        elif hp_percent >= 60:
            readiness += 20
            boss_info['warnings'].append("⚠️ Health could be better")
            boss_info['recommendations'].append("Look for Centaur Heart or Fountain")
        elif hp_percent < 60:
            readiness += 10
            boss_info['warnings'].append("🚨 LOW HEALTH - Dangerous!")
            boss_info['recommendations'].append("PRIORITIZE healing before boss")
        
        build_strength = self.calculate_build_strength()
        offense_score = (build_strength['offense'] / 40) * 35
        readiness += offense_score
        
        if build_strength['offense'] < 25:
            boss_info['warnings'].append("⚠️ Low damage output")
            boss_info['recommendations'].append("Get more offensive boons")
        
        defense_score = (build_strength['defense'] / 25) * 25
        readiness += defense_score
        
        if not any('Dash' in b for b in self.acquired_boons):
            boss_info['warnings'].append("⚠️ No defensive dash")
            boss_info['recommendations'].append("Get Athena/Poseidon dash")
        
        if not any('Aid' in b or 'Call' in b for b in self.acquired_boons):
            boss_info['warnings'].append("⚠️ No Call ability")
            boss_info['recommendations'].append("Get a Call for emergency damage")
        
        if len(self.acquired_boons) >= 6:
            readiness += 10
        elif len(self.acquired_boons) >= 4:
            readiness += 7
        else:
            readiness += 4
            boss_info['warnings'].append("⚠️ Need more boons")
        
        boss_info['readiness'] = min(int(readiness), 100)
        boss_info['ready'] = boss_info['readiness'] >= 70
        
        if not boss_info['warnings']:
            boss_info['warnings'].append("✅ Looking good!")
        
        return boss_info
    
    def pom_priority_ranking(self) -> List[Dict]:
        """Rank which boons to upgrade with Pom."""
        priorities = []
        
        for boon_name in self.acquired_boons:
            boon_data = BOON_NAME_TO_DATA.get(boon_name)
            if not boon_data:
                continue
            
            current_level = self.pom_levels.get(boon_name, 1)
            
            if current_level >= 10:
                continue
            
            score = 50
            reasons = []
            
            if 'Strike' in boon_name:
                score += 30
                reasons.append("Core attack damage")
            elif 'Flourish' in boon_name:
                score += 25
                reasons.append("Core special damage")
            elif 'Shot' in boon_name or 'Cast' in boon_name:
                score += 20
                reasons.append("Cast damage")
            
            is_duo_prereq = any(
                boon_name in [b for _, b in duo['prerequisites']]
                for duo in DUO_BOONS_DATA
            )
            if is_duo_prereq:
                score += 15
                reasons.append("Enables duo boon")
            
            if current_level <= 3:
                score += 15
                reasons.append("Low level - big gains")
            elif current_level <= 6:
                score += 8
            
            tier = boon_data.get('tier', 'B')
            if tier == 'S':
                score += 10
            elif tier == 'A':
                score += 5
            
            priorities.append({
                'boon': boon_name,
                'current_level': current_level,
                'score': score,
                'reasons': reasons,
                'god': boon_data['god']
            })
        
        priorities.sort(key=lambda x: x['score'], reverse=True)
        return priorities
    
    def chaos_gate_risk_assessment(self, curse_description: str, blessing_description: str) -> Dict:
        """Assess risk/reward of Chaos gate."""
        assessment = {
            'risk_level': 'MEDIUM',
            'should_take': True,
            'risk_score': 50,
            'warnings': [],
            'benefits': [],
            'recommendation': ''
        }
        
        risk = 0
        
        hp_percent = (self.current_health / self.max_health) * 100 if self.max_health > 0 else 0
        if hp_percent < 40:
            risk += 40
            assessment['warnings'].append("🚨 VERY LOW HP - High risk!")
        elif hp_percent < 60:
            risk += 25
            assessment['warnings'].append("⚠️ Low HP - Risky")
        elif hp_percent < 80:
            risk += 10
        
        boss_rooms = {'Tartarus': 14, 'Asphodel': 24, 'Elysium': 36, 'Temple of Styx': 45}
        boss_room = boss_rooms.get(self.region, 14)
        rooms_until_boss = boss_room - self.room_number
        
        if rooms_until_boss <= 2:
            risk += 35
            assessment['warnings'].append("🚨 BOSS VERY CLOSE - Avoid curse!")
        elif rooms_until_boss <= 4:
            risk += 20
            assessment['warnings'].append("⚠️ Boss approaching soon")
        elif rooms_until_boss <= 6:
            risk += 10
        
        build_strength = self.calculate_build_strength()
        if build_strength['total'] < 40:
            risk += 15
            assessment['warnings'].append("⚠️ Weak build - curse hurts more")
        
        curse_lower = curse_description.lower()
        high_risk_curses = ['damage', 'hp', 'health', 'move speed', 'attack speed']
        
        if any(keyword in curse_lower for keyword in high_risk_curses):
            risk += 15
            assessment['warnings'].append("Curse affects critical stats")
        
        assessment['risk_score'] = min(risk, 100)
        
        if risk >= 70:
            assessment['risk_level'] = "🔴 EXTREME"
            assessment['should_take'] = False
            assessment['recommendation'] = "❌ SKIP - Too risky!"
        elif risk >= 50:
            assessment['risk_level'] = "🟠 HIGH"
            assessment['should_take'] = False
            assessment['recommendation'] = "⚠️ NOT RECOMMENDED"
        elif risk >= 30:
            assessment['risk_level'] = "🟡 MEDIUM"
            assessment['should_take'] = True
            assessment['recommendation'] = "🤔 Your choice - manageable risk"
        else:
            assessment['risk_level'] = "🟢 LOW"
            assessment['should_take'] = True
            assessment['recommendation'] = "✅ SAFE TO TAKE"
        
        assessment['benefits'].append("Chaos boons are very powerful")
        assessment['benefits'].append("Curse only lasts 3-5 rooms")
        if rooms_until_boss > 5:
            assessment['benefits'].append("Curse will wear off before boss")
        
        return assessment
    
    def _count_duo_boons(self) -> int:
        """Count acquired duo boons."""
        count = 0
        for duo in DUO_BOONS_DATA:
            if all(g in self.selected_gods for g in duo['gods']):
                prereqs_met = all(b in self.acquired_boons for _, b in duo['prerequisites'])
                if prereqs_met:
                    count += 1
        return count
    
    def _count_legendary_boons(self) -> int:
        """Count acquired legendary boons."""
        count = 0
        for leg in LEGENDARY_BOONS_DATA:
            if leg['god'] in self.selected_gods:
                prereqs_met = all(b in self.acquired_boons for _, b in leg['prerequisites'])
                if prereqs_met:
                    count += 1
        return count
    
    def _has_good_synergy(self) -> bool:
        """Check if build has good synergy."""
        gods = list(self.selected_gods)
        
        if 'Zeus' in gods and 'Poseidon' in gods:
            return True
        if 'Artemis' in gods and 'Aphrodite' in gods:
            return True
        if 'Ares' in gods and 'Athena' in gods:
            return True
        
        for god in gods:
            has_attack = any(b for b in self.acquired_boons 
                           if BOON_NAME_TO_DATA.get(b, {}).get('god') == god and 'Strike' in b)
            has_special = any(b for b in self.acquired_boons 
                            if BOON_NAME_TO_DATA.get(b, {}).get('god') == god and 'Flourish' in b)
            if has_attack and has_special:
                return True
        
        return False
