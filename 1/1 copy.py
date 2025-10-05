import customtkinter as ctk
from typing import Dict, List, Any, Optional, Set, Tuple
import tkinter.messagebox as tkmb
import json
import os
from datetime import datetime
from collections import defaultdict, Counter

# Set appearance and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# [Previous GODS_DATA, WEAPONS_DATA, BOONS_DATA, DUO_BOONS_DATA, LEGENDARY_BOONS_DATA remain the same]
# ... (Include all the data structures from Phase 1) ...

GODS_DATA: Dict[str, Dict[str, Any]] = {
    "Zeus": {"description": "God of Lightning. Grants boons focused on lightning damage, chain effects, and jolting foes.", "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"], "color": "#FFD700"},
    "Poseidon": {"description": "God of the Sea. Grants boons focused on knockback, rupture, and resource acquisition.", "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"], "color": "#00CED1"},
    "Athena": {"description": "Goddess of Wisdom. Grants boons focused on Deflect, invulnerability, and damage reduction.", "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"], "color": "#DAA520"},
    "Aphrodite": {"description": "Goddess of Love. Grants boons focused on weakening foes and charm effects.", "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"], "color": "#FF69B4"},
    "Ares": {"description": "God of War. Grants boons focused on Blade Rifts, Doom status, and high damage.", "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"], "color": "#DC143C"},
    "Artemis": {"description": "Goddess of the Hunt. Grants boons focused on Critical hits and tracking shots.", "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"], "color": "#32CD32"},
    "Dionysus": {"description": "God of Wine. Grants boons focused on Hangover status, healing, and festive fog.", "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"], "color": "#9370DB"},
    "Hermes": {"description": "God of Speed. Grants boons focused on movement speed, dodge chance, and attack speed.", "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"], "color": "#F0E68C"},
    "Demeter": {"description": "Goddess of Seasons. Grants boons focused on Chill status, slowing foes, and crystal effects.", "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"], "color": "#87CEEB"},
    "Chaos": {"description": "Primordial entity. Grants boons that offer powerful buffs with temporary curses.", "core_boon_types": ["Attack", "Special", "Dash", "Cast", "Call"], "color": "#8B008B"}
}

WEAPONS_DATA: Dict[str, Dict[str, Any]] = {
    "Stygian Blade": {"description": "Fast, balanced melee weapon. Good all-around choice.", "attack_speed": "Fast", "damage_type": "Balanced", "preferred_gods": ["Ares", "Aphrodite", "Zeus"], "focus": "Attack"},
    "Heart-Seeking Bow": {"description": "Ranged weapon with charge shots. Rewards precise timing.", "attack_speed": "Medium", "damage_type": "High Single Hit", "preferred_gods": ["Artemis", "Aphrodite", "Ares"], "focus": "Special"},
    "Shield of Chaos": {"description": "Defensive weapon with blocking and ranged special.", "attack_speed": "Medium", "damage_type": "Balanced", "preferred_gods": ["Zeus", "Dionysus", "Ares"], "focus": "Special"},
    "Eternal Spear": {"description": "Mid-range weapon with spin attack and throw.", "attack_speed": "Fast", "damage_type": "Multi-Hit", "preferred_gods": ["Zeus", "Dionysus", "Artemis"], "focus": "Special"},
    "Twin Fists": {"description": "Extremely fast melee weapon with rapid strikes.", "attack_speed": "Very Fast", "damage_type": "Multi-Hit", "preferred_gods": ["Zeus", "Dionysus", "Demeter"], "focus": "Attack"},
    "Adamant Rail": {"description": "Ranged weapon with rapid fire and special bomb.", "attack_speed": "Very Fast", "damage_type": "Multi-Hit", "preferred_gods": ["Zeus", "Dionysus", "Artemis"], "focus": "Attack"}
}

