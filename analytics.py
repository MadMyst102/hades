"""
Hades Build Helper - Analytics Module
Handles run history tracking, statistics calculation, and data persistence.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict


class RunAnalytics:
    """
    Manages run history, calculates statistics, and handles data persistence.
    """
    
    RUNS_FILE = "hades_runs_history.json"
    
    def __init__(self):
        self.runs: List[Dict[str, Any]] = []
        self.load_runs()
    
    # === DATA PERSISTENCE ===
    
    def load_runs(self) -> None:
        """Load run history from JSON file."""
        if os.path.exists(self.RUNS_FILE):
            try:
                with open(self.RUNS_FILE, 'r', encoding='utf-8') as f:
                    self.runs = json.load(f)
                print(f"✓ Loaded {len(self.runs)} runs from history")
            except Exception as e:
                print(f"⚠ Error loading runs: {e}")
                self.runs = []
        else:
            self.runs = []
            print("ℹ No run history found, starting fresh")
    
    def save_runs(self) -> None:
        """Save run history to JSON file."""
        try:
            with open(self.RUNS_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.runs, f, indent=2, ensure_ascii=False)
            print(f"✓ Saved {len(self.runs)} runs to history")
        except Exception as e:
            print(f"⚠ Error saving runs: {e}")
    
    def add_run(self, run_data: Dict[str, Any]) -> int:
        """
        Add a new run to history.
        
        Args:
            run_data: Dictionary containing run information
            
        Returns:
            Run number of the added run
        """
        run_data['timestamp'] = datetime.now().isoformat()
        run_data['run_number'] = len(self.runs) + 1
        run_data['date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        self.runs.append(run_data)
        self.save_runs()
        
        return run_data['run_number']
    
    def export_data(self, filepath: str) -> bool:
        """Export run data to custom location."""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.runs, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Export failed: {e}")
            return False
    
    def import_data(self, filepath: str) -> bool:
        """Import run data from file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                imported_runs = json.load(f)
            self.runs.extend(imported_runs)
            self.save_runs()
            return True
        except Exception as e:
            print(f"Import failed: {e}")
            return False
    
    def clear_all_runs(self) -> None:
        """Clear all run history (with confirmation in GUI)."""
        self.runs = []
        self.save_runs()
    
    # === BASIC STATISTICS ===
    
    def get_total_runs(self) -> int:
        """Get total number of runs recorded."""
        return len(self.runs)
    
    def get_wins(self) -> int:
        """Get total number of victories."""
        return sum(1 for run in self.runs if run.get('victory', False))
    
    def get_defeats(self) -> int:
        """Get total number of defeats."""
        return self.get_total_runs() - self.get_wins()
    
    def get_win_rate(self) -> float:
        """Calculate overall win rate percentage."""
        total = self.get_total_runs()
        if total == 0:
            return 0.0
        return (self.get_wins() / total) * 100
    
    def get_avg_build_score(self) -> float:
        """Get average build score across all runs."""
        if not self.runs:
            return 0.0
        total_score = sum(run.get('build_score', 0) for run in self.runs)
        return total_score / len(self.runs)
    
    def get_avg_heat_level(self) -> float:
        """Get average heat level attempted."""
        if not self.runs:
            return 0.0
        total_heat = sum(run.get('heat_level', 0) for run in self.runs)
        return total_heat / len(self.runs)
    
    # === WEAPON STATISTICS ===
    
    def get_weapon_stats(self) -> Dict[str, Dict[str, Any]]:
        """
        Get detailed statistics by weapon.
        
        Returns:
            Dictionary with weapon names as keys and stats as values
        """
        weapon_stats = defaultdict(lambda: {
            'runs': 0,
            'wins': 0,
            'defeats': 0,
            'win_rate': 0.0,
            'avg_score': 0.0,
            'total_score': 0,
            'avg_heat': 0.0,
            'total_heat': 0,
            'best_score': 0,
            'aspects_used': defaultdict(int)
        })
        
        for run in self.runs:
            weapon = run.get('weapon', 'Unknown')
            aspect = run.get('aspect', 'Unknown')
            
            stats = weapon_stats[weapon]
            stats['runs'] += 1
            stats['total_score'] += run.get('build_score', 0)
            stats['total_heat'] += run.get('heat_level', 0)
            stats['aspects_used'][aspect] += 1
            
            if run.get('victory', False):
                stats['wins'] += 1
            else:
                stats['defeats'] += 1
            
            if run.get('build_score', 0) > stats['best_score']:
                stats['best_score'] = run.get('build_score', 0)
        
        # Calculate averages and percentages
        for weapon, stats in weapon_stats.items():
            if stats['runs'] > 0:
                stats['win_rate'] = (stats['wins'] / stats['runs']) * 100
                stats['avg_score'] = stats['total_score'] / stats['runs']
                stats['avg_heat'] = stats['total_heat'] / stats['runs']
        
        return dict(weapon_stats)
    
    def get_best_weapon(self) -> Optional[Tuple[str, float]]:
        """Get weapon with highest win rate (minimum 3 runs)."""
        weapon_stats = self.get_weapon_stats()
        qualified = {w: s for w, s in weapon_stats.items() if s['runs'] >= 3}
        
        if not qualified:
            return None
        
        best = max(qualified.items(), key=lambda x: x[1]['win_rate'])
        return (best[0], best[1]['win_rate'])
    
    # === GOD STATISTICS ===
    
    def get_god_stats(self) -> Dict[str, Dict[str, Any]]:
        """
        Get detailed statistics by god.
        
        Returns:
            Dictionary with god names as keys and stats as values
        """
        god_stats = defaultdict(lambda: {
            'runs': 0,
            'wins': 0,
            'defeats': 0,
            'win_rate': 0.0,
            'avg_score': 0.0,
            'total_score': 0
        })
        
        for run in self.runs:
            gods = run.get('gods', [])
            victory = run.get('victory', False)
            score = run.get('build_score', 0)
            
            for god in gods:
                stats = god_stats[god]
                stats['runs'] += 1
                stats['total_score'] += score
                
                if victory:
                    stats['wins'] += 1
                else:
                    stats['defeats'] += 1
        
        # Calculate percentages
        for god, stats in god_stats.items():
            if stats['runs'] > 0:
                stats['win_rate'] = (stats['wins'] / stats['runs']) * 100
                stats['avg_score'] = stats['total_score'] / stats['runs']
        
        return dict(god_stats)
    
    def get_god_combo_stats(self, min_runs: int = 2) -> List[Tuple[str, int, int, float]]:
        """
        Get statistics for god combinations.
        
        Args:
            min_runs: Minimum number of runs to include combo
            
        Returns:
            List of tuples: (combo_string, runs, wins, win_rate)
        """
        combo_stats = defaultdict(lambda: {'runs': 0, 'wins': 0})
        
        for run in self.runs:
            gods = sorted(run.get('gods', []))
            if len(gods) >= 2:
                combo = " + ".join(gods[:3])  # Limit to top 3 gods
                combo_stats[combo]['runs'] += 1
                if run.get('victory', False):
                    combo_stats[combo]['wins'] += 1
        
        # Filter by minimum runs and convert to list
        combo_list = []
        for combo, stats in combo_stats.items():
            if stats['runs'] >= min_runs:
                win_rate = (stats['wins'] / stats['runs'] * 100) if stats['runs'] > 0 else 0
                combo_list.append((combo, stats['runs'], stats['wins'], win_rate))
        
        # Sort by win rate, then runs
        combo_list.sort(key=lambda x: (x[3], x[1]), reverse=True)
        return combo_list
    
    # === BOON STATISTICS ===
    
    def get_most_used_boons(self, limit: int = 10) -> List[Tuple[str, int]]:
        """Get most frequently used boons."""
        boon_counter = defaultdict(int)
        
        for run in self.runs:
            for boon in run.get('boons', []):
                boon_counter[boon] += 1
        
        sorted_boons = sorted(boon_counter.items(), key=lambda x: x[1], reverse=True)
        return sorted_boons[:limit]
    
    def get_boon_win_rates(self) -> Dict[str, float]:
        """Calculate win rates for boons used."""
        boon_stats = defaultdict(lambda: {'runs': 0, 'wins': 0})
        
        for run in self.runs:
            victory = run.get('victory', False)
            for boon in run.get('boons', []):
                boon_stats[boon]['runs'] += 1
                if victory:
                    boon_stats[boon]['wins'] += 1
        
        win_rates = {}
        for boon, stats in boon_stats.items():
            if stats['runs'] >= 3:  # Minimum 3 uses
                win_rates[boon] = (stats['wins'] / stats['runs']) * 100
        
        return win_rates
    
    # === RUN QUERIES ===
    
    def get_recent_runs(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get most recent runs."""
        return list(reversed(self.runs[-limit:]))
    
    def get_best_run(self) -> Optional[Dict[str, Any]]:
        """Get run with highest build score."""
        if not self.runs:
            return None
        return max(self.runs, key=lambda r: r.get('build_score', 0))
    
    def get_runs_by_weapon(self, weapon: str) -> List[Dict[str, Any]]:
        """Get all runs with specific weapon."""
        return [r for r in self.runs if r.get('weapon') == weapon]
    
    def get_runs_by_god(self, god: str) -> List[Dict[str, Any]]:
        """Get all runs that included specific god."""
        return [r for r in self.runs if god in r.get('gods', [])]
    
    def get_victory_runs(self) -> List[Dict[str, Any]]:
        """Get all victorious runs."""
        return [r for r in self.runs if r.get('victory', False)]
    
    # === PROGRESSION TRACKING ===
    
    def get_streak_data(self) -> Dict[str, int]:
        """Calculate current and best win/loss streaks."""
        if not self.runs:
            return {'current_streak': 0, 'best_win_streak': 0, 'worst_loss_streak': 0}
        
        current_streak = 0
        best_win_streak = 0
        worst_loss_streak = 0
        temp_win_streak = 0
        temp_loss_streak = 0
        
        for run in reversed(self.runs):
            if run.get('victory', False):
                temp_win_streak += 1
                temp_loss_streak = 0
                current_streak = temp_win_streak
            else:
                temp_loss_streak += 1
                temp_win_streak = 0
                current_streak = -temp_loss_streak
            
            best_win_streak = max(best_win_streak, temp_win_streak)
            worst_loss_streak = max(worst_loss_streak, temp_loss_streak)
        
        return {
            'current_streak': current_streak,
            'best_win_streak': best_win_streak,
            'worst_loss_streak': worst_loss_streak
        }
    
    def get_progression_summary(self) -> Dict[str, Any]:
        """Get overall progression summary."""
        return {
            'total_runs': self.get_total_runs(),
            'victories': self.get_wins(),
            'defeats': self.get_defeats(),
            'win_rate': self.get_win_rate(),
            'avg_build_score': self.get_avg_build_score(),
            'avg_heat': self.get_avg_heat_level(),
            'best_run': self.get_best_run(),
            'best_weapon': self.get_best_weapon(),
            'streak_data': self.get_streak_data()
        }
# Add to imports at top
from room_tracker import RunTracker

# Add to RunAnalytics class:

def add_run_with_rooms(self, run_data: Dict[str, Any], run_tracker: RunTracker):
    """Add run with complete room-by-room data."""
    run_data['room_progression'] = run_tracker.to_dict()
    return self.add_run(run_data)

def get_room_statistics(self) -> Dict[str, Any]:
    """Get statistics about room choices across all runs."""
    total_rooms = 0
    reward_choices = {}
    god_encounter_frequency = {}
    reroll_usage = 0
    
    for run in self.runs:
        room_prog = run.get('room_progression', {})
        rooms = room_prog.get('rooms', [])
        
        total_rooms += len(rooms)
        
        for room in rooms:
            # Track reward choices
            if room.get('reward_chosen'):
                reward = room['reward_chosen']
                reward_choices[reward] = reward_choices.get(reward, 0) + 1
            
            # Track god encounters
            if room.get('god_chosen'):
                god = room['god_chosen']
                god_encounter_frequency[god] = god_encounter_frequency.get(god, 0) + 1
            
            # Track reroll usage
            if room.get('reroll_used'):
                reroll_usage += 1
    
    return {
        'total_rooms_cleared': total_rooms,
        'reward_preferences': reward_choices,
        'god_encounter_frequency': god_encounter_frequency,
        'reroll_usage': reroll_usage,
        'avg_rooms_per_run': total_rooms / len(self.runs) if self.runs else 0
    }

def get_boon_acquisition_patterns(self) -> Dict[str, List]:
    """Analyze when certain boons are typically acquired."""
    patterns = {}
    
    for run in self.runs:
        room_prog = run.get('room_progression', {})
        timeline = room_prog.get('boon_timeline', [])
        
        for entry in timeline:
            boon = entry['boon']
            room_num = entry['room']
            
            if boon not in patterns:
                patterns[boon] = []
            patterns[boon].append(room_num)
    
    # Calculate average acquisition room
    for boon, rooms in patterns.items():
        avg_room = sum(rooms) / len(rooms)
        patterns[boon] = {
            'times_taken': len(rooms),
            'avg_room_number': avg_room,
            'earliest': min(rooms),
            'latest': max(rooms)
        }
    
    return patterns
