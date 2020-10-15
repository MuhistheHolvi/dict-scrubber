from copy import copy

def sanitize_event(event, remove_keys):
    modified_event = copy(event)
    for key, value in event.items():
        if key in remove_keys:
            modified_event.pop(key, None)
        elif isinstance(value, dict):
            modified_event[key] = sanitize_event(value, remove_keys=remove_keys)
    return modified_event