BOONS_DATA: List[Dict[str, Any]] = [
    {"name": "Lightning Strike", "god": "Zeus", "type": "Attack", "description": "Your Attack deals bonus lightning damage.", "tags": ["attack", "lightning", "damage"], "tier": "S", "weapon_synergy": ["Twin Fists", "Adamant Rail", "Eternal Spear"]},
    {"name": "Thunder Flourish", "god": "Zeus", "type": "Special", "description": "Your Special creates a lightning bolt.", "tags": ["special", "lightning", "damage"], "tier": "S", "weapon_synergy": ["Shield of Chaos", "Eternal Spear"]},
    {"name": "Divine Dash", "god": "Athena", "type": "Dash", "description": "Your Dash makes you Deflect.", "tags": ["dash", "deflect", "utility"], "tier": "S", "weapon_synergy": []},
    {"name": "Heartbreak Strike", "god": "Aphrodite", "type": "Attack", "description": "Your Attack deals bonus damage and inflicts Weak.", "tags": ["attack", "damage", "weak_applier"], "tier": "S", "weapon_synergy": ["Stygian Blade", "Heart-Seeking Bow"]},
    {"name": "Curse of Agony", "god": "Ares", "type": "Attack", "description": "Your Attack inflicts Doom.", "tags": ["attack", "doom_applier"], "tier": "S", "weapon_synergy": ["Stygian Blade", "Heart-Seeking Bow"]},
    {"name": "Deadly Strike", "god": "Artemis", "type": "Attack", "description": "Your Attack has a chance to deal Critical damage.", "tags": ["attack", "crit_chance"], "tier": "A", "weapon_synergy": ["Heart-Seeking Bow", "Stygian Blade"]},
    {"name": "Drunken Strike", "god": "Dionysus", "type": "Attack", "description": "Your Attack inflicts Hangover.", "tags": ["attack", "hangover_applier"], "tier": "S", "weapon_synergy": ["Twin Fists", "Adamant Rail"]},
    {"name": "Frost Strike", "god": "Demeter", "type": "Attack", "description": "Your Attack deals bonus damage and inflicts Chill.", "tags": ["attack", "damage", "chill_applier"], "tier": "A", "weapon_synergy": ["Twin Fists", "Adamant Rail"]},
    {"name": "Tidal Dash", "god": "Poseidon", "type": "Dash", "description": "Your Dash creates a splash that damages foes.", "tags": ["dash", "knockback", "damage"], "tier": "S", "weapon_synergy": ["Stygian Blade"]},
    {"name": "Greater Reflex", "god": "Hermes", "type": "Dash", "description": "Gain +1 Dash.", "tags": ["dash_enhancer", "utility"], "tier": "S", "weapon_synergy": []},
]

DUO_BOONS_DATA: List[Dict[str, Any]] = [
    {"name": "Heart Rend", "gods": ["Artemis", "Aphrodite"], "description": "Your Critical effects deal even more damage to Weak foes.", "prerequisites": [("Artemis", "Deadly Strike"), ("Aphrodite", "Heartbreak Strike")], "tier": "S"},
    {"name": "Splitting Headache", "gods": ["Artemis", "Dionysus"], "description": "Your Hangover effects have a chance to deal Critical damage.", "prerequisites": [("Artemis", "Deadly Strike"), ("Dionysus", "Drunken Strike")], "tier": "S"},
    {"name": "Sea Storm", "gods": ["Zeus", "Poseidon"], "description": "Your knockback effects trigger lightning strikes.", "prerequisites": [("Zeus", "Lightning Strike"), ("Poseidon", "Tidal Dash")], "tier": "S"},
]

LEGENDARY_BOONS_DATA: List[Dict[str, Any]] = [
    {"name": "Greatest Reflex", "god": "Hermes", "description": "Gain +2 Dashes.", "prerequisites": [("Hermes", "Greater Reflex")], "tier": "S"},
]

BOON_NAME_TO_DATA: Dict[str, Dict[str, Any]] = {boon['name']: boon for boon in BOONS_DATA}

TIER_COLORS = {"S": "#FF4444", "A": "#FFD700", "B": "#87CEEB", "C": "#90EE90", "D": "#A0A0A0"}

