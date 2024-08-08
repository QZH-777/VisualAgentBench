from jarvis.utils import write_video

import json
from jarvis.assets import TASKS_FILE, TAG_ITEMS_FILE, SPAWN_FILE, SKILL_FILE, TRACE_TASK_FILE, TRAINING_TASK_FILE
with open(TASKS_FILE, 'r') as f:
    jarvis_tasks = json.load(f)

with open(TRACE_TASK_FILE, 'r') as f:
    trace_tasks = json.load(f)

with open(TRAINING_TASK_FILE, 'r') as f:
    training_tasks = json.load(f)

def get_task_config(task_name):
    task_dict = {}
    for task in jarvis_tasks:
        if task['task'] == task_name:
            task_dict = task
            return task_dict
    return {}

def get_task_config_trace(task_name):
    task_dict = {}
    for task in trace_tasks:
        if task['task'] == task_name:
            task_dict = task
            return task_dict
    return {}

with open(TAG_ITEMS_FILE, 'r') as f:
    tag_items = json.load(f)

with open(SKILL_FILE, 'r') as f:
    skills = json.load(f)

from jarvis.assets import MEMORY_FILE
with open(MEMORY_FILE, 'r') as f:
    memory = json.load(f)

class MarkBase:
    
    def __init__(self, **kwargs):
        pass
        
    def reset(self):
        self.record_frames = []
        self.record_infos = []
    
    def do(self):
        raise NotImplementedError

    def record_step(self):
        record_frames = getattr(self, 'record_frames', [])
        record_infos = getattr(self, 'record_infos', [])
        self.record_frames = record_frames + [self.info['pov']]
        self.record_infos = record_infos + [self.info]

    def make_traj_video(self, output_path: str):
        if getattr(self, 'record_frames', None) is None:
            return
        frames = [self.record_frames[i] for i in range(len(self.record_frames))]
        write_video(frames=frames, file_name=output_path)



