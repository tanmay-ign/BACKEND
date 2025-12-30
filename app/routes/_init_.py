# This file makes the routes directory a Python package
from . import detection, health, alerts, video, websocket, system, detections

__all__ = ['detection', 'health', 'alerts', 'video', 'websocket', 'system', 'detections']
