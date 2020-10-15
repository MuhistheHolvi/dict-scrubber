from unittest import TestCase
from main import sanitize_event


class MainTestCase(TestCase):
    def test_basic_case(self):
        event = {
            "remove_me": {"extra_key": "test value"}
        }
        remove_keys = ['remove_me']
        new_event = sanitize_event(event=event, remove_keys=remove_keys)

        self.assertNotEqual(new_event, event)
    
    def test_nested_dict(self):
        event = {
            "main_key": {
                "extra_key": "test value",
                "nested_key": "nested value"
            },
            "other_key": "other value"
        }
        remove_keys = ['nested_key']
        new_event = sanitize_event(event=event, remove_keys=remove_keys)
        self.assertNotIn("nested_key", new_event["main_key"])