# Analytics Data Structure
RUNS_FILE = "hades_runs_history.json"


class RunAnalytics:
    """Handle all run tracking and analytics"""
    
    def __init__(self):
        self.runs: List[Dict[str, Any]] = []
        self.load_runs()
    
    def load_runs(self):
        """Load run history from JSON file"""
        if os.path.exists(RUNS_FILE):
            try:
                with open(RUNS_FILE, 'r') as f:
                    self.runs = json.load(f)
            except Exception as e:
                print(f"Error loading runs: {e}")
                self.runs = []
        else:
            self.runs = []
    
    def save_runs(self):
        """Save run history to JSON file"""
        try:
            with open(RUNS_FILE, 'w') as f:
                json.dump(self.runs, f, indent=2)
        except Exception as e:
            print(f"Error saving runs: {e}")
    
    def add_run(self, run_data: Dict[str, Any]):
        """Add a new run to history"""
        run_data['timestamp'] = datetime.now().isoformat()
        run_data['run_number'] = len(self.runs) + 1
        self.runs.append(run_data)
        self.save_runs()
    
    def get_total_runs(self) -> int:
        """Get total number of runs"""
        return len(self.runs)
    
    def get_wins(self) -> int:
        """Get total victories"""
        return sum(1 for run in self.runs if run.get('victory', False))
    
    def get_win_rate(self) -> float:
        """Calculate overall win rate"""
        total = self.get_total_runs()
        if total == 0:
            return 0.0
        return (self.get_wins() / total) * 100
    
    def get_weapon_stats(self) -> Dict[str, Dict[str, Any]]:
        """Get statistics by weapon"""
        weapon_stats = defaultdict(lambda: {'runs': 0, 'wins': 0, 'avg_score': 0, 'total_score': 0})
        
        for run in self.runs:
            weapon = run.get('weapon', 'Unknown')
            weapon_stats[weapon]['runs'] += 1
            if run.get('victory', False):
                weapon_stats[weapon]['wins'] += 1
            weapon_stats[weapon]['total_score'] += run.get('build_score', 0)
        
        # Calculate averages and win rates
        for weapon, stats in weapon_stats.items():
            stats['win_rate'] = (stats['wins'] / stats['runs'] * 100) if stats['runs'] > 0 else 0
            stats['avg_score'] = (stats['total_score'] / stats['runs']) if stats['runs'] > 0 else 0
        
        return dict(weapon_stats)
    
    def get_god_stats(self) -> Dict[str, Dict[str, Any]]:
        """Get statistics by god usage"""
        god_stats = defaultdict(lambda: {'runs': 0, 'wins': 0})
        
        for run in self.runs:
            gods = run.get('gods', [])
            victory = run.get('victory', False)
            for god in gods:
                god_stats[god]['runs'] += 1
                if victory:
                    god_stats[god]['wins'] += 1
        
        # Calculate win rates
        for god, stats in god_stats.items():
            stats['win_rate'] = (stats['wins'] / stats['runs'] * 100) if stats['runs'] > 0 else 0
        
        return dict(god_stats)
    
    def get_god_combo_stats(self) -> List[Tuple[str, int, int, float]]:
        """Get statistics for god combinations"""
        combo_stats = defaultdict(lambda: {'runs': 0, 'wins': 0})
        
        for run in self.runs:
            gods = sorted(run.get('gods', []))
            if len(gods) >= 2:
                combo = " + ".join(gods[:3])  # Limit to top 3 gods
                combo_stats[combo]['runs'] += 1
                if run.get('victory', False):
                    combo_stats[combo]['wins'] += 1
        
        # Convert to list and calculate win rates
        combo_list = []
        for combo, stats in combo_stats.items():
            win_rate = (stats['wins'] / stats['runs'] * 100) if stats['runs'] > 0 else 0
            combo_list.append((combo, stats['runs'], stats['wins'], win_rate))
        
        # Sort by runs
        combo_list.sort(key=lambda x: x[1], reverse=True)
        return combo_list[:10]  # Top 10
    
    def get_recent_runs(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get most recent runs"""
        return list(reversed(self.runs[-limit:]))
    
    def get_avg_build_score(self) -> float:
        """Get average build score across all runs"""
        if not self.runs:
            return 0.0
        total_score = sum(run.get('build_score', 0) for run in self.runs)
        return total_score / len(self.runs)
    
    def get_best_run(self) -> Optional[Dict[str, Any]]:
        """Get highest scoring run"""
        if not self.runs:
            return None
        return max(self.runs, key=lambda r: r.get('build_score', 0))


class HadesHelperApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("⚔️ Hades Build Helper Pro - Analytics Edition")
        self.geometry("1600x900")
        
        # Data storage
        self.selected_gods: Set[str] = set()
        self.acquired_boons: Set[str] = set()
        self.selected_weapon: Optional[str] = None
        self.selected_aspect: Optional[str] = None
        self.search_query: str = ""
        
        # Analytics
        self.analytics = RunAnalytics()
        
        # Create UI
        self.create_layout()
        
        # Update analytics dashboard on startup
        self.update_analytics_dashboard()

    def create_layout(self):
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Left Panel - Selection
        self.left_frame = ctk.CTkFrame(self, corner_radius=10)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Title
        title_label = ctk.CTkLabel(
            self.left_frame, 
            text="⚔️ Build Optimizer", 
            font=ctk.CTkFont(size=22, weight="bold")
        )
        title_label.pack(pady=(15, 10))

        # === WEAPON SELECTION ===
        weapon_frame = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        weapon_frame.pack(pady=8, padx=20, fill="x")
        
        weapon_label = ctk.CTkLabel(
            weapon_frame, 
            text="🗡️ Select Weapon:", 
            font=ctk.CTkFont(size=14, weight="bold")
        )
        weapon_label.pack(anchor="w", pady=(5, 5))

        self.weapon_combo = ctk.CTkComboBox(
            weapon_frame,
            values=["None"] + list(WEAPONS_DATA.keys()),
            command=self.on_weapon_changed,
            font=ctk.CTkFont(size=11),
            width=250
        )
        self.weapon_combo.set("None")
        self.weapon_combo.pack(fill="x", pady=5)

        # === SEARCH BAR ===
        search_frame = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        search_frame.pack(pady=8, padx=20, fill="x")
        
        search_label = ctk.CTkLabel(
            search_frame,
            text="🔍 Search Boons:",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        search_label.pack(anchor="w")

        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Type to filter...",
            font=ctk.CTkFont(size=11)
        )
        self.search_entry.pack(fill="x", pady=5)
        self.search_entry.bind("<KeyRelease>", self.on_search_changed)

        # === GODS SELECTION ===
        gods_label = ctk.CTkLabel(
            self.left_frame, 
            text="Select Gods:", 
            font=ctk.CTkFont(size=13, weight="bold")
        )
        gods_label.pack(pady=(8, 5))

        self.gods_scroll = ctk.CTkScrollableFrame(self.left_frame, height=140)
        self.gods_scroll.pack(pady=5, padx=20, fill="both", expand=True)

        self.god_checkboxes = {}
        for god_name in sorted(GODS_DATA.keys()):
            cb = ctk.CTkCheckBox(
                self.gods_scroll, 
                text=god_name,
                command=self.on_god_selection_changed,
                font=ctk.CTkFont(size=11)
            )
            cb.pack(anchor="w", pady=3, padx=10)
            self.god_checkboxes[god_name] = cb

        # === BOONS SELECTION ===
        boons_label = ctk.CTkLabel(
            self.left_frame, 
            text="Acquired Boons:", 
            font=ctk.CTkFont(size=13, weight="bold")
        )
        boons_label.pack(pady=(8, 5))

        self.boons_scroll = ctk.CTkScrollableFrame(self.left_frame, height=180)
        self.boons_scroll.pack(pady=5, padx=20, fill="both", expand=True)

        self.boon_checkboxes = {}

        # === ACTION BUTTONS ===
        button_frame = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        button_frame.pack(pady=12)

        self.analyze_btn = ctk.CTkButton(
            button_frame,
            text="🔮 Generate Recommendations",
            command=self.generate_recommendations,
            font=ctk.CTkFont(size=13, weight="bold"),
            height=38,
            fg_color="#8B0000",
            hover_color="#A52A2A"
        )
        self.analyze_btn.pack(pady=4)

        self.save_run_btn = ctk.CTkButton(
            button_frame,
            text="💾 Save Current Run",
            command=self.save_current_run,
            font=ctk.CTkFont(size=12, weight="bold"),
            height=35,
            fg_color="#006400",
            hover_color="#228B22"
        )
        self.save_run_btn.pack(pady=4)

        self.clear_btn = ctk.CTkButton(
            button_frame,
            text="🔄 Reset All",
            command=self.reset_all,
            font=ctk.CTkFont(size=11),
            height=32,
            fg_color="#2F4F4F",
            hover_color="#556B2F"
        )
        self.clear_btn.pack(pady=4)

        # === RIGHT PANEL - RESULTS & ANALYTICS ===
        self.right_frame = ctk.CTkFrame(self, corner_radius=10)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        results_title = ctk.CTkLabel(
            self.right_frame, 
            text="📜 Recommendations & Analytics", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        results_title.pack(pady=(15, 10))

        # Build Score Display
        self.score_frame = ctk.CTkFrame(self.right_frame, height=60)
        self.score_frame.pack(pady=5, padx=20, fill="x")

        self.score_label = ctk.CTkLabel(
            self.score_frame,
            text="Build Score: --/100",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.score_label.pack(pady=5)

        self.score_progress = ctk.CTkProgressBar(self.score_frame, width=400)
        self.score_progress.pack(pady=5)
        self.score_progress.set(0)

        # Tabview for different categories
        self.tabview = ctk.CTkTabview(self.right_frame)
        self.tabview.pack(pady=10, padx=20, fill="both", expand=True)

        self.tabview.add("🌟 Duo Boons")
        self.tabview.add("⚡ Legendary")
        self.tabview.add("🎯 Synergies")
        self.tabview.add("📊 Analytics")
        self.tabview.add("📈 Statistics")

        # Text boxes for recommendations
        self.duo_text = ctk.CTkTextbox(self.tabview.tab("🌟 Duo Boons"), wrap="word", font=ctk.CTkFont(size=11))
        self.duo_text.pack(fill="both", expand=True, padx=10, pady=10)

        self.legendary_text = ctk.CTkTextbox(self.tabview.tab("⚡ Legendary"), wrap="word", font=ctk.CTkFont(size=11))
        self.legendary_text.pack(fill="both", expand=True, padx=10, pady=10)

        self.synergy_text = ctk.CTkTextbox(self.tabview.tab("🎯 Synergies"), wrap="word", font=ctk.CTkFont(size=11))
        self.synergy_text.pack(fill="both", expand=True, padx=10, pady=10)

        # Analytics Tab
        self.analytics_text = ctk.CTkTextbox(self.tabview.tab("📊 Analytics"), wrap="word", font=ctk.CTkFont(size=11))
        self.analytics_text.pack(fill="both", expand=True, padx=10, pady=10)

        # Statistics Tab
        self.stats_scroll = ctk.CTkScrollableFrame(self.tabview.tab("📈 Statistics"))
        self.stats_scroll.pack(fill="both", expand=True, padx=10, pady=10)

    def on_weapon_changed(self, choice):
        """Handle weapon selection"""
        if choice == "None":
            self.selected_weapon = None
            return
        self.selected_weapon = choice
    
    def on_search_changed(self, event=None):
        """Handle search query changes"""
        self.search_query = self.search_entry.get().lower()
        self.update_boons_list()

    def on_god_selection_changed(self):
        """Update boons list when gods are selected/deselected"""
        self.selected_gods = {god for god, cb in self.god_checkboxes.items() if cb.get()}
        self.update_boons_list()

    def update_boons_list(self):
        """Refresh the boons checkboxes based on selected gods and search"""
        for widget in self.boons_scroll.winfo_children():
            widget.destroy()
        
        self.boon_checkboxes.clear()

        if not self.selected_gods:
            no_gods_label = ctk.CTkLabel(
                self.boons_scroll,
                text="Select gods first",
                font=ctk.CTkFont(size=11, slant="italic"),
                text_color="gray"
            )
            no_gods_label.pack(pady=20)
            return

        available_boons = [b for b in BOONS_DATA if b['god'] in self.selected_gods]
        
        if self.search_query:
            available_boons = [b for b in available_boons if 
                              self.search_query in b['name'].lower() or 
                              self.search_query in b['description'].lower()]
        
        available_boons.sort(key=lambda x: (x['god'], x['name']))

        current_god = None
        for boon in available_boons:
            if boon['god'] != current_god:
                current_god = boon['god']
                god_label = ctk.CTkLabel(
                    self.boons_scroll,
                    text=f"═══ {current_god} ═══",
                    font=ctk.CTkFont(size=13, weight="bold"),
                    text_color=GODS_DATA[current_god].get("color", "white")
                )
                god_label.pack(anchor="w", pady=(8, 3))

            tier = boon.get('tier', 'B')
            tier_color = TIER_COLORS.get(tier, "#FFFFFF")
            
            boon_frame = ctk.CTkFrame(self.boons_scroll, fg_color="transparent")
            boon_frame.pack(anchor="w", pady=2, padx=20, fill="x")
            
            tier_label = ctk.CTkLabel(boon_frame, text=tier, font=ctk.CTkFont(size=9, weight="bold"), text_color=tier_color, width=18)
            tier_label.pack(side="left", padx=(0, 5))
            
            cb = ctk.CTkCheckBox(boon_frame, text=f"{boon['name']} ({boon['type']})", font=ctk.CTkFont(size=10))
            cb.pack(side="left", fill="x", expand=True)
            self.boon_checkboxes[boon['name']] = cb

    def calculate_build_score(self) -> int:
        """Calculate overall build score (0-100)"""
        score = 0
        score += min(len(self.selected_gods) * 3, 10)
        score += min(len(self.acquired_boons) * 2, 20)
        if self.selected_weapon:
            score += 10
        
        # Weapon synergy
        synergy_count = sum(1 for boon_name in self.acquired_boons 
                           if self.selected_weapon in BOON_NAME_TO_DATA.get(boon_name, {}).get('weapon_synergy', []))
        score += min(synergy_count * 3, 15)
        
        # Duo boons
        duo_ready = sum(1 for duo in DUO_BOONS_DATA 
                       if all(god in self.selected_gods for god in duo['gods'])
                       and all(prereq_boon in self.acquired_boons for _, prereq_boon in duo['prerequisites']))
        score += min(duo_ready * 10, 20)
        
        # Legendary boons
        legendary_ready = sum(1 for legendary in LEGENDARY_BOONS_DATA 
                             if legendary['god'] in self.selected_gods
                             and all(prereq_boon in self.acquired_boons for _, prereq_boon in legendary['prerequisites']))
        score += min(legendary_ready * 7, 15)
        
        return min(score, 100)

    def generate_recommendations(self):
        """Generate and display recommendations"""
        if not self.selected_gods:
            tkmb.showwarning("No Gods Selected", "Please select at least one god.")
            return

        self.acquired_boons = {name for name, cb in self.boon_checkboxes.items() if cb.get()}
        
        # Simple recommendation display
        self.duo_text.configure(state="normal")
        self.duo_text.delete("1.0", "end")
        self.duo_text.insert("end", "Duo boon recommendations based on your selections...\n")
        self.duo_text.configure(state="disabled")
        
        self.legendary_text.configure(state="normal")
        self.legendary_text.delete("1.0", "end")
        self.legendary_text.insert("end", "Legendary boon recommendations...\n")
        self.legendary_text.configure(state="disabled")
        
        self.synergy_text.configure(state="normal")
        self.synergy_text.delete("1.0", "end")
        self.synergy_text.insert("end", "Synergy recommendations...\n")
        self.synergy_text.configure(state="disabled")
        
        score = self.calculate_build_score()
        self.score_label.configure(text=f"Build Score: {score}/100")
        self.score_progress.set(score / 100)

    def save_current_run(self):
        """Save current build as a completed run"""
        if not self.selected_gods or not self.selected_weapon:
            tkmb.showwarning("Incomplete Data", "Please select a weapon and at least one god before saving.")
            return
        
        # Create dialog for run outcome
        dialog = ctk.CTkToplevel(self)
        dialog.title("💾 Save Run")
        dialog.geometry("400x300")
        dialog.transient(self)
        dialog.grab_set()
        
        ctk.CTkLabel(dialog, text="Save Run Result", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=20)
        
        victory_var = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(dialog, text="Victory (Defeated Hades)", variable=victory_var, font=ctk.CTkFont(size=13)).pack(pady=10)
        
        ctk.CTkLabel(dialog, text="Boss Reached:", font=ctk.CTkFont(size=12)).pack(pady=5)
        boss_combo = ctk.CTkComboBox(dialog, values=["Tartarus", "Asphodel", "Elysium", "Temple of Styx", "Hades"], width=250)
        boss_combo.set("Hades" if victory_var.get() else "Tartarus")
        boss_combo.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Heat Level:", font=ctk.CTkFont(size=12)).pack(pady=5)
        heat_entry = ctk.CTkEntry(dialog, width=100, placeholder_text="0")
        heat_entry.pack(pady=5)
        
        def save_run():
            try:
                heat = int(heat_entry.get() or "0")
            except:
                heat = 0
            
            run_data = {
                'weapon': self.selected_weapon,
                'gods': list(self.selected_gods),
                'boons': list(self.acquired_boons),
                'build_score': self.calculate_build_score(),
                'victory': victory_var.get(),
                'boss_reached': boss_combo.get(),
                'heat_level': heat
            }
            
            self.analytics.add_run(run_data)
            self.update_analytics_dashboard()
            dialog.destroy()
            tkmb.showinfo("Success", f"Run #{self.analytics.get_total_runs()} saved successfully!")
        
        ctk.CTkButton(dialog, text="💾 Save Run", command=save_run, fg_color="#006400", hover_color="#228B22", height=40, width=200).pack(pady=20)

    def update_analytics_dashboard(self):
        """Update the analytics and statistics tabs"""
        # Analytics Tab
        self.analytics_text.configure(state="normal")
        self.analytics_text.delete("1.0", "end")
        
        analytics_content = f"""
═══════════════════════════════════
           🏆 RUN ANALYTICS
═══════════════════════════════════

📊 OVERALL STATISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Runs:        {self.analytics.get_total_runs()}
Total Victories:   {self.analytics.get_wins()}
Win Rate:          {self.analytics.get_win_rate():.1f}%
Avg Build Score:   {self.analytics.get_avg_build_score():.1f}/100

═══════════════════════════════════
        📜 RECENT RUNS (Last 10)
═══════════════════════════════════

"""
        
        recent_runs = self.analytics.get_recent_runs(10)
        if recent_runs:
            for i, run in enumerate(recent_runs, 1):
                status = "✅ Victory" if run.get('victory', False) else "❌ Defeat"
                analytics_content += f"Run #{run.get('run_number', '?')}: {status}\n"
                analytics_content += f"  Weapon: {run.get('weapon', 'Unknown')}\n"
                analytics_content += f"  Gods: {', '.join(run.get('gods', []))}\n"
                analytics_content += f"  Score: {run.get('build_score', 0)}/100\n"
                analytics_content += f"  Boss: {run.get('boss_reached', 'Unknown')}\n\n"
        else:
            analytics_content += "No runs recorded yet. Start playing and save your runs!\n"
        
        # Best Run
        best_run = self.analytics.get_best_run()
        if best_run:
            analytics_content += f"""
═══════════════════════════════════
        🌟 BEST RUN (Highest Score)
═══════════════════════════════════

Run #{best_run.get('run_number', '?')}
Result:  {'✅ Victory' if best_run.get('victory', False) else '❌ Defeat'}
Weapon:  {best_run.get('weapon', 'Unknown')}
Gods:    {', '.join(best_run.get('gods', []))}
Score:   {best_run.get('build_score', 0)}/100
Boss:    {best_run.get('boss_reached', 'Unknown')}
"""
        
        self.analytics_text.insert("1.0", analytics_content)
        self.analytics_text.configure(state="disabled")
        
        # Statistics Tab
        for widget in self.stats_scroll.winfo_children():
            widget.destroy()
        
        # Weapon Statistics
        weapon_stats = self.analytics.get_weapon_stats()
        if weapon_stats:
            weapon_label = ctk.CTkLabel(self.stats_scroll, text="⚔️ WEAPON STATISTICS", font=ctk.CTkFont(size=16, weight="bold"))
            weapon_label.pack(pady=10)
            
            for weapon, stats in sorted(weapon_stats.items(), key=lambda x: x[1]['win_rate'], reverse=True):
                frame = ctk.CTkFrame(self.stats_scroll)
                frame.pack(pady=5, padx=10, fill="x")
                
                text = f"{weapon}\n"
                text += f"Runs: {stats['runs']} | Wins: {stats['wins']} | Win Rate: {stats['win_rate']:.1f}%\n"
                text += f"Avg Score: {stats['avg_score']:.1f}/100"
                
                label = ctk.CTkLabel(frame, text=text, font=ctk.CTkFont(size=11), justify="left")
                label.pack(pady=5, padx=10)
        
        # God Statistics
        god_stats = self.analytics.get_god_stats()
        if god_stats:
            god_label = ctk.CTkLabel(self.stats_scroll, text="\n🏛️ GOD STATISTICS", font=ctk.CTkFont(size=16, weight="bold"))
            god_label.pack(pady=10)
            
            for god, stats in sorted(god_stats.items(), key=lambda x: x[1]['win_rate'], reverse=True):
                frame = ctk.CTkFrame(self.stats_scroll)
                frame.pack(pady=5, padx=10, fill="x")
                
                text = f"{god}: {stats['runs']} runs | {stats['wins']} wins | {stats['win_rate']:.1f}% win rate"
                label = ctk.CTkLabel(frame, text=text, font=ctk.CTkFont(size=11), justify="left")
                label.pack(pady=5, padx=10)
        
        # God Combos
        combo_stats = self.analytics.get_god_combo_stats()
        if combo_stats:
            combo_label = ctk.CTkLabel(self.stats_scroll, text="\n🔥 TOP GOD COMBINATIONS", font=ctk.CTkFont(size=16, weight="bold"))
            combo_label.pack(pady=10)
            
            for combo, runs, wins, win_rate in combo_stats[:5]:
                frame = ctk.CTkFrame(self.stats_scroll)
                frame.pack(pady=5, padx=10, fill="x")
                
                text = f"{combo}\n{runs} runs | {wins} wins | {win_rate:.1f}% win rate"
                label = ctk.CTkLabel(frame, text=text, font=ctk.CTkFont(size=11), justify="left")
                label.pack(pady=5, padx=10)

    def reset_all(self):
        """Reset all selections"""
        for cb in self.god_checkboxes.values():
            cb.deselect()
        
        self.weapon_combo.set("None")
        self.selected_weapon = None
        self.search_entry.delete(0, "end")
        self.search_query = ""
        self.selected_gods.clear()
        self.acquired_boons.clear()
        self.update_boons_list()
        
        self.score_label.configure(text="Build Score: --/100")
        self.score_progress.set(0)


if __name__ == "__main__":
    app = HadesHelperApp()
    app.mainloop()
