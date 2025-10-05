"""
Hades Build Helper - Room Progression Tracker
Track your run chamber-by-chamber with reward choices
"""

from typing import List, Dict, Any, Optional
from datetime import datetime


class Room:
    """Represents a single chamber in a Hades run."""
    
    def __init__(self, room_number: int, region: str, room_type: str):
        self.room_number = room_number
        self.region = region
        self.room_type = room_type  # Combat, Elite, Mini-boss, Boss, Shop, Fountain, Trial
        self.reward_offered: Optional[str] = None
        self.reward_chosen: Optional[str] = None
        self.gods_offered: List[str] = []
        self.god_chosen: Optional[str] = None
        self.boon_chosen: Optional[str] = None
        self.pom_targets: List[str] = []
        self.reroll_used: bool = False
        self.timestamp = datetime.now().isoformat()
        self.notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert room to dictionary for storage."""
        return {
            'room_number': self.room_number,
            'region': self.region,
            'room_type': self.room_type,
            'reward_offered': self.reward_offered,
            'reward_chosen': self.reward_chosen,
            'gods_offered': self.gods_offered,
            'god_chosen': self.god_chosen,
            'boon_chosen': self.boon_chosen,
            'pom_targets': self.pom_targets,
            'reroll_used': self.reroll_used,
            'timestamp': self.timestamp,
            'notes': self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Room':
        """Create room from dictionary."""
        room = cls(data['room_number'], data['region'], data['room_type'])
        room.reward_offered = data.get('reward_offered')
        room.reward_chosen = data.get('reward_chosen')
        room.gods_offered = data.get('gods_offered', [])
        room.god_chosen = data.get('god_chosen')
        room.boon_chosen = data.get('boon_chosen')
        room.pom_targets = data.get('pom_targets', [])
        room.reroll_used = data.get('reroll_used', False)
        room.timestamp = data.get('timestamp', datetime.now().isoformat())
        room.notes = data.get('notes', '')
        return room


class RunTracker:
    """Tracks a complete Hades run room-by-room."""
    
    # Region definitions
    REGIONS = {
        'Tartarus': {'rooms': 14, 'color': '#8B0000'},
        'Asphodel': {'rooms': 10, 'color': '#DC143C'},
        'Elysium': {'rooms': 11, 'color': '#FFD700'},
        'Temple of Styx': {'rooms': 5, 'color': '#32CD32'},
        'Final Boss': {'rooms': 1, 'color': '#8B008B'}
    }
    
    ROOM_TYPES = [
        'Combat',
        'Elite Combat',
        'Mini-Boss',
        'Boss',
        'Shop',
        'Fountain',
        'Trial of the Gods',
        'Chaos Gate',
        'Erebus Gate',
        'Sisyphus',
        'Eurydice',
        'Patroclus'
    ]
    
    REWARD_TYPES = [
        'Boon',
        'Pom of Power',
        'Centaur Heart (+Health)',
        'Daedalus Hammer',
        'Obols (Gold)',
        'Darkness',
        'Gems',
        'Keys',
        'Nectar',
        'Ambrosia',
        'Hermes',
        'Chaos',
        'Well of Charon'
    ]
    
    def __init__(self):
        self.rooms: List[Room] = []
        self.current_room_number = 0
        self.current_region = 'Tartarus'
        self.run_active = False
        self.run_start_time: Optional[str] = None
        self.run_end_time: Optional[str] = None
        
    def start_new_run(self):
        """Start a new run."""
        self.rooms = []
        self.current_room_number = 0
        self.current_region = 'Tartarus'
        self.run_active = True
        self.run_start_time = datetime.now().isoformat()
        self.run_end_time = None
        
    def add_room(self, room_type: str) -> Room:
        """Add a new room to the run."""
        self.current_room_number += 1
        room = Room(self.current_room_number, self.current_region, room_type)
        self.rooms.append(room)
        return room
    
    def get_current_room(self) -> Optional[Room]:
        """Get the current room being tracked."""
        if self.rooms:
            return self.rooms[-1]
        return None
    
    def advance_region(self, new_region: str):
        """Move to next region."""
        if new_region in self.REGIONS:
            self.current_region = new_region
    
    def end_run(self, victory: bool):
        """Mark run as complete."""
        self.run_active = False
        self.run_end_time = datetime.now().isoformat()
        
        # Add final boss room if victory
        if victory and not any(r.room_type == 'Boss' and r.region == 'Final Boss' for r in self.rooms):
            final_room = Room(self.current_room_number + 1, 'Final Boss', 'Boss')
            final_room.notes = "Defeated Hades!"
            self.rooms.append(final_room)
    
    def get_boon_choices_timeline(self) -> List[Dict[str, Any]]:
        """Get timeline of all boon choices made."""
        timeline = []
        for room in self.rooms:
            if room.boon_chosen:
                timeline.append({
                    'room': room.room_number,
                    'region': room.region,
                    'god': room.god_chosen,
                    'boon': room.boon_chosen,
                    'rerolled': room.reroll_used
                })
        return timeline
    
    def get_god_encounter_order(self) -> List[str]:
        """Get the order gods were encountered."""
        gods = []
        for room in self.rooms:
            if room.god_chosen and room.god_chosen not in gods:
                gods.append(room.god_chosen)
        return gods
    
    def get_room_summary(self) -> Dict[str, int]:
        """Get summary of room types encountered."""
        summary = {}
        for room in self.rooms:
            summary[room.room_type] = summary.get(room.room_type, 0) + 1
        return summary
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert run to dictionary."""
        return {
            'rooms': [r.to_dict() for r in self.rooms],
            'current_room_number': self.current_room_number,
            'current_region': self.current_region,
            'run_active': self.run_active,
            'run_start_time': self.run_start_time,
            'run_end_time': self.run_end_time,
            'total_rooms': len(self.rooms),
            'boon_timeline': self.get_boon_choices_timeline(),
            'god_encounter_order': self.get_god_encounter_order(),
            'room_summary': self.get_room_summary()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RunTracker':
        """Create run tracker from dictionary."""
        tracker = cls()
        tracker.rooms = [Room.from_dict(r) for r in data.get('rooms', [])]
        tracker.current_room_number = data.get('current_room_number', 0)
        tracker.current_region = data.get('current_region', 'Tartarus')
        tracker.run_active = data.get('run_active', False)
        tracker.run_start_time = data.get('run_start_time')
        tracker.run_end_time = data.get('run_end_time')
        return tracker
