complex_dict = {
    "user": {
        "id": 101,
        "name": "Alice",
        "roles": ("admin", "editor"),
        "preferences": {
            "theme": "dark",
            "languages": ["Python", "Go", "Rust"],
            "notifications": {
                "email": True,
                "sms": False,
                "apps": ["Slack", "Discord"]
            }
        }
    },
    "projects": [
        {
            "title": "Project X",
            "contributors": ("Bob", "Charlie"),
            "tasks": [
                {"id": 1, "desc": "Setup repo", "done": True},
                {"id": 2, "desc": "Create API", "done": False},
                {"id": 3, "desc": "Write docs", "done": False}
            ],
            "tags": {"backend", "fastapi", "postgres"}
        },
        {
            "title": "UI Overhaul",
            "contributors": ["Diana"],
            "tasks": [],
            "tags": {"frontend", "react"}
        }
    ],
    "config": {
        "max_retries": 3,
        "features": {
            "beta": True,
            "experiments": [
                ("feature_flag", 0.75),
                ("new_login_flow", 0.2),
                ["dark_mode_v2", 0.05]
            ]
        },
        "limits": {
            "storage": {
                "free": 5 * 1024**3,
                "pro": float("inf")
            }
        }
    },
    "history": [
        {"action": "login", "timestamp": "2025-10-28T15:00:00Z"},
        {"action": "upload", "timestamp": "2025-10-28T15:05:10Z", "file": ("report.pdf", 1024 * 500)},
        {"action": "share", "timestamp": "2025-10-28T15:06:00Z", "to": ["Team A", "Team B"]}
    ],
    "misc": (
        {"nested_tuple_dict": {"numbers": (1, 2, 3)}},
        [True, False, None, {"key": "value"}],
        "end_of_world"
    )
}

print(type(complex_dict))
print(complex_dict.keys())
# dict_keys(['user', 'projects', 'config', 'history', 'misc'])

print(complex_dict["history"][1]["file"][0])


