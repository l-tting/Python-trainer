complex_dict_2 = {
    "company": {
        "name": "TechCorp",
        "departments": {
            "engineering": {
                "teams": [
                    {"name": "Backend", "members": [{"id": 101, "name": "Alice"}, {"id": 102, "name": "Bob"}]},
                    {"name": "Frontend", "members": [{"id": 103, "name": "Charlie"}, {"id": 104, "name": "Dana"}]}
                ],
                "budget": 1000000
            },
            "hr": {
                "teams": [
                    {"name": "Recruitment", "members": [{"id": 201, "name": "Eve"}, {"id": 202, "name": "Frank"}]},
                    {"name": "Training", "members": [{"id": 203, "name": "Grace"}]}
                ],
                "budget": 200000
            }
        },
        "offices": [
            {"city": "New York", "floors": (10, 20), "facilities": {"cafeteria": True, "gym": True, "parking": {"spots": 100, "reserved": 20}}},
            {"city": "London", "floors": (5, 15), "facilities": {"cafeteria": False, "gym": True, "parking": {"spots": 50, "reserved": 10}}}
        ]
    },
    "projects": [
        {
            "name": "Alpha",
            "deadline": "2025-12-31",
            "tasks": [
                {"task": "Design", "assigned_to": [101, 103], "status": "ongoing"},
                {"task": "Implementation", "assigned_to": [102, 104], "status": "pending"}
            ],
            "tags": {"priority": "high", "type": "internal"}
        },
        {
            "name": "Beta",
            "deadline": "2026-03-15",
            "tasks": [
                {"task": "Research", "assigned_to": [201, 203], "status": "completed"},
                {"task": "Deployment", "assigned_to": [102], "status": "pending"}
            ],
            "tags": {"priority": "medium", "type": "client"}
        }
    ],
    "metrics": {
        "employees": {"total": 10, "active": 9},
        "projects": {"active": 2, "completed": 1},
        "offices": {"total": 2, "remote_allowed": True}
    }
}
