#!/usr/bin/env python3

# EventPilot - אפליקציה לניהול משימות לצוותי הפקה

## Backend בסיסי בפייתון (Flask)


from flask import Flask, g, session, redirect, render_template, request, jsonify, Response
from markupsafe import escape

app = Flask(__name__)

# דאטה מבוסס זיכרון להדגמה
events = []
tasks = []

@app.route("/events", methods=["GET", "POST"])
def handle_events():
    if request.method == "POST":
        data = request.get_json()
        event = {
            "id": len(events) + 1,
            "name": data["name"],
            "date": data.get("date", str(datetime.now().date())),
        }
        events.append(event)
        return jsonify(event), 201
    return jsonify(events)

@app.route("/events/<int:event_id>/tasks", methods=["GET", "POST"])
def handle_tasks(event_id):
    if request.method == "POST":
        data = request.get_json()
        task = {
            "id": len(tasks) + 1,
            "event_id": event_id,
            "title": data["title"],
            "status": data.get("status", "To Do"),
            "team": data.get("team", "כללי"),
        }
        tasks.append(task)
        return jsonify(task), 201
    return jsonify([t for t in tasks if t["event_id"] == event_id])

@app.route("/metrics")
def metrics():
    return (
        f"# HELP eventpilot_tasks_total Total number of tasks\n"
        f"# TYPE eventpilot_tasks_total gauge\n"
        f"eventpilot_tasks_total {len(tasks)}\n"
    ), 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

print("Starting Flask server...")
@app.route("/")
def index():
    return "<h1>ברוך הבא ל־EventPilot</h1><p>שירות ה-API פעיל. השתמש ב־/events</p>"
 
